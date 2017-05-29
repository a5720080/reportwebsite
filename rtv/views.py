from .models import Report
from django.shortcuts import render,get_object_or_404

def index(request):
    all_report = Report.objects.all()
    context = {
        'all_report' : all_report,
    }
    return render(request , 'rtv/index.html',context)

def detail(request,report_id):
    report = get_object_or_404(Report,pk=report_id)
    return render(request , 'rtv/detail.html',{'report':report})
