from .models import Report
from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from .forms import UserForm
from django.views.generic import View

class IndexView(generic.ListView):
    template_name = 'rtv/index.html'
    context_object_name = 'all_report'

    def get_queryset(self):
        return Report.objects.all()

class DetailView(generic.DetailView):
    model = Report
    template_name = 'rtv/detail.html'

class ReportCreate(CreateView):
    model = Report
    fields = ['topic','license_plate','address','date','image']

class ReportUpdate(UpdateView):
    model = Report
    fields = ['topic','license_plate','address','date','image']

class ReportDelete(DeleteView):
    model = Report
    success_url = reverse_lazy('rtv:index')

class UserFormView(View):
    form_class = UserForm
    template_name = 'rtv/registration_form.html'

    # display blank form_class
    def get(self,request):
        form = self.form_class(None)
        return render(request, self.template_name, {'forms':form})
   #process form daata
    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit = False)
            # cleaed (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # return User objects if credentials are correct
            user = authenticate(username = username, password = password)

            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('rtv:index')

        return render(request, self.template_name, {'forms':form})

def about(request):
    return render(request, 'rtv/about.html')
