class Solution {
    boolean[] cols;
    boolean[] diag1;
    boolean[] diag2;
    List<List<String>> res;
    boolean[][] board;
    
    public List<List<String>> solveNQueens(int n) {
        res = new ArrayList<>();
        board = new boolean[n][n];
        cols = new boolean[n];
        diag1 = new boolean[2 * n - 1];
        diag2 = new boolean[2 * n - 1];
        
        putQueens(0, n);
        return res;
    }
    
    private boolean isAvailable(int x, int y, int n){
        return !cols[x] && !diag1[x + y] && !diag2[x - y + n - 1];
    }
    
    private void put(int x, int y, int n, boolean isPut){
        cols[x] = isPut;
        diag1[x + y] = isPut;
        diag2[x - y + n - 1] = isPut;
        board[y][x] = isPut;
    }
    
    private void putQueens(int y, int n){
        if(y == n){
            List<String> curr = new ArrayList<>();
            for(int i = 0; i < n; i++){
                StringBuilder sb = new StringBuilder();
                for(int j = 0; j < n; j++){
                    if(board[i][j]){
                        sb.append("Q");
                    } else{
                        sb.append(".");
                    }
                }
                curr.add(sb.toString());
            }
            res.add(curr);
            return;
        }
        for(int x = 0; x < n; x++){
            if(!isAvailable(x, y, n)){
                continue;
            }
            put(x, y, n, true);
            putQueens(y + 1, n);
            put(x, y, n, false);
        }
    }
}