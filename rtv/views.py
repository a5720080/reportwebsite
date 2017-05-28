from django.http import HttpResponse
from .models import Report
from django.template import loader

def index(request):
    all_report = Report.objects.all()
    template = loader.get_template('rtv/index.html')
    context = {
        'all_report' : all_report,
    }
    return HttpResponse(template.render(context , request))

def detail(request,report_id):
    return HttpResponse("<h2>Detail for Rreport id " + str(report_id) + "</h2>")
