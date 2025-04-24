#include <set>
#include <vector>

class Solution {
 public:
  std::vector<int> twoSum(std::vector<int>& nums, int target) {
    for (int i{0}; i < nums.size(); ++i) {
      int value{nums[i]};
      for (int j{i + 1}; j < nums.size(); ++j) {
        int second_value{nums[j]};
        if (value + second_value == target) {
          return std::vector<int>({i, j});
        }
      }
    }
    return std::vector<int>({-1, -1});
  }
};