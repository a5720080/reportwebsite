from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>This is Rtv app homepage </h1>")

def detail(request,report_id):
    return HttpResponse("<h2>Detail for Rreport id " + str(report_id) + "</h2>")
