#ifndef POINT_HPP
#define POINT_HPP

// Based on https://github.com/gatoatigrado/pyplusplusclone/blob/master/pyplusplus_dev/examples/custom_code_creator/properties.hpp

struct Point {
    explicit Point(int x = 0, int y = 0):
        x(x),
        y(y)
    {}

    int x;
    int y;
};

inline int extract_x(const Point & pt) {
    return pt.x;
}

inline int extract_y(const Point & pt) {
    return pt.y;
}

#endif
