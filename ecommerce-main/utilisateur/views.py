
from django.shortcuts import render, redirect
"""from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UtilisateurSerializer
from rest_framework.authtoken.serializers import AuthTokenSerializer """
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login 
#from knox.auth import AuthToken
import io 
from django.http import FileResponse
from reportlab.pdfgen import canvas
from django.utils.translation import gettext_lazy as _
from .models import Utilisateur
from client.models import Client
from commande.models import Commande
from livraison.models import Livraison
from recu.models import Recu
from django.contrib.auth.models import User 
from produit.utily import *
from .forms import *
#Importation for xhtml2pdf
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders

# Create your views here.
"""
def inscription(request):
	form, form1 = CreerUtilisateur(), CreateUtilisateur()
	if request.method == 'POST':
		form, form1 = CreerUtilisateur(request.POST), CreateUtilisateur(request.POST)
		if form.is_valid() and form1.is_valid():
			form.save(), form1.save()
			user, utilisateur, user_ins, utilisateur_ins, utilisateur_ins.user = form.cleaned_data.get('username'), form1.cleaned_data.get('nom'), User.objects.get(username=user), Utilisateur.objects.get(nom=utilisateur), user_ins
			messages.success(request, 'compte créer avec succèss'),  print(user), print(user1), utilisateur_ins.save() 
			return redirect('access')
	context = {'form': form, 'form1':form1}
	return render(request, 'admin/register.html', context) """

def inscription(request):
    form = CreerUtilisateur()
    form1 = CreerClient()
    data = cartData(request)
    cartItems = data['cartItems']
    if request.method == 'POST':
        form = CreerUtilisateur(request.POST)
        form1 = CreerClient(request.POST)
        
        try:
            if  form.is_valid and form1.is_valid :
                form.save()
                form1.save()
                user_save = form.cleaned_data.get('username')
                utilisateur_save = form1.cleaned_data.get('nom')
                user = User.objects.get(username=form.cleaned_data.get('username'))
                password = User.objects.get(password=form.cleaned_data.get('password'))
                utilisateur = Utilisateur.objects.get(nom=form1.cleaned_data.get('nom'))
                utilisateur.user = user 
                utilisateur.save()
                user_auth = authenticate(request, username=user, password=password)
                auth_login(request, user_auth)
                messages.success(request, 'Compte créer avec succèss')
                return redirect('home')
        except:
            pass
        
    context = {'form': form, 'form1': form1, "cartItems": cartItems}
    return render(request, 'admin/register.html', context)



def access(request):
    data = cartData(request)
    cartItems = data['cartItems']
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user), messages.info(request, 'Continuer')
            return redirect('home')
        else:
            messages.info(request, 'Le nom d\'utilisateur et/ou le mot de passe est incorrecte')
    context = {"cartItems": cartItems}
    return render(request, 'admin/login.html', context)

def quitter(request):
	logout(request)
	return redirect('access')


def index(request):
    client = request.user.utilisateur.client
    commandes = Commande.objects.filter(client=client).exclude(transaction_id=None)
    nombre = commandes.count
    context = {"commandes": commandes, "nombre": nombre}
    return render(request, 'admin/index.html', context)

def recu(request):
    client = request.user.utilisateur.client
    commandes = Commande.objects.filter(client=client).exclude(transaction_id=None)
    context = {"commandes": commandes}

    return render(request, 'admin/recu/recu.html', context) 

def recu_pdf(request, pk):
    commande = Commande.objects.get(id=pk)
    items = commande.constituer_set.all()
    livraisons = Livraison.objects.filter(commande=commande)
    template_path = 'pdf/recu.html'
    context = {'commande': commande, 'items': items, 'livraisons': livraisons}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    #response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    response['Content-Disposition'] = 'filename="recu.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response




def test(request):
    template_path = 'pdf/recu.html'
    context = {'myvar': 'this is your template context'}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    #response['Content-Disposition'] = 'attachment; filename="recu.pdf"'
    response['Content-Disposition'] = 'filename="recu.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response








"""

@api_view(['POST'])
def login_api(request):
    serializer = AuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']
    _, token = AuthToken.objects.create(user)

    return Response("bien ça marche!")





#API REST 
@api_view(['GET'])
def allUtilisateurs(request):
    utilisateurs = Utilisateur.objects.all()
    serialization = UtilisateurSerializer(utilisateurs, many=True)
    return Response(serialization.data)

@api_view(['GET'])
def getUtilisateur(request, id):
    utilisateur = Utilisateur.objects.get(id=id)
    serialization = UtilisateurSerializer(utilisateur)
    return Response(serialization.data)

@api_view(['POST'])
def addUtilisateur(request):
    serializer = UtilisateurSerializer(data=request.data, many=True)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def updateUtilisateur(request, id):
    utilisateur = Utilisateur.objects.get(id=id)
    serialization = UtilisateurSerializer(instance=utilisateur, data=request.data)
    if serialization.is_valid():
        serialization.save()
    return Response(serialization.data)

@api_view(['DELETE'])
def deleteUtilisateur(request, id):
    utilisateur = Utilisateur.objects.get(id=id)
    utilisateur.delete()
    return Response("Utilisateur supprimé avec succès!")

"""
"""
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer

# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })
"""