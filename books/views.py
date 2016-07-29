# Create your views here.


from django.http import HttpResponse
from django.shortcuts import render_to_response
from books.models import Book
from django.http  import HttpResponseRedirect
from books.forms import ContactForm
from django.core.mail import send_mail

def display_meta(request):
    values = request.META.items()
    values.sort()
    html= []
    for k,v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k,v))
    return HttpResponse('<table border="1 px">%s</table>' % '\n'.join(html))





def search(request):
        if request.method == 'POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                cd = form.clean_

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm()
    return render_to_response('contact_form.html', {'form': form})

