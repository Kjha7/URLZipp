from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.db.models import F
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.


def encodeUrl(request):
    urlencode = None
    encoded_url = None
    if request.method == 'POST':

        urlencode = request.POST.get('url')
        encoded_url = UrlModel()
        encoded_url.original_url = urlencode
        print(encoded_url.url_id)
        urlencode = int(hashlib.sha1(encoded_url.original_url.encode('utf-8')).hexdigest(), 16) % (10 ** 8)
        try:
            encoded_url.encrypted_url = urlencode
            encoded_url.creation_date = timezone.now()
            encoded_url.save()
            print(urlencode)
        except:
            encoded_url = UrlModel.objects.get(encrypted_url=urlencode)

    return render(request, 'home.html', {'urlencode': urlencode, 'encoded_url': encoded_url})


def get_original_url(request, id_):
    print(id_)
    original_url1 = UrlModel.objects.get(encrypted_url=id_)
    print("JNBGFD")
    print(original_url1.original_url)
    return HttpResponseRedirect(original_url1.original_url)
