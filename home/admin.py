# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import (ExpedienteMedico,AntecedentesQuirurgicos,MedicamentosPrescritos,Complementos,
	AlergiasMedicamentos,AntecedentesPersonalesCancer,AntecedentesPersonalesOtros,
	AlergiasMedicamentosLatex,AlergiasMedicamentosTela,DrogadiccionOtras,PadreCancer,MadreCancer,
	HermanosCancer,PadreOtros,MadreOtros,HermanosOtros,HermanosCausaMuerte,InmunizacionesOtras,
	HojaEvolucion,TipoUsuario,HojaTratamiento,Usuario
	)
from django.contrib.auth.models import Permission
admin.site.register(Permission)
# Register your models here.

admin.site.register(ExpedienteMedico)
admin.site.register(AntecedentesQuirurgicos)
admin.site.register(MedicamentosPrescritos)
admin.site.register(Complementos)
admin.site.register(AlergiasMedicamentos)
admin.site.register(AntecedentesPersonalesCancer)
admin.site.register(AntecedentesPersonalesOtros)
admin.site.register(AlergiasMedicamentosLatex)
admin.site.register(AlergiasMedicamentosTela)
admin.site.register(DrogadiccionOtras)

admin.site.register(PadreCancer)
admin.site.register(MadreCancer)
admin.site.register(HermanosCancer)
admin.site.register(PadreOtros)
admin.site.register(MadreOtros)
admin.site.register(HermanosOtros)
admin.site.register(HermanosCausaMuerte)
admin.site.register(InmunizacionesOtras)
admin.site.register(HojaEvolucion)
admin.site.register(TipoUsuario)
admin.site.register(Usuario)
admin.site.register(HojaTratamiento)
