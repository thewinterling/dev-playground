# DevPlayground
A mono repository for all sorts of training code.

## Content

* [C++](cpp/README.md)
* [github actions](.github/README.md)
* [python](python/README.md)
* [bazel](bazel/README.md)
* [uv](uv/README.md)




### C++

In `training/cpp` there are all sorts of cpp-training examples. Right now 
there is only small leetcode examples. More to come.

## Github Actions / Pre commit hooks

We run github actions acting as a minimalist CI Pipeline. Also there are `pre-commit` hooks in-place
so that we do not have to worry about ill-formated code (and removing it as a topic of discussion in the PRs)
hence ultimately making things more efficient.
While the CI pipeline is to enforce certain standarts on the code of this repo, it is also to _train_ how to
set it up - and maintain it.








## Setup the repo

```bash

sudo apt update
sudo apt install clang-format-15 # This is used in the pre-commit hook.

pre-commit install
```



For C++, install `bazelisk` as mentioned above.