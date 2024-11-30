import sys
import fileops
import task
import time

class TaskList:
	def __init__(self):
		self.__tasklist=[]

	def main_menu(self):
		print("== TODO LIST ==")
		print("[1] show task")
		print("[2] add task")
		print("[3] edit task")
		print("[4] complete task")
		print("[5] exit")
		print("")
		print(f"The date is {time.strftime('%d-%m-%Y at %I:%M:%S %p')}")

	def show_task(self):
		print("[YOUR TASK]")
		self.__tasklist=fileops.retrieve_file()
		if len(self.__tasklist)==0:
			print("Empty List")
		else:
			for index,task in enumerate(self.__tasklist):
				print(str(index+1) + ' | ',end='')
				print(task)
		print("")

	def add_task(self):
		print("[ADD TASK]")
		self.show_task()
		task_name=input("What is the task? ")
		deadline=input("What is the deadline? ")
		self.__tasklist.append(task.task(task_name,deadline))
		fileops.update_file(self.__tasklist)
		print("")

	def edit_task(self):
		print("[EDIT TASK]")
		print("")
		self.show_task()
		if (len(self.__tasklist)>0): # if there is no task, there is no need to capture input
			index=self.output_int("Enter index to complete: ",[ i+1 for i in range(len(self.__tasklist))])
			task_name = input("What is the task? ")
			deadline = input("What is the deadline? ")
			self.__tasklist[index-1]=task.task(task_name,deadline)
			fileops.update_file((self.__tasklist))
		else:
			print("There are no task in task list")
		print("")


	def complete_task(self):
		print("[COMPLETE TASK]")
		print("")
		self.show_task()
		if (len(self.__tasklist)>0): # if there is no task, there is no need to capture input
			index=self.output_int("Enter index to complete: ",[ i+1 for i in range(len(self.__tasklist))])
			del self.__tasklist[index-1]
			fileops.update_file(self.__tasklist)
		else:
			print("There are no task in task list")
		print("")

	def run_app(self):
		input=9999
		self.__tasklist=fileops.retrieve_file()  #initial loading of task list to load existing task
		print("")
		while (input!=5):
			self.main_menu()
			input=self.output_int("Your choice : ",[1,2,3,4,5])
			match input:
				case 1:
					self.show_task()
				case 2:
					self.add_task()
				case 3:
					self.edit_task()
				case 4:
					self.complete_task()
				case 5:
					sys.exit(1)

	def output_int(self, display_text, allowed_input=[],any_int=False):
		while True:
			try:
				my_input = int(input(display_text))
				if (any_int == True) or (my_input in allowed_input):
					return my_input
				else:
					print("Please enter a correct value", allowed_input)
			except ValueError:
				print("Please enter a correct value", allowed_input)

	def gui_retrieve_task(self):
		self.__tasklist = fileops.retrieve_file()
		result=[]
		for task in self.__tasklist:
			result.append(task.return_list())
		return result


	def gui_show_task(self):
		self.__tasklist = fileops.retrieve_file()
		result=[]
		for task in self.__tasklist:
			result.append(task.return_list())
		return result

	def gui_add_task(self,taskinfo,deadline):
		self.__tasklist.append(task.task(taskinfo,deadline))
		fileops.update_file(self.__tasklist)

	def gui_edit_task(self,origtask,origdeadline,newtask,newdeadline):
		for task in self.__tasklist:
			if (task.check_data(origtask,origdeadline)):
				task.update_data(newtask,newdeadline)
				fileops.update_file(self.__tasklist)

	def gui_complete_task(self,taskinfo,taskdeadline):
		for index,task in enumerate(self.__tasklist):
			if(task.check_data(taskinfo,taskdeadline)):
				self.__tasklist.pop(index)
				fileops.update_file(self.__tasklist)

	def web_complete_task(self,taskindex):
		self.__tasklist.pop(taskindex)
		fileops.update_file(self.__tasklist)

	def __iter__(self):
		# return iter(self.__stations[1:]) #uncomment this if you wanted to skip the first element.
		return iter(self.__tasklist)


if __name__=='__main__':
	myapp=TaskList()
	myapp.run_app()
