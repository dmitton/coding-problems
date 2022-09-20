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
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode dummyList = new ListNode();
        ListNode temp = dummyList;
        
        while(list1 != null || list2 != null){
            int x = (list1 != null) ? list1.val : 101;
            int y = (list2 != null) ? list2.val : 101;
            
            
            if(x < y) {
                temp.next = new ListNode(x);
                temp = temp.next;
                if(list1 != null){
                    list1 = list1.next;
                }
            }
            else if(x > y){
                temp.next = new ListNode(y);
                temp = temp.next;
                if(list2 != null){
                    list2 = list2.next;
                }
            }
            else if(x == y){
                temp.next = new ListNode(x);
                temp = temp.next;
                temp.next = new ListNode(y);
                temp = temp.next;
                list1 = list1.next;
                list2 = list2.next;
            }
            
        }
    return dummyList.next;
    }
}
