from django.urls import path
from meta import views

urlpatterns = [
    path('listaCargos/', views.lista_cargo),
    path('listaCargos/<int:pk>', views.lista_cargo_detail),

    path('listaEquipos/', views.lista_equipos),
    path('listaEquipos/<int:pk>', views.lista_equipos_detail),

    path('listaMiembros/', views.lista_miembros),
    path('listaMiembros/<int:pk>', views.lista_miembros_detail),

    path('listaMiembros/', views.lista_miembros),
    path('listaMiembros/<int:pk>', views.lista_miembros_detail),

    path('listaCarreras/', views.lista_carreras),
    path('listaCarreras/<int:pk>', views.lista_carreras_detail),

    path('listaVueltas/', views.lista_vueltas),
    path('listaVueltas/<int:pk>', views.lista_vueltas_detail),
    path('listaPosiciones/<int:teams>',views.lista_posiciones)
]