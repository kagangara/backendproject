from django.shortcuts import render

from .models import People,Contact


# Create your views here.
def index(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
# create an object
        new_person = People(first_name=first_name, last_name=last_name, email=email)
        new_person.save()

    # get all persons
        people = People.objects.all()
        return render(request, 'index.html', {'people': people})

    return render(request,'index.html')
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('names')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        course = request.POST.get('course')
        message = request.POST.get('message')

        savecontact=Contact(name=name, email=email, phone=phone, course=course, message=message)
        savecontact.save()

    return render(request, 'contact.html')