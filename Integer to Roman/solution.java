class Solution {
    public String intToRoman(int num) {
        String answer = "";
        if(num % 1000 != num){
            int number = num / 1000;
            for(int i = 0; i < number;++i){
                answer += "M";
            }
            num = num % 1000;
            System.out.print(num);
        }
        if(num % 900 != num){
            answer += "CM";
            num = num % 900;
            System.out.print("\n" + num);
        }
        if(num % 500 != num){
            answer += "D";
            num = num % 500;
            System.out.print("\n" + num);
        }
        if(num % 400 != num){
            answer += "CD";
            num = num % 400;
            System.out.print("\n" + num);
        }
        if(num % 100 != num){
            int number = num / 100;
            for(int i = 0; i < number;++i){
                answer += "C";
            }
            num = num % 100;
            System.out.print("\n" + num);
        }
        if(num % 90 != num){
            answer += "XC";
            num = num % 90;
            System.out.print("\n" + num);
        }
        if(num % 50 != num){
            answer += "L";
            num = num % 50;
            System.out.print("\n" + num);
        }
        if(num % 40 != num){
            answer += "XL";
            num = num % 40;
            System.out.print("\n" + num);
        }
        if(num % 10 != num){
            int number = num / 10;
            for(int i = 0; i < number;++i){
                answer += "X";
            }
            num = num % 10;
            System.out.print("\n" + num);
        }
        if(num % 9 != num){
            answer += "IX";
            num = num % 9;
            System.out.print("\n" + num);
        }
        if(num % 5 != num){
            answer += "V";
            num = num % 5;
            System.out.print("\n" + num);
        }
        if(num % 4 != num){
            answer += "IV";
            num = num % 4;
            System.out.print("\n" + num);
        }
        if(num <= 3){
            for(int i = 0; i < num;++i){
                answer += "I";
            }
        }
        return answer;
    }
}
