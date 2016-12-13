public class Solution {        //数组中至少有n个数字大于n
    public int hIndex(int[] citations) {
        int len = citations.length;
        int[] li = new int[len+1];
        for (int i = 0; i < len; i++){   //哈希表
            if (citations[i] > len){
                li[len]++;
            } else{
                li[citations[i]]++;
            }
        }
        int t = 0;
        for (int i = len; i >= 0; i--){    //返回只能在[0，len]中取
            t += li[i];
            if (t >= i){
                return i;
            }
        }
        return 0;
    }
}