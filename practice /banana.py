'''
def greeting(name):
	print("Welcome to The Hundred Acre Wood! " + name + " My name is Christopher Robin.")
	return 


greeting("Michael")
greeting("Winnie the Pooh")


'''

def sum_honey(hunny_jars):
	total = 0
	for num in range(0, len(hunny_jars)):
		total += hunny_jars[num]

	return total
		
		


hunny_jars = [2, 3, 4, 5]
print(sum_honey(hunny_jars))

hunny_jars = []
print(sum_honey(hunny_jars))
