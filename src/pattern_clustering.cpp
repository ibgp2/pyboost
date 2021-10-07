#include "pattern_clustering.hpp"

#include <iostream>
using namespace std;

PatternClustering::PatternClustering(
    const PatternAutomata & pattern_automata,
    const Densities & densities,
    double threshold
):
    pattern_automata(pattern_automata),
    densities(densities),
    threshold(threshold)
{}


void PatternClustering::compute() {
    cout << "compute" << endl;
}
