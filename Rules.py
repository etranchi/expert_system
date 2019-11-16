from Operation import Fact, Operation
import Utils
import Parser

class Rules:
	def __init__(self):
		self.operations = []
		self.facts = []

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
		if string.find(Utils.MAIN_OPERATOR) > 0: 
			self.create_operation(string.split(Utils.MAIN_OPERATOR))

	def create_operation(self, array_string):
		s1 = Parser.shunting(array_string[0])
		s2 = array_string[1]

		# need nettoyage strings
#		if len(array_string[1]) > 2:
#			s2 = Parser.shunting(array_string[1])
		op = Operation(s1, s2)

		print(op.left, op.right)
		self.operations.append(op)

	def create_fact_if_not_existing(self, name):
		for f in self.facts:
			if f.name == name:
				print("Fact already created " + name)
				return
		fact = Fact(name)
		print("Adding Fact not created : " + fact.name)
		self.facts.append(fact)
		return

	def solve(self):
		# solving array of op
		print("solving")