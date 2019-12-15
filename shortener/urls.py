from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('links', views.links, name='links'),
    path('<slug:shortened_url>', views.goto, name='goto'),
    path('links/filter-by-day', views.filterbyday, name='filterbyday'),
    path('links/filter-by-week', views.filterbyweek, name='filterbyweek'),
    path('links/filter-by-month', views.filterbymonth, name='filterbymonth'),
    path('links/<slug:shortened_url>', views.linkdetail, name='linkdetail'),
    
    
    

]