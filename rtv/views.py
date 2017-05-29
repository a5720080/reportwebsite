from .models import Report
from django.views import generic

class IndexView(generic.ListView):
    template_name = 'rtv/index.html'
    context_object_name = 'all_report'

    def get_queryset(self):
        return Report.objects.all()

class DetailView(generic.DetailView):
    model = Report
    template_name = 'rtv/detail.html'

class ReportCreate(generic.CreateView):
    model = Report
    fields = ['topic',
              'license_plate',
              'address',
              'date']
