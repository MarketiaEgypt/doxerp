from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from doxerp.models import Solutions


class SolutionsListView(ListView):
    model = Solutions
    template_name = 'dox/solution.html'
    context_object_name = 'solutions'