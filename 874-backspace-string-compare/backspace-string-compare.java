class Solution {
    public boolean backspaceCompare(String s, String t) {
        Stack<Character> s1 = new Stack<>();
        Stack<Character> t1 = new Stack<>();

        for(int i = 0; i < s.length(); i++) {
            if(s.charAt(i) == '#' && !s1.isEmpty()) {
                s1.pop();
            } else if(s.charAt(i) != '#') {
                s1.push(s.charAt(i));
            }
        }

        for(int i = 0; i < t.length(); i++) {
            if(t.charAt(i) == '#' && !t1.isEmpty()) {
                t1.pop();
            } else if(t.charAt(i) != '#') {
                t1.push(t.charAt(i));
            }
        }

        System.out.println(s1.toString());
        System.out.println(t1.toString());

        return s1.toString().compareTo(t1.toString()) == 0;
    }
}