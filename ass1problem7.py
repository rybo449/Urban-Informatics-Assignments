import csv
import sys
from collections import defaultdict
from collections import OrderedDict
import collections
import operator
ifile = open(sys.argv[2],"rb")
reader = csv.reader(ifile)
rownum = 0
zipcode = {}
for row in reader:
	if rownum == 0:
		rownum+=1
		continue
	else:
		zipcode[int(row[0])] = str(row[1])



#print zipcode
ifile.close()
ifile = open(sys.argv[1],"rb")
reader = csv.reader(ifile)
rownum = 0
low = 0
high = 0
complaint = []
ans = defaultdict(list)
#print ans
ans1 = []
dict1 = {}
dict1['Manhattan'] = 0
dict1['Brooklyn'] = 0
dict1['Queens'] = 0
dict1['Bronx'] = 0
dict1['Staten Island'] = 0
for row in reader:
	if rownum == 0:
		header = row
	else:
		colnum = 0

		if zipcode[int(row[7])] == "MANHATTAN":
			dict1['Manhattan']+=1
		elif zipcode[int(row[7])] == "BROOKLYN":
			dict1['Brooklyn']+=1
		elif zipcode[int(row[7])] == "QUEENS":
			dict1['Queens']+=1
		elif zipcode[int(row[7])] == "BRONX":
			dict1['Bronx']+=1
		elif zipcode[int(row[7])] == "STATEN ISLAND":
			dict1['Staten Island']+=1
	rownum+=1
#print dict1
dict1 = sorted(dict1.items(), key = operator.itemgetter(1),reverse = True)
#print dict1
for a,b in dict1:
	print a, "with",b,"complaints"
'''print "Brooklyn with",brooklyn,"complaints"
print "Queens with",queens,"complaints"
print "Bronx with",bronx,"complaints"
print "Manhattan with",manhattan,"complaints"
print "Staten Island with",statenisland,"complaints"
'''

'''		for col in row:

			if header[colnum] == "Agency":
				zipcode = int(row[7])
				
				ans[col].append(zipcode)
				ans1.append(col)
				#print ans
				#ans1[zipcode]+=1
				
			colnum+=1'''
#	rownum+=1
#print ans1
#ans1 = list(OrderedDict.fromkeys(ans1))
#print ans1
#ans1.sort()
#print ans1
#for i in ans1:
#	ans2 = {}
	#print ans[i]
'''	for j in ans[i]:
		if j not in ans2:
			ans2[j] = 1
		else:
			ans2[j]+=1
	temp = 0
	#print ans2	
	max1 = []
	for j,k in ans2.iteritems():
		if temp<=k:
			max1.append([j,k])
			temp = k
	print i,
	for j in max1:
		print j[0],
	print j[1]'''

#print ans['HPD']
#counter = collections.Counter(complaint)
#print counter
'''for i in ans:
	print i
	counter = collections.Counter(i)
	print counter'''

'''for i in ans:
	print str(i),
	for k,l in j.iteritems():
		print str(k),str(l)
	print''' 
#print counter
#ans1 = counter.keys()
#ans2 = counter.values()
#temp = ans2[0]
#for i in xrange(len(ans2)):
#	if temp == ans2[i]:
		

#sorted_complaint = sorted(counter.iteritems(),key = operator.itemgetter(1,0))
#sorted_complaint = sorted(sorted_complaint, key = operator.itemgetter(1),reverse = True)
#print sorted_complaint

#for i in xrange(int(sys.argv[2])):
#	print sorted_complaint[i][0], "with ",sorted_complaint[i][1], "complaints"

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
