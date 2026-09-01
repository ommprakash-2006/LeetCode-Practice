# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = nextS
class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """

        positions = []

        prev = head
        curr = head.next
        pos = 1

        while curr.next:
            next_node = curr.next

            # Check if current node is a critical point
            if (curr.val > prev.val and curr.val > next_node.val) or \
               (curr.val < prev.val and curr.val < next_node.val):
                positions.append(pos)

            prev = curr
            curr = next_node
            pos += 1

        # Less than 2 critical points
        if len(positions) < 2:
            return [-1, -1]

        # Minimum distance
        min_distance = float('inf')

        for i in range(1, len(positions)):
            distance = positions[i] - positions[i - 1]

            if distance < min_distance:
                min_distance = distance

        # Maximum distance
        max_distance = positions[-1] - positions[0]

        return [min_distance, max_distance]