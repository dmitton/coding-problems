/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode swapPairs(ListNode head) {
        if(head == null || head.next == null){
            return head;
        }
        
        ListNode temp = new ListNode(0);
        temp.next = head;
        
        ListNode tempPoint = temp;
        
        while(tempPoint.next != null && tempPoint.next.next != null){
            ListNode firstNode = tempPoint.next;
            ListNode secondNode = tempPoint.next.next;
            
            firstNode.next = secondNode.next;
            tempPoint.next = secondNode;
            
            tempPoint.next.next = firstNode;
            tempPoint = tempPoint.next.next;
        }
        return temp.next;
    }
}
