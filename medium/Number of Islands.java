public class Solution {     //数二维数组中的“孤岛”
    private int m;
    private int n;
    public int numIslands(char[][] grid) {
        m = grid.length;
        if (m == 0) return 0;
        n = grid[0].length;
        int ret = 0;
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                if(grid[i][j] == '1'){
                    mark(grid, i, j);
                    ret++;
                }
            }
        }
        return ret;
    }
    public void mark(char[][] grid, int i, int j){   //把四周的1都标记一遍置0
        if (i < 0 || j < 0 || i >= m || j >= n || grid[i][j] != '1'){
            return;
        }
        grid[i][j] = '0';
        mark(grid, i-1, j);
        mark(grid, i+1, j);
        mark(grid, i, j+1);
        mark(grid, i, j-1);
    }
    
}