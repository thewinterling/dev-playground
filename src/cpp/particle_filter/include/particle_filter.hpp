#ifndef PARTICLE_FILTER_PARTICLE_FILTER_HPP
#define PARTICLE_FILTER_PARTICLE_FILTER_HPP

#include "particle.hpp"

#include <vector>

struct ParticleFilter {
  std::vector<Particle> particles_{};

  ParticleFilter(const int num_particles) {}
};


#endif  // PARTICLE_FILTER_PARTICLE_FILTER_HPP