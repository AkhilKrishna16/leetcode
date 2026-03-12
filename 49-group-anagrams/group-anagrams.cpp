class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> m;

        for(int i = 0; i < strs.size(); i++) {
            string copy = strs[i];
            sort(copy.begin(), copy.end());
            
            if(m.contains(copy)) {
                m[copy].push_back(strs[i]);
            } else {
                vector<string> value;
                value.push_back(strs[i]);
                m[copy] = value;
            }
        }

        vector<vector<string>> res;
        for(const auto &pair: m) {
            res.push_back(pair.second);
        }

        return res;
    }
};