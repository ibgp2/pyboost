#ifndef PATTERN_CLUSTERING_HPP
#define PATTERN_CLUSTERING_HPP

#include <vector>
#include "pattern_automaton.hpp"

class PatternClustering {
    public:
        typedef std::vector<PatternAutomaton> PatternAutomata;
        typedef std::vector<double> Densities;
    private:
        PatternAutomata pattern_automata;
        Densities densities;
    public:
        double threshold;

        PatternClustering(
            const PatternAutomata & pattern_automata,
            const Densities & densities,
            double threshold
        );

        void compute();
};

#endif

