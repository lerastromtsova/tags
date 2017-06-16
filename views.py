from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from .forms import SearchForm
from .tags_from_vk import count_tag
import datetime
import time

def search(request):
    values = []
    if request.GET['tag'] != '':
        tag = request.GET['tag']

        start_date = request.GET['start_date']
        end_date = request.GET['end_date']

        step = int(request.GET['interval']) * 3600

        start = int(time.mktime(datetime.datetime.strptime(start_date, "%Y-%m-%d").timetuple()))
        end = int(time.mktime(datetime.datetime.strptime(end_date, "%Y-%m-%d").timetuple()))

        while (start <= end - step):
            time.sleep(1)
            count = count_tag(tag, start, start + step)
            print(count)
            format_date = datetime.datetime.fromtimestamp(start).strftime("%b %d %Y %H:%M:%S")
            print(format_date)
            values.append([format_date, count])
            start = start + step
        return render(request, 'search_results.html', {'color': request.GET['color'],
                                                       'tag': tag,
                                                       'values': values})

    else:
        return HttpResponse('You submitted an empty form.')


def search_form(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        # tagname = request.GET['tag']
        if form.is_valid():
            return HttpResponseRedirect('/search/')
        else:
            form = SearchForm()

    return render(request, 'search_form.html', {'form': form})
