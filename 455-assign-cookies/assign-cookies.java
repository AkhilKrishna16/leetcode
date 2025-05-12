class Solution {
    public int findContentChildren(int[] g, int[] s) {
        // first pointer for the greed
        // second pointer for the cookies, 
        // whenever we move the second pointer, we are giving the current first pointer their cookie
        
        int greed = 0;
        int cookie = 0;

        Arrays.sort(g);
        Arrays.sort(s);
        
        while(greed < g.length && cookie < s.length) {
            if(g[greed] <= s[cookie]) {
                cookie++;
                greed++;
            } else {
                cookie++;
            }
        }

        return greed;
    }
}