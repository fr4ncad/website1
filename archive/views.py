from django.shortcuts import render
from .models import user

cu = ''

def signup(request):
    context = {'felhasznalok':user.objects.all()}
    if request.method == 'POST':
        if user.form(request.POST):
            cu = request.POST['name']
            print(cu)
            return render(request, 'archives.html', context)
    return render(request, 'login_page.html')

def bejegyzes(request):
    content = {'felhasznalonev':cu}
    return render(request, 'content.html')