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

    def set_initials_facts(self, string):
        print("Setting facts : " + string)
        string = string.replace(" ", "")
        for c in string:
            if c == "=":
                continue
            if c.isalpha():
                f = self.create_fact_if_not_existing(c)
                f.value = 1
                print("Fact set : " + f.name)
            else :
                Utils.end("Error in initial facts")

    def print_all_facts(self):
        for f in self.facts:
            print(str(f.name) + " - " + str(f.value > 0))

    def set_question(self, string):
        string = string.replace(" ", "")
        for c in string:
            if c == "?":
                continue
            if not c.isalpha():
                Utils.end("Error in question")
        self.question = string

    def print_answer(self):
        for c in self.question:
            if c != "?":
                f = self.create_fact_if_not_existing(c)
                print(f.name + " : " + str(f.value > 0))

    def create_rules(self, string):
        # splitting expression : array[0] => array[1]
        for c in string:
            if c.isalpha():
                self.create_fact_if_not_existing(c)
        if string.find(Utils.MAIN_OPERATOR): 
 #           string = string.replace(" ", "")
            self.create_operation(string.split(Utils.MAIN_OPERATOR))

    def create_operation(self, array_string):
        print("CHECK ", array_string)
        s1 = array_string[0].strip().replace("", " ")
        if len(s1) > 5:
            s1 = Parser.shunting(s1).replace(" ", "")
        else :
            Parser.get_input(s1)
            s1 = s1.replace(" ","")
        print("coucou",s1)
        s2 = array_string[1].strip().replace("", " ")
        if len(s2) > 5:
            s2 = Parser.shunting(s2).replace(" ", "")
        else:
            Parser.get_input(s2)
            s2 = s2.replace(" ", "")
        print("coucou2")
        op = Operation(s1, s2)
        self.operations.append(op)

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
            operation = op.right.strip()
            for c in operation:
                if c == name:
                    buff.append(op)
        return buff

    def addValueToConclusion(self, op, res):
        # check if fact or op
        # if fact
        t_res = res
        for c in op.right:
            if c == "!":
                t_res = 1 if not res else 0
            elif c.isalpha():
                fact = self.get_fact(c)
                if fact:
                    fact.value += t_res
                    print("Fact " + fact.name + " set to " + str(fact.value) + " from rule : " + op.left + " => " + op.right)
                    t_res = res
                    

    def perform_rpn(self, op, rpn):
        op.done = True
        twin = op.left + op.right
        if twin in self.hash:
            return
        self.hash.append(twin)
        i = 0
        buff = []
        rpn = list(rpn)
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
        self.addValueToConclusion(op, buff[0])
        return


    def checkFactInConclusion(self, op):
        inv = 0
        buff = ""
        op.done = True
        for c in op.left:
            if c == '!':
                inv = 1
            elif c.isalpha():
                a_op = self.findOperations(c)
                for o in a_op:
                    if o and not o.done:
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
        # solving array of op
        for op in self.operations:
            if op.done == False:
                self.checkFactInConclusion(op)

            #
