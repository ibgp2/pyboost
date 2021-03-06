#!/usr/bin/env python3

import os

def find(path = ".", extension = ""):
    return (
        os.path.join(root, f)
        for (root, dirs, files) in os.walk(path)
        for f in files
        if f.endswith(extension)
    )

def init(
    use_pyplusplus = False,
    sources_ext = "cpp",
    headers_ext = "hpp",
    headers_dir = "src",
    sources_dir = "src"
):
    if use_pyplusplus:
        # Py++ can automatically generate python bindings under some limitations:
        # - It supports well std:: streams (like std::cout) and std::string
        # - It does not automatically wrap std:: containers (like std::vector)
        # - It does not support well parameters typed by a std::container
        # - It does not handle well references (for instance, do not return a reference)
        # - Only public std::vector read property is automatically supported.
        # See https://pyplusplus.readthedocs.io/en/latest/tutorials/containers/indexing_suite_v2.html.html
        from pyplusplus import make_bindings_auto
        filename_bindings_auto = os.path.join(sources_dir, "bindings_auto.cpp")
        make_bindings_auto(headers_dir, headers_ext, filename_bindings_auto)
        # Ignore bindings manually written
        exclude = "bindings.cpp"
    else:
        # Ignore bindings generated by ++
        exclude = "bindings_auto.cpp"
        # The developer must manually write/complete bindings_auto.cpp

    sources = [
        f
        for f in find(sources_dir, sources_ext)
        if f != os.path.join(sources_dir, exclude)
    ]
    return sources

