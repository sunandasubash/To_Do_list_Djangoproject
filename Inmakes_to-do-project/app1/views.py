from django.shortcuts import render, redirect

from app1.forms import todoform
from app1.models import table1


# Create your views here.
def home(request):
    todo = table1.objects.all()
    if request.method == 'POST':
        name=request.POST.get('task','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        task=table1(name=name,priority=priority,date=date)
        task.save()
    return render(request,'home.html',{'todo':todo})

def delete(request,taskid):
    if request.method =='POST':
        task1=table1.objects.get(id=taskid)
        task1.delete()
        return redirect('/')
    return render(request,'delete.html')


from django.shortcuts import render, redirect
from .forms import todoform

def update(request,taskid):
    if request.method == 'POST':
        to = table1.objects.get(id=taskid)
        form = todoform(request.POST or None,instance=to)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = todoform()

    return render(request, 'update.html', {'form': form})


