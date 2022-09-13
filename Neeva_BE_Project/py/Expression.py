import tokenize
from io import StringIO
from collections import deque

class Expression :
    # https://www.algotree.org/algorithms/stack_based/evaluate_infix/
    # Set the precedence level of the operators
    precedence = {
                  "&" : 2,
                  "|" : 2,
                  "(" : 1 } 

    def __init__(self, exp_str, wd) :
        self.exp_str = exp_str
        self.infix_tokens = []  
        self.postfix_tokens = []  
        self.wd = wd

    def Evaluate(self) :
        self.Tokenize()
        self.InfixToPostfix()
        self.EvaluatePostfix()

    def Tokenize(self) :

        tuplelist = tokenize.generate_tokens(StringIO(self.exp_str).readline)

        for x in tuplelist :
            if x.string :
                self.infix_tokens.append(x.string)

        print("\nExpression : " + self.exp_str)

    def InfixToPostfix(self) :

        stack = deque()
        stack.appendleft("(")
        self.infix_tokens.append(")")
    
        while self.infix_tokens :
    
             token = self.infix_tokens.pop(0) 

             if token == "(" :
                 stack.appendleft(token)

             elif token == ")" :
                 # Pop out all the operators from the stack and append them to 
                 # postfix expression till an opening bracket "(" is found

                 while stack[0] != "(" : # peek at topmost item in the stack
                     self.postfix_tokens.append(stack.popleft())
                 stack.popleft()

             elif token == "&" or token == "|" :

                 # Pop out the operators with higher precedence from the top of the
                 # stack and append them to the postfix expression before
                 # pushing the current operator onto the stack.
                 while ( stack and self.precedence[stack[0]] >= self.precedence[token] ) : 
                     self.postfix_tokens.append(stack.popleft())
                 stack.appendleft(token)

             else :
                 # Positions of the operands do not change in the postfix
                 # expression so append an operand as it is to the postfix expression
                 self.postfix_tokens.append(token)
    
        print("Postfix expression : ", end=' ')
        for token in self.postfix_tokens :
            print(token, end=',')
        print("\n----------------------------")
    # a and b are set of timestamp
    def AND(a, b) -> set():
        return a.intersection(b) 
    # a and b are set of timestamp
    def OR(a, b) -> set():
        return a.union(b)

    def EvaluatePostfix(self) :
        # for key, val in self.wd:
        #     print(key)
        stack_result = deque()
        print("=== start to do EvaluatePostfix ===")
        while self.postfix_tokens :
            token = self.postfix_tokens.pop(0)
            print(token)
            if token[0].isalpha():
                if token in self.wd.keys():
                    stack_result.appendleft(self.wd[token])
                else:
                    stack_result.appendleft(set())
            elif token[0] == '!':
                tmp = set()
                for key in self.wd.keys():
                    if key != token[1:]:
                        tmp = tmp.union(self.wd[key])
                stack_result.appendleft(tmp)      

            else :
               x = stack_result.popleft()
               y = stack_result.popleft()

               # Note the order of operands(x, y), result equals [y(operator)x]
               if (token == "|") :
                   stack_result.appendleft(x.union(y))
               elif (token == "&") :
                    #if y in self.wd.keys() and x in  self.wd.keys():
                    stack_result.appendleft(x.intersection(y) )
        lol = stack_result.popleft()
        print("\n"+self.exp_str + " = " + str(lol))
        print(len(lol))
        for s in lol:
            print (s)
        
