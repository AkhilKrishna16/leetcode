class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        // count the number of unique characters and their respective occurances in p
        // then iterate s using a sliding window alg. and every time u run into a `p char`, decrement its count
        // if that characters count goes to zero, record the number of unique characters less by 1
        // at the end, if we have k character substring, then shift the start index
        // if the start index increases and the start index character was in the map, increment it and count 
        // if necessary. iterate both start and end at the point. if less than k characters, just end++

        Map<Character, Integer> m = new HashMap<>();
        int start = 0, end = 0;
        List<Integer> ans = new ArrayList<>();

        for(int i = 0; i < p.length(); i++) {
            m.put(p.charAt(i), m.getOrDefault(p.charAt(i), 0) + 1);
        }

        int count = m.size();

        for(end = 0; end < s.length(); end++) {
            char endChar = s.charAt(end);
            if(m.containsKey(endChar)) {
                m.put(endChar, m.get(endChar) - 1);
                if(m.get(endChar) == 0) {
                    count--;
                }
            }

            if(end - start + 1 == p.length()) {
                if(count == 0) {
                    ans.add(start);
                }

                char startChar = s.charAt(start);
                if(m.containsKey(startChar)) {
                    if(m.get(startChar) == 0) {
                        count++;
                    }

                    m.put(startChar, m.get(startChar) + 1);
                }

                start++;
            }
        }

        return ans;

       
    }
}