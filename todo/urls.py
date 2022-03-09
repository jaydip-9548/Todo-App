


from django.contrib import admin
from django.urls import URLPattern, path,include
from Mytodo import views
from rest_framework import routers

router = routers.DefaultRouter()
# Register the url
router.register(r'todoapi',views.TodoList,basename="Todo")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
]















#     # path('todoapi/',views.TodoList.as_view({'get': 'list'}))
#     path('todoapi/',views.TodoList.as_view({'get':'list','post':'create'}),),
#     path('todoapi/<int:pk>/',views.TodoList.as_view(
#         {'delete':'destroy','get':'retrieve','put':'update'}
        
#         ),),