#!/Users/etranchi/.brew/bin/python3

MAIN_OPERATOR = ["=>", "<=>"]
OPERATOR = ["|", "+", "^"]



def checkIfMain(operator):
	if operator in MAIN_OPERATOR:
		return (1)
	return (0)

def checkIfOperator(operator):
	if operator in OPERATOR:
		return (1)
	return (0)


class Operation:
	def __init__(operator, lhs, rhs):
		self.lhs = lhs
		self.rhs = rhs
		self.solved = 0

class Fact:
	def __init__(name, value = 0):
		self.name = name
		self.value = value