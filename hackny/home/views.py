from django.shortcuts import render, render_to_response
from django.template import RequestContext
from home.models import suggestion as suggestion_entry

def homepage(request):
	if request.POST:
		suggestion = request.POST.get('suggestion')

		new_entry = suggestion_entry(data=suggestion)
		new_entry.save()

	return render_to_response('homepage.html', context_instance = RequestContext(request))	
