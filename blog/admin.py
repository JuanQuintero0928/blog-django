from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

# django-import-export 
class CategoriaResource(resources.ModelResource):
    class Meta:
        model = Categoria

class AutorResource(resources.ModelResource):
    class Meta:
        model = Autor

class PostResource(resources.ModelResource):
    class Meta:
        model = Post

#Personalizar la forma en la que se visualiza la informacion en el admin, para que funcione el import-export debe heredar de ImportExportModelAdmin
class CategoriaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ('nombre','estado','fecha_creacion',)
    resource_class = CategoriaResource

class AutorAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['nombres','apellidos','correo']
    list_display = ('nombres','apellidos','correo','estado','fecha_creacion',)
    resource_class = AutorResource

class PostAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['titulo','slug']
    list_display = ('titulo','slug','autor','categoria','estado','fecha_creacion',)
    resource_class = PostResource

admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Autor,AutorAdmin)
admin.site.register(Post,PostAdmin)