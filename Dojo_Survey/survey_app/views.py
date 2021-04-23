from django.shortcuts import render, redirect
def index(request):
    return render(request, 'form.html')

def process(request):
    if request.method == 'POST':
        context = {
            'name': request.POST['name'],
            'loc': request.POST['location'],
            'lang': request.POST['language'],
            'comment': request.POST['comment']
        }
        return render(request, 'results.html', context)
    return render(request, 'results.html')
# Create your views here.
