# Python package manager `uv`

We use `uv` as python package manager. For more infos see
https://github.com/astral-sh/uv and https://docs.astral.sh/uv/.

Example usage:

```bash
uv add <some-py-module>     # Adds the dependency to the pyproject.toml file.
uv sync                     # Updates the projects environment.
uv venv                     # Creates a venv for the project.
source .venv/bin/activate   # Activate the venv.
<work as 'normal'>
```

or instead of sourcing the venv, `uv` can also be used like 

```bash
uv run <script_name>
```

which then uses the environment for the script as well.