from django.apps import AppConfig

from django.http import HttpResponse

class BaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base'

    
    def home(request):
        return HttpResponse('Home page')

    def rome(request):
        return HttpResponse(' Rome')

