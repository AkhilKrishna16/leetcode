class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        // count the number of unique characters that present in p using map.size()
        // iterate using sliding window for a k length and when you add a character to the end, 
        // remove one from that one. if the value for it becomes 0, decreases the count by 1. 
        // if the count becomes 0, then you have a indice to start from and add it to the list. 

        // whenever we transition the window, we start from the beginning 

        Map<Character, Integer> m = new HashMap<>();
        int start = 0, end = 0;
        List<Integer> ans = new ArrayList<>();
        
        for(int i = 0; i < p.length(); i++) {
            m.put(p.charAt(i), m.getOrDefault(p.charAt(i), 0) + 1);
        }

        int count = m.size();
        int k = p.length();

        while(end < s.length()) {
            char last = s.charAt(end);

            if(m.containsKey(last)) {
                m.put(last, m.get(last) - 1);
                if(m.get(last) == 0) {
                    count--;
                }
            }

            if(end - start + 1 < k) {
                end++;
            } else if(end - start + 1 == k) {
                if(count == 0) {
                    ans.add(start);
                }

                char first = s.charAt(start);
                if(m.containsKey(first)) {
                    if(m.get(first) == 0) {
                        count++;
                    }
                    m.put(first, m.get(first) + 1);
                }

                start++;
                end++;
            }
        }

        return ans;
    }
}