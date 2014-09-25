import csv
import sys
import collections
import operator
ifile = open(sys.argv[1],"rb")
reader = csv.reader(ifile)
rownum = 0
low = 0
cnt = {}
high = 0
complaint = []
for row in reader:
	if rownum == 0:
		header = row
	else:
		colnum = 0
		for col in row:

			if header[colnum] == "Complaint Type":
				complaint.append(col)
			
			colnum+=1
	rownum+=1
counter = collections.Counter(complaint)
#print counter

#print counter
ans1 = counter.keys()
ans2 = counter.values()
temp = ans2[0]
#for i in xrange(len(ans2)):
#	if temp == ans2[i]:
		

sorted_complaint = sorted(counter.iteritems(),key = operator.itemgetter(1,0))
sorted_complaint = sorted(sorted_complaint, key = operator.itemgetter(1),reverse = True)
#print sorted_complaint

for i in xrange(int(sys.argv[2])):
	print sorted_complaint[i][0], "with ",sorted_complaint[i][1], "complaints"

'''complaint.sort()
for i in complaint:
	temp = i
	count = 0
	while temp == i:
		count+=1
	c1.append(count,i)
print c1'''
#print rownum-1, "complaints between",low, "and", high
ifile.close()
