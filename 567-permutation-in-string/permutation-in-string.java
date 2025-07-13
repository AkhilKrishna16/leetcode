class Solution {
    public boolean checkInclusion(String s1, String s2) {
        // "eidbaooo"

        // i have to create a map that contains characters of s1

        Map<Character, Integer> s1Count = new HashMap<>();

        for(int i = 0; i < s1.length(); i++) {
            s1Count.put(s1.charAt(i), s1Count.getOrDefault(s1.charAt(i), 0) + 1);
        }

        int start = 0, end = 0;
        Map<Character, Integer> m = new HashMap<>();

        for(end = 0; end < s2.length(); end++) {
            m.put(s2.charAt(end), m.getOrDefault(s2.charAt(end), 0) + 1);
            
            if(end - start + 1 > s1.length()) {
                m.put(s2.charAt(start), m.get(s2.charAt(start)) - 1);
                if(m.get(s2.charAt(start)) == 0) {
                    m.remove(s2.charAt(start));
                }
                start++;
            }

            if(m.equals(s1Count)) {
                return true;
            }
        }

        return false;
    }
}