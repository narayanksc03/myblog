from django.shortcuts import render

# Create your views here.
def demoIndex(request):
    template = 'index.html'
    return render(request, template)
#render()-> takes three parameter among which two of them are compulsory
#  1. request
#  2. templates
#  3. data(must be in dict)optional parameter