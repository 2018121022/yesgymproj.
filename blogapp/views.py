from django.shortcuts import get_object_or_404, redirect, render
from .models import Gym

# Create your views here.

def home(request):
    return render(request, 'home.html')

def comment(request):
    gym_comment = Gym.objects.all()
    return render(request, "comment.html", {"gym_comment":gym_comment})

def lesson(request):
    return render(request, "lesson.html")

def content(request):
    return render(request, "content.html")

def detail(request, gym_id):
    gym = get_object_or_404(Gym, pk = gym_id)

    return render(request, "detail.html", {"gym":gym})

def write(request):
    if request.method == "GET":
        return render(request, "write.html")
    
    gym = Gym.objects.create()
    gym.title = request.POST['title']
    gym.content = request.POST['content']
    gym.save()

    return redirect('detail', gym.id)

def update(request, gym_id):
    if request.method == "GET":
        gym = get_object_or_404(Gym, pk = gym_id)
        return render(request, "update.html", {"gym":gym})

    gym = get_object_or_404(Gym, pk = gym_id)
    title = request.POST['title']
    content = request.POST['content']

    gym.title = title
    gym.content = content
    gym.save()
    return redirect('detail', gym.id)

def delete(request, gym_id):
    gym = get_object_or_404(Gym, pk = gym_id)
    gym.delete()
    return redirect('comment')