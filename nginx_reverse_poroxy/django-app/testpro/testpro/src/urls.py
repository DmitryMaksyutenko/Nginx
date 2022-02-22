from django.urls import path

from .views import main_page, page_1


urlpatterns = [
    path('', main_page, name='main-page'),
    path('page1', page_1, name='page-1')
]
