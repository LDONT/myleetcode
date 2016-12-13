public class Solution {       //带括号的字符串加减运算
    public int calculate(String s) {
        int n = s.length() - 1;
        int result = 0;
        int sign = 1;
        Stack<Integer> stack = new Stack<Integer>();
        for (int i = 0; i <= n; i++){
            if (Character.isDigit(s.charAt(i))){
                int temp = s.charAt(i) - '0';
                while (i+1 <= n && Character.isDigit(s.charAt(i+1))){
                    temp = temp*10 + s.charAt(i+1) - '0';
                    i++;
                }
                result += temp * sign;
            }
            else if (s.charAt(i) == '+'){
                sign = 1;
            }
            else if (s.charAt(i) == '-'){
                sign = -1;
            }
            else if (s.charAt(i) == '('){
                stack.push(result);
                stack.push(sign);
                result = 0;
                sign = 1;
            }
            else if (s.charAt(i) == ')'){
                result = result * stack.pop() + stack.pop();
            }
        }
        return result;
    }
}