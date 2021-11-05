from django.shortcuts import render

# Create your views here.
def index(request):
    context_dict = {'text':'hello world', 'number':100}
    return render(request, 'levelfourapp/index.html', context = context_dict)

def other(request):
    return render(request, 'levelfourapp/other.html')

def relative(request):
    return render(request, 'levelfourapp/relative_url_template.html')
