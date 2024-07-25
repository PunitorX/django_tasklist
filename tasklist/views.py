from django.shortcuts import render
from .models import Todo

# Rendering home page
def index(request):
  todos = Todo.objects.all().order_by('-id')
  return render(request, 'index.html', {'todos': todos})

# Create a new task
def create_todo(request):
  title = request.POST.get('title') # Retrieves title from POST
  todo = Todo.objects.create(title=title) # Creates task
  todo.save() # Saves new task
  todos = Todo.objects.all().order_by('-id') # Retrieves all task from database, ordered by ID in descending order
  return render(request, 'todo-list.html', {'todos': todos}) # Renders template with updated list

# Marking a task completed
def mark_todo(request, pk): # PK = primary key as a parameter
  todo = Todo.objects.get(pk=pk) # Retrieves task 
  todo.completed = True # Sets task to completed
  todo.save() # Saves changes
  todos = Todo.objects.all().order_by('-id') # Retrieves all task from database, ordered by ID in descending order
  return render(request, 'todo-list.html', {'todos': todos}) # Renders template with updated list

# Deleting a task
def delete_todo(request, pk): # PK = primary key as a parameter
  todo = Todo.objects.get(pk=pk) # Retrieves task
  todo.delete() # Deletes task
  todos = Todo.objects.all().order_by('-id') # Retrieves all task from database, ordered by ID in descending order
  return render(request, 'todo-list.html', {'todos': todos}) # Renders template with updated list
