#pragma once
#include <iostream>
#include <string>
class Rectangle {
public:
    Rectangle() = default;
    Rectangle(std::string color, double height, double width)
        : m_color{ color }, m_height{ height }, m_width{ width }
    {}
    void setHeight(double height,){
        m_height = height
    }
    void setColor(std::string color, ) {
        m_color = color
    }
    void setWidth(double width, ) {
        m_width = width
    }
    double getHeight() const{
        return m_height
    }
    double getWidth() const{
        return m_width
    }
    std::string getColor() const{
        return m_color
    }
    double getPerimeter() const {
        return 2 * (m_height + m_width);
    }

    double getArea() const {
        return m_height * m_width;
    }
private:
    std::string m_color = "";
    double m_width = 4.0;
    double m_height = 15.0;
};