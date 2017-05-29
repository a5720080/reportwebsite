from django.http import Http404
from .models import Report
from django.shortcuts import render

def index(request):
    all_report = Report.objects.all()
    context = {
        'all_report' : all_report,
    }
    return render(request , 'rtv/index.html',context)

def detail(request,report_id):
    try:
        report = Report.objects.get(pk=report_id)
    except Report.DoesNotExist:
        raise Http404("Report Does not exist")
    return render(request , 'rtv/detail.html',{'report':report})
