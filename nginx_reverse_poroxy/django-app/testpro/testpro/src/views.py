from django.http import HttpResponse



def main_page(request) -> HttpResponse:
    return HttpResponse('<p>Django main page.</p>')

def page_1(request) -> HttpResponse:
    return HttpResponse('<p>Django Page one.</p>')
