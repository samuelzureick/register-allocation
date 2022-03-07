import sys
import string

def main():
	# read input file
	if len(sys.argv) != 3:
		print("WRONG PARAMETER COUNT! NEED TO SPECIFY INPUT AND OUTPUT FILE")
		sys.exit()
	input_file = sys.argv[1]
	out_file = sys.argv[2]
	try:
		with open(input_file) as f:
			int_graph = f.readlines()
	except:
		print("FILE NOT FOUND! ABORTING")
		sys.exit()

	# translate input into a 2d array
	t = []
	for line in int_graph:
		t.append(line.split())
	int_graph = t

	# create array of "colours" A-Z
	colours = [letter for letter in string.ascii_uppercase]

	# sort graph by number of neighbors
	int_graph = sorted(int_graph, key=len, reverse = True)
	# *****MAIN PROGRAM*****
	# here, I basically create a 2d array that I call bags
	# it holds a bunch of smaller arrays, that all contain
	# the nodes that are allowed to be coloured the same
	# It checks if a nodes value is contained within any bag- if it is, it created a new bag
	# If not, it inserts the node into the appropriate bag

	bags = [[int_graph[0]]]
	for i in range(1,len(int_graph)):
		inserted = False
		for bag in bags:
			if not any(int_graph[i][0] in item for item in bag) and not inserted:
				bag.append(int_graph[i])
				inserted = True
		if not inserted:
			bags.append([int_graph[i]])

	# Gives each bag a colour coding by popping them off the array
	# Here errors are handeled in case of not enough colours
	for i in range(len(bags)):
		try:
			bags[i].insert(0,colours.pop(0))
		except:
			print("RAN OUT OF COLOURS! ABORTING")
			sys.exit()
			
	# Generates output string
	output = []
	for i in range(len(bags)):
		letter = bags[i][0]
		for j in range(1, len(bags[i])):
			output.append(bags[i][j][0]+letter+"\n")

	output = sorted(output, key = lambda x: int(x[:-2]),reverse = False)
	outputString = ""
	for txt in output:
		outputString += txt

	# writes output
	try:
		f = open(out_file, "w")
		f.write(outputString)
		f.close()
	except:
		print("ERROR WRITING OUTPUT FILE! ABORTING")
		sys.exit()

if __name__ == '__main__':
	main()
