from django.shortcuts import render, redirect
LANGUAGES = (
    'Python',
    'C#',
    'JavaScript',
    'Java'
)
LOCATIONS = (
    'Seattle',
    'SanJose',
    'Chicago',
    'Dallas',
    'DC'
)

def index(request):
    context = {
        'location': LOCATIONS,
        'language': LANGUAGES
    }
    return render(request, 'form.html', context)

def survey(request):
    if request.method == 'GET':
        return redirect('/')
    request.session['result'] = {
        'name': request.POST['name'],
        'location': request.POST['location'],
        'language': request.POST['language'],
        'commment': request.POST['comment']
    }
    return redirect('/result')

def result(request):
    context = {
        'result': request.session['result']
    }
    return render(request,'result.html', context)