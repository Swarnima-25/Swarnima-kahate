from django.contrib import admin
from django.urls import path
from demoapp import views
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.homepage_view),
    path('entertain/',views.entertainment_view),
    path('exerciise/',views.exercise_view),
    path('dietplan/',views.diet_view),
    path('doctor/',views.doctor_view),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/',views.logout_view),
    path('signup/',views.signup_view),

]
