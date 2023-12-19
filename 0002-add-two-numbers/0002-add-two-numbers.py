# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # traverse both LLs and store vals of all nodes in arrays
        """
         let sum = 0;
    let current = new ListNode(0);
    let result = current;
    
    while(l1 || l2) {
        if(l1) {
            sum += l1.val;
            l1 = l1.next;
        }
        
        if(l2) {
            sum += l2.val;
            l2 = l2.next;
        }
        
        current.next = new ListNode(sum % 10);
        current = current.next;
        
        sum = sum > 9 ? 1 : 0;
    }
    
    if(sum) {
        current.next = new ListNode(sum);
    }
    
    return result.next;
};
        """
        summ = 0
        current = ListNode()
        result = current
        while l1 or l2:
            if l1:
                summ += l1.val
                l1 = l1.next
            if l2:
                summ += l2.val
                l2 = l2.next
                
            current.next = ListNode(summ % 10)
            current = current.next
            if summ > 9:
                summ = 1
            else:
                summ = 0
            
        if summ:
            current.next = ListNode(summ)

        return result.next
        
        
            
        
        
        