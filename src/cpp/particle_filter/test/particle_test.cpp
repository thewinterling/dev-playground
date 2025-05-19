#include "particle.hpp"

#include <gtest/gtest.h>

TEST(ParticleTest, DefaultConstructor) {
  Particle p;
  EXPECT_EQ(p.theta_, 0);
  EXPECT_EQ(p.weight_, 0);
}

TEST(ParticleTest, ParameterizedConstructor) {
  Particle p(Point(1, 2, CoordinateSystem::kSensorCoordinateSystem), 1.57, 0.5);
  EXPECT_EQ(p.theta_, 1.57);
  EXPECT_EQ(p.weight_, 0.5);
  EXPECT_EQ(1, 2);
}