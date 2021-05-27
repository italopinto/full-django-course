from django.shortcuts import render, redirect, get_object_or_404
from .models import Client, ID
from .forms import ClientForm, IdForm
from django.contrib.auth.decorators import login_required #-> para limitar o acesso a certas views a usuarios com sessoes logadas


# Client's views
# C: Create
@login_required
def new_client(request):
    form = ClientForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('core:list_clients')

    context = {
        'form': form,
    }
    return render(request, 'form.html', context=context)


# R: Read
def list_clients(request):
    clients = Client.objects.all()
    context = {
        'clients': clients,
    }
    return render(request, 'clients.html', context=context)


# U: Update
@login_required
def update_client(request, id):
    client = get_object_or_404(Client, pk=id)
    form = ClientForm(request.POST or None, request.FILES or None, instance=client) #-> criara o form com informacoes predefinidas o client

    if form.is_valid():
        form.save()
        return redirect('core:list_clients')

    context = {
        'form': form,
    }
    return render(request, 'form.html', context=context)


# D: Delete
@login_required
def delete_client(request, id):
    client = get_object_or_404(Client, pk=id)

    if request.method == 'POST': #->so caira aqui quando clicar em apagar que mandara um post aqui
        client.delete()
        return redirect('core:list_clients')

    context = {
        'client': client,
    }
    return render(request, 'confirm.html', context=context)#-> so chega aqui com metodo get pois e apenas uma requisicao


# Id's views
# C: Create
@login_required
def new_id(request):
    form = IdForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('core:list_id')

    context = {
        'form': form,
    }
    return render(request, 'form.html', context=context)


# R: Read
@login_required
def list_id(request):
    doc_ids = ID.objects.all()
    context = {
        'id': doc_ids,
    }
    return render(request, 'clients_id.html', context=context)


# U: Update
@login_required
def update_id(request, id):
    doc_id = get_object_or_404(ID, pk=id)
    form = IdForm(request.POST or None, instance=doc_id)

    if form.is_valid():
        form.save()
        return redirect('core:list_id')

    context = {
        'form': form,
    }
    return render(request, 'form.html', context=context)


# D: Delete
@login_required
def delete_id(request, id):
    doc_id = get_object_or_404(ID, pk=id)

    if request.method == 'POST':
        doc_id.delete()
        return redirect('core:list_id')

    context = {
        'id': doc_id,
    }
    return render(request, 'confirm.html', context=context)

