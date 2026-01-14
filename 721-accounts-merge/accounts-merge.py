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
        email_to_name = defaultdict(str)

        # first, create the graph
        # by creating an entry for every email

        for account in accounts:
            name = account[0]
            first_email = account[1]

            for i in range(1, len(account)):
                graph[account[i]].add(first_email)
                graph[first_email].add(account[i])
                email_to_name[account[i]] = name
            
        
        # dfs
        visited = set()
        def dfs(email, connected_components):
            visited.add(email)
            connected_components.append(email)
            for neighbor_email in graph[email]:
                if neighbor_email not in visited:
                    dfs(neighbor_email, connected_components)
            
            return connected_components
        
        # for every head_email, dfs() to clear out the connected components
        # and add to ret list
        ret = []
        for email in graph:
            if email not in visited:
                name_of_email = email_to_name[email]
                list_of_connected_emails = dfs(email, [])
                ret.append([name_of_email] + sorted(list_of_connected_emails))
        
        return ret





        