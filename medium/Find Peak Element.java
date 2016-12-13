public class Solution {        //寻找峰点位置
    public int findPeakElement(int[] nums) {
        int end = nums.length - 1;
        int start = 0;
        int mid;
        while(start < end){     //二分查找，保证start大于左边，end大于右边
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