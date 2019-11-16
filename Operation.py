#!/Users/etranchi/.brew/bin/python3
import Utils


class Operation:
	def __init__(self, lhs = None, rhs = None, done = False):
		self.left = lhs
		self.right = rhs
		self.result = None
		self.done = done

class Fact:
	def __init__(self, name, value = 0):
		self.name = name
		self.value = value

	def sv(self, value):
		self.value = value