public class Solution {        //Ѱ�ҷ��λ��
    public int findPeakElement(int[] nums) {
        int end = nums.length - 1;
        int start = 0;
        int mid;
        while(start < end){     //���ֲ��ң���֤start������ߣ�end�����ұ�
            mid = start + (end - start)/2;
            if(nums[mid] < nums[mid + 1]){
                start = mid + 1;
            }
            if(nums[mid] > nums[mid + 1]){
                end = mid; 
            }
        }
        return start; 
    }     
}