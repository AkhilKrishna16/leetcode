class Solution {
    public int[] countBits(int n) {
        int[] bits = new int[n + 1];

        // for(int i = 0; i <= n; i++) {
        //     int temp_num = i;
        //     while(temp_num != 0) {
        //         bits[i] += temp_num % 2;
        //         temp_num /= 2;
        //     } 
        // }

        bits[0] = 0;
        int sub = 1;

        for(int i = 1; i <= n; i++) {
            if(sub * 2 == i) {
                sub = i;
            }

            bits[i] = bits[i - sub] + 1;
        }

        return bits;
    }
}