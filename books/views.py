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


def test(request,a):
    html='test.html'
    b=a
    return render_to_response(html,locals())