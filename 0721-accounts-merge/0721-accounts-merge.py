class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        from collections import defaultdict

        # Email to name mapping and graph construction
        email_to_name = {}
        graph = defaultdict(set)
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                graph[account[1]].add(email)
                graph[email].add(account[1])
                email_to_name[email] = name

        # DFS to group emails
        def dfs(email, emails):
            emails.add(email)
            for next_email in graph[email]:
                if next_email not in emails:
                    dfs(next_email, emails)

        visited = set()
        merged_accounts = []
        for email in graph:
            if email not in visited:
                emails = set()
                dfs(email, emails)
                merged_accounts.append([email_to_name[email]] + sorted(emails))
                visited.update(emails)

        return merged_accounts