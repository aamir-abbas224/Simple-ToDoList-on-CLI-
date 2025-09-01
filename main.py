import os

class ToDoList:
    def __init__(self,filename = 'ToDoList.txt'):
        self._filename = filename
        self.tasks = self.load_tasks()

    def file_creator(self):
        with open(self._filename,'w') as f:
            pass
    
    @property
    def filename(self):
        return self._filename
    
    @filename.setter
    def filename(self,value):
        print('File name is protected')
        raise PermissionError()    
        
    def load_tasks(self) -> str:
        if not os.path.exists(self._filename):
            self.file_creator()
            print('file has been saved or created!')
            
        with open(self._filename,'r') as f:
            return [line.strip() for line in f.readlines()]    
        
    def save_tasks(self):
        with open(self._filename,'w') as f:
               for tasks in self.tasks:
                   f.write(tasks +'\n')
                               
    def view_tasks(self) -> str:
        if not self.tasks:
            print('No Tasks were saved!')
            return
        print('\n Your tasks are: ')
        for i, tasks in enumerate(self.tasks, start=1):
            print(f'{{{i}: {tasks}}}')
        print()
        
    def add_tasks(self):
        task = input('Enter a Task: ').strip()
        if task:
            self.tasks.append(task)
            self.save_tasks()
            print('Task Updated \n')
        else:
            print('Please provide a task')
            
    def delete_tasks(self):
        self.view_tasks()
        if not self.tasks:
            return
        try:
            num = int(input('Enter the index of task to be deleted : '))
            if 1 <= num <= len(self.tasks):
                removed = self.tasks.pop(num-1)
                self.save_tasks()
                print(f"The Tasks <{removed}> has been removed!")
            else:
                print('invalid index')
        except ValueError:
            print('Please enter a valid index: ')
            
            
def main():
    todo = ToDoList()
    while True:
        print("=== To-Do List ===")
        print("1. View tasks")
        print("2. Add task")
        print("3. Delete task")
        print("4. Exit")                            
        
        choice = input('Choose an option : ').strip()
        
        if choice == '1':
            todo.view_tasks()
        elif choice == '2':
            todo.add_tasks()
        elif choice == '3':
            todo.delete_tasks()
        elif choice == '4':
            print("Program Completed!")
            exit()
        else:
            print('Invalid Choice')
            
if __name__ == '__main__':
    main()            