from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db import IntegrityError
from .models import Sitio_Desembarco, Familia, Especie, Caladero, Registrador, Embarcacion, Capitan, Desembarco, Categoria, Estado, Desembarco_Capturas, Costo
from .forms import FormSitio, FormEspecie, FormFamilia, FormCaladero, FormEmbarcacion, FormCapitan, FormRegistrador, FormCategoria, FormEstado, CapturaFormSet, DesembarcoForm, FormCosto, CostoFormSet
from django.views.generic.edit import (CreateView, UpdateView)
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .filters import DesembarcoFiltro, EspecieFiltro, SitioFiltro, FamiliaFiltro, CategoriaFiltro, EstadoFiltro, CaladeroFiltro, EmbarcacionFiltro, CostoFiltro, CapitanFiltro, RegistradorFiltro

def acceso(request):

    if request.user.is_authenticated:
        return redirect('menu_principal')

    if request.method == 'GET':
        return render(request, 'acceso_new.html', {'form': AuthenticationForm})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'acceso_new.html', {
                'form': AuthenticationForm,
                'error': 'Usuario o Contraseña incorrectos'
            })
        else:
            login(request, user)
            return redirect('menu_principal') 
        
def cerrar_sesion(request):

    logout(request)
    return redirect('acceso')        

def registrar_usuario(request):

    if request.method == 'GET':
        return render(request, 'registrar.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                username=request.POST['username'], password=request.POST['password1'], first_name=request.POST['first_name'], last_name = request.POST['last_name'], email=request.POST['email'])
                user.save()
                login(request, user)
                return render(request, 'menu_principal.html')
            except IntegrityError:
                return render(request, 'registrar.html', {
                    'form': UserCreationForm,
                    'error': 'Usuario ya existe!'
                })
        return render(request, 'registrar.html', {
            'form': UserCreationForm,
            'error': 'Contraseña no coinciden!'
        })


def menu_principal(request):

    return render(request, 'menu_principal.html')


def listar_sitio(request):

    context = {}

    filtered_sitios = SitioFiltro(request.GET, queryset=Sitio_Desembarco.objects.all())

    context['filtered_sitios'] = filtered_sitios
    
    paginated_filtered_sitios = Paginator(filtered_sitios.qs,15)
    page_number = request.GET.get('page')
    sitio_page_obj = paginated_filtered_sitios.get_page(page_number)

    context['sitio_page_obj'] = sitio_page_obj
    
    return render(request, 'sitios_lista.html', context=context)


def editar_sitio(request, id):

    if request.method == 'GET':
        sitio = get_object_or_404(Sitio_Desembarco, pk=id)
        form = FormSitio(instance=sitio)
        return render(request, 'sitios_editar.html',{
            'sitio': sitio,
            'form': form    
        })
    else:
        try:
            sitio = get_object_or_404(Sitio_Desembarco, pk=id)
            form = FormSitio(request.POST, instance=sitio)
            form.save()
            return redirect('listar_sitios')
        except ValueError:
            return render(request, 'sitios_editar.html', {
                'sitio': sitio,
                'form': form,
                'error': "Error al editar"
            })

def crear_sitio(request):

    if request.method == 'GET':
        return render(request, 'sitios_crear.html', {
            'form': FormSitio
        })
    else:
        try:
            form = FormSitio(request.POST)
            nuevo_sitio = form.save(commit=False)
            nuevo_sitio.save()
            return redirect('listar_sitios')
        except:
            return render(request, 'sitios_crear.html', {
                'form': FormSitio,
                'error': 'Sitio de Desembarco ya existe!'
            })

def eliminar_sitio(request, id):

    sitio = get_object_or_404(Sitio_Desembarco, pk=id)
    sitio.delete()
    return redirect('listar_sitios')


def listar_especie(request):
    
    context = {}

    filtered_especies = EspecieFiltro(request.GET, queryset=Especie.objects.all())

    context['filtered_especies'] = filtered_especies
    
    paginated_filtered_especies = Paginator(filtered_especies.qs,13)
    page_number = request.GET.get('page')
    especie_page_obj = paginated_filtered_especies.get_page(page_number)

    context['especie_page_obj'] = especie_page_obj
    
    return render(request, 'especies_lista.html', context=context)
 

def editar_especie(request, id):
    if request.method == 'GET':
        especie = get_object_or_404(Especie, pk=id)
        form = FormEspecie(request.POST or None, request.FILES or None, instance=especie)
        return render(request, 'especies_editar.html',{
            'especie': especie,
            'form': form    
        })
    else:
        try:
            especie = get_object_or_404(Especie, pk=id)
            form = FormEspecie(request.POST or None, request.FILES or None, instance=especie)
            form.save()
            return redirect('listar_especies')
        except ValueError:
            return render(request, 'especies_editar.html', {
                'especie': especie,
                'form': form,
                'error': "Error al editar"
            })

def crear_especie(request):
    if request.method == 'GET':
        return render(request, 'especies_crear.html', {
            'form': FormEspecie
        })
    else:
        try:
            form = FormEspecie(request.POST or None, request.FILES or None)
            nuevo_especie = form.save(commit=False)
            nuevo_especie.save()
            return redirect('listar_especies')
        except Exception as e: 
            return render(request, 'especies_crear.html', {
                'form': FormEspecie,
                'error': 'Datos inválidos!'
            })

def eliminar_especie(request, id):
    especie = get_object_or_404(Especie, pk=id)
    especie.delete()
    return redirect('listar_especies')


def listar_familia(request):

    context = {}

    filtered_familias = FamiliaFiltro(request.GET, queryset=Familia.objects.all())

    context['filtered_familias'] = filtered_familias
    
    paginated_filtered_familias = Paginator(filtered_familias.qs,13)
    page_number = request.GET.get('page')
    familia_page_obj = paginated_filtered_familias.get_page(page_number)

    context['familia_page_obj'] = familia_page_obj
    
    return render(request, 'familias_lista.html', context=context)


def editar_familia(request, id):
    if request.method == 'GET':
        familia = get_object_or_404(Familia, pk=id)
        form = FormFamilia(instance=familia)
        return render(request, 'familias_editar.html',{
            'familia': familia,
            'form': form    
        })
    else:
        try:
            familia = get_object_or_404(Familia, pk=id)
            form = FormFamilia(request.POST, instance=familia)
            form.save()
            return redirect('listar_familias')
        except ValueError:
            return render(request, 'familias_editar.html', {
                'familia': familia,
                'form': form,
                'error': "Error al editar"
            })

def crear_familia(request):
    if request.method == 'GET':
        return render(request, 'familias_crear.html', {
            'form': FormFamilia
        })
    else:
        try:
            form = FormFamilia(request.POST)
            nuevo_familia = form.save(commit=False)
            nuevo_familia.save()
            return redirect('listar_familias')
        except:
            return render(request, 'familias_crear.html', {
                'form': FormFamilia,
                'error': 'Familia ya existe!'
            })

def eliminar_familia(request, id):
    familia = get_object_or_404(Familia, pk=id)
    familia.delete()
    return redirect('listar_familias')


def listar_categoria(request):
 
    context = {}

    filtered_categorias = CategoriaFiltro(request.GET, queryset=Categoria.objects.all())

    context['filtered_categorias'] = filtered_categorias
    
    paginated_filtered_categorias = Paginator(filtered_categorias.qs,13)
    page_number = request.GET.get('page')
    categoria_page_obj = paginated_filtered_categorias.get_page(page_number)

    context['categoria_page_obj'] = categoria_page_obj
    
    return render(request, 'categorias_lista.html', context=context)


def editar_categoria(request, id):
    if request.method == 'GET':
        categoria = get_object_or_404(Categoria, pk=id)
        form = FormCategoria(instance=categoria)
        return render(request, 'categorias_editar.html',{
            'categoria': categoria,
            'form': form    
        })
    else:
        try:
            categoria = get_object_or_404(Categoria, pk=id)
            form = FormCategoria(request.POST, instance=categoria)
            form.save()
            return redirect('listar_categorias')
        except ValueError:
            return render(request, 'categorias_editar.html', {
                'categoria': categoria,
                'form': form,
                'error': "Error al editar"
            })

def crear_categoria(request):
    if request.method == 'GET':
        return render(request, 'categorias_crear.html', {
            'form': FormCategoria
        })
    else:
        try:
            form = FormCategoria(request.POST)
            nuevo_categoria = form.save(commit=False)
            nuevo_categoria.save()
            return redirect('listar_categorias')
        except:
            return render(request, 'categorias_crear.html', {
                'form': FormCategoria,
                'error': 'Categoría Comercial ya existe!'
            })


def eliminar_categoria(request, id):
    categoria = get_object_or_404(Categoria, pk=id)
    categoria.delete()
    return redirect('listar_categorias')


def listar_estado(request):

    context = {}

    filtered_estados = EstadoFiltro(request.GET, queryset=Estado.objects.all())

    context['filtered_estados'] = filtered_estados
    
    paginated_filtered_estados = Paginator(filtered_estados.qs,13)
    page_number = request.GET.get('page')
    estado_page_obj = paginated_filtered_estados.get_page(page_number)

    context['estado_page_obj'] = estado_page_obj
    
    return render(request, 'estados_lista.html', context=context)


def editar_estado(request, id):
    if request.method == 'GET':
        estado = get_object_or_404(Estado, pk=id)
        form = FormEstado(instance=estado)
        return render(request, 'estados_editar.html',{
            'estado': estado,
            'form': form    
        })
    else:
        try:
            estado = get_object_or_404(Estado, pk=id)
            form = FormEstado(request.POST, instance=estado)
            form.save()
            return redirect('listar_estados')
        except ValueError:
            return render(request, 'estados_editar.html', {
                'estado': estado,
                'form': form,
                'error': "Error al editar"
            })

def crear_estado(request):
    if request.method == 'GET':
        return render(request, 'estados_crear.html', {
            'form': FormEstado
        })
    else:
        try:
            form = FormEstado(request.POST)
            nuevo_estado = form.save(commit=False)
            nuevo_estado.save()
            return redirect('listar_estados')
        except:
            return render(request, 'estados_crear.html', {
                'form': FormEstado,
                'error': 'Estado ya existe!'
            })

def eliminar_estado(request, id):
    estado = get_object_or_404(Estado, pk=id)
    estado.delete()
    return redirect('listar_estados')

def listar_caladero(request):
    
    context = {}

    filtered_caladeros = CaladeroFiltro(request.GET, queryset=Caladero.objects.all())

    context['filtered_caladeros'] = filtered_caladeros
    
    paginated_filtered_caladeros = Paginator(filtered_caladeros.qs,13)
    page_number = request.GET.get('page')
    caladero_page_obj = paginated_filtered_caladeros.get_page(page_number)

    context['caladero_page_obj'] = caladero_page_obj
    
    return render(request, 'caladeros_lista.html', context=context)


def crear_caladero(request):
    if request.method == 'GET':
        return render(request, 'caladeros_crear.html', {
            'form': FormCaladero
        })
    else:
        try:
            form = FormCaladero(request.POST)
            nuevo_caladero = form.save(commit=False)
            nuevo_caladero.save()
            return redirect('listar_caladeros')
        except:
            return render(request, 'caladeros_crear.html', {
                'form': FormCaladero,
                'error': 'Caladero de Pesca ya existe!'
            })

def editar_caladero(request, id):
    if request.method == 'GET':
        caladero = get_object_or_404(Caladero, pk=id)
        form = FormCaladero(instance=caladero)
        return render(request, 'caladeros_editar.html',{
            'caladero': caladero,
            'form': form    
        })
    else:
        try:
            caladero = get_object_or_404(Caladero, pk=id)
            form = FormCaladero(request.POST, instance=caladero)
            form.save()
            return redirect('listar_caladeros')
        except ValueError:
            return render(request, 'caladeros_editar.html', {
                'caladero': caladero,
                'form': form,
                'error': "Error al editar"
            })

def eliminar_caladero(request, id):
    caladero = get_object_or_404(Caladero, pk=id)
    caladero.delete()
    return redirect('listar_caladeros')


def listar_embarcacion(request):

    context = {}

    filtered_embarcaciones = EmbarcacionFiltro(request.GET, queryset=Embarcacion.objects.all())

    context['filtered_embarcaciones'] = filtered_embarcaciones
    
    paginated_filtered_embarcaciones = Paginator(filtered_embarcaciones.qs,13)
    page_number = request.GET.get('page')
    embarcacion_page_obj = paginated_filtered_embarcaciones.get_page(page_number)

    context['embarcacion_page_obj'] = embarcacion_page_obj
    
    return render(request, 'embarcaciones_lista.html', context=context)


def editar_embarcacion(request, id):
    if request.method == 'GET':
        embarcacion = get_object_or_404(Embarcacion, pk=id)
        form = FormEmbarcacion(instance=embarcacion)
        return render(request, 'embarcaciones_editar.html',{
            'embarcacion': embarcacion,
            'form': form    
        })
    else:
        try:
            embarcacion = get_object_or_404(Embarcacion, pk=id)
            form = FormEmbarcacion(request.POST, instance=embarcacion)
            form.save()
            return redirect('listar_embarcaciones')
        except ValueError:
            return render(request, 'embarcaciones_editar.html', {
                'embarcacion': embarcacion,
                'form': form,
                'error': "Error al editar"
            })

def crear_embarcacion(request):
    if request.method == 'GET':
        return render(request, 'embarcaciones_crear.html', {
            'form': FormEmbarcacion
        })
    else:
        try:
            form = FormEmbarcacion(request.POST)
            nuevo_embarcacion = form.save(commit=False)
            nuevo_embarcacion.save()
            return redirect('listar_embarcaciones')
        except:
            return render(request, 'embarcaciones_crear.html', {
                'form': FormEmbarcacion,
                'error': 'Embarcación ya existe!'
            })

def eliminar_embarcacion(request, id):
    embarcacion = get_object_or_404(Embarcacion, pk=id)
    embarcacion.delete()
    return redirect('listar_embarcaciones')


def listar_costo(request):
    
    context = {}

    filtered_costos = CostoFiltro(request.GET, queryset=Costo.objects.all())

    context['filtered_costos'] = filtered_costos
    
    paginated_filtered_costos = Paginator(filtered_costos.qs,13)
    page_number = request.GET.get('page')
    costo_page_obj = paginated_filtered_costos.get_page(page_number)

    context['costo_page_obj'] = costo_page_obj
    
    return render(request, 'costos_lista.html', context=context)


def editar_costo(request, id):
    if request.method == 'GET':
        costo = get_object_or_404(Costo, pk=id)
        form = FormCosto(instance=costo)
        return render(request, 'costos_editar.html',{
            'costo': costo,
            'form': form    
        })
    else:
        try:
            costo = get_object_or_404(Costo, pk=id)
            form = FormCosto(request.POST, instance=costo)
            form.save()
            return redirect('listar_costos')
        except ValueError:
            return render(request, 'costos_editar.html', {
                'costo': costo,
                'form': form,
                'error': "Error al editar"
            })

def crear_costo(request):
    if request.method == 'GET':
        return render(request, 'costos_crear.html', {
            'form': FormCosto
        })
    else:
        try:
            form = FormCosto(request.POST)
            nuevo_costo = form.save(commit=False)
            nuevo_costo.save()
            return redirect('listar_costos')
        except:
            return render(request, 'costos_crear.html', {
                'form': FormCosto,
                'error': 'Costo ya existe!'
            })

def eliminar_costo(request, id):
    costo = get_object_or_404(Costo, pk=id)
    costo.delete()
    return redirect('listar_costos')


def listar_capitan(request):
    
    context = {}

    filtered_capitanes = CapitanFiltro(request.GET, queryset=Capitan.objects.all())

    context['filtered_capitanes'] = filtered_capitanes
    
    paginated_filtered_capitanes = Paginator(filtered_capitanes.qs,13)
    page_number = request.GET.get('page')
    capitan_page_obj = paginated_filtered_capitanes.get_page(page_number)

    context['capitan_page_obj'] = capitan_page_obj
    
    return render(request, 'capitanes_lista.html', context=context)


def editar_capitan(request, id):
    if request.method == 'GET':
        capitan = get_object_or_404(Capitan, pk=id)
        form = FormCapitan(instance=capitan)
        return render(request, 'capitanes_editar.html',{
            'capitan': capitan,
            'form': form    
        })
    else:
        try:
            capitan = get_object_or_404(Capitan, pk=id)
            form = FormCapitan(request.POST, instance=capitan)
            form.save()
            return redirect('listar_capitanes')
        except ValueError:
            return render(request, 'capitanes_editar.html', {
                'capitan': capitan,
                'form': form,
                'error': "Error al editar"
            })

def crear_capitan(request):
    if request.method == 'GET':
        return render(request, 'capitanes_crear.html', {
            'form': FormCapitan
        })
    else:
        try:
            form = FormCapitan(request.POST)
            nuevo_capitan = form.save(commit=False)
            nuevo_capitan.save()
            return redirect('listar_capitanes')
        except:
            return render(request, 'capitanes_crear.html', {
                'form': FormCapitan,
                'error': 'Capitán ya existe!'
            })

def eliminar_capitan(request, id):
    capitan = get_object_or_404(Capitan, pk=id)
    capitan.delete()
    return redirect('listar_capitanes')


def listar_registrador(request):
    
    context = {}

    filtered_registradores = RegistradorFiltro(request.GET, queryset=Registrador.objects.all())

    context['filtered_registradores'] = filtered_registradores
    
    paginated_filtered_registradores = Paginator(filtered_registradores.qs,13)
    page_number = request.GET.get('page')
    registrador_page_obj = paginated_filtered_registradores.get_page(page_number)

    context['registrador_page_obj'] = registrador_page_obj
    
    return render(request, 'registradores_lista.html', context=context)


def editar_registrador(request, id):
    if request.method == 'GET':
        registrador = get_object_or_404(Registrador, pk=id)
        form = FormRegistrador(instance=registrador)
        return render(request, 'registradores_editar.html',{
            'registrador': registrador,
            'form': form    
        })
    else:
        try:
            registrador = get_object_or_404(Registrador, pk=id)
            form = FormRegistrador(request.POST, instance=registrador)
            form.save()
            return redirect('listar_registradores')
        except ValueError:
            return render(request, 'registradores_editar.html', {
                'registrador': registrador,
                'form': form,
                'error': "Error al editar"
            })

def crear_registrador(request):
    if request.method == 'GET':
        return render(request, 'registradores_crear.html', {
            'form': FormRegistrador
        })
    else:
        try:
            form = FormRegistrador(request.POST)
            nuevo_registrador = form.save(commit=False)
            nuevo_registrador.save()
            return redirect('listar_registradores')
        except:
            return render(request, 'registradores_crear.html', {
                'form': FormRegistrador,
                'error': 'Registrador ya existe!'
            })

def eliminar_registrador(request, id):
    registrador = get_object_or_404(Registrador, pk=id)
    registrador.delete()
    return redirect('listar_registradores')


def listar_desembarco(request):

    context = {}

    filtered_desembarcos = DesembarcoFiltro(request.GET, queryset=Desembarco.objects.all())

    context['filtered_desembarcos'] = filtered_desembarcos
    
    paginated_filtered_desembarcos = Paginator(filtered_desembarcos.qs,13)
    page_number = request.GET.get('page')
    desembarco_page_obj = paginated_filtered_desembarcos.get_page(page_number)

    context['desembarco_page_obj'] = desembarco_page_obj
    
    return render(request, 'desembarcos_lista.html', context=context)


class DesembarcoRegistro():
    form_class = DesembarcoForm
    model = Desembarco
    template_name = "desembarcos_detalle.html"

    def form_valid(self, form):
        named_formsets = self.get_named_formsets()
        if not all((x.is_valid() for x in named_formsets.values())):
            return self.render_to_response(self.get_context_data(form=form))

        self.object = form.save()
        for name, formset in named_formsets.items():
            formset_save_func = getattr(self, 'formset_{0}_valid'.format(name), None)
            if formset_save_func is not None:
                formset_save_func(formset)
            else:
                formset.save()
        return redirect('listar_desembarcos')

    def formset_capturas_valid(self, formset):
 
        capturas = formset.save(commit=False)  
        for obj in formset.deleted_objects:
            obj.delete()
        for captura in capturas:
            captura.desembarco = self.object
            captura.save()

    def formset_costos_valid(self, formset):
 
        costos = formset.save(commit=False)  
        for obj in formset.deleted_objects:
            obj.delete()
        for costo in costos:
            costo.desembarco = self.object
            costo.save()

class DesembarcoCrear(DesembarcoRegistro, CreateView):

    def get_context_data(self, **kwargs):
        ctx = super(DesembarcoCrear, self).get_context_data(**kwargs)
        ctx['named_formsets'] = self.get_named_formsets()
        return ctx

    def get_named_formsets(self):
        if self.request.method == "GET":
            return {
                'capturas': CapturaFormSet(prefix='capturas'),
                'costos': CostoFormSet(prefix='costos')
            }
        else:
            return {
                'capturas': CapturaFormSet(self.request.POST or None, self.request.FILES or None, prefix='capturas'),
                'costos': CostoFormSet(self.request.POST or None, self.request.FILES or None, prefix='costos')
            }  
  

class DesembarcoActualizar(DesembarcoRegistro, UpdateView):

    def get_context_data(self, **kwargs):
        ctx = super(DesembarcoActualizar, self).get_context_data(**kwargs)
        ctx['named_formsets'] = self.get_named_formsets()
        return ctx

    def get_named_formsets(self):
        return {
            'capturas': CapturaFormSet(self.request.POST or None, self.request.FILES or None, instance=self.object, prefix='capturas'),
            'costos': CostoFormSet(self.request.POST or None, self.request.FILES or None, instance=self.object, prefix='costos'),
        }


def delete_captura(request, pk):
    try:
        captura = Desembarco_Capturas.objects.get(id=pk)
    except Desembarco_Capturas.DoesNotExist:
        messages.success(
            request, 'Desembarco no existe'
            )
        return redirect('actualizar_desembarco', pk=captura.desembarco.id)

    captura.delete()
    messages.success(request, 'El item fue quitado')
    return redirect('actualizar_desembarco', pk=captura.desembarco.id)

def delete_costo(request, pk):
    try:
        costo = Desembarco_Capturas.objects.get(id=pk)
    except Desembarco_Capturas.DoesNotExist:
        messages.success(
            request, 'Desembarco no existe'
            )
        return redirect('actualizar_desembarco', pk=costo.desembarco.id)

    costo.delete()
    messages.success(request, 'El item fue quitado')
    return redirect('actualizar_desembarco', pk=costo.desembarco.id)
