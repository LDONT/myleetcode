public class Solution {        //������������n�����ִ���n
    public int hIndex(int[] citations) {
        int len = citations.length;
        int[] li = new int[len+1];
        for (int i = 0; i < len; i++){   //��ϣ��
            if (citations[i] > len){
                li[len]++;
            } else{
                li[citations[i]]++;
            }
        }
        int t = 0;
        for (int i = len; i >= 0; i--){    //����ֻ����[0��len]��ȡ
            t += li[i];
            if (t >= i){
                return i;
            }
        }
        return 0;
    }
}