from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
#from django.views.generic import CreateView
from django.views.generic import DetailView
#from django.views.generic import UpdateView
# from django.views.generic import DeleteView
from todo.models import Task


class TaskListView(ListView): #paramètres disponibles dans ListeView    
    """Documentation de notre controleur"""
    model = Task # modèle relative
    context_object_name = "tasks"  #es el que ponemos en el html
    template_name = "todo/tasks-list.html" # chemin vers le template
    paginate_by = None # pour préciser qu'on ne veut pas de pagination 

# class TaskCreateView(CreateView):
#     model = Task
#     template_name = "todo/tasks-create.html"

class TaskDetailView(DetailView):
    model = Task 
    context_object_name = "task"
    template_name = "todo/tasks-detail.html"

# class TaskUpdateView(UpdateView):
#     model = Task 
#     context_object_name = "update"
#     template_name = "todo/tasks-update.html"

# class TaskDeleteView(DeleteView):
#     model = Task
#     context_object_name = "tasks"
#     template_name = "todo/tasks-delete.html"
