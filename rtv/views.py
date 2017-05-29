from .models import Report
from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy
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
