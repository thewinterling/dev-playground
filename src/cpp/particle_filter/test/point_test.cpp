#include "point.hpp"

#include "particle.hpp"

#include <gtest/gtest.h>

TEST(PointTest, DefaultConstructor) {
  Point p;
  EXPECT_EQ(p.x_, 0);
  EXPECT_EQ(p.y_, 0);
  EXPECT_EQ(p.coordinate_system_, CoordinateSystem::kNotSet);
}

TEST(PointTest, ParameterizedConstructor) {
  Point p(1.57, 0.5, CoordinateSystem::kSensorCoordinateSystem);
  EXPECT_EQ(p.x_, 1.57);
  EXPECT_EQ(p.y_, 0.5);
  EXPECT_EQ(p.coordinate_system_, CoordinateSystem::kSensorCoordinateSystem);
}