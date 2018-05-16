document.getElementById("id_fecha_de_nacimiento").oninput = function() {check_user()};
document.getElementById("id_nombre").oninput = function() {check_user()};
document.getElementById("id_ap_paterno").oninput = function() {check_user()};
document.getElementById("id_ap_materno").oninput = function() {check_user()};

vocales="aeiouAEIOU";  
function sacarvocal(paterno){
    for(a=0;a<paterno.length+1;a++)
    { 
        letra=paterno.trim().charAt(a); 
        if(vocales.indexOf(letra)!=-1)
        { 
            return letra; 
            break; 
        } 
    } 
} 

function check_user(){
    nombre=document.getElementById("id_nombre").value;
    letra_nombre=nombre.trim().charAt(0);
    apellido_materno=document.getElementById("id_ap_materno").value;
    letra_apellido_materno=apellido_materno.trim().charAt(0);
    fecha=document.getElementById("id_fecha_de_nacimiento").value;
    yy_fecha=fecha.trim().substring(2,4);
    mm_fecha=fecha.trim().substring(5,7);
    dd_fecha=fecha.trim().substring(8,10);

/* CambiarInputFecha.js*/
    submitBday();

    if((document.getElementById("id_ap_paterno").value != "") || (document.getElementById("id_fecha_de_nacimiento").value != "")) 
    {
        apellido_paterno=document.getElementById("id_ap_paterno").value;
        letra_apellido_paterno=apellido_paterno.trim().charAt(0);
        apellido_paterno=apellido_paterno.trim().substr(1);
        var funcion=sacarvocal(apellido_paterno);
        result=letra_apellido_paterno+funcion+letra_apellido_materno+letra_nombre+yy_fecha+mm_fecha+dd_fecha;
        document.getElementById("id_rfc").value = result.toUpperCase();
    }
    else
    {
        result=letra_apellido_materno+letra_nombre;
        document.getElementById("id_rfc").value = result.toUpperCase();
    }
}


function submitBday() {
    var edad = "";
    var fechanacimiento = document.getElementById('id_fecha_de_nacimiento').value;
    var dia = +new Date(fechanacimiento);
    edad += ~~ ((Date.now() - dia) / (31557600000));
    
    document.getElementById('id_edad_paciente').value = edad;
}

/*SOLO SELECCIONAR UN CHECKBOX*/
$('input[name="sexo"]').on('change', function() {
   $('input[name="sexo"]').not(this).prop('checked', false);
});

$('input[name="estado_civil"]').on('change', function() {
   $('input[name="estado_civil"]').not(this).prop('checked', false);
});

$('input[name="tiempo_escolaridad"]').on('change', function() {
   $('input[name="tiempo_escolaridad"]').not(this).prop('checked', false);
});

$('input[name="practica_deporte"]').on('change', function() {
   $('input[name="practica_deporte"]').not(this).prop('checked', false);
});

$('input[name="lado_dominante"]').on('change', function() {
   $('input[name="lado_dominante"]').not(this).prop('checked', false);
});

$('input[name="nivel"]').on('change', function() {
   $('input[name="nivel"]').not(this).prop('checked', false);
});

$('input[name="esta_embarazada"]').on('change', function() {
   $('input[name="esta_embarazada"]').not(this).prop('checked', false);
});

$('input[name="esta_amamantando"]').on('change', function() {
   $('input[name="esta_amamantando"]').not(this).prop('checked', false);
});




/* AGREGAR PLACEHOLDER A LAS TABLAS DE INLINE-FORMSET*/

$('[id^="id_antecedentespersonalescancer_set"][id$="-tipo"]').attr("placeholder", " Tipo Cáncer");
$('[id^="id_antecedentespersonalescancer_set"][id$="-tratamiento"]').attr("placeholder", " Tratamiento");
$('[id^="id_antecedentespersonalesotros_set"][id$="-otro_antecedentes_personales"]').attr("placeholder", " Especificar (Otro)");

$('[id^="id_alergiasmedicamentos_set"][id$="-alergia"]').attr("placeholder", " Alergia");
$('[id^="id_alergiasmedicamentos_set"][id$="-reaccion"]').attr("placeholder", " Reacción");
$('[id^="id_alergiasmedicamentoslatex_set"][id$="-reaccion"]').attr("placeholder", " Reacción (Látex)");
$('[id^="id_alergiasmedicamentostela_set"][id$="-reaccion"]').attr("placeholder", " Reacción (Tela adhesiva)");

$('[id^="id_complementos_set"][id$="-medicamento"]').attr("placeholder", " Medicamento");
$('[id^="id_complementos_set"][id$="-dosis"]').attr("placeholder", " Dosis");

$('[id^="id_medicamentosprescritos_set"][id$="-medicamento"]').attr("placeholder", " Medicamento");
$('[id^="id_medicamentosprescritos_set"][id$="-dosis"]').attr("placeholder", " Dosis");

$('[id^="id_antecedentesquirurgicos_set"][id$="-tipo_de_cirugia"]').attr("placeholder", " Cirugía");

$('[id^="id_drogadiccionotras_set"][id$="-otra"]').attr("placeholder", " Otra Drogadicción");

$('[id^="id_padrecancer_set"][id$="-tipo"]').attr("placeholder", " Tipo de Cáncer");
$('[id^="id_padreotros_set"][id$="-otro"]').attr("placeholder", " Otro (Especificar)");
$('[id^="id_madrecancer_set"][id$="-tipo"]').attr("placeholder", " Tipo de Cáncer");
$('[id^="id_madreotros_set"][id$="-otro"]').attr("placeholder", " Otro (Especificar)");
$('[id^="id_hermanoscancer_set"][id$="-tipo"]').attr("placeholder", " Tipo de Cáncer");
$('[id^="id_hermanosotros_set"][id$="-otro"]').attr("placeholder", " Otro (Especificar)");

$('[id^="id_hermanoscausamuerte_set"][id$="-causamuerte"]').attr("placeholder", "Causa de muerte");
$('[id^="id_inmunizacionesotras_set"][id$="-otra"]').attr("placeholder", "Otra Inmunización");


