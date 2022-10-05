class Solution {
    public int numIslands(char[][] grid) {
        int count = 0;
        for(int i = 0; i < grid.length;++i){
            for(int j = 0; j < grid[0].length;++j){
                if(grid[i][j] == '1'){
                    count++;
                    sinkIsland(grid,i,j);
                }
            }
        }
        return count;
        
    }
    
    public void sinkIsland(char[][] grid, int i, int j){
        if(i < 0 || j < 0 || i >= grid.length || j >= grid[0].length || grid[i][j] != '1'){
            return;
        }
        
        grid[i][j] = '0';
        
        sinkIsland(grid,i + 1,j);
        sinkIsland(grid,i - 1,j);
        sinkIsland(grid,i,j + 1);
        sinkIsland(grid,i,j - 1);
    }
}
