from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from .forms import SearchForm

def search(request):
    if 'tag' in request.GET and request.GET['tag']!='':
        return HttpResponseRedirect('/search/')
    else:
        return HttpResponse('You submitted an empty form.')




def search_form(request):
    # if this is a POST request we need to process the form data
    if request.method == 'GET':
        # create a form instance and populate it with data from the request:
        form = SearchForm(request.GET)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/search/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SearchForm()

    return render(request, 'search_form.html', {'form': form})

