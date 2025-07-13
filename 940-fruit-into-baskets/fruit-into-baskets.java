class Solution {
    public int totalFruit(int[] fruits) {
        // iterate over the list by using Set<Integer> as a container for characters in the window
        // have a sliding window whenever we have too many integers in the window, remove 
        // the set can only have at most two values at all times

        Map<Integer, Integer> map = new HashMap<>();

        int start = 0, end = 0;
        int maxCount = 0;

        for(end = 0; end < fruits.length; end++) {
            map.put(fruits[end], map.getOrDefault(fruits[end], 0) + 1);

            if(map.size() > 2) {
                map.put(fruits[start], map.get(fruits[start]) - 1);
                if(map.get(fruits[start]) == 0) {
                    map.remove(fruits[start]);
                }
                start++;
            }

            maxCount = Math.max(maxCount, end - start + 1);
        }

        return maxCount;
    }
}