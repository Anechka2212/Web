from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_view

from lab_app.views import FilmView, ListFilmView, AddFilmView, \
    SignUpView, LoginView, LogoutView, create_review, AboutView

urlpatterns = [
    url(r'^$', ListFilmView.as_view()),
    url(r'^page=(?P<page>\d+)', ListFilmView.as_view()),
    url(r'^film/(?P<film_id>\d+)', FilmView.as_view()),
    url(r'^film/create_review/$', create_review, name='create_review'),
    url(r'^film/add_film/$', AddFilmView.as_view()),
    url(r'^signup/$', SignUpView.as_view()),
    url(r'^login/$', auth_view.login, {'template_name': '/login_form.html'}),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^about/', AboutView.as_view()),
    url(r'^admin/', admin.site.urls),
]