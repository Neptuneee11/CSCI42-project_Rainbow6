from pyexpat.errors import messages
from .forms import RegisterForm
from .models import UserProfile
from web.models import customerActions
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views import View
from django.views.generic.edit import FormView

# Create your views here.



class RegisterView(FormView):

    #form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'register/register.html'

    def get(self, request, *args, **kwargs):
        form = RegisterForm(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = RegisterForm(request.POST)

        print(form)

        if form.is_valid():
            try:
                newProfile = form.save()
                idNum = form.cleaned_data['id_number']
                schYear = form.cleaned_data['school_year']
                cou = form.cleaned_data['course']
                cpN = form.cleaned_data['phone_number']

                username = form.cleaned_data.get('username')

                UserProfile.objects.create(
                    user = newProfile,
                    id_number = idNum,
                    school_year = schYear,
                    course = cou,
                    phone_number = cpN,
                )

                customerActions.objects.create(
                    user = newProfile,
                )
                #messages.success(request, f'Account created for {username}')
                print(f"Account create for {username}")

                return redirect(to='/')
            
            except:
                print("Account creation failed due to incorrect forms")
            
            

        return render(request, self.template_name, {'form': form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')

