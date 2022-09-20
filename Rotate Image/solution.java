class Solution {
    public void rotate(int[][] matrix) {
        
        //transpose the matrix and swap the columns to the rows
        for(int row = 0; row < matrix.length; row ++ ){
            for(int col = row; col < matrix.length; col ++){
                int temp = matrix[row][col];
                matrix[row][col] = matrix [col][row];
                matrix[col][row] = temp;
            }
        }
        
        
        //next thing to do is swap the matrix
        
        for(int i = 0; i < matrix.length; i++){
            for(int j = 0; j < (matrix.length/2);j++){
                int temp = matrix[i][j];
                matrix[i][j] = matrix[i][matrix.length-1-j];
                matrix[i][matrix.length-1-j] = temp;
            }
        }
    }
}
