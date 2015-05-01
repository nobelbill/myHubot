import psutil

def getCpu(times) :
	list = []
	for x in range(0,times):
		list.append(psutil.cpu_percent(interval=1))
	return list


print getCpu(10)
