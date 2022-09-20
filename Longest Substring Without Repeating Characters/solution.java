import java.util.*;
class Solution {
    public int lengthOfLongestSubstring(String s) {
        if(s.equals("")){
            return 0;
        }
        else if(s.length() == 1){
            return 1;
        }
       
        Map<String,Integer>subStringMap = new HashMap();
        
        
        
        //for loop to run through everything
        for(int i = 0; i < s.length() - 1;++i){
            String letter = Character.toString(s.charAt(i));
            String sequence = letter;
            int counter = 1;
            int temp = i + 1;
            while(!(sequence.contains(Character.toString(s.charAt(temp))))){
                counter += 1;
                sequence += Character.toString(s.charAt(temp));
                if(temp == s.length() - 1){
                    break;
                }
                else{
                    temp = temp + 1;
                }
            }
            System.out.print(counter + " " + sequence + "\n");   
            subStringMap.put(sequence, counter);
        }
        
        
        int max = 0;
        for(Map.Entry<String,Integer> entry : subStringMap.entrySet()){
            if(entry.getValue() > max){
                max = entry.getValue();
            }
        }
        System.out.print(subStringMap);
        return max;
    }
}
