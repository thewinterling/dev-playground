# Python Packaging Example

This package is soley here for the purpose of demonstrating how to package a python package.
The package itself is not of any relevance.

Packaging done following https://packaging.python.org/en/latest/tutorials/packaging-projects/ but we used
`uv` for it. Thus we only took the linked page as a reference.

## Steps

### 1. Create the package
- create the package incl. python files
- add readme, license and pyproject.toml (we created the latter by running `uv init` in our package folder)

### 2. Build the wheel
- run `uv build` (see https://docs.astral.sh/uv/reference/cli/#uv-build)

### (optional) 3. Upload to an index
- run `uv publish` (see https://docs.astral.sh/uv/reference/cli/#uv-publish)

(For this example we did not publish anything, we just build the wheel file and verified that it can be
installed and used again - see next step.)

### 4. Test the build
```bash
$ mkdir test
$ uv init
$ uv venv
$ source .venv/bin/activate
$ uv pip install /home/<USER>/workspace/dev-playground/dist/packaging_example-0.0.1-py3-none-any.whl
Resolved 1 package in 2ms
Prepared 1 package in 5ms
Installed 1 package in 13ms
 + packaging-example==0.0.1 (from file:///home/<USER>/workspace/dev-playground/dist/packaging_example-0.0.1-py3-none-any.whl)
```
Then you can use the package as any python package:

```python
>>> from packaging_example.example import hello
>>> hello()
this is a dummy example.
```

