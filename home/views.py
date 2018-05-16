# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse_lazy,reverse
from django.shortcuts import render,redirect
from django.views.generic import FormView
from django.db import transaction
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from .models import (ExpedienteMedico,AntecedentesQuirurgicos,MedicamentosPrescritos,Complementos,
    AlergiasMedicamentos,AntecedentesPersonalesCancer,AntecedentesPersonalesOtros,
    AlergiasMedicamentosLatex,AlergiasMedicamentosTela,DrogadiccionOtras,PadreCancer,MadreCancer,
    HermanosCancer,PadreOtros,MadreOtros,HermanosOtros,HermanosCausaMuerte,InmunizacionesOtras,
    HojaEvolucion,Usuario,HojaTratamiento
    )
from .forms import (AntecedentesQuirurgicosFormSet,MedicamentosPrescritosFormSet,ComplementosFormSet,
    AlergiasMedicamentosFormSet,AntecedentesPersonalesCancerFormSet,
    AntecedentesPersonalesOtrosFormSet,AlergiasMedicamentosLatexFormSet,
    AlergiasMedicamentosTelaFormSet,DrogadiccionOtrasFormSet,PadreCancerFormSet,
    PadreOtrosFormSet,MadreCancerFormSet,MadreOtrosFormSet,HermanosCancerFormSet,
    HermanosOtrosFormSet,HermanosCausaMuerteFormSet,InmunizacionesOtrasFormSet,
    HojaEvolucionFormSet,Users_Form,HojaTratamientoFormSet
    )
from easy_pdf.views import PDFTemplateView
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User,Group
from django.contrib.auth import authenticate, login, logout
from django.contrib.messages.views import SuccessMessageMixin
import json
from django.http import HttpResponse
# Create your views here.
# def Inicio(request):
# 	return render(request,'home/inicio.html')


def idx_auto_complete(request):
    if request.is_ajax:
        text=request.GET.get('term','')

        # Como se esta haciendo el queryset de todos los registros
        # en la lista le saldran repetidos [solo se mostraran 5 opciones en la lista
        # si es que existen registros]
        query=ExpedienteMedico.objects.filter(idx__icontains=text)[:5]
        #query=ExpedienteMedico.objects.values_list('idx', flat=True).distinct()
        results=[]

        for e in query:
            e_json={}
            e_json['label']=e.idx
            e_json['value']=e.idx
            results.append(e_json)

        data_json=json.dumps(results)

    else:
        data_json='fail'
    mimetype="application/json"
    return HttpResponse(data_json,mimetype)


def login_view(request):
    mensaje = ""
    if request.user.is_authenticated():
        return redirect(reverse('Busqueda_de_Pacientes'))
    if request.method == 'POST':
        username = request.POST.get('u')
        password = request.POST.get('p')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect(reverse('Busqueda_de_Pacientes'))
            else:
                pass
        mensaje = 'Nombre de usuario o contraseña no valido'
    return render(request, 'home/Login.html', {'mensaje': mensaje})


def logout_view(request):
    logout(request)
    return redirect(reverse('login'))

# no FK
class RegistrarExpedienteMedico(CreateView):
    model = ExpedienteMedico
    fields= '__all__'

# tiene FK
class RegistrarExpedienteMedicoCompleto(CreateView):
    model = ExpedienteMedico
    fields= '__all__'
    success_url = reverse_lazy('Busqueda_de_Pacientes')
    def get_context_data(self, **kwargs):
        data = super(RegistrarExpedienteMedicoCompleto, self).get_context_data(**kwargs)
        if self.request.POST:
            data['antecedentesquirurgicos'] = AntecedentesQuirurgicosFormSet(self.request.POST)
            data['medicamentosprescritos'] = MedicamentosPrescritosFormSet(self.request.POST)
            data['complementos'] = ComplementosFormSet(self.request.POST)
            data['alergiasmedicamentos'] = AlergiasMedicamentosFormSet(self.request.POST)
            data['antecedentespersonalescancer'] = AntecedentesPersonalesCancerFormSet(self.request.POST)
            data['antecedentespersonalesotros'] = AntecedentesPersonalesOtrosFormSet(self.request.POST)
            data['alergiasmedicamentoslatex'] = AlergiasMedicamentosLatexFormSet(self.request.POST)
            data['alergiasmedicamentostela'] = AlergiasMedicamentosTelaFormSet(self.request.POST)
            data['drogadiccionotras'] = DrogadiccionOtrasFormSet(self.request.POST)
            data['padrecancer'] = PadreCancerFormSet(self.request.POST)
            data['padreotros'] = PadreOtrosFormSet(self.request.POST)
            data['madrecancer'] = MadreCancerFormSet(self.request.POST)
            data['madreotros'] = MadreOtrosFormSet(self.request.POST)
            data['hermanoscancer'] = HermanosCancerFormSet(self.request.POST)
            data['hermanosotros'] = HermanosOtrosFormSet(self.request.POST)
            data['hermanoscausamuerte'] = HermanosCausaMuerteFormSet(self.request.POST)
            data['inmunizacionesotras'] = InmunizacionesOtrasFormSet(self.request.POST)
        else:
            data['antecedentesquirurgicos'] = AntecedentesQuirurgicosFormSet()
            data['medicamentosprescritos'] = MedicamentosPrescritosFormSet()
            data['complementos'] = ComplementosFormSet()
            data['alergiasmedicamentos'] = AlergiasMedicamentosFormSet()
            data['antecedentespersonalescancer'] = AntecedentesPersonalesCancerFormSet()
            data['antecedentespersonalesotros'] = AntecedentesPersonalesOtrosFormSet()
            data['alergiasmedicamentoslatex'] = AlergiasMedicamentosLatexFormSet()
            data['alergiasmedicamentostela'] = AlergiasMedicamentosTelaFormSet()
            data['drogadiccionotras'] = DrogadiccionOtrasFormSet()
            data['padrecancer'] = PadreCancerFormSet()
            data['padreotros'] = PadreOtrosFormSet()
            data['madrecancer'] = MadreCancerFormSet()
            data['madreotros'] = MadreOtrosFormSet()
            data['hermanoscancer'] = HermanosCancerFormSet()
            data['hermanosotros'] = HermanosOtrosFormSet()
            data['hermanoscausamuerte'] = HermanosCausaMuerteFormSet()
            data['inmunizacionesotras'] = InmunizacionesOtrasFormSet()
        return data
    def form_valid(self, form):
        context = self.get_context_data()
        antecedentesquirurgicos = context['antecedentesquirurgicos']
        medicamentosprescritos = context['medicamentosprescritos']
        complementos = context['complementos']
        alergiasmedicamentos = context['alergiasmedicamentos']
        antecedentespersonalescancer = context['antecedentespersonalescancer']
        antecedentespersonalesotros = context['antecedentespersonalesotros']
        alergiasmedicamentoslatex = context['alergiasmedicamentoslatex']
        alergiasmedicamentostela = context['alergiasmedicamentostela']
        drogadiccionotras = context['drogadiccionotras']
        padrecancer = context['padrecancer']
        padreotros = context['padreotros']
        madrecancer = context['madrecancer']
        madreotros = context['madreotros']
        hermanoscancer = context['hermanoscancer']
        hermanosotros = context['hermanosotros']
        hermanoscausamuerte = context['hermanoscausamuerte']
        inmunizacionesotras = context['inmunizacionesotras']
        with transaction.atomic():
            self.object = form.save()
            if (antecedentesquirurgicos.is_valid() and medicamentosprescritos.is_valid() and
                complementos.is_valid() and alergiasmedicamentos.is_valid() and
                antecedentespersonalescancer.is_valid() and antecedentespersonalesotros.is_valid() and
                alergiasmedicamentoslatex.is_valid() and alergiasmedicamentostela.is_valid() and
                drogadiccionotras.is_valid() and padrecancer.is_valid() and padreotros.is_valid() and
                madrecancer.is_valid() and madreotros.is_valid() and hermanoscancer.is_valid() and
                hermanosotros.is_valid() and hermanoscausamuerte.is_valid() and
                inmunizacionesotras.is_valid()):

                antecedentesquirurgicos.instance = self.object
                medicamentosprescritos.instance = self.object
                complementos.instance = self.object
                alergiasmedicamentos.instance = self.object
                antecedentespersonalescancer.instance = self.object
                antecedentespersonalesotros.instance = self.object
                alergiasmedicamentoslatex.instance = self.object
                alergiasmedicamentostela.instance = self.object
                drogadiccionotras.instance = self.object
                padrecancer.instance = self.object
                padreotros.instance = self.object
                madrecancer.instance = self.object
                madreotros.instance = self.object
                hermanoscancer.instance = self.object
                hermanosotros.instance = self.object
                hermanoscausamuerte.instance = self.object
                inmunizacionesotras.instance = self.object

                antecedentesquirurgicos.save()
                medicamentosprescritos.save()
                complementos.save()
                alergiasmedicamentos.save()
                antecedentespersonalescancer.save()
                antecedentespersonalesotros.save()
                alergiasmedicamentoslatex.save()
                alergiasmedicamentostela.save()
                drogadiccionotras.save()
                drogadiccionotras.save()
                padrecancer.save()
                padreotros.save()
                madrecancer.save()
                madreotros.save()
                hermanoscancer.save()
                hermanosotros.save()
                hermanoscausamuerte.save()
                inmunizacionesotras.save()
        return super(RegistrarExpedienteMedicoCompleto, self).form_valid(form)


class ModificarExpedienteMedico(UpdateView):
    model = ExpedienteMedico
    success_url = '/'
    fields= '__all__'


class ModificarExpedienteMedicoCompleto(UpdateView):
    model = ExpedienteMedico
    fields= '__all__'
    template_name = "home/Modificar_Expediente_Medico.html"
    success_url = reverse_lazy('Busqueda_de_Pacientes')
    def get_context_data(self, **kwargs):
        data = super(ModificarExpedienteMedicoCompleto, self).get_context_data(**kwargs)
        if self.request.POST:
            data["expedientemedico"] = ExpedienteMedico.objects.get(pk=self.kwargs.get('pk'))
            data['antecedentesquirurgicos'] = AntecedentesQuirurgicosFormSet(self.request.POST, instance=self.object)
            data['medicamentosprescritos'] = MedicamentosPrescritosFormSet(self.request.POST, instance=self.object)
            data['complementos'] = ComplementosFormSet(self.request.POST, instance=self.object)
            data['alergiasmedicamentos'] = AlergiasMedicamentosFormSet(self.request.POST, instance=self.object)
            data['antecedentespersonalescancer'] = AntecedentesPersonalesCancerFormSet(self.request.POST, instance=self.object)
            data['antecedentespersonalesotros'] = AntecedentesPersonalesOtrosFormSet(self.request.POST, instance=self.object)
            data['alergiasmedicamentoslatex'] = AlergiasMedicamentosLatexFormSet(self.request.POST, instance=self.object)
            data['alergiasmedicamentostela'] = AlergiasMedicamentosTelaFormSet(self.request.POST, instance=self.object)
            data['drogadiccionotras'] = DrogadiccionOtrasFormSet(self.request.POST, instance=self.object)
            data['padrecancer'] = PadreCancerFormSet(self.request.POST, instance=self.object)
            data['padreotros'] = PadreOtrosFormSet(self.request.POST, instance=self.object)
            data['madrecancer'] = MadreCancerFormSet(self.request.POST, instance=self.object)
            data['madreotros'] = MadreOtrosFormSet(self.request.POST, instance=self.object)
            data['hermanoscancer'] = HermanosCancerFormSet(self.request.POST, instance=self.object)
            data['hermanosotros'] = HermanosOtrosFormSet(self.request.POST, instance=self.object)
            data['hermanoscausamuerte'] = HermanosCausaMuerteFormSet(self.request.POST, instance=self.object)
            data['inmunizacionesotras'] = InmunizacionesOtrasFormSet(self.request.POST, instance=self.object)
        else:
            data["expedientemedico"] = ExpedienteMedico.objects.get(pk=self.kwargs.get('pk'))
            data['antecedentesquirurgicos'] = AntecedentesQuirurgicosFormSet(instance=self.object)
            data['medicamentosprescritos'] = MedicamentosPrescritosFormSet(instance=self.object)
            data['complementos'] = ComplementosFormSet(instance=self.object)
            data['alergiasmedicamentos'] = AlergiasMedicamentosFormSet(instance=self.object)
            data['antecedentespersonalescancer'] = AntecedentesPersonalesCancerFormSet(instance=self.object)
            data['antecedentespersonalesotros'] = AntecedentesPersonalesOtrosFormSet(instance=self.object)
            data['alergiasmedicamentoslatex'] = AlergiasMedicamentosLatexFormSet(instance=self.object)
            data['alergiasmedicamentostela'] = AlergiasMedicamentosTelaFormSet(instance=self.object)
            data['drogadiccionotras'] = DrogadiccionOtrasFormSet(instance=self.object)
            data['padrecancer'] = PadreCancerFormSet(instance=self.object)
            data['padreotros'] = PadreOtrosFormSet(instance=self.object)
            data['madrecancer'] = MadreCancerFormSet(instance=self.object)
            data['madreotros'] = MadreOtrosFormSet(instance=self.object)
            data['hermanoscancer'] = HermanosCancerFormSet(instance=self.object)
            data['hermanosotros'] = HermanosOtrosFormSet(instance=self.object)
            data['hermanoscausamuerte'] = HermanosCausaMuerteFormSet(instance=self.object)
            data['inmunizacionesotras'] = InmunizacionesOtrasFormSet(instance=self.object)
        return data
    def form_valid(self, form):
        context = self.get_context_data()
        antecedentesquirurgicos = context['antecedentesquirurgicos']
        medicamentosprescritos = context['medicamentosprescritos']
        complementos = context['complementos']
        alergiasmedicamentos = context['alergiasmedicamentos']
        antecedentespersonalescancer = context['antecedentespersonalescancer']
        antecedentespersonalesotros = context['antecedentespersonalesotros']
        alergiasmedicamentoslatex = context['alergiasmedicamentoslatex']
        alergiasmedicamentostela = context['alergiasmedicamentostela']
        drogadiccionotras = context['drogadiccionotras']
        padrecancer = context['padrecancer']
        padreotros = context['padreotros']
        madrecancer = context['madrecancer']
        madreotros = context['madreotros']
        hermanoscancer = context['hermanoscancer']
        hermanosotros = context['hermanosotros']
        hermanoscausamuerte = context['hermanoscausamuerte']
        inmunizacionesotras = context['inmunizacionesotras']
        with transaction.atomic():
            self.object = form.save()
            if (antecedentesquirurgicos.is_valid() and medicamentosprescritos.is_valid() and
                complementos.is_valid() and alergiasmedicamentos.is_valid() and
                antecedentespersonalescancer.is_valid() and antecedentespersonalesotros.is_valid() and
                alergiasmedicamentoslatex.is_valid() and alergiasmedicamentostela.is_valid() and
                drogadiccionotras.is_valid() and padrecancer.is_valid() and padreotros.is_valid() and
                madrecancer.is_valid() and madreotros.is_valid() and hermanoscancer.is_valid() and
                hermanosotros.is_valid() and hermanoscausamuerte.is_valid() and
                inmunizacionesotras.is_valid()):

                antecedentesquirurgicos.instance = self.object
                medicamentosprescritos.instance = self.object
                complementos.instance = self.object
                alergiasmedicamentos.instance = self.object
                antecedentespersonalescancer.instance = self.object
                antecedentespersonalesotros.instance = self.object
                alergiasmedicamentoslatex.instance = self.object
                alergiasmedicamentostela.instance = self.object
                drogadiccionotras.instance = self.object
                padrecancer.instance = self.object
                padreotros.instance = self.object
                madrecancer.instance = self.object
                madreotros.instance = self.object
                hermanoscancer.instance = self.object
                hermanosotros.instance = self.object
                hermanoscausamuerte.instance = self.object
                inmunizacionesotras.instance = self.object

                antecedentesquirurgicos.save()
                medicamentosprescritos.save()
                complementos.save()
                alergiasmedicamentos.save()
                antecedentespersonalescancer.save()
                antecedentespersonalesotros.save()
                alergiasmedicamentoslatex.save()
                alergiasmedicamentostela.save()
                drogadiccionotras.save()
                drogadiccionotras.save()
                padrecancer.save()
                padreotros.save()
                madrecancer.save()
                madreotros.save()
                hermanoscancer.save()
                hermanosotros.save()
                hermanoscausamuerte.save()
                inmunizacionesotras.save()
        return super(ModificarExpedienteMedicoCompleto, self).form_valid(form)



class PDF_ExpedienteMedico(PDFTemplateView):
    #template_name = "home/pdf_expediente_medico.html"
    model = ExpedienteMedico
    #download_filename = 'hello.pdf'
    def get_context_data(self,pk, **kwargs):
        context = super(PDF_ExpedienteMedico, self).get_context_data(**kwargs)
        context["expedientemedico"] = ExpedienteMedico.objects.get(id=pk)
        #TOMA EL ID MODELO EXPEDIENTEMEDICO
        context["antecedentesquirurgico"] = AntecedentesQuirurgicos.objects.filter(fk_expedientemedico_id=pk)
        context["medicamentosprescritos"] = MedicamentosPrescritos.objects.filter(fk_expedientemedico_id=pk)
        context["complementos"] = Complementos.objects.filter(fk_expedientemedico_id=pk)
        context["alergiasmedicamentos"] = AlergiasMedicamentos.objects.filter(fk_expedientemedico_id=pk)
        context["antecedentespersonalescancer"] = AntecedentesPersonalesCancer.objects.filter(fk_expedientemedico_id=pk)
        context["antecedentespersonalesotros"] = AntecedentesPersonalesOtros.objects.filter(fk_expedientemedico_id=pk)
        context["alergiasmedicamentoslatex"] = AlergiasMedicamentosLatex.objects.filter(fk_expedientemedico_id=pk)
        context["alergiasmedicamentostela"] = AlergiasMedicamentosTela.objects.filter(fk_expedientemedico_id=pk)
        context["drogadiccionotras"] = DrogadiccionOtras.objects.filter(fk_expedientemedico_id=pk)
        context['padrecancer'] = PadreCancer.objects.filter(fk_expedientemedico_id=pk)
        context['padreotros'] = PadreOtros.objects.filter(fk_expedientemedico_id=pk)
        context['madrecancer'] = MadreCancer.objects.filter(fk_expedientemedico_id=pk)
        context['madreotros'] = MadreOtros.objects.filter(fk_expedientemedico_id=pk)
        context['hermanoscancer'] = HermanosCancer.objects.filter(fk_expedientemedico_id=pk)
        context['hermanosotros'] = HermanosOtros.objects.filter(fk_expedientemedico_id=pk)
        context['hermanoscausamuerte'] = HermanosCausaMuerte.objects.filter(fk_expedientemedico_id=pk)
        context['inmunizacionesotras'] = InmunizacionesOtras.objects.filter(fk_expedientemedico_id=pk)
        return context



def BusquedaPacientes(request):
    username=request.user
    #print username
    #if username.is_superuser:
    if username:
        todos = ExpedienteMedico.objects.all()
        contexto = {
        'pacientes':todos }
        return render(request, 'home/Busqueda_pacientes.html', contexto)
    # else:
    #     filtrados = ExpedienteMedico.objects.filter(usuario=username)
    #     cxt = {
    #     'pacientes':filtrados }
    #     return render(request, 'home/Busqueda_pacientes.html', cxt)





# ======================== HOJA EVOLUCION
class ModificarHojaEvolucion(UpdateView):
    model = ExpedienteMedico
    fields= ['nombre','ap_paterno','ap_materno'] #INDICAR SOLO LOS CAMPOS QUE USARE
    template_name = 'home/Registrar_Hoja_Evolucion.html'
    success_url = reverse_lazy('Busqueda_de_Pacientes')
    def get_context_data(self, **kwargs):
        data = super(ModificarHojaEvolucion, self).get_context_data(**kwargs)
        if self.request.POST:
            data['hojaevolucion'] = HojaEvolucionFormSet(self.request.POST, instance=self.object)
        else:
            data['hojaevolucion'] = HojaEvolucionFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        hojaevolucion = context['hojaevolucion']
        with transaction.atomic():
            self.object = form.save()
            if (hojaevolucion.is_valid()):
                hojaevolucion.instance = self.object
                hojaevolucion.save()
        return super(ModificarHojaEvolucion, self).form_valid(form)


class PDF_HojaEvolucion(PDFTemplateView):
    #template_name = "home/pdf_expediente_medico.html"
    model = ExpedienteMedico
    #download_filename = 'hello.pdf'
    def get_context_data(self,pk, **kwargs):
        context = super(PDF_HojaEvolucion, self).get_context_data(**kwargs)
        context["expedientemedico"] = ExpedienteMedico.objects.get(id=pk)
        #TOMA EL ID MODELO EXPEDIENTEMEDICO
        context['hojaevolucion'] = HojaEvolucion.objects.filter(fk_expedientemedico_id=pk)
        return context


# ================= HOJA DE TRATAMIENTO
class ModificarHojaTratamiento(UpdateView):
    model = ExpedienteMedico
    fields= ['nombre','ap_paterno','ap_materno','idx'] #INDICAR SOLO LOS CAMPOS QUE USARE
    template_name = 'home/Registrar_Hoja_Tratamiento.html'
    success_url = reverse_lazy('Busqueda_de_Pacientes')
    def get_context_data(self, **kwargs):
        data = super(ModificarHojaTratamiento, self).get_context_data(**kwargs)
        if self.request.POST:
            data['hojatratamiento'] = HojaTratamientoFormSet(self.request.POST, instance=self.object)
        else:
            data['hojatratamiento'] = HojaTratamientoFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        hojatratamiento = context['hojatratamiento']
        with transaction.atomic():
            self.object = form.save()
            if (hojatratamiento.is_valid()):
                hojatratamiento.instance = self.object
                hojatratamiento.save()
        return super(ModificarHojaTratamiento, self).form_valid(form)


class PDF_HojaTratamiento(PDFTemplateView):
    #template_name = "home/pdf_expediente_medico.html"
    model = ExpedienteMedico
    #download_filename = 'hello.pdf'
    def get_context_data(self,pk, **kwargs):
        context = super(PDF_HojaTratamiento, self).get_context_data(**kwargs)
        context["expedientemedico"] = ExpedienteMedico.objects.get(id=pk)
        #TOMA EL ID MODELO EXPEDIENTEMEDICO
        context['hojatratamiento'] = HojaTratamiento.objects.filter(fk_expedientemedico_id=pk)
        return context


# =================== USUARIOS
class AddUserView(SuccessMessageMixin,FormView):
    template_name= 'home/agregar_usuario.html'
    form_class = Users_Form
    success_url = reverse_lazy('usuario_list')
    #success_message = "Se ha agregado el usuario con éxito!"
    def form_valid(self, form):
        if self.request.method == 'POST':
            user = form.save()
            print user
            p = Usuario()
            p.name = user

            p.tipo_de_usuario = form.cleaned_data['tipo_de_usuario']
            if p.tipo_de_usuario.tipo_de_usuario == 'Médico':
                group = Group.objects.get(name='medico')
            elif p.tipo_de_usuario.tipo_de_usuario == 'Asistente':
                group = Group.objects.get(name='asistente')
            elif p.tipo_de_usuario.tipo_de_usuario == 'Terapeuta':
                group = Group.objects.get(name='terapeuta')
            elif p.tipo_de_usuario.tipo_de_usuario == 'Administración':
                group = Group.objects.get(name='administracion')
            else:
                pass
            user.groups.add(group)
            p.save()
            return super(AddUserView, self).form_valid(form)


class Usuario_list(ListView):
    template_name="usuario_list.html"
    # 1 = superuser id
    queryset=Usuario.objects.exclude(name=1)

class UsuarioUpdate(UpdateView):
    template_name= 'home/modificar_usuario.html'
    model=User
    form_class = Users_Form
    success_url = reverse_lazy('usuario_list')

    def form_valid(self,form):
        # modelo usuario y modelo user tienen distintos id ..por eso no funciona
        # debe ser mismo id...como creo superuser desde terminal se pierde orden
        # si cree un superuser debo agregarlo a usuarios
        #obj_user = User.objects.get(username=form.cleaned_data['username'])
        #print obj_user
        #print obj_user.pk
        #obj = Usuario.objects.get(pk=self.kwargs.get('pk'))
        #obj.tipo_de_usuario = form.cleaned_data['tipo_de_usuario']
        #obj.save()

        if self.request.method == 'POST':
            user = form.save()
            #print user
            # otra opcion seria tomar nombre y de ahi pk, pero entonces 
            # no permitir editar nombre
            p = Usuario.objects.get(pk=self.kwargs.get('pk')) #con esta opcion se permite editar nombre
            p.name = user

            p.tipo_de_usuario = form.cleaned_data['tipo_de_usuario']
            if p.tipo_de_usuario.tipo_de_usuario == 'Médico':
                group = Group.objects.get(name='medico')
            elif p.tipo_de_usuario.tipo_de_usuario == 'Asistente':
                group = Group.objects.get(name='asistente')
            elif p.tipo_de_usuario.tipo_de_usuario == 'Terapeuta':
                group = Group.objects.get(name='terapeuta')
            elif p.tipo_de_usuario.tipo_de_usuario == 'Administración':
                group = Group.objects.get(name='administracion')
            else:
                pass
            user.groups.clear()
            user.groups.add(group)
            p.save()
        return super(UsuarioUpdate, self).form_valid(form)


class UsuarioDelete(DeleteView):
    template_name= 'home/user_confirm_delete.html'
    model = User
    success_url = reverse_lazy('usuario_list')


class EliminarExpedienteMedico(DeleteView):
    template_name= 'home/user_confirm_delete.html'
    model = ExpedienteMedico
    success_url = reverse_lazy('Busqueda_de_Pacientes')