class Solution {
    public double[] calcEquation(List<List<String>> equations, double[] values, List<List<String>> queries) {

        Map<String, Map<String, Double>> g = new HashMap<>();

        for (int i = 0; i < equations.size(); i++) {
            List<String> eq = equations.get(i);
            String numerator = eq.get(0);
            String denominator = eq.get(1);
            double v = values[i];

            g.putIfAbsent(numerator, new HashMap<>());
            g.putIfAbsent(denominator, new HashMap<>());

            g.get(numerator).put(denominator, v);
            g.get(denominator).put(numerator, 1 / v);
        }

        double[] ans = new double[queries.size()];

        for (int i = 0; i < queries.size(); i++) {
            List<String> q = queries.get(i);
            String numerator = q.get(0);
            String denominator = q.get(1);

            if (!g.containsKey(numerator) || !g.containsKey(denominator))
                ans[i] = -1;
            else if (numerator.equals(denominator))
                ans[i] = 1;
            else
                ans[i] = dfs(numerator, denominator, 1, new HashSet<>(), g);
        }
        return ans;
    }

    private double dfs(String current, String target, double acc, Set<String> visited,
                       Map<String, Map<String, Double>> graph) {

        if (current.equals(target)) return acc;

        visited.add(current);

        Map<String, Double> neighbors = graph.get(current);

        for (String neighbor : neighbors.keySet()) {

            if (visited.contains(neighbor)) continue;

            double result = dfs(neighbor, target, acc * neighbors.get(neighbor), visited, graph);

            if (result != -1.0) return result;
        }

        return -1.0;
    }
}