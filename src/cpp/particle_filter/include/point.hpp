#ifndef PARTICLE_FILTER_POINT_HPP
#define PARTICLE_FILTER_POINT_HPP

#include <string>

enum CoordinateSystem {
  kSensorCoordinateSystem = 0,
  kVehihicleCoordinateSystem = 1,
  kWorldCoordinateSystem = 2,
  kNotSet = 3,
};


struct Point {
  double x_{};
  double y_{};
  CoordinateSystem coordinate_system_{};

  Point(double x, double y, CoordinateSystem coordinate_system) : x_(x), y_(y), coordinate_system_(coordinate_system) {}
  Point() : x_(0), y_(0), coordinate_system_(CoordinateSystem::kNotSet) {}
};


#endif  // PARTICLE_FILTER_POINT_HPP