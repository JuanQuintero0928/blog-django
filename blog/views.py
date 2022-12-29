from django.shortcuts import render
from .models import Post,Categoria
from django.shortcuts import get_object_or_404
from django.db.models import Q

# Create your views here.

def home(request):
    queryset = request.GET.get("buscar") # para guardar lo que se escribe en el boton de buscar
    posts = Post.objects.filter(estado = True)
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |  # para hacer consultas con condicionales "O"
            Q(descripcion__icontains = queryset)
        ).distinct()                # para no traer el mismo campo dentro de una consulta
    return render(request,'index.html',{'posts':posts})

def detallePost(request,slug):
    # post = Post.objects.get(slug=slug)
    post = get_object_or_404(Post,slug = slug) # Se realiza la consulta y a la vez si devuelve un DoesNotExist muestra el template
    print(post.imagen)
    return render(request,"post.html",{'detalle_post':post})

def generales(request):
    posts = Post.objects.filter(
        estado=True,
        categoria = Categoria.objects.get(nombre__iexact='general'))
    return render(request, 'generales.html',{'posts':posts})

def programacion(request):
    queryset = request.GET.get("buscar") # para guardar lo que se escribe en el boton de buscar
    posts = Post.objects.filter(
            estado = True,
            categoria = Categoria.objects.get(nombre__iexact='programacion')
        )   # se hace la primera consulta que se muestra en el template
    if queryset:    # si se utiliza el boton de buscar, pasa por el if, realiza las consultas de Q, y luego valida el estado y categoria
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
            estado = True,
            categoria = Categoria.objects.get(nombre__iexact='programacion')
        )
    return render(request, 'programacion.html',{'posts':posts})

def tutoriales(request):
    posts = Post.objects.filter(
        estado = True,
        categoria = Categoria.objects.get(nombre__iexact = 'Tutoriales')
    )
    return render(request, 'tutoriales.html',{'posts':posts})

def tecnologia(request):
    posts = Post.objects.filter(
        estado = True,
        categoria = Categoria.objects.get(nombre__iexact = 'Tecnologia')
    )
    return render(request, 'tecnologia.html',{'posts':posts})

def videojuegos(request):
    posts = Post.objects.filter(
        estado = True,
        categoria = Categoria.objects.get(nombre__iexact = 'VideoJuegos')
    )
    return render(request, 'videojuegos.html',{'posts':posts})