# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from multiselectfield import MultiSelectField
from django.db import models
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.contrib.auth.models import User

Aseguranzas = (
	('Banorte','Banorte'),('Axxa','Axxa'),('Allianz','Allianz'),('GNP','GNP'),
	('La Latino Seguros','La Latino Seguros'),('MAPFRE','MAPFRE'),('Metlife','Metlife'),
	('Seguros Atlas','Seguros Atlas'),('Seguros Monterrey','Seguros Monterrey'),
	('Bupa','Bupa')
	)

ECivil = ( 
	('Soltero(a)','Soltero(a)'),('Casado(a)','Casado(a)'),('Divorciado(a)','Divorciado(a)'),
	('Viudo(a)','Viudo(a)'),('Unión Libre','Unión Libre')
	)

Genero = (
	('Masculino','Masculino'),('Femenino','Femenino')
	)
 
Enfermedades = (
			  ('Ninguna', 'Ninguna'),('Enf. del corazón', 'Enf. del corazón'),('Presión Alta', 'Presión Alta'),
              ('Infarto/Embolia', 'Infarto/Embolia'),('Apnea del Sueño', 'Apnea del Sueño'),
              ('Enf. Coronaria', 'Enf. Coronaria'),('Depresión', 'Depresión'),('Ansiedad', 'Ansiedad'),
              ('Sangrados', 'Sangrados'),('Hepatitis A B o C', 'Hepatitis A B o C'),('HIV', 'HIV'),
              ('Diabetes-Dieta', 'Diabetes-Dieta'),('Diabetes-Meds', 'Diabetes-Meds'),('Diabetes-Insulina', 'Diabetes-Insulina'),
              ('Colesterol Alto', 'Colesterol Alto'),('Convulsiones', 'Convulsiones'),('Desmayos', 'Desmayos'),
              ('Artritis', 'Artritis'),('Asma', 'Asma'),('Enfisema', 'Enfisema'),('Osteoporosis', 'Osteoporosis'),
              ('Alergia:Comida', 'Alergia:Comida'),('Alergia:Estacional', 'Alergia:Estacional'),
              ('Tuberculosis', 'Tuberculosis'),('Hipotiroidismo', 'Hipotiroidismo'),
              ('Hipertiroidismo', 'Hipertiroidismo'),('Cáncer', 'Cáncer'),('Otra', 'Otra'))


# *************************** PRACTICAS SOCIALES
Opciones_tabaquismo = (
	('Nunca','Nunca'),('Abandonó?','Abandonó?'),('# día?','# día?'),('Pipa','Pipa'),('Puros','Puros')
	)

Opciones_alcoholismo = (
	('Nunca','Nunca'),('Social','Social'),('Diario','Diario'),('Embriaguez','Embriaguez')
	)

Opciones_drogadiccion = (
	('Nunca','Nunca'),('Mariguana','Mariguana'),('Anfetaminas','Anfetaminas'),('Otras','Otras')
	)

Opciones_ejercicio = (
	('Nunca','Nunca'),('1-2x/semana','1-2x/semana'),('3-4x/semana','3-4x/semana'),('5-7x/semana','5-7x/semana')
	)

Opciones_cafeina = (
	('Nunca','Nunca'),('Ocasional','Ocasional'),('Diario','Diario')
	)

# *************************** ESCOLARIDAD
Opciones_escolaridad = (
	('Trunca','Trunca'),('Completa','Completa')
	)
Opciones_select_escolaridad = (
	('Primaria','Primaria'),('Secundaria','Secundaria'),('Preparatoria','Preparatoria'),
	('Licenciatura','Licenciatura'),('Post Grado','Post Grado')
	)
# *************************** ANTECEDENTES FAMILIARES
Opciones_antecedentes_familiares_padres = (
	('Vivo','Vivo'),('Finado','Finado'),('Alta Presión Arterial','Alta Presión Arterial'),('Diabetes','Diabetes'),
	('Colesterol','Colesterol'),('Cáncer','Cáncer'),('Otro','Otro')
	)

Opciones_antecedentes_familiares_hermanos = (
	('Alta Presión Arterial','Alta Presión Arterial'),('Diabetes','Diabetes'),
	('Colesterol','Colesterol'),('Cáncer','Cáncer'),('Otro','Otro')
	)

Opciones_sino = (
	('Si','Si'),('No','No')
	)

Opciones_lado_dominante = (
	('Diestro','Diestro'),('Zurdo','Zurdo')
	)

Opciones_nivel = (
	('Amateur','Amateur'),('Profesional','Profesional')
	)

Opciones_alergias_medicamentos = (
	('Ninguna alergia conocida a Medicamentos','Ninguna alergia conocida a Medicamentos'),
	('Látex','Látex'),('Tela adhesiva','Tela adhesiva'),('Otra','Otra')
	)

Opcion_Inmunizacion = (
	('Otra','Otra'),('Ninguna','Ninguna')
	)

Opcion_Menarca = (
	('Menarca','Menarca'),('Ninguna','Ninguna')
	)
# ***************************** MODELOS

class TipoUsuario(models.Model):
	tipo_de_usuario = models.CharField(max_length=40)

	def __unicode__(self):
		return self.tipo_de_usuario

class Usuario(models.Model):
	name = models.OneToOneField(User)
	tipo_de_usuario = models.ForeignKey(TipoUsuario)


	def __unicode__(self):
		return ("%s - %s") % (self.name, self.tipo_de_usuario )

class ExpedienteMedico(models.Model): 
	fecha = models.DateField(default=timezone.now)
	rfc = models.CharField(max_length=20)
	nombre = models.CharField(max_length=1000)
	ap_paterno = models.CharField(max_length=1000)
	ap_materno = models.CharField(max_length=1000)
	edad_paciente = models.CharField(max_length=1000,blank=True)
	fecha_de_nacimiento = models.CharField(max_length=100) 
	sexo = MultiSelectField(choices=Genero,blank=True)
	estado_civil = MultiSelectField(choices=ECivil,blank=True)
	num_hijos = models.CharField(max_length=1000,blank=True)
	medico_que_refiere = models.CharField(max_length=1000,blank=True)
	motivo_de_consulta = models.CharField(max_length=1000,blank=True)

	#ESTE CAMPO ESTARA ESCONDIDO EN EL HTML, GUARDARA EL NOMBRE DE USUARIO QUE HAGA EL REGISTRO
	usuario = models.CharField(max_length=1000,blank=True)

	# ************** ANTECEDENTES PERSONALES
	antecedentes_personales = MultiSelectField(choices=Enfermedades,blank=True)
	
	# ************** ALERGIAS A MEDICAMENTOS 
	alergias_medicamentos = MultiSelectField(choices=Opciones_alergias_medicamentos,blank=True)

	# ************** PRACTICAS SOCIALES
	tabaquismo = MultiSelectField(choices=Opciones_tabaquismo,blank=True)
	dias_tabaquismo = models.CharField(max_length=1000,blank=True)
	year_tabaquismo = models.CharField(max_length=1000,blank=True)
	alcoholismo = MultiSelectField(choices=Opciones_alcoholismo,blank=True)
	year_alcoholismo = models.CharField(max_length=1000,blank=True)
	drogadiccion = MultiSelectField(choices=Opciones_drogadiccion,blank=True)
	year_drogadiccion = models.CharField(max_length=1000,blank=True)
	ejercicio = MultiSelectField(choices=Opciones_ejercicio,blank=True)
	year_ejercicio = models.CharField(max_length=1000,blank=True)
	cafeina = MultiSelectField(choices=Opciones_cafeina,blank=True)
	year_cafeina = models.CharField(max_length=1000,blank=True)
	creencia_religiosa = models.CharField(max_length=1000,blank=True) 

	# ************** ESCOLARIDAD
	nivel_escolaridad = models.CharField(max_length=100,blank=True,choices=Opciones_select_escolaridad)
	tiempo_escolaridad = MultiSelectField(choices=Opciones_escolaridad,blank=True)
	alcance_escolaridad = models.CharField(max_length=1000,blank=True)

	# ************** ANTECEDENTES HEREDO-FAMILIARES
	# PADRE
	edad_padre = models.CharField(max_length=1000,blank=True)
	antecedentes_padre = MultiSelectField(choices=Opciones_antecedentes_familiares_padres,blank=True)
	causa_muerte_padre = models.CharField(max_length=300,blank=True)
	# MADRE
	edad_madre = models.CharField(max_length=1000,blank=True)
	antecedentes_madre = MultiSelectField(choices=Opciones_antecedentes_familiares_padres,blank=True)
	causa_muerte_madre = models.CharField(max_length=1000,blank=True)
	# HERMANOS
	edad_hermanos = models.CharField(max_length=1000,blank=True)
	num_hermanos_vivos = models.CharField(max_length=1000,blank=True)
	num_hermanos_finados = models.CharField(max_length=1000,blank=True)
	antecedentes_hermanos = MultiSelectField(choices=Opciones_antecedentes_familiares_hermanos,blank=True)
	#Preguntas extra
	practica_deporte = MultiSelectField(choices=Opciones_sino,blank=True)
	que_deporte = models.CharField(max_length=1000,blank=True)
	lado_dominante = MultiSelectField(choices=Opciones_lado_dominante,blank=True)
	nivel = MultiSelectField(choices=Opciones_nivel,blank=True)

	# ************** SECCION PARA MUJERES
	esta_embarazada = MultiSelectField(choices=Opciones_sino,blank=True)
	esta_amamantando = MultiSelectField(choices=Opciones_sino,blank=True)
	menarca = MultiSelectField(choices=Opcion_Menarca,blank=True)
	num_embarazos = models.CharField(max_length=1000,blank=True)
	tipos_de_anticonceptivos = models.CharField(max_length=1000,blank=True)
	fecha_de_ultima_regla = models.CharField(max_length=1000,blank=True)

	# ************** INMUNIZACIONES
	fecha_gripe = models.CharField(max_length=1000,blank=True)
	fecha_tetanos = models.CharField(max_length=1000,blank=True)
	otra_inmunizacion = MultiSelectField(choices=Opcion_Inmunizacion,blank=True)

	# ************** CAMPOS NUEVOS
	padecimiento_actual = models.TextField(max_length=100000, blank=True)
	idx = models.CharField(max_length=1000,blank=True)
	aseguranza = models.CharField(max_length=100,blank=True,choices=Aseguranzas)

	# subir archivos
	archivos = models.FileField(upload_to='archivos_physiomed',blank=True, null=True)
	# def get_absolute_url(self):
	# 	return reverse('Modificar_Expediente_Medico', kwargs={'pk': self.pk})


	def __str__(self):
		return "%s %s" % (self.rfc, self.usuario)


# Formset para ANTECEDENTES PERSONALES (Tipo de CANCER)
class AntecedentesPersonalesCancer(models.Model): 
	fk_expedientemedico = models.ForeignKey(ExpedienteMedico) 
	tipo = models.CharField(max_length=1000,blank=True)
	tratamiento = models.CharField(max_length=1000,blank=True)

	def __str__(self): 
		return "%s %s" % (self.fk_expedientemedico.rfc, self.tipo)

# Formset para ANTECEDENTES PERSONALES (Otros)
class AntecedentesPersonalesOtros(models.Model): 
	fk_expedientemedico = models.ForeignKey(ExpedienteMedico) 
	otro_antecedentes_personales = models.CharField(max_length=1000,blank=True)    

	def __str__(self): 
		return "%s %s" % (self.fk_expedientemedico.rfc, self.otro_antecedentes_personales)


# Formset para ANTECEDENTES Quirurgicos
class AntecedentesQuirurgicos(models.Model): 
	fk_expedientemedico = models.ForeignKey(ExpedienteMedico) 
	tipo_de_cirugia = models.CharField(max_length=1000,blank=True)    
	year = models.CharField(max_length=100,blank=True) 

	def __str__(self): 
		return "%s %s" % (self.fk_expedientemedico.rfc, self.tipo_de_cirugia)

# Formset
class MedicamentosPrescritos(models.Model): 
	fk_expedientemedico = models.ForeignKey(ExpedienteMedico) 
	medicamento = models.CharField(max_length=1000,blank=True)    
	dosis = models.CharField(max_length=100,blank=True) 

	def __str__(self): 
		return "%s %s" % (self.fk_expedientemedico.rfc, self.medicamento)

# Formset
class Complementos(models.Model): 
	fk_expedientemedico = models.ForeignKey(ExpedienteMedico) 
	medicamento = models.CharField(max_length=1000,blank=True)    
	dosis = models.CharField(max_length=100,blank=True) 

	def __str__(self): 
		return "%s %s" % (self.fk_expedientemedico.rfc, self.medicamento)

# Formset
class AlergiasMedicamentos(models.Model): 
	fk_expedientemedico = models.ForeignKey(ExpedienteMedico) 
	alergia = models.CharField(max_length=1000,blank=True)    
	reaccion = models.CharField(max_length=100,blank=True) 

	def __str__(self): 
		return "%s %s" % (self.fk_expedientemedico.rfc, self.alergia)


# Formset
class AlergiasMedicamentosLatex(models.Model): 
	fk_expedientemedico = models.ForeignKey(ExpedienteMedico)  
	reaccion = models.CharField(max_length=100,blank=True) 

	def __str__(self): 
		return "%s %s" % (self.fk_expedientemedico.rfc, self.reaccion)

class AlergiasMedicamentosTela(models.Model): 
	fk_expedientemedico = models.ForeignKey(ExpedienteMedico)  
	reaccion = models.CharField(max_length=100,blank=True) 

	def __str__(self): 
		return "%s %s" % (self.fk_expedientemedico.rfc, self.reaccion)

class DrogadiccionOtras(models.Model): 
	fk_expedientemedico = models.ForeignKey(ExpedienteMedico)  
	otra = models.CharField(max_length=100,blank=True) 

	def __str__(self): 
		return "%s %s" % (self.fk_expedientemedico.rfc, self.otra)


# Formsets Para Seccion Heredo Familiar (Cancer y Otro)
class PadreCancer(models.Model): 
	fk_expedientemedico = models.ForeignKey(ExpedienteMedico) 
	tipo = models.CharField(max_length=1000,blank=True)

	def __str__(self): 
		return "%s %s" % (self.fk_expedientemedico.rfc, self.tipo)

class PadreOtros(models.Model): 
	fk_expedientemedico = models.ForeignKey(ExpedienteMedico) 
	otro = models.CharField(max_length=1000,blank=True)    

	def __str__(self): 
		return "%s %s" % (self.fk_expedientemedico.rfc, self.otro)


class MadreCancer(models.Model): 
	fk_expedientemedico = models.ForeignKey(ExpedienteMedico) 
	tipo = models.CharField(max_length=1000,blank=True)

	def __str__(self): 
		return "%s %s" % (self.fk_expedientemedico.rfc, self.tipo)

class MadreOtros(models.Model): 
	fk_expedientemedico = models.ForeignKey(ExpedienteMedico) 
	otro = models.CharField(max_length=1000,blank=True)    

	def __str__(self): 
		return "%s %s" % (self.fk_expedientemedico.rfc, self.otro)


class HermanosCancer(models.Model): 
	fk_expedientemedico = models.ForeignKey(ExpedienteMedico) 
	tipo = models.CharField(max_length=1000,blank=True)

	def __str__(self): 
		return "%s %s" % (self.fk_expedientemedico.rfc, self.tipo)

class HermanosOtros(models.Model): 
	fk_expedientemedico = models.ForeignKey(ExpedienteMedico) 
	otro = models.CharField(max_length=1000,blank=True)    

	def __str__(self): 
		return "%s %s" % (self.fk_expedientemedico.rfc, self.otro)

class HermanosCausaMuerte(models.Model): 
	fk_expedientemedico = models.ForeignKey(ExpedienteMedico) 
	causamuerte = models.CharField(max_length=1000,blank=True)    

	def __str__(self): 
		return "%s %s" % (self.fk_expedientemedico.rfc, self.causamuerte)

class InmunizacionesOtras(models.Model): 
	fk_expedientemedico = models.ForeignKey(ExpedienteMedico) 
	otra = models.CharField(max_length=1000,blank=True)   
	fecha = models.CharField(max_length=1000,blank=True)    

	def __str__(self): 
		return "%s %s" % (self.fk_expedientemedico.rfc, self.otra)


class HojaEvolucion(models.Model): 
	fk_expedientemedico = models.ForeignKey(ExpedienteMedico) 
	fecha = models.CharField(max_length=1000,blank=True)   
	evolucion = models.TextField(max_length=100000,blank=True)    

	def __str__(self): 
		return "%s %s" % (self.fk_expedientemedico.rfc, self.evolucion)


class HojaTratamiento(models.Model): 
	fk_expedientemedico = models.ForeignKey(ExpedienteMedico) 
	fecha = models.CharField(max_length=1000,blank=True)
	tx = models.TextField(max_length=100000,blank=True)    

	def __str__(self): 
		return "%s %s" % (self.fk_expedientemedico.rfc, self.tx)