/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int[] findMode(TreeNode root) {
        Map<Integer, Integer> freqMap = new HashMap<>();

        // Perform DFS to populate the frequency map
        dfs(root, freqMap);

        // Find the maximum frequency and collect all values with that frequency
        List<Integer> modes = new ArrayList<>();
        int maxFreq = 0;
        for (Map.Entry<Integer, Integer> entry : freqMap.entrySet()) {
            int key = entry.getKey();
            int freq = entry.getValue();
            if (freq > maxFreq) {
                modes.clear();
                maxFreq = freq;
                modes.add(key);
            } else if (freq == maxFreq) {
                modes.add(key);
            }
        }

        // Convert the list of modes to an array
        return modes.stream().mapToInt(i -> i).toArray();
    }

    private void dfs(TreeNode root, Map<Integer, Integer> freqMap) {
        if (root == null) {
            return;
        }

        // Update frequency in the map
        freqMap.put(root.val, freqMap.getOrDefault(root.val, 0) + 1);

        // Recursively traverse left and right subtrees
        dfs(root.left, freqMap);
        dfs(root.right, freqMap);
    }
}
