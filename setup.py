#!/usr/bin/env python3

import platform
from setuptools     import setup
from distutils.core import Extension
from setup_common   import init

sources = init(
    use_pyplusplus = False,
    sources_ext = "cpp",
    headers_ext = "hpp",
    headers_dir = "src",
    sources_dir = "src"
)

# https://stackoverflow.com/questions/20872698/place-boost-python-extension-inside-package
cxx_flags = ["-std=c++11", "-W", "-Wall", "-fPIC"] # Optional
(x, y, z) = platform.python_version().split(".")
lib_boost = f"boost_python{x}{y}"
lib_python = f"python{x}.{y}"

setup(
    name = "pyboost",
    version = "0.0.1",
    description = "A python wrapping some simple C++ classes",
    # Do not include pure python file in the same module to prevent clashes.
    # For example, adding the following statement is a bad idea!
    #py_modules = ["pyboost.my_class"],
    ext_modules = [
        Extension(
            # The extension must have the name of the package
            "pyboost", # This generates pyboost*.so, than may directly be imported in python3
            # The following macros remove some irrelevant compilation warnings.
            define_macros = [
                ("BOOST_BIND_GLOBAL_PLACEHOLDERS", None),
                ("BOOST_ALLOW_DEPRECATED_HEADERS", None),
            ],
            sources = sources,
            extra_compile_args = cxx_flags,
            extra_link_args    = cxx_flags,
            libraries = [lib_boost, lib_python]
        )
    ],
)
