class Solution {
public:

    bool dfs(vector<vector<char>>& board, string word, int row, int col, int i) {
        if(i == word.length()) {
            return true;
        } 

        if (row < 0||row == board.size() || col < 0 || col == board[0].size() || board[row][col] != word[i] || board[row][col] == '#') {
            return false;
        }

        char temp = board[row][col];
        board[row][col] = '#';

        bool result = dfs(board, word, row + 1, col, i + 1) || dfs(board, word, row - 1, col, i + 1) || dfs(board, word, row, col + 1, i + 1) || dfs(board, word, row, col - 1, i + 1);

        board[row][col] = temp;
        return result;
    }

    bool exist(vector<vector<char>>& board, string word) {
        // only dfs from characters that are the same as the starting character of `word`
        // keep track of some index `i` which is the index into word.
        // on the dfs, first check if the character we are currently on for the cell is equal to the index 
        // keep a visited set, to make sure that we are not revisiting cells on a specific path -> use unordered_set
        for(int row = 0; row < board.size(); row++) {
            for(int col = 0; col < board[0].size(); col++) {
                if(dfs(board, word, row, col, 0) == true) {
                    return true;
                }
            }
        }

        return false;
    }
};