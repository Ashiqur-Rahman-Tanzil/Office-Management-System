from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),

    path('attendance_page', views.attendance_page, name="attendance_page"),
    path('ab_view', views.ab_view, name='ab_view'),
    path('ab_input', views.ab_input, name='ab_input'),
    path('input_attendance', views.input_attendance, name='input_attendance'),

    path('employee_of_the_month', views.employee_of_the_month, name='employee_of_the_month'),
    path('emb_view', views.emb_view, name='emb_view'),
    path('emb_rate', views.emb_rate, name='emb_rate'),
    path('emb_rate_input', views.emb_rate_input, name='emb_rate_input')

]
