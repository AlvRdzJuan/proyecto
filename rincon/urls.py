"""rincon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from home import views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login, logout_then_login
#from home.views import RegistrarExpedienteMedicoCompleto,ModificarExpedienteMedicoCompleto
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.login_view, name='login1'),
    url(r'^login/$', views.login_view, name='login'),
    #url(r'^inicio/$', login_required(views.Inicio), name='inicio'),
    url(r'^Registrar_Expediente_Medico/$', login_required(views.RegistrarExpedienteMedicoCompleto.as_view()), name='profile-add'),
    url(r'^Modificar_Expediente_Medico/(?P<pk>[0-9]+)/$', login_required(views.ModificarExpedienteMedicoCompleto.as_view()), name='profile-update'),
    url(r"^PDF_Expediente_Medico.pdf/(?P<pk>[-\w]+)/$", login_required(views.PDF_ExpedienteMedico.as_view(template_name='home/pdf_expediente_medico.html'))),
    url(r'^logout/$', login_required(views.logout_view), name='logout'),
    url(r'^Agregar_Usuario_Physiomed/$', login_required(views.AddUserView.as_view()), name='Agregar_Usuario_Physiomed'),
    url(r'^Busqueda_de_Pacientes/$', login_required(views.BusquedaPacientes), name='Busqueda_de_Pacientes'),
    url(r'^Modificar_Hoja_Evolucion/(?P<pk>[0-9]+)/$', login_required(views.ModificarHojaEvolucion.as_view())),
    url(r"^PDF_Hoja_Evolucion.pdf/(?P<pk>[-\w]+)/$", login_required(views.PDF_HojaEvolucion.as_view(template_name='home/pdf_hoja_evolucion.html'))),
    url(r'^Modificar_Hoja_Tratamiento/(?P<pk>[0-9]+)/$', login_required(views.ModificarHojaTratamiento.as_view())),
    url(r"^PDF_Hoja_Tratamiento.pdf/(?P<pk>[-\w]+)/$", login_required(views.PDF_HojaTratamiento.as_view(template_name='home/pdf_hoja_tratamiento.html'))),
    url(r'^idx_auto_complete/$', login_required(views.idx_auto_complete), name='idx_auto_complete'),
    url(r'^usuario/(?P<pk>[0-9]+)/$', login_required(views.UsuarioUpdate.as_view()), name='usuario_update'),
    url(r'^usuario/(?P<pk>[0-9]+)/delete/$', login_required(views.UsuarioDelete.as_view()), name='usuario_delete'),
    url(r'^lista_de_usuarios/$', login_required(views.Usuario_list.as_view()), name='usuario_list'),
    url(r'^Eliminar_Expediente_Medico/(?P<pk>[0-9]+)/$', login_required(views.EliminarExpedienteMedico.as_view()), name='Eliminar_Expediente_Medico'),


    #url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,}),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
