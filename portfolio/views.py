from django.shortcuts import redirect

def redirect_about(request):
    response = redirect('/about')
    return response
