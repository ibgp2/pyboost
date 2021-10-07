#!/usr/bin/env python3
# https://stackoverflow.com/questions/42585210/extending-setuptools-extension-to-use-cmake-in-setup-py

import os, pathlib
from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext
from setup_common import init

sources = init(
    use_pyplusplus = False,
    sources_ext = "cpp",
    headers_ext = "hpp",
    headers_dir = "src",
    sources_dir = "src"
)

class CMakeExtension(Extension):
    def __init__(self, name):
        # Don't invoke the original build_ext for this special extension
        super().__init__(name, sources=[])

class BuildExt(build_ext):
    def run(self):
        for ext in self.extensions:
            self.build_cmake(ext)
        super().run()

    def build_cmake(self, ext):
        cwd = pathlib.Path().absolute()
        print(f"-------------> cwd={cwd}")

        # These dirs will be created in build_py, so if you don't have
        # any python sources to bundle, the dirs will be missing
        #build_dir = pathlib.Path(self.build_dir)
        build_dir = cwd / "build"
        build_dir.mkdir(parents=True, exist_ok=True)

        os.chdir(str(build_dir))
        print(f"-------------> cwd={str(build_dir)}")
        extdir = pathlib.Path(self.get_ext_fullpath(ext.name))
        extdir.mkdir(parents=True, exist_ok=True)

        # Example of cmake args
        # Specifying CMAKE_LIBRARY_OUTPUT_DIRECTORY is needed to build the .so
        # according to the naming conventions expected by distutils.
        config = "Debug" if self.debug else "Release"
        cmake_args = [
            "-DCMAKE_LIBRARY_OUTPUT_DIRECTORY=" + str(extdir.parent.absolute()),
            "-DCMAKE_BUILD_TYPE=" + config,
        ]

        # example of build args
        build_args = [
            #"--config", config,
            "--", "-j4",
            "VERBOSE=1"
        ]

        # Call CMake
        os.chdir(str(build_dir))
        print(["cmake", str(cwd)] + cmake_args)
        self.spawn(["cmake", str(cwd)] + cmake_args)

        if not self.dry_run:
            self.spawn(["cmake", "--build", "."] + build_args)
            print(["cmake", "--build", "."] + build_args)
        # Troubleshooting: if fail on line above then delete all possible
        # temporary CMake files including "CMakeCache.txt" in top level dir.

        #self.spawn(["make", "all"])
        os.chdir(str(cwd))

setup(
    name = "pyboost",
    version = "0.0.1",
    #packages = find_packages(),
    #py_modules = ["pyboost"],
    ext_modules = [CMakeExtension("pyboost")],
    cmdclass = { "build_ext" : BuildExt },
)
