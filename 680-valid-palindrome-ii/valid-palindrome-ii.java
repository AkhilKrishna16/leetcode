class Solution {
    public boolean checkPalindrome(String s) {
        int left = 0;
        int right = s.length() - 1;

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
                return checkPalindrome(s.substring(left + 1, right + 1)) || checkPalindrome(s.substring(left, right));
            } else {
                left++;
                right--;
            }
        }

        return true;
    }
}