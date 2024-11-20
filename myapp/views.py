from django.shortcuts import render, redirect
from myapp.models import Appointment, Contacts


# Create your views here
def index(request):
    return render(request, 'index.html')


def service(request):
    return render(request, 'service-details.html')


def starter(request):
    return render(request, 'starter-page.html')


def about(request):
    return render(request, 'about.html')


def myservice(request):
    return render(request, 'services.html')


def doctors(request):
    return render(request, 'doctors.html')


def departments(request):
    return render(request, 'departments.html')


def contacts(request):
    if request.method == 'POST':
        mycontacts = Contacts(
            name=request.POST['name'],
            email=request.POST['email'],
            subject=request.POST['subject'],
            message=request.POST['message'],
        )
        mycontacts.save()
        return redirect('/showcontacts')

    else:
        return render(request, 'contacts.html')


def appointment(request):
    if request.method == 'POST':
        myappointment = Appointment(
            name=request.POST['name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            date=request.POST['date'],
            department=request.POST['department'],
            doctor=request.POST['doctor'],
            message=request.POST['message'],
        )
        myappointment.save()
        return redirect('/show')

    else:
        return render(request,'appointment.html')

def show(request):
    allappointments = Appointment.objects.all()
    return render(request,'show.html',{'appointment':allappointments})

def delete(request,id):
    appoint = Appointment.objects.get(id=id)
    appoint.delete()
    return redirect('/show')

def showcontacts(request):
    allcontacts = Contacts.objects.all()
    return render(request,'showcontacts.html',{'contact':allcontacts})

def deletecontacts(request,id):
    mycontacts = Contacts.objects.get(id=id)
    mycontacts.delete()
    return redirect('/showcontacts')