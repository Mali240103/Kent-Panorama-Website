from django.urls import path 
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
path("",views.homepage, name="anasayfa"),
path("kupikInsaat", views.kupikInsaat, name="kupik"),
path("konum", views.konum, name="konum"),
path("konsept", views.konsept, name="konsept"),

path("projePlani", views.projePlani, name="projeplan"),

]

