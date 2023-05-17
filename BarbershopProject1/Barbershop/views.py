from django.shortcuts import render, redirect, get_object_or_404
from .models import ServiceModel
from .forms import ServiceForm
from django.views.generic import ListView, DetailView


def barberservice(request):
    services = ServiceModel.objects.all()
    return render(request, 'barberservice.html', {'services': services})


def create(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('barberservice')
    form = ServiceForm()

    return render(request, 'addservice.html', {'form': form})


def edit(request, id, template_name='edit.html'):
    old_data = get_object_or_404(ServiceModel, id=id)
    if request.method == 'POST':
        form = ServiceForm(request.POST, instance=old_data)
        if form.is_valid():
            form.save()
            return redirect('barberservice')
    else:
        form = ServiceForm(instance=old_data)
        return render(request, template_name, {'form': form})


def delete(request, id):
    contact = get_object_or_404(ServiceModel, id=id)
    if request.method == 'POST':
        contact.delete()
        return redirect('barberservice')
    else:
        return render(request, 'delete.html')
