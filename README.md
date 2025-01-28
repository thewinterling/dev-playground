
# DevPlayground
A repository for all sorts of training code


# Setup

```bash

sudo apt update
sudo apt install clang-format-15 # This is used in the pre-commit hook.

pre-commit install
```

For python, we use `uv` as package manager

```bash
uv venv
source .venv/bin/activate
```

or 
```bash
uv sync

# Then run scripts via
uv run <script_name>
```