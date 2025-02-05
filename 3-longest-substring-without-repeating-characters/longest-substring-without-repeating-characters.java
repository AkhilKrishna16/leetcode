class Solution {
    public int lengthOfLongestSubstring(String s) {
        int start = 0;
        int end = 0;
        int maxLength = 0;
        Map<Character, Integer> map = new HashMap<>();

        while(start >= 0 && start < s.length() && end >= 0 && end < s.length()) {
            if(!map.containsKey(s.charAt(end))) {
                map.put(s.charAt(end), end);
            } else {
                start = Math.max(map.get(s.charAt(end)) + 1, start);
                map.put(s.charAt(end), end);
            }
            maxLength = Math.max(end - start + 1, maxLength);
            end++;
        }

        return maxLength;
    }
}