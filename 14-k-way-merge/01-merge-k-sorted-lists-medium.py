from __future__ import print_function
from heapq import *
from typing import List


class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


def merge_lists(lists: List[ListNode]):
    result_head, result_tail = None, None
    min_heap = []
    # put the root of each list in the min heap
    for i in range(len(lists)):
        if lists[i].value:
            heappush(min_heap, (lists[i].value, i, lists[i]))
    while min_heap:
        val, idx, node = heappop(min_heap)
        if result_head is None:
            result_head = node
            result_tail = node
        else:
            result_tail.next = node
            result_tail = result_tail.next
        if node.next is not None:
            heappush(min_heap, (node.next.value, idx, node.next))
    return result_head


def main():
    l1 = ListNode(2)
    l1.next = ListNode(6)
    l1.next.next = ListNode(8)

    l2 = ListNode(3)
    l2.next = ListNode(6)
    l2.next.next = ListNode(7)

    l3 = ListNode(1)
    l3.next = ListNode(3)
    l3.next.next = ListNode(4)

    result = merge_lists([l1, l2, l3])
    print("Here are the elements form the merged list: ", end="")
    while result is not None:
        print(str(result.value) + " ", end="")
        result = result.next


if __name__ == "__main__":
    main()
