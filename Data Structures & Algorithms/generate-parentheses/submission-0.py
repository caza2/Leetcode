class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def isValid(array: list[str]) -> bool:
            stack: list[str] = []
            for parenthesis in array:
                if not stack and parenthesis == ")":
                    return False
                elif parenthesis == ")":
                    stack.pop()
                elif parenthesis == "(":
                    stack.append(parenthesis)
            if stack:
                return False
            return True
        array: list[str] = []
        res: str = ""
        def backtrack(i: int) -> None:
            nonlocal res
            if i == 2*n:
                if isValid(res):
                    array.append(res)    
                return 
            # Scénario 1: on rajoute un "("
            res = res + "("
            backtrack(i+1)

            # Scénario 2: on rajoute un ")"
            res = res[:-1]
            res = res + ")"
            backtrack(i+1)

            res = res[:-1]
            return
        backtrack(0)
        return array


