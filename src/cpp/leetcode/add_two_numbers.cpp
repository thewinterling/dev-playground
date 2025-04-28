
#include <iostream>

struct ListNode {
  int val;
  ListNode* next;
  ListNode() : val(0), next(nullptr) {}
  ListNode(int x) : val(x), next(nullptr) {}
  ListNode(int x, ListNode* next) : val(x), next(next) {}
};

class Solution {
 public:
  ListNode* addTwoNumbers(ListNode* list_node_1, ListNode* list_node_2) {
    ListNode* dummy_head = new ListNode();  // Dummy node to simplify result list construction
    ListNode* current = dummy_head;
    int carry{0};

    while (list_node_1 != nullptr || list_node_2 != nullptr || carry > 0) {
      int value_1{(list_node_1 != nullptr) ? list_node_1->val : 0};
      int value_2{(list_node_2 != nullptr) ? list_node_2->val : 0};

      int sum{value_1 + value_2 + carry};
      carry = sum / 10;

      current->next = new ListNode(sum % 10);
      current = current->next;

      if (list_node_1 != nullptr) list_node_1 = list_node_1->next;
      if (list_node_2 != nullptr) list_node_2 = list_node_2->next;
    }

    return dummy_head->next;  // Return actual head (skip dummy node)
  }
};
