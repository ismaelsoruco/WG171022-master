from django.shortcuts import render, redirect # si
from django.views.generic import View, CreateView

from django.views.generic import CreateView # registration
from django.contrib.auth import get_user_model #registration
from .forms import  SignUpForm

from django.contrib.auth.forms import UserCreationForm # register
from django.contrib.auth import login, authenticate #register
from django.contrib.sites.shortcuts import get_current_site #register
from django.utils.encoding import force_bytes #register
from django.utils.http import urlsafe_base64_encode # register
from django.template.loader import render_to_string # register
from register.forms import SignUpForm # register
from register.tokens import account_activation_token # register
from django.contrib.auth.models import User # register
from django.utils.encoding import force_text # register
from django.utils.http import urlsafe_base64_decode # register
from apli.models import Person, Project, Attachment, Assignment, Horaire, Cost, Time

User = get_user_model()


   

#REGISTER

#a continuación, se explica el codigo en el orden que ocurren las cosas:
#primero el usuari ingresa sus datos y se envia el mail con un codigo personal de confirmacion.
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Activate Your MySite Account'
            message = render_to_string('account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            return redirect('account_activation_sent')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


# entonces te manda a la pagina, tu mail fue enviado. 
def account_activation_sent(request):
    return render(request, 'account_activation_sent.html', )

#REGISTER: activacion de mail entra aca para guardar su usuario. se crea un perfil tambien. 

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('account_activation_complete')
    else:
        return render(request, 'account_activation_invalid.html')


#te manda a la pagina que se confirmo tu registro.
def account_activation_complete(request):
    return render(request, 'account_activation_complete.html', )


    #en teoria lo siguiente no se necesita, pero lo dejo por si las mosca...deberia ser automatico con auth_views

# def password_reset_complete(request):
#   return render(request, 'password_reset_complete.html', )

# def password_reset_confirm(request):
#   return render(request, 'password_reset_confirm.html', )

# def password_reset_done(request):
#   return render(request, 'password_reset_done.html', )

# def password_reset_email(request):
#   return render(request, 'password_reset_email.html', )

# def password_reset(request):
#   return render(request, 'password_reset_form.html', )



##########################################################################################







