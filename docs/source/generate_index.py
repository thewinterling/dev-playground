from pathlib import Path
import os

REPO_ROOT = Path(__file__).resolve().parents[2]
DOCS_INDEX = REPO_ROOT / "docs/source/index.md"
DOCS_SOURCE = DOCS_INDEX.parent

lines = ["# Project Docs\n"]
for readme in REPO_ROOT.glob("**/README.md"):
    rel_path = os.path.relpath(readme, start=DOCS_SOURCE)
    lines.append(f"## {readme.parent.name}")
    lines.append(f"```{{include}} {rel_path}")
    lines.append("```")
    lines.append("")

DOCS_INDEX.write_text("\n".join(lines))
