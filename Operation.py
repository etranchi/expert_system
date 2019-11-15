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
	def __init__(self, operator, lhs = None, rhs = None, depth = 0):
		self.operator = operator
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

class Fact:
	def __init__(self, name, value = 0, setter = False):
		self.name = name
		self.value = value
		self.set = setter