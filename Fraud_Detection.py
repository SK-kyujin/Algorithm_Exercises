import queue
import copy

# get n,d
string=input()
n,d=string.split()
n,d=int(n),int(d)

# get expenditures
a=input()
x=a.split(' ')
for i in range(len(x)):
	x[i]=int(x[i])

# make a queue for reading expenditures 
Q=queue.Queue()

# make a dict for counting sort & median calculation
dict1={}
for i in range(201):
	dict1[i]=0

# output varible
total_count=0

def update_QnDict(i):
	if i==0:
		for j in range(d):
			Q.put(x[j])
			dict1[x[j]]+=1
	else:
		out=Q.get()
		Q.put(x[i+d-1])
		dict1[out]-=1
		dict1[x[i+d-1]]+=1
		
def compute_median(dict1):
	count=0
	if d%2==0:
		for i in range(201):
			num=dict1.get(i,0)
			count+=num
			if count>=d/2 and count>=d/2+1:
				return i
			elif count>=d/2 and count<d/2+1:
				return (2*i+1)/2
	else:
		for i in range(201):
			num=dict1.get(i,0)
			count+=num
			if count>=(d+1)/2:
				return i			
	
def update_total_count(med1,total_count):
	if y>=2*med1:
		total_count+=1
	return total_count

for i in range(n-d):
	update_QnDict(i)
	y=x[i+d]
	med1=compute_median(dict1)
	total_count=update_total_count(med1,total_count)

print(total_count)