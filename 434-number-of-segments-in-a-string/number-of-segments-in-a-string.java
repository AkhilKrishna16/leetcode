class Solution {
    public int countSegments(String s) {
        if(s.equals("")) {
            return 0;
        }

        int count = 0;

        for(int i = 0; i < s.length() - 1; i++) {
            if(s.charAt(i) != ' ' && s.charAt(i + 1) == ' ') {
                count++;
            }
        }

        if(s.charAt(s.length() - 1) != ' ') {
            count++;
        }

        return count;
    }
}
