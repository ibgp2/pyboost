Overview
---------

``pyboost`` is a skeleton project aimaing at demonstrating how to wrap a C++ library using the Python Boost Library (and possibly: ``cmake`` and Py++).

Requirements
-------------

Install a C++ compiler, the Python3 library and the Python Boost library.
* Example: under Debian-like distributions, run:

.. code:: shell

  sudo apt update
  sudo apt install g++ python3-dev libboost-python-dev

Conventions
-----------

The project conventions is defined in ``setup.py``.

These files assume that:
* C++ headers are located in ``src/`` (or a sub-directory) and suffixed by ``.hpp``;
* C++ sources are located in ``src/`` (or a sub-directory) and suffixed by ``.cpp``.

You may obviously update these settings.

Build (without Py++ nor cmake)
------------------------------

To expose the C++ classes and functions to Python3, the developper must specify how to wrap them. This is done in ``src/bindings.cpp``. To ease these declarations, some convenient functions are made available in ``src/bindings.hpp``. Note that ``src/bindings_auto.cpp`` is ignored (see ``setup_common.py``) as it is only needed when using Py++.

To enrich the pyboost library
1. Add your C++ classes in ``src``.
2. Enrich consequently ``src/bindings.cpp``.
3. Build and install resulting the python module:

.. code:: shell

  python3 setup.py build
  sudo python3 setup.py install

4. Complete the test suite (see the Testing section).

Compilation (with Py++)
-----------------------

Py++ aims at automating the development of the source file used to bind your C++ library and Python3. The bindings are automatically generated in ``src/bindings_auto.cpp`` and thus ``src/bindings.cpp`` is ignored, as stated in ``setup_common.py``.

1. Install Py++ and its dependencies:

.. code:: shell

  sudo apt install castxml python3-pygccxml python3-pip
  sudo pip3 install pyplusplus

2. Add your C++ classes in ``src``.
3. Build and install resulting the python module:

.. code:: shell

  python3 setup.py build
  sudo python3 setup.py install

4. Complete the test suite (see the Testing section).

Note that Py++ is (unfortunately) not perfect and might fail depending on your C++ code. Recommandations:
* Types involved in setter/getter must be consistent and ``const`` qualifier and must be prefixed as expected in pyplusplus. Otherwise, python properties won't be correctly exposed in ``binding_auto.cpp``.
* Methods should not return const std::string &, as this may cause memory issues when using them through the python module.
* (Default) parameter names are exposed to python, so that you can use them in a kwargs based syntax.

Example: ``foo.hpp``

.. code:: cpp 

  #ifndef FOO_HPP
  #define FOO_HPP
  #include <string>

  class Foo {
    private:
      std::string msg;
    public:
      Foo(std::string msg = ""):
		msg(msg)
	  {}
      std::string get_msg() const { return msg; }
      void set_msg(m) { msg = m; }
  }

  #endif

cmake (work in progress)
------------------------


To build ``pyboost``, an alternative way to build the library consists in using ``cmake``.

``cmake`` is an utility commonly used in C++ projects.  It relies on the ``CMakeLists.txt`` file to auto-generate a ``Makefile`` according to the installed library installed on your system and according to your operating system. The resulting ``Makefile`` is used by the ``make`` command to compile the C++ project.

1. Install ``cmake``:

.. code:: shell

  sudo apt cmake make 

2. Check the project conventions are moved in ``setup_cmake.py`` and in ``CMakeLists.txt``.
3. Compile the project:

.. code:: shell

  python3 setup_cmake.py build 
  sudo python3 setup_cmake.py install 


TODO: solve:

  (ImportError: dynamic module does not define module export function (PyInit_pyboost))

Testing
-------

To test the produced python module, a convenient way is to rely on a test suite (see ``tests/``) that is processed by ``pytest-3``.

In the details, ``pytest-3`` explore each subdirectory and for each file ``test_*.py``, it runs each function with a name prefixed by ``test_``. We recommend to do one test file per C++ class.

1. Install ``pytest-3``:

.. code:: shell

  sudo apt install python3-test

2. Run the whole test suite.

.. code:: shell

  pytest-3 

References
----------

.. _tutorial: https://flanusse.net/interfacing-c++-with-python.html 
.. _boost: https://www.boost.org/doc/libs/1_68_0/libs/python/doc/
.. _pyplusplus: https://github.com/ompl/pyplusplus
.. _stackoverflow: https://stackoverflow.com/

- The tutorial proposed by F. Lanusse [tutorial_].
- The Python boost documentation [boost_]
- The PyPlusPlus GitHub repository [pyplusplus_].
- Stackoverflow [stackoverflow_] (see the numerous pointers in the code, many thanks to the community) :)
