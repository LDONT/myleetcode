public class Solution {     //最少的平方数字相加
    public int numSquares(int n) {
        int[] li = new int[n+1];
        //Arrays.fill(li, Integer.MAX_VALUE);
        //li[0] = 0;
        for (int i = 1; i <= n; i++){    //动态规划
            int min = Integer.MAX_VALUE;
            for (int j = 1; j*j <= i; j++){
                min = Math.min(min, li[i-j*j]+1);
            }
            li[i] = min;
        }
        return li[n];
    }
}