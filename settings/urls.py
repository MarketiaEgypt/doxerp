
from django.urls import path

from doxerp.views import SolutionsListView
from settings import views
from settings.views import ContactSuccessView

app_name = 'settings'

urlpatterns = [
    path('', views.SettingListView.as_view(), name='home'),
    path('about-us/', views.AboutUsListView.as_view(), name='about'),
    path('contact-us/', views.contact, name='contact'),
    path('success/', ContactSuccessView.as_view(), name="success"),
    path('solution/', SolutionsListView.as_view(), name="solution"),
    path('sitemap.xml/', views.sitemap, name='sitemap'),
    path('robots.txt/', views.robots, name='robots')
]
