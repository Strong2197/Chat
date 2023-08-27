from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import Message
from django.utils import timezone
from .forms import ChatForm
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from django.core.paginator import Paginator
# Create your views here.

#def main(request, x=Message.objects.order_by('-created_date').count(), ):
   # pages = (x//10)+1
    #messages = Message.objects.order_by('-created_date')[:10]

   # return render(request, 'chat/main.html', {'messages': messages, 'x': x, 'pages': pages})


def main(request):
    messages = Message.objects.order_by('-created_date')
    paginator = Paginator(messages, 10)  # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'chat/main.html', {'page_obj': page_obj})
def leave_message(request):
    messages = Message.objects.order_by('-created_date')
    try:
        messages.create(text=request.POST['text'], author=request.user, photo = request.FILES['images'])
    except:
        messages.create(text = request.POST['text'], author = request.user)

    return HttpResponseRedirect(reverse('main'))
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('main'))
                else:
                    return HttpResponse('Disabled account')
            else:
                return render(request, 'chat/login.html', {'form': form})
    else:
        form = LoginForm()
    return render(request, 'chat/login.html', {'form': form})
def photos(request,):
    messages = Message.objects.order_by('-created_date')

    return render(request, 'chat/photos.html', {'messages': messages})