class Solution {
    public int lengthOfLongestSubstring(String s) {
        // have some kind of container that keeps track of the letters in the current
        // substring
        // have a sliding window alg. that adds on whenever we have a character that is 
        // not a duplicate and whenever it is a duplicate, keep incrementing the start
        // counter until we get rid of the duplicate

        int start = 0;
        int end = 0;
        Set<Character> c = new HashSet<>();
        int maxLength = 0;

        for(end = 0; end < s.length(); end++) {
            if(c.contains(s.charAt(end))) {
                while(s.charAt(start) != s.charAt(end)) {
                    c.remove(s.charAt(start));
                    start++;
                }
                start++;
            } 
            c.add(s.charAt(end));
            maxLength = Math.max(maxLength, end - start + 1);
        }

        return maxLength; 
    }
}