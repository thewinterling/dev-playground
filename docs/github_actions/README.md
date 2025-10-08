# Github Actions / Pre commit hooks

We run github actions acting as a minimalist CI Pipeline. Also there are `pre-commit` hooks in-place
so that we do not have to worry about ill-formated code (and removing it as a topic of discussion in the PRs)
hence ultimately making things more efficient.
While the CI pipeline is to enforce certain standards on the code of this repo, it is also to _train_ how to
set it up - and maintain it.

Implementation is in `<REPO_ROOT>/.github`.