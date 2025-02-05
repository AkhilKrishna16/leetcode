class Solution {
    public int lengthOfLongestSubstring(String s) {
        int start = 0;
        int maxLength = 0;
        Map<Character, Integer> map = new HashMap<>();

        for (int end = 0; end < s.length(); end++) {
            char c = s.charAt(end);
            if (map.containsKey(c)) {
                start = Math.max(start, map.get(c) + 1); // Ensure `start` doesn't move backward
            }
            map.put(c, end); // Update last occurrence
            maxLength = Math.max(maxLength, end - start + 1);
        }

        return maxLength;
    }
}
