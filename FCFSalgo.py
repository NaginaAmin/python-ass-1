def initialize(process,total_process):
	index=0	
	for index in xrange(int(total_process)):
		process.append([])
		process[index].append(raw_input(" Name of process:"))
		process[index].append(int(raw_input("Arrival Time:")))
		process[index].append(int(raw_input("burst time:")))

	
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




process=[]
total_process=0
total_process=raw_input("Enter total number of processes:")
initialize(process,total_process)
sorting(process)
print_process(process,total_process)

