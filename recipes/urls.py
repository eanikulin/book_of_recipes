from django.urls import path
from .views import recipe_list, recipe_detail, recipe_create, recipe_edit, recipe_delete
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', recipe_list, name='recipe_list'),
    path('<int:pk>/', recipe_detail, name='recipe_detail'),
    path('create/', recipe_create, name='recipe_create'),
    path('<int:pk>/edit/', recipe_edit, name='recipe_edit'),
    path('<int:pk>/delete/', recipe_delete, name='recipe_delete'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
