class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        

        result = []


        def dfs(open_parenthesis: int, close_parenthesis: int, s: str):
            if len(s) == 2*n:
                result.append(s)
                return
            if open_parenthesis < n:
                dfs(open_parenthesis + 1, close_parenthesis, s + "(")
            if close_parenthesis < open_parenthesis:
                dfs(open_parenthesis, close_parenthesis + 1, s + ")")


        dfs(0, 0, "")
        return result
                
