# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev=head
        cur=head.next
        first_cp=-1
        second_cp=-1
        min_dist=1e9
        index=1
        while cur and cur.next:
            nxt=cur.next
            maxima=cur.val>prev.val and cur.val>nxt.val
            minima=cur.val<prev.val and cur.val<nxt.val
            if minima or maxima:
                if first_cp==-1:
                    first_cp=index
                else:
                    min_dist=min(min_dist,index-second_cp)
                second_cp=index
            prev=cur
            cur=nxt
            index=index+1
        if min_dist==1e9:
            return [-1,-1]
        max_dist=second_cp-first_cp
        return [min_dist,max_dist]
        