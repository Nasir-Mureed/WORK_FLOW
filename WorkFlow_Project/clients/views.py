from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from .models import Client
from django.shortcuts import get_object_or_404
# Create your views here.
@login_required
def clients(request):
    clients = Client.objects.filter(user = request.user)
    return render(request, 'clients/clients.html' ,{'clients' : clients} )

@login_required
def addClient(request):
    if request.method == 'POST':
        data = request.POST
        name = data.get('name')
        email = data.get('email')

        Client.objects.create(
            user = request.user,
            name = name ,
            email = email,
        )

        return redirect('clients:clients')
    return render(request , 'clients/addClient.html')    

@login_required
def editClient(request,id):
    client =  get_object_or_404(Client, id = id, user = request.user)
    if request.method == 'POST':
        client.name = request.POST.get('name')  
        client.email = request.POST.get('email')
        client.save()
        if client:
            return redirect('clients:clients')
    return render(request, 'clients/editClient.html' ,{'client' : client})    

@login_required
def deleteClient(request,id):
    client = get_object_or_404(Client,id = id,user = request.user)
    if client:
        client.delete()
        return redirect('clients:clients')
    return render(request,'clients/clients.html')
