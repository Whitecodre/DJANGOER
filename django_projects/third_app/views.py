from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import practice, customer_data, apis
from django.http import Http404
from rest_framework import generics
from .serializers import customer_dataSerializer, practiceSerializer, apiSerializer

# Create your views here.

def appfirst(request):
    customer_info = customer_data.objects.all()
    all_info = {"key" : customer_info}
    return render(request, 'first.html', all_info)

def appclass(request):
    return render(request, 'Classroom.html')

def appinfo(request):
    return render(request, 'Informate.html')

def appcontact(request):
    try:
        std = customer_data.objects.all()
        context = {'key':std}
    except:
        raise Http404()
    return render(request, 'Contact_form.html', context)


def apptable(request):
    customer_display = customer_data.objects.all()
    customer_dis = {'info' : customer_display}
    return render(request, 'table.html', customer_dis)

def appsign(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login = (request, user)
        return redirect('apptable')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form':form})


class customerCreateView(generics.ListCreateAPIView):
    serializer_class = customer_dataSerializer
    queryset = customer_data.objects.all()


class customerCreateSpecific(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = customer_dataSerializer
    queryset = customer_data.objects.all()


class practiceCreateView(generics.RetrieveAPIView):
    serializer_class = practiceSerializer
    queryset = practice.objects.all()

class apiCreateView(generics.ListCreateAPIView):
    serializer_class = apiSerializer
    queryset = apis.objects.all()

class apiCreateSpecific(generics.RetrieveAPIView):
    serializer_class = apiSerializer
    queryset = apis.objects.all()