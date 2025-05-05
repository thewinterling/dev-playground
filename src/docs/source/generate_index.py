import os
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
DOCS_INDEX = REPO_ROOT / "src/docs/source/index.md"
DOCS_SOURCE = DOCS_INDEX.parent


def generate_index():
    lines = ["# Project Docs\n"]
    for readme in sorted(REPO_ROOT.glob("**/README.md")):
        if any(p.startswith(".") for p in readme.resolve().parts):
            continue
        rel_path = os.path.relpath(readme, start=DOCS_SOURCE)
        lines.append(f"```{{include}} {rel_path}")
        lines.append("```")
        lines.append("")

    DOCS_INDEX.write_text("\n".join(lines))


if __name__ == "__main__":
    generate_index()
