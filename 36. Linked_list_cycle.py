## We are using FLoyd's tortoise and Hare algorithm here instead of usign Hash Set for better time complexity.
## Time = O(n)


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 
            if slow == fast:
                return True
            
        return False
