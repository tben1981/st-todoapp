import uuid

class task:
	def __init__(self,task_name,deadline,my_uuid=None):
		if my_uuid==None:
			self.__task={'uuid': str(uuid.uuid1()),'task':task_name,'deadline':deadline}
		else:
			self.__task = {'uuid': my_uuid, 'task': task_name, 'deadline': deadline}

	def __str__(self):
		return (self.__task['uuid']+" | "+self.__task['task']+' | '+self.__task['deadline'])

	def to_string(self):
		return (self.__task['uuid'] + "|" + self.__task['task'] + '|' + self.__task['deadline']+'\n')

	def check_data(self,taskinfo,deadline):
		return((taskinfo,deadline)==(self.__task['task'],self.__task['deadline']))

	def update_data(self,newtask,newdeadline):
		self.__task['task']=newtask
		self.__task['deadline']=newdeadline

	def return_tuple(self):
		return(self.__task['task'],self.__task['deadline'])

	def return_list(self):
		return[self.__task['task'],self.__task['deadline']]

	def return_deadline(self):
		return self.__task['deadline']

	def return_todo(self):
		return self.__task['task']




if __name__=="__main__":
	mytask=task("Test task","Today")
	print(mytask)
	mytaskv2=task("Test taskv2","Tomorrrow","abcs234")
	print(mytaskv2)
