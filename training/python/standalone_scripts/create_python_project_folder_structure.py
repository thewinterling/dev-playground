#!/usr/bin/env python

import argparse
import datetime
from pathlib import Path
import logging

"""Script to create a boilerplate folder structure for a python project."""


def _parse_args():
    parser = argparse.ArgumentParser(description="Creates a boilerplate folder structure for a python project.")
    parser.add_argument(
        "--name",
        type=str,
        help="Name of the project",
    )
    parser.add_argument(
        "--path",
        type=Path,
        help="Where the 'project' shall be created.",
    )
    parser.add_argument(
        "--owner",
        type=str,
        help="The owner of the project.",
    )
    return parser.parse_args()


def write_mit_license_file(license_file: Path, owner):
    mit_license = f"""MIT License

Copyright (c) {datetime.datetime.now().year} {owner}

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""
    with open(license_file, "w") as file:
        file.write(mit_license)


def write_gitignore_file(gitignore_file: Path):
    gitignore_content = """*.pyc
__pycache__
"""
    with open(gitignore_file, "w") as file:
        file.write(gitignore_content)


def write_readme_file(readme_file: Path, project_name: str):
    readme_content = f"""# {project_name.capitalize()}

This is the default readme for the project.
TODO: Add your relevant content here.

## Install

```bash
python -m venv <venv_name>
source <venv_name>/bin/activate
pip install -r requirements.txt

# and more ....
```

## How to use

Explain how the project shall be used i.e. with a simple
call to the main module:
```bash
python -m {project_name} <...>
```

"""
    with open(readme_file, "w") as file:
        file.write(readme_content)


def create_structure(project_name: str, base_folder: Path, owner: str):
    """Creates a boilerplate folder structure usable for any python project.
    Adapted from: https://dev.to/codemouse92/dead-simple-python-project-structure-and-imports-38c6
    (tests moved one level above, everything else is the same).

    project_name
    ├── LICENSE.md // MIT License
    ├── project_name
    │   ├── __main__.py
    │   ├── common
    │   │   ├── common_dummy.py
    │   │   └── __init__.py
    │   ├── data
    │   │   ├── data_dummy.py
    │   │   └── __init__.py
    │   ├── __init__.py
    │   ├── __main__.py
    |   └── scripts
    │       └── script_dummy.py
    ├── tests
    │   ├── test_dummy.py
    │   └── __init__.py
    ├── README.md
    └── .gitignore

    Note: no pyproject.toml or whatsoever is created here since we believe you already have a proper/working
    setup there!
    """
    if (base_folder / project_name).exists():
        logging.error(f"{base_folder / project_name} exists already, doing nothing here.")
        exit(-1)

    folders = [
        base_folder / project_name,
        base_folder / project_name / project_name,
        base_folder / project_name / project_name / "common",
        base_folder / project_name / project_name / "data",
        base_folder / project_name / project_name / "scripts",
        base_folder / project_name / "tests",
    ]
    for folder in folders:
        folder.mkdir()
        logging.info(f"Created folder: {folder}")

    write_mit_license_file(base_folder / project_name / "LICENSE.md", owner)
    write_gitignore_file(base_folder / project_name / ".gitignore")
    write_readme_file(base_folder / project_name / "README.md", project_name)

    (base_folder / project_name / project_name / "__main__.py").touch()

    (base_folder / project_name / project_name / "common" / "common_dummy.py").touch()
    (base_folder / project_name / project_name / "common" / "__init__.py").touch()

    (base_folder / project_name / project_name / "data" / "data_dummy.py").touch()
    (base_folder / project_name / project_name / "data" / "__init__.py").touch()

    (base_folder / project_name / "tests" / "test_dummy.py").touch()
    (base_folder / project_name / "tests" / "__init__.py").touch()

    (base_folder / project_name / project_name / "scripts" / "script_dummy.py").touch()


if __name__ == "__main__":
    args = _parse_args()

    create_structure(args.name, args.path.resolve(), args.owner)
