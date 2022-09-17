from django.urls import path
from recipes.views import home 
# ,create, post, update, delete


urlpatterns = [
    path('', home, name='home'),
   # path('create/', create, name='create'),
   # path('post/<int:pk>', repost, name='post'),
   # path('update/<int:pk>', update, name='update'),
   # path('delete/<int:pk>', delete, name='delete'),
]