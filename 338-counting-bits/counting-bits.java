class Solution {
    public int[] countBits(int n) {
        int[] bits = new int[n + 1];

        for(int i = 0; i <= n; i++) {
            int temp_num = i;
            while(temp_num != 0) {
                bits[i] += temp_num % 2;
                temp_num /= 2;
            } 
        }

        return bits;
    }
}