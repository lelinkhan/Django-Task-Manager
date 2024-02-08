from django.shortcuts import render
from django.views import View
from .forms import RegistrationsFrom


class RegistrationView(View):
    def get(self, request):
        form = RegistrationsFrom()
        context = {
            'form': form
        }
        return render(request, 'registration.html', context)
