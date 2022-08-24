from django.urls import path
from . import views

urlpatterns = [
    path('', views.Main_Page.as_view(), name="shiny-main"),
    path('add-shiny/', views.ShinyCreateView.as_view(), name='add-shiny'),
    path('user/<str:username>', views.ShinyListView.as_view(template_name='shinydb/shiny_user.html'), name='shiny-user'),
    path('shiny/<int:pk>/update', views.ShinyUpdateView.as_view(template_name='shinydb/shiny_update.html'), name='shiny-update'),
    path('shiny/<int:pk>/delete', views.ShinyDeleteView.as_view(template_name='shinydb/shiny_delete.html'), name='shiny-delete'),
    path('shiny/<int:pk>', views.ShinyDetailView.as_view(template_name='shinydb/shiny_detail.html'), name='shiny-detail'),
]