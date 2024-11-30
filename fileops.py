import task

def retrieve_file(filename='todo-list-data.txt'):
	try:
		tasklist = []
		filedata = open(filename, 'r')
		content = filedata.readlines()
		if len(content) != 0:  # File is empty
			for line in content:
				line = line.replace('\n', '')  # remove last \n read by file
				line_list = line.split('|')
				tasklist.append(task.task(line_list[1], line_list[2], line_list[0]))
		return tasklist
	except Exception as e:
		print("Exception caught", e)
	finally:
		filedata.close()


# Returns a list of task

def update_file(tasklist,filename='todo-list-data.txt'):
	try:
		filedata = open(filename, 'w')
		if len(tasklist) == 0:  # no task
			filedata.write("")
		else:
			filedata.write("")  ##Blank the file before writing
			for task in tasklist:
				filedata.write(task.to_string())
	except Exception as e:
		print("Exception caught", e)
	finally:
		filedata.close()