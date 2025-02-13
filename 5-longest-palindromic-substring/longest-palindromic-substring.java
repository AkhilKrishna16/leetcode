class Solution {
    public String longestPalindrome(String s) {
        if(s == null || s.length() < 1) return "";

        int start = 0;
        int end = 0;

        for(int i = 0; i < s.length(); i++) {
            int len1 = expandUponMiddle(s, i, i);
            int len2 = expandUponMiddle(s, i, i + 1);
            int len = Math.max(len1, len2);

            if(len > end - start) {
                start = i - ((len - 1) / 2);
                end = i + (len / 2);
            }
        }

        return s.substring(start, end + 1);
    }

    public static int expandUponMiddle(String s, int a, int b) {
        if(a > b || s == null) return 0;

        while(a >= 0 && b < s.length() && s.charAt(a) == s.charAt(b)) {
            a--;
            b++;
        }

        return b - a - 1;
    }
}