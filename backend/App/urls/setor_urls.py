from django.urls import path
from ..views import setor_views

app_name = 'setores'

urlpatterns = [
    path('datatable/', setor_views.datatable, name='setores_datatable'),
    path('show/', setor_views.show, name='show'),
    path('store', setor_views.store, name='store'),
    path('edit/<int:id>/', setor_views.edit, name='edit'),
    path('update/<int:id>/', setor_views.update, name='update'),
    path('destroy/<int:id>/', setor_views.destroy, name='destroy'),
]