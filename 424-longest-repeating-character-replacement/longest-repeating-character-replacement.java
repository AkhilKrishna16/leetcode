class Solution {
    public int characterReplacement(String s, int k) {
        int[] counter = new int[26];
        int maxFreq = 0;
        int ret = 0;
        int start = 0, end = 0;

        for(end = 0; end < s.length(); end++) {
            // we need to check the current character
            char curr = s.charAt(end);
            // add it to frequency
            int index = curr - 'A';
            counter[index]++;
            // update the counter if it is the max frequency
            maxFreq = Math.max(maxFreq, counter[index]);
            // make the check
            if(end - start + 1 - maxFreq > k) {
                // if we have too many replacements, we have start chopping
                while(end - start + 1 - maxFreq > k) {
                    index = s.charAt(start) - 'A';
                    counter[index]--;
                    start++;
                }
            } else {
                ret = Math.max(ret, end - start + 1);
            }
        }

        return ret;
    }
}