cmake_minimum_required(VERSION 3.5)
set(name "pyboost")
project(${name})

# Inputs: *.cpp and *.hpp
set(src_dir "${PROJECT_SOURCE_DIR}/src")
#message("src_dir=${src_dir}")
set(hdr_dir "${src_dir}")
#message("hdr_dir=${hdr_dir}")

# Outputs: installed *.hpp and *.so
#set(out_dir "${PROJECT_SOURCE_DIR}/out")
#set(install_inc_dir "${out_dir}/include/${PROJECT_NAME}")
#message("install_inc_dir=${install_inc_dir}")
#set(install_lib_dir "${out_dir}/lib")
set(install_lib_dir "${PROJECT_SOURCE_DIR}/${name}")
message("install_lib_dir=${install_lib_dir}")

# Compilation flags
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11 -W -Wall")

# Discards some (irrelevant) compilation warnings
add_definitions(-DBOOST_BIND_GLOBAL_PLACEHOLDERS -DBOOST_ALLOW_DEPRECATED_HEADERS)

# Requirements
# - python
find_package(PythonLibs ${PYTHON_VERSION_STRING} REQUIRED)
include_directories(${PYTHON_INCLUDE_DIRS})
# - libboost_python39
find_package(Boost COMPONENTS python REQUIRED)
include_directories(${Boost_INCLUDE_DIR})

# Lists provided *.hpp and *.cpp 
file(GLOB_RECURSE cpps "${src_dir}/*.cpp")
file(GLOB_RECURSE hpps "${hdr_dir}/*.hpp")
#include_directories("${hdr_dir}")

#--------------------------------------------------------
# bindings.cpp
#--------------------------------------------------------

# Define target "${name}"
add_library(${name} SHARED ${cpps})
# Without this, any build libraries automatically have names "lib{x}.so"
set_target_properties(${name} PROPERTIES PREFIX "")
target_link_libraries(${name} ${Boost_LIBRARIES} ${PYTHON_LIBRARIES})
message("Boost_LIBRARIES=${Boost_LIBRARIES}")
message("PYTHON_LIBRARIES=${PYTHON_LIBRARIES}")

# Define target "install" 
install (TARGETS ${name} DESTINATION ${install_lib_dir} )
#install (FILES ${hpps} DESTINATION ${install_inc_dir} )

