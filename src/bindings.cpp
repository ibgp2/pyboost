/*
This file is only required if you want to specify manually the Python bindings.
See https://www.boost.org/doc/libs/1_68_0/libs/python/doc/html/tutorial/tutorial/exposing.html
See in setup.py how to turn on bindings_auto.cpp generation.
*/

#include <boost/python.hpp>
#include "pattern_clustering.hpp"
#include "bindings_stl.hpp"

// {python <-> STL objects} converters
// Custom converter, allowing to manipulate dict and list python-side
static list_to_vector<PatternClustering::PatternAutomata> reg1;
static vector_to_list<PatternClustering::PatternAutomata> reg2;
static list_to_vector<PatternClustering::Densities> reg3;
static vector_to_list<PatternClustering::Densities> reg4;

BOOST_PYTHON_MODULE(pattern_clustering) // Pass the python module name (as defined in setup.py)
{
    using namespace boost::python;

    class_<PatternAutomaton>(
        "PatternAutomaton",
        init<optional<
            std::size_t,
            std::size_t,
            const std::string &
        > > ((
            arg("num_vertices") = 0,
            arg("alphabet_size") = 0,
            arg("word") = ""
        ))
    )
        .def("add_vertex",      &PatternAutomaton::add_vertex)
        .def("add_edge",        &PatternAutomaton::add_edge)
        .def("num_vertices",    &PatternAutomaton::num_vertices)
        .def("num_edges",       &PatternAutomaton::num_edges)
        .def("alphabet_size",   &PatternAutomaton::get_alphabet_size)
        .def("__str__",         &PatternAutomaton::to_string)
    ;

    class_<PatternClustering>(
        "PatternClustering",
        init<
            const PatternClustering::PatternAutomata &,
            const PatternClustering::Densities &,
            double
        > ((
            arg("pattern_automata"),
            arg("densities"),
            arg("threshold")
        ))
    )
        .def_readwrite("threshold", &PatternClustering::threshold)
        .def("compute", &PatternClustering::compute)
    ;
}
