from django.views.generic import ListView
from django.contrib.auth import get_user_model

# Create your views here.


class Accessed(ListView):
    context_object_name = 'users'

    template_name = 'users/logged_in.html'

    def get_queryset(self):
        return get_user_model().objects.exclude(last_login=None)