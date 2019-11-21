from Operation import Fact, Operation
import Utils
import Parser
import sys 

class Rules:
    def __init__(self):
        self.operations = []
        self.facts = []
        self.hash = []
        self.question = ""
        self.init_f = 0
        self.init_q = 0

    def set_initials_facts(self, string):
        if self.init_f:
            raise Exception
        string = string.replace(" ", "")
        if string[0] == "=":
            string = string[1:]
            for c in string:
                if c.isalpha():
                    f = self.create_fact_if_not_existing(c)
                    f.value = 1
                else :
                    raise Exception
        else :
            raise Exception
        self.init_f = 1

    def print_all_facts(self):
        for f in self.facts:
            print(str(f.name) + " - " + str(f.value > 0))

    def set_question(self, string):
        if self.init_q:
            raise Exception
        string = string.replace(" ", "")
        if string[0] == "?":
            tmp_str = string[1:]
            for c in tmp_str:
                if not c.isalpha():
                    raise Exception
        else :
            raise Exception
        self.question = string
        self.init_q = 1

    def print_answer(self):
        for c in self.question:
            if c != "?":
                f = self.create_fact_if_not_existing(c)
                print(f.name + " : " + str(f.value > 0))

    def create_rules(self, string):
        for c in string:
            if c.isalpha():
                self.create_fact_if_not_existing(c)
        if string.find(Utils.MAIN_OPERATOR): 
            self.create_operation(string.split(Utils.MAIN_OPERATOR), string)

    def check_if_already_here(self, operation):
        for o in self.operations:
            if o.right == operation.right and o.left == operation.left:
                return
        self.operations.append(operation)

    def create_operation(self, array_string, string):
        try:
            s1 = Parser.shunting(array_string[0])
            s2 = Parser.shunting(array_string[1])
            op = Operation(s1, s2, array_string)
            op.str = string
            
            self.check_if_already_here(op)
        except Exception:
            Utils.end("Error in parsing.")
        

    def get_fact(self, name):
        for f in self.facts:
            if f.name == name:
                return f
        return None

    def create_fact_if_not_existing(self, name):
        for f in self.facts:
            if f.name == name:
                return f
        fact = Fact(name)
        self.facts.append(fact)
        return fact

    def findOperations(self, name):
        buff = []
        for op in self.operations:
            if not op.done:
                operation = op.right.strip()
                for c in name:
                    for char in operation:
                        if c == char:
                            op.done = True
                            buff.append(op)
        return buff

    def addValueToConclusion(self, op):
        
        ops = self.findOperations(op.right)
        # !B => !A
        print("OP : RES = ", op.str, op.result, ops, len(ops))
        res = op.result
        for o in ops:
            self.checkFactInConclusion(o)
            res = res or o.result
        for c in op.right:
            if c == "!":
                res = 1 if not op.result else 0
            elif c.isalpha():
                fact = self.get_fact(c)
                fact.value = res
                print("SETTING FACT " + fact.name + " " + str(res) + " " + op.str)
                op.result = res
                
                




                    

    def perform_rpn(self, op, rpn):
        twin = op.left + op.right
        if twin in self.hash:
            return
        self.hash.append(twin)
        i = 0
        buff = []
        rpn = list(rpn)
        print(rpn)
        while i < len(rpn):
            if rpn[i] in Utils.OPERATOR:                
                left, right = buff.pop(), buff.pop()
                if rpn[i] == "+":
                    res = left and right
                elif rpn[i] == "|":
                    res = left or right
                elif rpn[i] == "^":
                    res = left ^ right
                rpn[i - 2] = res
                rpn = rpn[:i - 1] + rpn[i + 1:]
                i = 0
            else :
                buff.append(int(rpn[i]))
                i += 1
        print(buff)
        op.result = buff[-1]
        return self.addValueToConclusion(op)


    def checkFactInConclusion(self, op):
        inv = 0
        buff = ""
        op.done = True
        res = 0

        print("OP", op.str)
        for c in op.left:
            if c == '!':
                inv = 1
            elif c.isalpha():
                a_op = self.findOperations(c)
                for o in a_op:
                   if o:
                        print("RELATED ", o.str)
                        self.checkFactInConclusion(o)
                fact = self.create_fact_if_not_existing(c)
                if inv == 1:
                    res = 1 if not fact.value else 0
                    buff += str(res)
                    inv = 0
                else:
                    buff += str(fact.value)
            else:
                buff += c
        self.perform_rpn(op, buff)

    def solve(self):
        for op in self.operations:
            if op.done == False:
                self.checkFactInConclusion(op)

