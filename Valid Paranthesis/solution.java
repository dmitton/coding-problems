class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<Character>();
        
        
        for(int i = 0; i < s.length();++i){
            if(s.charAt(i) == '(' || s.charAt(i) == '{' || s.charAt(i) == '['){
                System.out.print(s.charAt(i));
                stack.push(s.charAt(i));
            }
            else if(s.charAt(i) == ')' || s.charAt(i) == '}' || s.charAt(i) == ']'){
                if(stack.empty() == true){
                    return false;
                }
                if(s.charAt(i) == ')'){
                    char symbol = stack.peek();
                    if(symbol == '('){
                        stack.pop();
                        continue;
                    }
                    else{
                        return false;
                    }
                }
                else if(s.charAt(i) == ']'){
                    char symbol = stack.peek();
                    if(symbol == '['){
                        stack.pop();
                        continue;
                    }
                    else{
                        return false;
                    }
                }
                else if(s.charAt(i) == '}'){
                    char symbol = stack.peek();
                    if(symbol == '{'){
                        stack.pop();
                        continue;
                    }
                    else{
                        return false;
                    }
                }
            }
        }
        
        if(stack.empty() != true){
            return false;
        }
        return true;
    }
}
