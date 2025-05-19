# Bazel

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

# Enable verbose test output
test --test_output=all

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
bazelisk query '//cpp/...'              # Shows targets in cpp

bazelisk run //your/target:target_name  # Run the target
bazelisk test //your/target:target_name # Run the test
```