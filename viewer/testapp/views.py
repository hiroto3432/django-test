from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.

MOVIES = [['eKoD2CRr_KA','cyq5bUXpnYI','MKINc7Rs6v8','PRJoAPH0ZGo','WgAhMfhdZ4c','EczxghXYxQ8'],
          ['x8VYWazR5mE','ZNFKZI7L9xE','Y4nEEZwckuU','dy90tA3TT1c'],
          ['MpYy6wwqxoo','qIBWRPqJcGQ','8JU7DetRbaI','GvL7mXF6WOc','K2pCnvLXdks']]
def top(request):
    info = {
    'param':1,
    'param_max':len(MOVIES),
    'movies': MOVIES[0]
    }
    return render(request, 'testapp/top.html', info) 

def settings(request):
    return render(request, 'testapp/settings.html') 

def index(request,param):
	info = {
	'param': param,
	'param_max':len(MOVIES),
    'movies': MOVIES[param-1]
    }
	return render(request, 'testapp/top.html', info) 