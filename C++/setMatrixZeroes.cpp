class Solution{
public:
    void zeroRow(vector<vector<int>>& matrix, int f){
        for(int i=0; i<matrix[f].size(); i++){
            matrix[f][i]=0;
        }
    }

    void zeroColumn(vector<vector<int>>& matrix, int c){
        for(int i=0; i<matrix.size(); i++){
            matrix[i][c]=0;
        }
    }

    void setZeroes(vector<vector<int>>& matrix){
        vector<pair<int,int>> v;
        for(int i=0; i<matrix.size(); i++){
            for(int j=0; j<matrix[i].size(); j++){
                if(matrix[i][j]==0){
                    v.push_back(make_pair(i,j));
                }
            }
        }

        for(auto i : v){
            cout<<i.first<<" , "<< i.second<<endl;
            zeroRow(matrix, i.first);
            zeroColumn(matrix, i.second);
        }
    }
};
