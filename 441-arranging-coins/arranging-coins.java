class Solution {
    public int arrangeCoins(int n) {
        // int i = 0;
        // int j = 0;

        // while(j + i + 1 <= n) {
        //     i++;
        //     j += i;
        // }

        // return i;
        return (int)(Math.sqrt(2 * (long)n + 0.25) - (0.5));
    }
}