import csv
import sys
import datetime

ifile = open(sys.argv[1],"rb")
reader = csv.reader(ifile)
rownum = 0
low = 0
high = 0
for row in reader:
	if rownum == 0:
		header = row
	else:
		colnum = 0
		for col in row:

			if header[colnum] == "Created Date":
				if rownum == 1:
					low = col
					low = datetime.datetime.strptime(low,'%m/%d/%Y %I:%M:%S %p')
					high = datetime.datetime.strptime(col,'%m/%d/%Y %I:%M:%S %p')
				else:
					col = datetime.datetime.strptime(col,'%m/%d/%Y %I:%M:%S %p')
					low = min(col,low)
					high = max(col,high)
			colnum+=1
	rownum+=1
low = low.strftime('%m/%d/%Y %H:%M:%S')
high = high.strftime('%m/%d/%Y %H:%M:%S')
print rownum-1, "complaints between",low, "and", high
ifile.close()
