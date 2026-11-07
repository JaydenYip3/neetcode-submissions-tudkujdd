class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        ret = 0

        for operation in operations:
            if operation == "+":
                new = stack[-1] + stack[-2] 
                stack.append(new)
                ret += new 
            elif operation == "D":
                new = stack[-1] * 2
                stack.append(new)
                ret += new
            elif operation == "C":
                remove = stack.pop()
                ret -= remove
            else:
                num = int(operation)
                stack.append(num)
                ret += num
        
        return ret
        

        