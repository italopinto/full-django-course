"""clients URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views #-> views de autenticacao, login e logout, para funcionarem faça os htmls
from django.urls import path, include

# para o django servir imagens (static files) em debug mode
# to serve files uploaded by a user during development > https://docs.djangoproject.com/en/3.2/howto/static-files/
# from django.conf import settings
# from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('login/', auth_views.LoginView.as_view(), name='login'), #-> o django ja sabe que e uma view
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
] 
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # -> Return a URL pattern for serving files in debug mode
# dessa forma esta-se concatenando as urls existentes, novas url'patterns' dos arquivos estaticos, nesse caso
