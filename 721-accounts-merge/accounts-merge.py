class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # utilize a dfs 
        # its basically checking the number of connected components within a graph
        # it starts from one email
        # utilize a set for everything since we want only unique emails

        # the email to name should map the name to the starting email
        # the starting email maps to the other emails which is in a set
        # basically mark all the emails as visited or not

        graph = defaultdict(set)
        name_to_email = defaultdict(str)

        for account in accounts:
            name = account[0]
            head_email = account[1]
            for i in range(1, len(account)):
                # add these to the graph
                graph[head_email].add(account[i])
                graph[account[i]].add(head_email)
                name_to_email[account[i]] = name
        visited = set()
        # traverse the graph
        def dfs(email, list_of_names):
            # should return a list of all the names on this path
            visited.add(email)
            list_of_names.append(email)
            for neighbor in graph[email]:
                if neighbor not in visited:
                    dfs(neighbor, list_of_names)

            return list_of_names
        
        # for name in graph
        res = []
        for head_email in graph:
            if head_email not in visited:
                res.append([name_to_email[head_email]] + sorted(dfs(head_email, [])))
        return res



        