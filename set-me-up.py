#!/usr/bin/env python3
"""Setup script for dev-playground.

Run it from the root of the repository:
`./set-me-up.py`
without any arguments.
"""

import os
import shutil
import subprocess
import sys
from pathlib import Path
import platform
import json

EXPECTED_UV_VERSION = "0.6.14"
EXPECTED_CLANG_FORMAT_VERSION = "15"

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RESET = "\033[0m"


def _install_uv() -> None:
    """Installs uv if requested by the user."""
    if input().lower() == "n":
        sys.exit(1)
    subprocess.run(f"curl -LsSf https://astral.sh/uv/{EXPECTED_UV_VERSION}/install.sh | sh", check=True)  # noqa: S603
    _inject_local_path()


def _update_uv() -> None:
    """Updates uv when already installed but in outdated version."""
    subprocess.run(["uv", "self", "update"], check=True)  # noqa: S603, S607


def _inject_local_path() -> None:
    """Adds '.local/bin.' to PATH if not already present."""
    local_bin = Path("~/.local/bin").expanduser().as_posix()
    paths = os.getenv("PATH", "").split(":")
    if local_bin not in paths:
        os.environ["PATH"] = ":".join(local_bin, *paths)


def _get_uv_version() -> str:
    """Returns the version of the installed uv package."""
    return subprocess.check_output(["uv", "--version"], text=True).split(" ")[1].strip()  # noqa: S607, S603


def _get_path_to_installable_sub_packages() -> str:
    TOP_LEVEL = "radar-ai-perception/pyproject.toml"
    files = Path(__file__).parent.glob("**/pyproject.toml")
    files = [f.resolve() for f in files]
    files = [f.parent for f in files if TOP_LEVEL not in str(f)]
    return files


def setup_with_uv() -> None:
    """Installs uv if not already installed. Checks if '.local/bin' is in PATH,
    if not it will be added. Creates the venv and installs the required packages.

    Args:
    ----
        None

    Returns:
    ----
        None

    """
    _inject_local_path()
    if shutil.which("uv") is None:
        print(f"{YELLOW}uv is not installed. Shall I install it for you? [Y/n]{RESET}", end="")
        _install_uv()
        return

    uv_version_str = _get_uv_version()
    uv_version = tuple(map(int, uv_version_str.split(".")))

    if uv_version < tuple(map(int, EXPECTED_UV_VERSION.split("."))):
        print(f"{YELLOW}uv {uv_version_str} is too old, will be updated to {EXPECTED_UV_VERSION} now.{RESET}")
        _update_uv()
    try:
        subprocess.run(["uv", "sync"], check=True)
        subprocess.run(["uv", "run", "pre-commit", "install"], check=True)
        sub_packages = _get_path_to_installable_sub_packages()
        for package_path in sub_packages:
            subprocess.run(["uv", "pip", "install", "-e", str(package_path)], check=True)
    except (subprocess.CalledProcessError, Exception) as e:
        print(f"{RED}Installation failed: {e}\n{RESET}")
        exit(-1)


def setup_clang_format() -> None:
    """Installs clang-format if not already installed.

    Args:
    ----
        None

    Returns:
    ----
        None
    """
    clang_format = f"clang-format-{EXPECTED_CLANG_FORMAT_VERSION}"
    if shutil.which(f"{clang_format}") is None:
        print(
            f"{YELLOW}{clang_format} is not installed. Shall I install it for you? [Y/n]{RESET}",
            end="",
        )
        if input().lower() == "n":
            sys.exit(1)
        subprocess.run(["sudo", "apt", "install", f"{clang_format}"], stdout=subprocess.DEVNULL, check=True)  # noqa: S603
    print(f"{GREEN}✅ {clang_format} is installed.{RESET}")


def _get_latest_bazelisk_version():
    result = subprocess.run(
        ["curl", "-s", "https://api.github.com/repos/bazelbuild/bazelisk/releases/latest"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        check=True,
    )
    if result.returncode != 0:
        raise RuntimeError(f"Error fetching version: {result.stderr}")

    latest_version = json.loads(result.stdout).get("tag_name", None)
    if latest_version is None:
        raise ValueError("Could not find 'tag_name' in API response.")
    return latest_version


def setup_bazelisk() -> None:
    """Installs bazelisk if not already installed.

    Args:
    ----
        None

    Returns:
    ----
        None
    """
    if shutil.which("bazelisk") is None:
        print(f"{YELLOW}bazelisk is not installed. Shall I install it for you? [Y/n]{RESET}", end="")
        version = _get_latest_bazelisk_version()

        subprocess.run(
            ["wget", f"https://github.com/bazelbuild/bazelisk/releases/download/{version}/bazelisk-linux-amd64"],
            check=True,
        )
        subprocess.run(["chmod", "+x", "bazelisk-linux-amd64"], check=True)
        subprocess.run(["sudo", "mv", "bazelisk-linux-amd64", "/usr/local/bin/bazel"], check=True)
    print(f"{GREEN}✅ bazelisk is installed.{RESET}")


if __name__ == "__main__":
    if platform.system() != "Linux":
        print(f"{RED}This script is only supported on Linux.{RESET}")
        sys.exit(1)

    os.chdir(Path(__file__).parent)

    print(f"{GREEN}Setting up your development environment...{RESET}")

    subprocess.run(["sudo", "apt", "update"], stdout=subprocess.DEVNULL, check=True)  # noqa: S603
    setup_clang_format()
    setup_bazelisk()
    setup_with_uv()
    print(f"{GREEN}✅ You're all set. Source the venv via `source .venv/bin/activate`{RESET}")
