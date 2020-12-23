from django.shortcuts import render

def home(request):
	return render(request, 'home.html')

def reverse(request):
	user_text = request.GET['usertext']
	kol = len(user_text.split())
	reverse_text = user_text[::-1]
	return render(request, 'Reverse.html', {'usertext':user_text, 'kol':kol, 'rev_text': reverse_text})