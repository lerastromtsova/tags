from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import search_form,search
from .forms import SearchForm

urlpatterns = {
    url(r'^search_form/$', search_form, name="search"),
    url(r'^search/$', search),
}

urlpatterns = format_suffix_patterns(urlpatterns)


