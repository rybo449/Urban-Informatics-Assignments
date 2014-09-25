import csv
import sys
import collections
import operator
import datetime


today = datetime.date.today()
sunday = today - datetime.timedelta(today.weekday()+1)

ifile = open(sys.argv[1],"rb")
reader = csv.reader(ifile)
rownum = 0
low = 0
high = 0
datelist = []
datelistDict = {}

datelistDict['Monday'] = 0
datelistDict['Tuesday'] = 0
datelistDict['Wednesday'] = 0
datelistDict['Thursday'] = 0
datelistDict['Friday'] = 0
datelistDict['Saturday'] = 0
datelistDict['Sunday'] = 0

for row in reader:
	if rownum == 0:
		header = row
	else:
		colnum = 0
		for col in row:

			if header[colnum] == "Created Date":
			
				datelistDict[str(datetime.datetime.strptime(col,'%m/%d/%Y %I:%M:%S %p').strftime('%A'))]+=1
				#low = min(col,low)
				#high = max(col,high)
				#datelist.append(date_object)			
			colnum+=1
	rownum+=1
#print datelist
#counter = collections.Counter(datelist)
#print counter
#counter = sorted(counter, key = operator.itemgetter(1),reverse = True)
#ans1 = counter.keys()
#ans2 = counter.values()
#print datelistDict

d = {name:val for val, name in enumerate(datelistDict)}
n = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
d = sorted(n, key=d.get)
#print d
for i,j in datelistDict.iteritems():
	datelist.append([i,j])
#print datelist
datelist1=[]
for i in datelist:
	if i[0] == 'Monday':
		datelist1.append([0,i[1]])
	elif i[0] == 'Tuesday':
		datelist1.append([1,i[1]])

	elif i[0] == 'Wednesday':
		datelist1.append([2,i[1]])
	elif i[0] == 'Thursday':
		datelist1.append([3,i[1]])
		
	elif i[0] == 'Friday':
		datelist1.append([4,i[1]])

	elif i[0] == 'Saturday':
		datelist1.append([5,i[1]])

	elif i[0] == 'Sunday':
		datelist1.append([6,i[1]])

for i in xrange(7):
	print n[i],"==",datelist1[i][1]
#print rownum-1, "complaints between",low, "and", high
ifile.close()
