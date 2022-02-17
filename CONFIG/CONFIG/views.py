from django.shortcuts import render
from django.views import View





class HomePageView(View):
    http_method_names = ['get',]
    def get(self,request):
        return render(request,"homepage.html")




