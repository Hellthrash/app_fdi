from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.principal, name='principal'),
	url(r'^academicos/nuevo/', views.nuevo_academico, name='nuevo_academico'),
	url(r'^academicos/editar/(?P<pk>\d+)$', views.editar_academico, name='editar_academico'),
	url(r'^academicos/eliminar/(?P<pk>\d+)$', views.eliminar_academico, name='eliminar_academico'),
	]
