class Solution {
    public String longestCommonPrefix(String[] strs) {
        if(strs == null){
            return "";
        }
        if(strs[0].length() == 0){
            return "";
        }
        if(strs.length == 1){
            return strs[0];
        }
        int index = 0;
        while(true){
            boolean isDifferent = false;
            for(int i = 1;i < strs.length;++i){
                if(strs[i].length() <= index || strs[i-1].length() <= index || strs[i].charAt(index) != strs[i - 1].charAt(index) ){
                    isDifferent = true;
                }
            }
            if(isDifferent == true){
                break;
            }
            else{
                index += 1;
            }
        }
        return strs[0].substring(0,index);
    }
}
