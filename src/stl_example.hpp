#ifndef INDEXED_HPP
#define INDEXED_HPP

#include <vector>
#include <map>

class StlExample {
    public:
        typedef std::vector<int> Ints;
        typedef std::map<std::string, int> MapStrInt;
        typedef std::vector<double> Floats;
        typedef std::map<std::string, double> MapStrFloat;
    private:
        Ints ints;
        Floats floats;
        MapStrInt map_str_int;
        MapStrFloat map_str_float;
    public:
        StlExample() {
            ints = {1, 2, 3};
            floats = {1.1, 2.2, 3.3};
            map_str_int["a"] = 10;
            map_str_int["b"] = 20;
            map_str_int["c"] = 30;
            map_str_float["a"] = 10.1;
            map_str_float["b"] = 20.2;
            map_str_float["c"] = 30.3;
        }

        Ints get_ints() const {
            return this->ints;
        }

        void set_ints(Ints ints0) {
            this->ints = ints0;
        }

        MapStrInt get_map_str_int() const {
            return this->map_str_int;
        }

        void set_map_str_int(MapStrInt map) {
            this->map_str_int = map;
        }

        Floats get_floats() const {
            return this->floats;
        }

        void set_floats(Floats floats0) {
            this->floats = floats0;
        }

        MapStrFloat get_map_str_float() const {
            return this->map_str_float;
        }

        void set_map_str_float(MapStrFloat map) {
            this->map_str_float = map;
        }
};

#endif

