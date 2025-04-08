class Solution {
    public String addStrings(String num1, String num2) {
        int i = num1.length() - 1;
        int j = num2.length() - 1;
        StringBuilder ret = new StringBuilder("");
        int carry = 0;

        while(i >= 0 || j >= 0 || carry != 0) {
            int a = i >= 0 ? num1.charAt(i) - 48 : 0;
            int b = j >= 0 ? num2.charAt(j) - 48 : 0;
            int sum = a + b + carry;
            
            carry = sum / 10;
            sum %= 10;
            ret.append(sum);

            i--;
            j--;
        }

        return ret.reverse().toString();
    }
}