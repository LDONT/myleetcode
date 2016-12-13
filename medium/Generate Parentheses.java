public class Solution {     //括号的组合方式
    public List<String> generateParenthesis(int n) {
        List<String> li = new ArrayList<String>();
        backtracking(li, "", n, 0, 0);
        return li;
    }
    public void backtracking(List list, String str, int n, int p, int q){
        if (p+q == 2*n){
            list.add(str);
            return;
        }
        if (p < n){
            backtracking(list, str + '(', n, p + 1, q);
        }
        if (q < p){
            backtracking(list, str + ')', n, p, q+1);
        }
    }
}