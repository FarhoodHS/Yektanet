from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('detail', views.detail, name='detail'),
    path('short', views.home),
    path('<slug:shortened_url>', views.goto, name='goto'),
    path('detail/filter-by-day', views.filterbyday, name='filterbyday'),
    path('detail/filter-by-week', views.filterbyweek, name='filterbyweek'),
    path('detail/filter-by-month', views.filterbymonth, name='filterbymonth'),
    path('detail', views.detail, name='detail'),
    

]