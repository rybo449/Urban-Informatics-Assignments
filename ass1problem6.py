import csv
import sys
from collections import defaultdict
from collections import OrderedDict
import collections
import operator

ifile = open(sys.argv[1],"rb")
reader = csv.reader(ifile)
rownum = 0
low = 0
high = 0
complaint = []
ans = defaultdict(list)
ans1 = []

for row in reader:
	if rownum == 0:
		header = row
	else:
		colnum = 0
		for col in row:

			if header[colnum] == "Agency":
				zipcode = int(row[7])
				
				ans[col].append(zipcode)
				ans1.append(col)
				
			colnum+=1
	rownum+=1

ans1 = list(OrderedDict.fromkeys(ans1))
ans1.sort()
print ans1

for i in ans1:
	ans2 = {}
	
	for j in ans[i]:
		if j not in ans2:
			ans2[j] = 1
		else:
			ans2[j]+=1
	temp = 0
	
	max1 = []
	temp1 = 0
	ans2 = sorted(ans2.iteritems(), key=operator.itemgetter(1), reverse = True)
	for j,k in ans2:
		if temp1 == 0:
			temp1+=1
			temp = k
		if temp==k:
			max1.append([j,k])
			
	print i,
	for j in max1:
		print j[0],
	print j[1]


ifile.close()
