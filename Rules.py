from Operation import Fact, Operation
import Utils
import Parser

class Rules:
    def __init__(self):
        self.operations = []
        self.facts = []
        self.hash = []

    def set_initials_facts(self, string):
        print("Setting facts : " + string)
        for c in string:
            for f in self.facts:
                 if c == f.name :
                    f.value = 1
                    print("Fact set : " + f.name)

    def print_questions(self, string):
        print("Setting questions : " + string)
        for c in string:
            for f in self.facts:
                if c == f.name :
                    print(f.name + " : ", f.value)

    def create_rules(self, string):
        # splitting expression : array[0] => array[1]
        for c in string:
            if c.isalpha():
                self.create_fact_if_not_existing(c)
        if string.find(Utils.MAIN_OPERATOR): 
 #           string = string.replace(" ", "")
            self.create_operation(string.split(Utils.MAIN_OPERATOR))

    def create_operation(self, array_string):

        s1 = array_string[0].strip().replace("", " ")
        s1 = Parser.shunting(s1)
        s2 = array_string[1].replace("", " ")
        ## NEED TO CHECK IF S2 NEED SHUNTING
        s1 = s1.replace(" ", "")
        s2 = s2.replace(" ", "")
        op = Operation(s1, s2)
        self.operations.append(op)

    def create_fact_if_not_existing(self, name):
        for f in self.facts:
            if f.name == name:
                return
        fact = Fact(name)
        print("Adding Fact not created : " + fact.name)
        self.facts.append(fact)
        return

    def findOperations(self, name):
        for op in self.operations:
            if op.right.strip() == name:
                # faire operation
                return op
        return None


    def perform_rpn(self, op):
        twin = op.left + op.right
        if twin in self.hash:
            return
        self.hash.append(twin)
        print("rpn to do before:", op.left)

    def checkFactInConclusion(self, op):
        inv = 0
        for i,c in enumerate(op.left):
            if c == '!':
                inv = 1
            if c.isalpha():
                t_op = self.findOperations(c)
                if t_op != None and not t_op.done:
                    self.checkFactInConclusion(t_op)
                    self.perform_rpn(t_op)
        

    				

    def solve(self):
        # solving array of op
        for op in self.operations:
            self.checkFactInConclusion(op)
            self.perform_rpn(op)

            #
