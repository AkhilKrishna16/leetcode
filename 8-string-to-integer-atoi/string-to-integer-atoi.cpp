class Solution {
public:
    int myAtoi(string s) {
        int i = 0;
        while(i < s.length() && s[i] == ' ') {
            i++;
        }

        // check if positive or negative 
        int signFlag = 1;
        if(!isdigit(s[i])) {
            if(s[i] == '-') {
                signFlag = -1;
            } else if(s[i] == '+') {
                signFlag = 1;
            } else {
                return 0;
            }

            i++;
        }

        // now we are at the first digit; process 0's until not 0
        while(i < s.length() && s[i] == '0') {
            i++;
        }

        if(i < s.length() && !isdigit(s[i])) {
            return 0;
        }

        // we are the first non-zero digit; add values 
        long result = 0;

        while(i < s.length() && isdigit(s[i])) {
            result = result * 10 + (s[i] - '0');
            if(result * signFlag <= INT_MIN) return INT_MIN;
            if(result * signFlag >= INT_MAX) return INT_MAX;
            i++;
        }
        
        return result * signFlag;
    }
};