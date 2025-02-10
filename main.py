from fastapi import FastAPI #FastAPI is the web framework that helps us build APIs.
from pydantic import BaseModel #BaseModel is from the pydantic library. We use it to define the structure of data (like a Task), including what fields it should have and the types of those fields

app = FastAPI() #creates an instance of the FastAPI app. App object is used to define API endpoints


class Task(BaseModel): #add BaseModel to class for data validation and structure
        title: str
        description: str
        completed: bool

#empty list to store tasks
tasks = []

@app.post("/tasks/") #handle POST request to /tasks URL
def create_task(task: Task): #function expects a Task object to be sent in the request body
        tasks.append(task) #adds the task to the tasks list
        return task

@app.get("/tasks/") #handle GET request to /tasks URL
def get_tasks(): 
        return tasks #returns the list of tasks as a JSON response

@app.get("/tasks/{task_id}") #route accepts a task ID in the URL (e.g., /tasks/1).
def get_task(task_id: int): #convert URL part into an integer and pass to function
        return tasks[task_id] if 0 <= task_id < len(tasks) else {"error": "Task not found"} #check if task_id is in range of list
        

