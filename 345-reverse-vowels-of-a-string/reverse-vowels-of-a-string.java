class Solution {

    public static void swap(char[] c, int front, int back) {
        char temp = c[front];
        c[front] = c[back];
        c[back] = temp;
    }

    public String reverseVowels(String s) {
        char[] c = s.toCharArray();
        int front = 0;
        int back = s.length() - 1;

        Set<Character> vowels = new HashSet<>();
        vowels.add('a');
        vowels.add('e');
        vowels.add('i');
        vowels.add('o');
        vowels.add('u');
        vowels.add('A');
        vowels.add('E');
        vowels.add('I');
        vowels.add('O');
        vowels.add('U');

        while(front <= back) {
            if(vowels.contains(c[front]) && vowels.contains(c[back])) {
                swap(c, front, back);
                front++;
                back--;
                continue;
            } 

            if(vowels.contains(c[front])) {
                back--;
            } else if(vowels.contains(c[back])) {
                front++;
            } else {
                front++;
                back--;
            }
        }

        return new String(c);
    }
}