from django.core.mail import send_mail
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, FormView, TemplateView, CreateView

from blog.models import Post
from doxerp.models import Services
from settings import forms
from settings.forms import ContactForm
from settings.models import Setting, ClientLogo


class SettingListView(ListView):
    model = Setting
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["services"] = Services.objects.all()
        context["posts"] = Post.objects.all()[:3]
        context["client_logo"] = ClientLogo.objects.all()
        return context


def sitemap(request):
    return render(request, 'home/sitemap.xml')


def robots(request):
    return render(request, 'home/robots.txt')


class AboutUsListView(ListView):
    model = Setting
    template_name = 'settings/about.html'


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'settings/success.html')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'settings/contact.html', context)


class ContactSuccessView(TemplateView):
    template_name = 'settings/success.html'


class SolutionsListView(ListView):
    model = Setting
    template_name = 'dox/solution.html'
