from django.shortcuts import render
from django.http import HttpResponseRedirect
from workapp.models import Works, Lives, WorksForm, SearchForm, LivesForm

def index(request):
    return render(request, 'workapp/index.html')

def insert_work(request):
    if request.method == 'POST':
        works_form = WorksForm(request.POST)
        lives_form = LivesForm(request.POST)
        if works_form.is_valid() and lives_form.is_valid():
            works_form.save()
            lives_form.save()
            return HttpResponseRedirect('/')
    else:
        works_form = WorksForm()
        lives_form = LivesForm()
    return render(request, 'workapp/insert.html', {'works_form': works_form, 'lives_form': lives_form})

def search(request):
    results = []
    company = ''
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            company = form.cleaned_data['company_name']
            workers = Works.objects.filter(company_name__iexact=company)
            for worker in workers:
                try:
                    lives = Lives.objects.get(person_name__iexact=worker.person_name)
                    street = lives.street
                    city = lives.city
                except Lives.DoesNotExist:
                    street = 'Not found'
                    city = 'Not found'
                results.append({'name': worker.person_name, 'street': street, 'city': city})
    else:
        form = SearchForm()
    return render(request, 'workapp/search.html', {'form': form, 'results': results, 'company': company})