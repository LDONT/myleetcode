public class Solution {      //康威生命游戏
    public void gameOfLife(int[][] board) {
        int m = board.length;
        if (m == 0){
            return;
        }
        int n = board[0].length;
        for (int i = 0; i < m; i++){    //根据周边存活保存下个状态
            for (int j = 0; j < n; j++){
                if (board[i][j] == 0 && numlive(board, i, j, m, n) == 3){
                    board[i][j] = 2;
                }
                if (board[i][j] == 1 && (numlive(board, i, j, m, n) == 2 || numlive(board, i, j, m, n) == 3)){
                    board[i][j] = 3;
                }
            }
        }
        for (int i =0; i < m; i++){     // 通过移位，实现in-place，无需额外内存
            for (int j = 0; j < n; j++){
                board[i][j] >>= 1;
            }
        }
    }
    private int numlive(int[][] board, int i, int j, int m, int n){
        int live = 0;
        for (int p = Math.max(i-1, 0); p <= Math.min(i+1, m-1); p++){
            for (int q = Math.max(j-1, 0); q <= Math.min(j+1, n-1); q++){
                live += board[p][q] & 1;
            }
        }
        live -= (board[i][j] & 1);
        return live;
    }
}