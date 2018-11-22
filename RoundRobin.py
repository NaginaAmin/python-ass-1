def initialize(process,total_process):
	index=0	
	for index in xrange(int(total_process)):
		process.append([])
		process[index].append(raw_input("Process:"))
		process[index].append(int(raw_input("A.T:")))
        	process[index].append(int(raw_input("B.T:")))

def sorting(process):
	process.sort(key=lambda process:process[1])

def setvalues():
	process=[]
	total_process=int(raw_input("Enter a count of process :"))
	time_slice=int(raw_input("Time Slice"))
	initialize(process,total_process)
	perform(process,total_process,time_slice)	

def perform(process,total_process,time_slice):
	running_process=[]
	total_burst=0
	import Queue
	ready_queue=Queue
	ready_queue=ready_queue.Queue()
	element_count=0
	ready_queue.put(process[element_count])
	element_count+=1
	calculation(process,total_process,time_slice,total_burst,ready_queue,element_count)

def calculation(process,total_process,time_slice,total_burst,ready_queue,element_count):
	while not ready_queue.empty() or element_count<total_process:
		running_process=ready_queue.get()
		if running_process[2]>=time_slice:
			running_process[2]=running_process[2]-time_slice
			print running_process
			total_burst+=time_slice
			if element_count<=total_process:
				while element_count<total_process:
					if process[element_count][1]<=total_burst:	
						ready_queue.put(process[element_count])
					element_count+=1
			if running_process[2]!=0:
				ready_queue.put(running_process)
		else:
			print running_process
			total_burst+=running_process[2]
			
						
						
