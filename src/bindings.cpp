/*
This file is only required if you want to specify manually the Python bindings.
See https://www.boost.org/doc/libs/1_68_0/libs/python/doc/html/tutorial/tutorial/exposing.html
See in setup.py how to turn on bindings_auto.cpp generation.
*/

#include <boost/python.hpp>
#include "bonjour.hpp"
#include "point.hpp"
#include "stl_example.hpp"

// {python <-> STL objects} converters
// The same principle holds for custom C++ objects.
#include "bindings_stl.hpp"
#include <boost/python/suite/indexing/map_indexing_suite.hpp>
#include <boost/python/suite/indexing/vector_indexing_suite.hpp>

// Method1: use custom converter, allowing to manipulate dict and list python-side
static map_to_dict<StlExample::MapStrInt> reg0;
static dict_to_map<StlExample::MapStrInt> reg1;
static list_to_vector<StlExample::Ints> reg2;
static vector_to_list<StlExample::Ints> reg3;

BOOST_PYTHON_MODULE(pyboost)
{
    using namespace boost::python;

    // Class with default named parameter.
    // Named parameters are managed thanks to boost::python::arg
    class_<Bonjour>("Bonjour", init<optional<const std::string &, int> >((
        arg("msg") = "",
        arg("x") = (int) 7
    )))
        .def("greet", &Bonjour::greet, "built on top of 'Bonjour::greet'")
        .def("sum",   &Bonjour::sum)
        // If there is no setter, just omit the 3rd parameter
        .add_property("int", &Bonjour::get_int, &Bonjour::set_int)
        .add_property("msg", &Bonjour::get_msg, &Bonjour::set_msg)
    ;

    class_<Point>("Point", init<optional<int, int> >((
        arg("x") = (int) 0,
        arg("y") = (int) 0
    )))
        // Access to member (def_readwrite | def_readonly)
        .def_readwrite("x", &Point::x)
        .def_readwrite("y", &Point::y)
    ;

    // Functions
    typedef int (*extract_function_type)(Point const &);
    def("extract_x", extract_function_type(&::extract_x), arg("pt"));
    def("extract_y", extract_function_type(&::extract_y), arg("pt"));

    // Class with STL containers (std::vector, std::map)
    // Note the two methods are exclusive.

    // Method2
    // Expose the STL-based object to python.
    // Python-side, declare an Floats and populate it using append and exend methods.
    class_<StlExample::Floats>("Floats")
        .def(vector_indexing_suite<StlExample::Floats>());
    class_<StlExample::MapStrFloat>("MapStrFloat")
        .def(map_indexing_suite<StlExample::MapStrFloat>());


    class_<StlExample>("StlExample")
        // Method1:
        // Thanks to converters, we can use python-side a normal dict or list
        .add_property(
            "ints",
            &StlExample::get_ints,
            &StlExample::set_ints
        )
        .add_property(
            "map_str_int",
            &StlExample::get_map_str_int,
            &StlExample::set_map_str_int
        )
        // Method2
        .add_property(
            "floats",
            &StlExample::get_floats,
            &StlExample::set_floats
        )
        .add_property(
            "map_str_float",
            &StlExample::get_map_str_float,
            &StlExample::set_map_str_float
        )
    ;

}
