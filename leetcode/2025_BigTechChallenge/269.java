class Solution {

    public String alienOrder(String[] words) {

        Map<Character, Set<Character>> g = new HashMap<>();
        Map<Character, Integer> id = new HashMap<>();

        for (String w : words) {
            for (char c : w.toCharArray()) {
                g.putIfAbsent(c, new HashSet<>());
                id.putIfAbsent(c, 0);
            }
        }

        for (int i = 0; i < words.length - 1; i++) {
            String first = words[i];
            String second = words[i + 1];

            if (first.length() > second.length() && first.startsWith(second)) return "";

            int minLength = Math.min(first.length(), second.length());
            for (int j = 0; j < minLength; j++) {
                char parent = first.charAt(j);
                char child = second.charAt(j);
                if (parent != child) {
                    if (!g.get(parent).contains(child)) {
                        g.get(parent).add(child);
                        id.put(child, id.get(child) + 1);
                    }
                    break;
                }
            }
        }

        Queue<Character> q = new LinkedList<>();
        for (char c : id.keySet())
            if (id.get(c) == 0) q.offer(c);

        StringBuilder ans = new StringBuilder();
        while (!q.isEmpty()) {
            char current = q.poll();
            ans.append(current);
            for (char neighbor : g.get(current)) {
                id.put(neighbor, id.get(neighbor) - 1);
                if (id.get(neighbor) == 0) q.offer(neighbor);
            }
        }

        if (ans.length() != id.size()) return "";

        return ans.toString();
    }
}