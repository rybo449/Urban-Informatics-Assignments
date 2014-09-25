import sys

def clear():
  # TODO Complete with your code and remove print below.
  #print 'clear'    
  mainlist = []
  f = open('output.txt','w')
  f.write('')
  f.close()
# Inserts a job offer into the database.
def insert(fieldValues):
  # TODO Complete with your code and remove print below.
  #print 'insert ' + str(fieldValues)
  sublist = []
  counter = 0
  check = 0
  for i in fieldValues:
	if counter == 0:
		counter+=1
		if i not in jobid:
			jobid.append(i)
			check = 1
	if check == 1:		
  		sublist.append(i)
		sublist.append('|')
  if check == 1:
  	mainlist.append(sublist)
  #print mainlist


# Updates all job offers that attend the field_name=old_value pair.
def update_all(params):
    query_field_name = params[0]
    query_field_value = params[1]
    update_field_name = params[2]
    update_field_value = params[3]
    updatecount = 0
    for i in mainlist:
    	if i[headerlist.index(query_field_name)] == query_field_value:
		i[headerlist.index(update_field_name)] = update_field_value
		updatecount +=1
    f = open('output.txt','a+')
    f.write(str(updatecount))
    f.write("\n")
    f.close()	    
    # TODO Complete with your code and remove print below.
    #print 'update_all set ' + update_field_name + '=' + update_field_value\
    #+ ' where ' + query_field_name + '=' + query_field_value

    # Prints number of updated rows in the database.
    updatedRowCount = 0
    #print str(updatedRowCount)


# Deletes all job offers that attend the field_name=field_value pair.
def delete_all(params):
  field_name, field_value = params
  for i in mainlist:
	if i[headerlist.index(field_name)] == field_value:
		jobid.remove(i[0])		
		mainlist.remove(i)
		
  # TODO Complete with your code and remove print below.
  #print 'delete_all where ' + field_name + '=' + field_value


# Prints all job offers that match the query field_name=field_value, one per
# line, semicolon-separated, with fields in the order defined in the assignment.
def find(params):
  field_name, field_value = params
  temp_list = []
  for i in mainlist:
	if i[headerlist.index(field_name)] == field_value:
		temp_list.append(i)
  temp_list.sort(key = lambda x:x[0])

  for i in temp_list:
	for j in i:
		sys.stdout.write(j)
  	print

  # TODO Complete with your code and remove print below.
  #print 'find where ' + field_name + '=' + field_value


# Prints how many job offers match the query field_name=field_value.
def count(params):
  field_name, field_value = params

  # TODO Complete with your code and remove print below.
  #print 'count job offers where ' + field_name + '=' + field_value


# Prints all job offers in the database, one per line, semicolon-separated, with
# fields in the order defined in the assignment.
def dump(params):
  # TODO Complete with your code and remove print below.
  #print 'dump'
  mainlist.sort(key = lambda x:x[0])
  f = open('output.txt','a+')
  for i in mainlist:
  	for j in i:
		f.write(j)
  	f.write('\n')
  f.close()


# Prints all job offers, one per line, semicolon-separated, but only the
# specified fields, in the order specified for the view.
def view(fieldNames):
  # TODO Complete with your code and remove print below.
  #print 'view for fields ' + str(fieldNames)
  mainlist.sort(key = lambda x:x[0])
  
  for i in mainlist:
	t = 0
	for j in fieldNames:
		t+=1
		sys.stdout.write(i[headerlist.index(j)])
		if t != len(fieldNames):
			sys.stdout.write('|')
	print

def executeCommand(commandLine):
  tokens = commandLine.split('|') #assume that this symbol is not part of the data
  command = tokens[0]
  #print command
  parameters = tokens[1:]

  if command == 'insert':
    insert(parameters)
  elif command == 'delete_all':
    delete_all(parameters)
  elif command == 'update_all':
    update_all(parameters)
  elif command == 'find':
    find(parameters)
  elif command == 'count':
    count(parameters)
  elif command == 'count_unique':
    count_unique(parameters)
  elif command == 'clear':
    clear()
  elif command == 'dump':
    dump(parameters)
  elif command == 'view':
    view(parameters)
  #else:
    #print 'ERROR: Command %s does not exist' % (command,)
    #assert(False)
  
def executeCommands(commandFileName):
  f = open(commandFileName)
  for line in f:
    executeCommand(line.strip())
  f.close()
  
  #print mainlist
  #sys.stdout.write(j)

if __name__ == '__main__':
  #TODO: You should load the data from the database here
  #print 'load'
  mainlist = []
  jobid = []
  headerlist = ['Job ID','|','Agency','|','# Of Positions','|','Business Title','|','Civil Service Title','|','Salary Range From','|','Salary Range To','|','Salary Frequency','|','Work Location','|','Division/Work Unit','|','Job Description','|','Minimum Qual Requirements','|','Preferred Skills','|','Additional Information','|','Posting Date']
  #print headerlist
  #
  executeCommands(sys.argv[1])
  #print mainlist
  #TODO: You should save the data here
  #print 'save'
