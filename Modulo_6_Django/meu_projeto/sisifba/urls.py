from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('sisifba.urls')),
    path('aluno/', include('aluno.urls')),
    path('curso/', include('curso.urls')),
    path('professor/', include('professor.urls')),
]