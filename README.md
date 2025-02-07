# DevPlayground
A repository for all sorts of training code


## Bazel

We use `bazel` for the C++ part (in the future possibly for everything).
Therefore we installed `bazelisk`, for more reference see here:
https://bazel.build/install/bazelisk
https://github.com/bazelbuild/bazelisk/blob/master/README.md

After installation check its correct install via

```bash
bazelisk version
```

Create a `~/.bazelrc`:

```bash
# If you wish cross-workspace caching.
build --disk_cache=/home/<USER>/.bazelcache

# Limit the resources that Bazel is allowed to use.
# This prevents the PC from freezing because Bazel uses everything.
build --local_resources=cpu=HOST_CPUS-4
build --local_resources=memory=HOST_RAM*.6

# Use colors in GCC output.
build --copt=-fdiagnostics-color=always
```

Then you can

```bash
bazelisk build ...                      # Builds everything
bazelisk build //path/to/package        # Builds a specific target 

bazelisk query '...'                    # Shows all targets
bazelisk query '//training/cpp/...'     # Shows targets in training/cpp

bazelisk run //your/target:target_name  # Run the target
bazelisk test //your/target:target_name # Run the test
```

### C++

In `training/cpp` there are all sorts of cpp-training examples. Right now 
there is only small leetcode examples. More to come.

## Github Actions / Pre commit hooks

We run github actions acting as a minimalist CI Pipeline. Also there are `pre-commit` hooks in-place
so that we do not have to worry about ill-formated code (and removing it as a topic of discussion in the PRs)
hence ultimately making things more efficient.
While the CI pipeline is to enforce certain standarts on the code of this repo, it is also to _train_ how to
set it up - and maintain it.

## Python package manager

We use `uv` as python package manager. For more infos see
https://github.com/astral-sh/uv and https://docs.astral.sh/uv/.
This is to not go the 'we have always done it like this' way but to explore novel (and good) tools.


## Python

Python training is located in `training/python`. There exist many small snippets where
we tested behaviour that we discussed on real-world examples. Those examples were
extracted from the original source and made the topic of concern explicit.
Most of the snippets however are not yet transfered to this repo.
Since the focus right now is not on python, it will most likely stay like this for a while.




## Setup the repo

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

For C++, install `bazelisk` as mentioned above.