class Solution {
    public int romanToInt(String s) {
        int total = 0;
            for(int i = 0;i < s.length();++i){
                if(s.charAt(i) == 'I'){
                    if(i != s.length() -1){
                        if(s.charAt(i+1) == 'V'){
                            total += 4;
                            total -= 5;
                        }
                        else if(s.charAt(i + 1) == 'X'){
                            total += 9;
                            total -= 10;
                        }
                        else{
                            total += 1;
                        }
                    }
                    else{
                        total += 1;
                    }
                }
                else if(s.charAt(i) == 'V'){
                    total += 5;
                }
                else if(s.charAt(i) == 'X'){
                    if(i != s.length() -1){
                        if(s.charAt(i+1) == 'L'){
                            total += 40;
                            total -= 50;
                        }
                        else if(s.charAt(i + 1) == 'C'){
                            total += 90;
                            total -= 100;
                        }
                        else{
                            total += 10;
                        }
                    }
                    else{
                        total += 10;
                    }

                }
                else if(s.charAt(i) == 'L'){
                    total += 50;
                }
                else if(s.charAt(i) == 'C'){
                    if(i != s.length() -1){
                        if(s.charAt(i+1) == 'D'){
                            total += 400;
                            total -= 500;
                        }
                        else if(s.charAt(i + 1) == 'M'){
                            total += 900;
                            total -= 1000;
                        }
                        else{
                            total += 100;
                        }
                    }
                    else{
                        total += 100;
                    }
                }
                else if(s.charAt(i) == 'D'){
                    total += 500;
                }
                else if(s.charAt(i) == 'M'){
                    total += 1000;
                }

            }

            return total;
    }
}
