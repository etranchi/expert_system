#!/Users/etranchi/.brew/bin/python3
from enum import Enum, unique

MAIN_OPERATOR = ["=>"]
OPERATOR = ["^", "|", "+"]

@unique
class Side(Enum):
	LEFT = 0
	MOTHER = 1
	RIGHT = 2
	

def end(reason):
	print(reason)
	exit()