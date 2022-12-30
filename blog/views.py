from django.shortcuts import render
from .models import Post,Categoria
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.

def home(request):
    queryset = request.GET.get("buscar") # para guardar lo que se escribe en el boton de buscar
    posts = Post.objects.filter(estado = True)
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |  # para hacer consultas con condicionales "O"
            Q(descripcion__icontains = queryset)
        ).distinct()                # para no traer el mismo campo dentro de una consulta
    paginator = Paginator(posts,2)  # numero de elementos a mostrar por pagina
    page = request.GET.get('page')  # para saber en que pagina se encuentra
    posts = paginator.get_page(page)
    return render(request,'index.html',{'posts':posts})

def detallePost(request,slug):
    # post = Post.objects.get(slug=slug)
    post = get_object_or_404(Post,slug = slug) # Se realiza la consulta y a la vez si devuelve un DoesNotExist muestra el template
    print(post.imagen)
    return render(request,"post.html",{'detalle_post':post})

def generales(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(
        estado = True,
        categoria = Categoria.objects.get(nombre__iexact='general')
    )
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
            estado=True,
            categoria = Categoria.objects.get(nombre__iexact='General')
        ).distinct()
    paginator = Paginator(posts,2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
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
    paginator = Paginator(posts,2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'programacion.html',{'posts':posts})

def tutoriales(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(
        estado = True,
        categoria = Categoria.objects.get(nombre__iexact = 'Tutoriales')
    )
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
            estado = True,
            categoria = Categoria.objects.get(nombre__iexact = 'Tutoriales')
        )
    paginator = Paginator(posts,2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'tutoriales.html',{'posts':posts})

def tecnologia(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(
        estado = True,
        categoria = Categoria.objects.get(nombre__iexact = 'Tecnologia')
    )
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
            estado = True,
            categoria = Categoria.objects.get(nombre__iexact = 'Tecnologia')
        )
    paginator = Paginator(posts,2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'tecnologia.html',{'posts':posts})

def videojuegos(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(
        estado = True,
        categoria = Categoria.objects.get(nombre__iexact = 'VideoJuegos')
    )
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
            estado = True,
            categoria = Categoria.objects.get(nombre__iexact = 'VideoJuegos')
        )
    paginator = Paginator(posts,2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'videojuegos.html',{'posts':posts})