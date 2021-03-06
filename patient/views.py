from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Record
from practitioner.models import Profile
from django.views.generic import ListView, DetailView, CreateView

# Create your views here.
def home(request):
    records = Record.objects.order_by('-created_at')
    practitioners = Profile.objects.all()
    users = User.objects.all()
    context = {
        'records': records,
        'practitioners': practitioners,
        'users': users
        }
    return render(request, 'patient/home.html', context)

def search(request):
    records = Record.objects.order_by('-created_at')

    if 'condition' in request.GET:
        keywords = request.GET['condition']
        if keywords:
            records = records.filter(condition__iexact=keywords)

    return render(request, 'patient/record_list.html', {'records': records})

class RecordListView(ListView):
    model = Record
    context_object_name = 'records'
    ordering = ['-created_at']

class RecordDetailView(DetailView):
    model = Record

class RecordCreateView(LoginRequiredMixin, CreateView):
    model = Record
    fields = ['firstname', 'lastname', 'telephone', 'gender', 'address', 'condition', 'description']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        messages.success(self.request, f'Your record was added successfullly.')
        return super().form_valid( form)
    