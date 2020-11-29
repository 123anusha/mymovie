from django.shortcuts import render

# Create your views here.
def creater(request):
    if request.method == 'POST':
        pass
    else:
        return render(request, 'editor/creater.html')