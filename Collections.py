#	Jacob Stelzriede
#
#
#
#
import collections

def addition(*args):
	result = 0
	for arg in args:
		result += arg
	return result



def main():
	print(addition(5, 10, 15, 20))
	print(addition(1, 2, 3))

	myNums = [5, 10, 15, 20]
	print(addition(*myNums))

	# examples of named tuples
	Point = collections.namedtuple("Point", "x y")
	p1 = Point(10,20)
	p2 = Point(20,40)
	print(p1,p2)
	print(p1.x, p2.y)


if __name__ == "__main__":
	main()
