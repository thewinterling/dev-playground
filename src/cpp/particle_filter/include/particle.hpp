#ifndef PARTICLE_FILTER_PARTICLE_HPP
#define PARTICLE_FILTER_PARTICLE_HPP

#include "point.hpp"

struct Particle {
  Point point_{};
  double theta_;
  double weight_;

  Particle(Point point, double theta, double weight) : point_(point), theta_(theta), weight_(weight) {}
  Particle() : point_(Point(0, 0, CoordinateSystem::kSensorCoordinateSystem)), theta_(0), weight_(0) {}
};


#endif  // PARTICLE_FILTER_PARTICLE_HPP