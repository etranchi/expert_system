#!/Users/etranchi/.brew/bin/python3

MAIN_OPERATOR = ["=>", "<=>"]
OPERATOR = ["|", "+", "^"]

class Operation:
	def __init__(self, operator, lhs, rhs):
		self.lhs = lhs
		self.rhs = rhs
		self.solved = 0

class Fact:
	def __init__(self, name, value = 0):
		self.name = name
		self.value = value