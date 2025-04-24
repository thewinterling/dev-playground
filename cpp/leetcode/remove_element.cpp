#include <cstddef>
#include <vector>

class Solution {
 public:
  int removeElement(std::vector<int>& nums, int value_to_remove) {
    for (size_t i{0}; i < nums.size(); ++i) {
      int current_value{nums[i]};
      if (current_value == value_to_remove) {
        nums.erase(nums.begin() + i);
        --i;
      }
    }
    return nums.size();
  }
};