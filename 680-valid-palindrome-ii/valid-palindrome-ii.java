class Solution {
    public boolean checkPalindrome(String s, int start, int end) {
        int left = start;
        int right = end;

        while(left < right) {
            if(s.charAt(left) != s.charAt(right)) {
                return false;
            } else {
                left++;
                right--;
            }
        }

        return true;
    }
    public boolean validPalindrome(String s) {
        int left = 0;
        int right = s.length() - 1;

        while(left < right) {
            if(s.charAt(left) != s.charAt(right)) {
                return checkPalindrome(s, left + 1, right) || checkPalindrome(s, left, right - 1);
            } else {
                left++;
                right--;
            }
        }

        return true;
    }
}