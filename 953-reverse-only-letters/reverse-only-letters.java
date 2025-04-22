class Solution {
    public String reverseOnlyLetters(String s) {
        char[] chars = s.toCharArray();
        int start = 0, end = s.length() - 1;

        while(start < end) {
            if(!Character.isLetter(s.charAt(start))) {
                start++;
            } else if(!Character.isLetter(s.charAt(end))) {
                end--;
            } else {
                // swap characters
                char temp = chars[start];
                chars[start] = chars[end];
                chars[end] = temp;
                start++;
                end--;
            }
        }

        return new String(chars);
    }
}