from django.forms import ModelForm, inlineformset_factory
from django import forms
from . import widgets
from .widgets import (DateInput,PasswordInput
    )
from django.contrib.auth.forms import UserCreationForm

from .models import (ExpedienteMedico,AntecedentesQuirurgicos,MedicamentosPrescritos,Complementos,
    AlergiasMedicamentos,AntecedentesPersonalesCancer,AntecedentesPersonalesOtros,
    AlergiasMedicamentosLatex,AlergiasMedicamentosTela,DrogadiccionOtras,PadreCancer,MadreCancer,
    HermanosCancer,PadreOtros,MadreOtros,HermanosOtros,HermanosCausaMuerte,InmunizacionesOtras,
    HojaEvolucion,HojaTratamiento
    )

from .models import TipoUsuario
from django.contrib.auth.models import User



class RegistrarExpedienteForm(ModelForm):
    class Meta:
        model = ExpedienteMedico
        #padecimiento_actual =  forms.Textarea(attrs={'cols': 80, 'rows': 20})
        exclude = ()


class AntecedentesPersonalesCancerForm(ModelForm):
    class Meta:
        model = AntecedentesPersonalesCancer
        fields = ('tipo','tratamiento')
AntecedentesPersonalesCancerFormSet = inlineformset_factory(ExpedienteMedico, AntecedentesPersonalesCancer,
                                            form=AntecedentesPersonalesCancerForm, extra=1)


class AntecedentesPersonalesOtrosForm(ModelForm):
    class Meta:
        model = AntecedentesPersonalesOtros
        fields = ('otro_antecedentes_personales',)
AntecedentesPersonalesOtrosFormSet = inlineformset_factory(ExpedienteMedico, AntecedentesPersonalesOtros,
                                            form=AntecedentesPersonalesOtrosForm, extra=1)



class AntecedentesQuirurgicosForm(ModelForm):
    class Meta:
        model = AntecedentesQuirurgicos
        fields = ('tipo_de_cirugia', 'year')
        widgets = {
            'year': DateInput(),
        }
AntecedentesQuirurgicosFormSet = inlineformset_factory(ExpedienteMedico, AntecedentesQuirurgicos,
                                            form=AntecedentesQuirurgicosForm, extra=1)


class MedicamentosPrescritosForm(ModelForm):
    class Meta:
        model = MedicamentosPrescritos
        fields = ('medicamento', 'dosis')
MedicamentosPrescritosFormSet = inlineformset_factory(ExpedienteMedico, MedicamentosPrescritos,
                                            form=MedicamentosPrescritosForm, extra=1)


class ComplementosForm(ModelForm):
    class Meta:
        model = Complementos
        fields = ('medicamento', 'dosis')
ComplementosFormSet = inlineformset_factory(ExpedienteMedico, Complementos,
                                            form=ComplementosForm, extra=1)

class AlergiasMedicamentosForm(ModelForm):
    class Meta:
        model = AlergiasMedicamentos
        fields = ('alergia', 'reaccion')
AlergiasMedicamentosFormSet = inlineformset_factory(ExpedienteMedico, AlergiasMedicamentos,
                                            form=AlergiasMedicamentosForm, extra=1)


class AlergiasMedicamentosLatexForm(ModelForm):
    class Meta:
        model = AlergiasMedicamentosLatex
        fields = ('reaccion',)
AlergiasMedicamentosLatexFormSet = inlineformset_factory(ExpedienteMedico, AlergiasMedicamentosLatex,
                                            form=AlergiasMedicamentosLatexForm, extra=1)

class AlergiasMedicamentosTelaForm(ModelForm):
    class Meta:
        model = AlergiasMedicamentosTela
        fields = ('reaccion',)
AlergiasMedicamentosTelaFormSet = inlineformset_factory(ExpedienteMedico, AlergiasMedicamentosTela,
                                            form=AlergiasMedicamentosTelaForm, extra=1)

class DrogadiccionOtrasForm(ModelForm):
    class Meta:
        model = DrogadiccionOtras
        fields = ('otra',)
DrogadiccionOtrasFormSet = inlineformset_factory(ExpedienteMedico, DrogadiccionOtras,
                                            form=DrogadiccionOtrasForm, extra=1)


class PadreCancerForm(ModelForm):
    class Meta:
        model = PadreCancer
        fields = ('tipo',)
PadreCancerFormSet = inlineformset_factory(ExpedienteMedico, PadreCancer,
                                            form=PadreCancerForm, extra=1)

class PadreOtrosForm(ModelForm):
    class Meta:
        model = PadreOtros
        fields = ('otro',)
PadreOtrosFormSet = inlineformset_factory(ExpedienteMedico, PadreOtros,
                                            form=PadreOtrosForm, extra=1)

class MadreCancerForm(ModelForm):
    class Meta:
        model = MadreCancer
        fields = ('tipo',)
MadreCancerFormSet = inlineformset_factory(ExpedienteMedico, MadreCancer,
                                            form=MadreCancerForm, extra=1)
class MadreOtrosForm(ModelForm):
    class Meta:
        model = MadreOtros
        fields = ('otro',)
MadreOtrosFormSet = inlineformset_factory(ExpedienteMedico, MadreOtros,
                                            form=MadreOtrosForm, extra=1)
class HermanosCancerForm(ModelForm):
    class Meta:
        model = HermanosCancer
        fields = ('tipo',)
HermanosCancerFormSet = inlineformset_factory(ExpedienteMedico, HermanosCancer,
                                            form=HermanosCancerForm, extra=1)

class HermanosOtrosForm(ModelForm):
    class Meta:
        model = HermanosOtros
        fields = ('otro',)
HermanosOtrosFormSet = inlineformset_factory(ExpedienteMedico, HermanosOtros,
                                            form=HermanosOtrosForm, extra=1)

class HermanosCausaMuerteForm(ModelForm):
    class Meta:
        model = HermanosCausaMuerte
        fields = ('causamuerte',)
HermanosCausaMuerteFormSet = inlineformset_factory(ExpedienteMedico, HermanosCausaMuerte,
                                            form=HermanosCausaMuerteForm, extra=1)

class InmunizacionesOtrasForm(ModelForm):
    class Meta:
        model = InmunizacionesOtras
        fields = ('otra','fecha')
        widgets = {
            'fecha': DateInput(),
        }
InmunizacionesOtrasFormSet = inlineformset_factory(ExpedienteMedico, InmunizacionesOtras,
                                            form=InmunizacionesOtrasForm, extra=1)


class HojaEvolucionForm(ModelForm):
    class Meta:
        model = HojaEvolucion
        fields = ('fecha','evolucion')
        widgets = {
            'fecha': DateInput(),
        }
HojaEvolucionFormSet = inlineformset_factory(ExpedienteMedico, HojaEvolucion,
                                            form=HojaEvolucionForm, extra=1)

class HojaTratamientoForm(ModelForm):
    class Meta:
        model = HojaTratamiento
        fields = ('fecha','tx')
        widgets = {
            'fecha': DateInput(),
        }
HojaTratamientoFormSet = inlineformset_factory(ExpedienteMedico, HojaTratamiento,
                                            form=HojaTratamientoForm, extra=1)






class Users_Form(UserCreationForm):
        tipo_de_usuario= forms.ModelChoiceField(queryset=TipoUsuario.objects.all())
