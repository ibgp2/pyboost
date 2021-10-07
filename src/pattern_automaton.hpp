#ifndef PATTERN_AUTOMATON_HPP
#define PATTERN_AUTOMATON_HPP

#include <ostream>    // std::ostream
#include <string>     // std::string
#include <vector>     // std::vector

typedef int State;
typedef std::size_t Label;

const static int BOTTOM = -1;

class PatternAutomaton
{
    public:
        typedef std::vector<    // q
            std::vector<        // r
                State           // a
            >
        > Adjacencies;
    private:
        Adjacencies adjacencies;
        std::size_t alphabet_size;
        std::string word;
    public:
        PatternAutomaton(
            std::size_t num_vertices = 0,
            std::size_t alphabet_size = 0,
            const std::string & word = ""
        );

        void add_vertex();
        void add_edge(State q, State r, Label a);
        int delta(State q, Label a) const;
        std::size_t num_vertices() const;
        std::size_t num_edges() const;
        std::string to_string() const;
        const std::string & get_word() const;
        std::size_t get_alphabet_size() const;
};

std::ostream & operator << (std::ostream & out, const PatternAutomaton & g);

#endif
