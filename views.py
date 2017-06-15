from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from .forms import SearchForm

def search(request):
    if request.GET['tag'] != '':
        return render(request, 'search_results.html', {'tag': request.GET['tag']})
        # return HttpResponseRedirect('/search/')

    else:
        return HttpResponse('You submitted an empty form.')


def search_form(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        tagname = request.GET['tag']
        if form.is_valid():
            return HttpResponseRedirect('/search/?tag=%tagname/')
    else:
        form = SearchForm()

    return render(request, 'search_form.html', {'form': form})

