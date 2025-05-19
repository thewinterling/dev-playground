cc_library(
    name = "particle_filter_lib",
    srcs = glob(["src/**/*.cpp"]),
    hdrs = glob(["include/**/*.hpp"]),
    includes = ["include"],
    visibility = ["//visibility:public"],
)

cc_test(
    name = "particle_filter_test",
    srcs = glob(["test/**/*.cpp"]),
    deps = [
        ":particle_filter_lib",
        "@googletest//:gtest_main",
    ],
)

cc_binary(
    name = "particle_filter",
    srcs = ["src/particle_filter.cpp"],
    deps = [":particle_filter_lib"],
)