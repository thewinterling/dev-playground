from pathlib import Path
import os

REPO_ROOT = Path(__file__).resolve().parents[2]
DOCS_INDEX = REPO_ROOT / "docs/source/index.md"
DOCS_SOURCE = DOCS_INDEX.parent


def find_level(readme: Path) -> int:
    """Find the level of the README file based on its directory depth."""
    return len(readme.relative_to(REPO_ROOT).parts) - 1


def generate_index():
    lines = ["# Project Docs\n"]
    for readme in sorted(REPO_ROOT.glob("**/README.md")):
        if any(p.startswith(".") for p in readme.resolve().parts):
            continue
        rel_path = os.path.relpath(readme, start=DOCS_SOURCE)
        level = find_level(readme)
        lines.append(f"#{'#' * level} {readme.parent.name}")
        lines.append(f"```{{include}} {rel_path}")
        lines.append("```")
        lines.append("")

    DOCS_INDEX.write_text("\n".join(lines))


if __name__ == "__main__":
    generate_index()
