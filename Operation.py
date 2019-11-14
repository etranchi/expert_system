#!/Users/etranchi/.brew/bin/python3
import Utils

def checkIfMain(operator):
	if operator in Utils.MAIN_OPERATOR:
		return (1)
	return (0)

def checkIfOperator(operator):
	if operator in Utils.OPERATOR:
		return (1)
	return (0)


class Operation:
	def __init__(self, operator, array_op, side, lhs = None, rhs = None):
		self.operator = operator
		self.side = side
		self.array_op = array_op
		self.left = lhs # Operation | Fact
		self.right = rhs # Operation | Fact
		self.solved = False
		self.result = None
		
	def make_operation(self):
		if self.operator == "+":
			name = "ADD"
		elif self.operator == "|":
			name = "OR"
		elif self.operator == "^":
			name = "XOR"
		elif self.operator == "=>":
			name = "IMP"
		method = getattr(self, name, lambda: "Error")
		print("Making operation : " + self.array_op[0] + self.operator + self.array_op[1])
		self.result = method()
		self.solved = True

	def is_possible_to_make(self):
		if (type(self.left) == Fact or (type(self.left) == Operation and self.left.solved == True)) and (type(self.right) == Fact or (type(self.right) == Operation and self.right.solved == True)):
			self.make_operation()

	def get_value_or_result(self, side):
		if type(side) == Fact:
			return side.value
		if type(side) == Operation:
			return side.result

	def ADD(self):
		return self.get_value_or_result(self.left) and self.get_value_or_result(self.right)
	
	def OR(self):
		return self.get_value_or_result(self.left) or self.get_value_or_result(self.right)
	
	def XOR(self):
		return self.get_value_or_result(self.left) ^ self.get_value_or_result(self.right)
	
	def IMP(self):
		print("We got a conclusion : " + str(self.side))

class Fact:
	def __init__(self, name, value = 0, setter = False):
		self.name = name
		self.value = value
		self.set = setter