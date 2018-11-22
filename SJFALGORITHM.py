def initialize(process,total_process):
	index=0	
	for index in xrange(total_process):
		process.append([])
		process[index].append(raw_input(" P.Name:"))
		process[index].append(int(raw_input("A.T:")))
		process[index].append(int(raw_input("B.T:")))

def print_process(process,total_process):
	total_burst=0
	print 'PName\tA. Time\tB.Time'
	index=0
	for index in xrange(int(total_process)):
        	print process[index][0] ,'\t',process[index][1],'\t',process[index][2]
        	total_burst+=process[index][2]
	
	print "Total Time : ",total_burst

def sorting(process):
	process.sort(key=lambda process:process[1])
	process.sort(key=lambda process:process[2])


total_process=int(raw_input("Enter Count:"))
process=[] 
initialize(process,total_process)
sorting(process)
print_process(process,total_process)



