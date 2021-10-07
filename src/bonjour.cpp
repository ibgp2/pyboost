#include "bonjour.hpp"
#include <iostream>

Bonjour::Bonjour(std::string msg, int x):
    m_msg(msg),
    m_int(x)
{
    for (int i = 0; i < 10; i++) {
        vector.push_back(i);
        list.push_back(10 * i);
    }
}

void Bonjour::greet() {
    std::cout << m_msg << std::endl;
}

int Bonjour::sum(int x, int y) {
    return x + y;
}

void Bonjour::set_msg(std::string msg) {
    m_msg = msg;
}

std::string Bonjour::get_msg() const {
    return m_msg;
}

void Bonjour::set_int(int x) {
    m_int = x;
}

int Bonjour::get_int() const {
    return m_int;
}
