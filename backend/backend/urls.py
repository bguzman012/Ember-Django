from django.conf.urls import url, include  
from django.contrib import admin  
from rest_framework import routers

from estudiantes import views 

router = routers.DefaultRouter(trailing_slash=False)  
router.register(r'estudiantes', views.EstudianteViewSet)
router.register(r'representantes', views.RepresentanteViewSet)

urlpatterns = [  
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
]