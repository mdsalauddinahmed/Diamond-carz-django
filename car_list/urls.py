from django.urls import path,include
from .import views

urlpatterns = [
  path('', views.addCategories,name='category' ),
    # path('category/',include('car_list.urls')),
    # path('post/', include('car_post.urls')),
    # path('history/', include('car_sold_history.urls')),
    # path('user/', include('user.urls')),
]
