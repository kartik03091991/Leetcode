class Solution:
    def interpret(self, command: str) -> str:
        #command = "G()(al)"
        #command = "G()()()()(al)"
        #command = "(al)G(al)()()G"
        p = command.replace("()","o")
        #print(p)
        q = p.replace("(al)","al")
        return(q)
    

"""
Example 1:

Input: command = "G()(al)"
Output: "Goal"
Explanation: The Goal Parser interprets the command as follows:
G -> G
() -> o
(al) -> al
The final concatenated result is "Goal".
Example 2:

Input: command = "G()()()()(al)"
Output: "Gooooal"
"""