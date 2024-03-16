class Solution {
public:
    bool checkXMatrix(vector<vector<int>>& grid) {
        for(int i=0; i<grid.size(); i++){
            if(grid[i][i]==0)
                return false;
            if(grid[i][grid.size()-i-1]==0)
                return false;
            for(int j=0; j<grid[0].size(); j++){
                if(i!=j && j!=grid.size()-i-1){
                    if(grid[i][j]!=0)
                        return false;
                }
            }

        }
        return true;
    }
};
