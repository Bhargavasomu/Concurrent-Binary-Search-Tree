# importing the required module 
import matplotlib.pyplot as plt

def process_file(fp):
	x_values = []
	y_values = []
	lines = fp.readlines()
	for line in lines:
		line = line.strip()
		obj = line.split(' - ')
		if not obj[0].isdigit():
			continue
		x_values.append(int(obj[0]) * 3)
		y_values.append(int(obj[1]))

	return x_values, y_values

  
def main():
	fp1 = open('LockBasedResults.txt', 'r')
	fp2 = open('LockFreeResults.txt', 'r')

	g1_x, g1_y = process_file(fp1)
	g2_x, g2_y = process_file(fp2)
	
	# plotting the LockBasedResults Graph
	plt.plot(g1_x, g1_y, label = 'Lock Based')

	# plotting the LockFreeResults Graph
	plt.plot(g2_x, g2_y, label = 'Lock Free')
	  
	# naming the x axis 
	plt.xlabel('Num of Ops') 
	# naming the y axis 
	plt.ylabel('Time (ms)') 
	  
	# giving a title to my graph 
	plt.title('Comparision of Throughput') 

	# Showing the legend
	plt.legend(loc='upper left')
	  
	# function to show the plot 
	plt.show()


if __name__ == '__main__':
	main()