from django.http import HttpResponse
from .models import Report
from django.shortcuts import render

def index(request):
    all_report = Report.objects.all()
    context = {
        'all_report' : all_report,
    }
    return render(request , 'rtv/index.html',context)

def detail(request,report_id):
    return HttpResponse("<h2>Detail for Rreport id " + str(report_id) + "</h2>")
