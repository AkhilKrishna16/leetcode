class Solution {
    public String longestPalindrome(String s) {
        int start = 0;
        int end = 0;

        for(int i = 0; i < s.length(); i++) {
            int len1 = expandAroundMiddle(s, i, i);
            int len2 = expandAroundMiddle(s, i, i + 1);
            int len = Math.max(len1, len2);

            if(len > end - start) {
                start = i - ((len - 1) / 2);
                end = i + (len / 2);
            }
        }

        return s.substring(start, end + 1);
    }

    public static int expandAroundMiddle(String s, int a, int b) {
        if(s == null || a > b || a < 0 || b >= s.length()) {
            return 0;
        }

        while(a >= 0 && b < s.length() && s.charAt(a) == s.charAt(b)) {
            a--;
            b++;
        }

        return b - a - 1;
    }
}