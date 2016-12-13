public class Solution {  //�ж�һ�����Ƿ��ڶ�ά������
    public boolean searchMatrix(int[][] matrix, int target) {
        if (matrix == null){
            return false;
        }
        int row = 0;
        int col = matrix[0].length -1;
        while (row < matrix.length && col >= 0){  //ÿ�λ������һ�л��ߵ�һ��
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

