public class Solution {  //判断一个数是否在二维数组中
    public boolean searchMatrix(int[][] matrix, int target) {
        if (matrix == null){
            return false;
        }
        int row = 0;
        int col = matrix[0].length -1;
        while (row < matrix.length && col >= 0){  //每次划掉最后一列或者第一行
            int temp = matrix[row][col];
            if (temp == target){
                return true;
            }
            if (temp > target){
                col -= 1;
            } 
            if (temp < target){
                row += 1;
            }
        }
        return false;
    }
}

