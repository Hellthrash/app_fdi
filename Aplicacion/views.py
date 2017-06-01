# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

from django.http import HttpResponseRedirect

from . models import Academico

from django import forms

def principal(request):
	return render(request, 'Aplicacion/principal.html',{'var':Academico.objects.all()})

def nuevo_academico(request):
	if(request.method=='POST'):
		form=Form_nuevo_academico(request.POST)
		if form.is_valid():
			datos=form.cleaned_data
			nuevo=Academico()
			nuevo.rut=datos.get('rut')
			nuevo.nombre=datos.get('nombre')
			nuevo.apellido=datos.get('apellido')
			nuevo.save()
			return principal(request)
		else:
			return HttpResponse("datos invalidos");
	elif(request.method=='GET'):
		return render(request, 'Aplicacion/nuevo_academico.html')
	else:
		return HttpResponse('metodo no soportado')

def editar_academico(request, pk):
	aux = get_object_or_404(Academico, pk=pk)
	if(request.method=='POST'):
		form=Form_nuevo_academico(request.POST)
		if form.is_valid():
			datos=form.cleaned_data
			aux.rut=datos.get('rut')
			aux.nombre=datos.get('nombre')
			aux.apellido=datos.get('apellido')
			aux.save()
			return principal(request)
		else:
			return HttpResponse("datos invalidos");
	elif(request.method=='GET'):
		return render(request, 'Aplicacion/editar_academico.html',{'var':aux})
	else:
		return HttpResponse('metodo no soportado')

def eliminar_academico(request, pk):
	aux = get_object_or_404(Academico,pk=pk)
	if(request.method=='POST'):
		aux.delete();
		return principal(request)
	elif(request.method=='GET'):
		return render(request, 'Aplicacion/eliminar_academico.html',{'var':aux})
	else:
		return HttpResponse('metodo no soportado')



class Form_nuevo_academico(forms.Form):
	nombre = forms.CharField(max_length=200)
	apellido = forms.CharField(max_length=200)
	rut = forms.CharField(max_length=20)

