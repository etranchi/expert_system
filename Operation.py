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
	def __init__(self, operation):
		self.operation = operation
		
		self.solved = False
		self.result = None

class Fact:
	def __init__(self, name, value = 0, setter = False):
		self.name = name
		self.value = value
		self.set = setter