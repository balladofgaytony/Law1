from django.shortcuts import render
from .models import ClientCase



def home(request):
	return render(request,'case/home_employee.html')
def about(request):
	return render(request, 'main/about.html')
def case_list(request):
	cases = ClientCase.objects.all()
	return render(request,'case/case_list.html', {'cases': cases})



