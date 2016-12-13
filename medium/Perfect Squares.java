public class Solution {     //���ٵ�ƽ���������
    public int numSquares(int n) {
        int[] li = new int[n+1];
        //Arrays.fill(li, Integer.MAX_VALUE);
        //li[0] = 0;
        for (int i = 1; i <= n; i++){    //��̬�滮
            int min = Integer.MAX_VALUE;
            for (int j = 1; j*j <= i; j++){
                min = Math.min(min, li[i-j*j]+1);
            }
            li[i] = min;
        }
        return li[n];
    }
}