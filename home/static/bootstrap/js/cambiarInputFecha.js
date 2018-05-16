    // $("#id_fecha").focus(function(){
    //     $(this).prop('type', 'date');
    // });

    $("#id_fecha_de_nacimiento").focus(function(){
        $(this).prop('type', 'date');
    });

function submitBday() {
    var edad = "";
    var fechanacimiento = document.getElementById('id_fecha_de_nacimiento').value;
    var dia = +new Date(fechanacimiento);
    edad += ~~ ((Date.now() - dia) / (31557600000));
    
    document.getElementById('id_edad_paciente').value = edad;
}


/* Funciones para revisar si checkbox esta marcado y mostrar/esconder 
secciones donde se presente la opcion de "Otros"/"Tipo de Cancer"*/
$( document ).ready(function() { 
    /* Al momento de abrir la Plantilla*/
    if ($('#id_antecedentes_personales_26').is(':checked')){
        $('#antecedentespersonales_cancer').show();
    }
    else
    {
        $('#antecedentespersonales_cancer').hide();
    }
    if ($('#id_antecedentes_personales_27').is(':checked')){
        $('#antecedentespersonales_otros').show();
    }
    else
    {
        $('#antecedentespersonales_otros').hide();
    }
    /* Al momento de editar la plantilla */
    $(":checkbox").on("change", function() {
        if (this.id === "id_antecedentes_personales_26" && this["name"] === "antecedentes_personales" && this.checked) 
        {
            $('#antecedentespersonales_cancer').show();
        }
        else if (this.id === "id_antecedentes_personales_27" && this["name"] === "antecedentes_personales" && this.checked) 
        {
            $('#antecedentespersonales_otros').show();
        }
        else
        {
            if (this.id === "id_antecedentes_personales_26" && this["name"] === "antecedentes_personales" && !this.checked) 
        {
            $('#antecedentespersonales_cancer').hide();
        }
        else if (this.id === "id_antecedentes_personales_27" && this["name"] === "antecedentes_personales" && !this.checked) 
        {
            $('#antecedentespersonales_otros').hide();
        }
        else
        {
            
        }
        }
    });
}); /* Finaliza funcion ready */



$( document ).ready(function() { 
    /* Al momento de abrir la Plantilla*/
    if ($('#id_alergias_medicamentos_3').is(':checked')){
        $('#alergias_otros').show();
    }
    else
    {
        $('#alergias_otros').hide();
    }
    if ($('#id_alergias_medicamentos_2').is(':checked')){
        $('#alergias_tela').show();
    }
    else
    {
        $('#alergias_tela').hide();
    }
    if ($('#id_alergias_medicamentos_1').is(':checked')){
        $('#alergias_latex').show();
    }
    else
    {
        $('#alergias_latex').hide();
    }
    /* Al momento de editar la plantilla */
    $(":checkbox").on("change", function() {
        if (this.id === "id_alergias_medicamentos_3" && this["name"] === "alergias_medicamentos" && this.checked) 
        {
            $('#alergias_otros').show();
        }
        else if (this.id === "id_alergias_medicamentos_2" && this["name"] === "alergias_medicamentos" && this.checked) 
        {
            $('#alergias_tela').show();
        }
        else if (this.id === "id_alergias_medicamentos_1" && this["name"] === "alergias_medicamentos" && this.checked) 
        {
            $('#alergias_latex').show();
        }
        else
        {
            if (this.id === "id_alergias_medicamentos_3" && this["name"] === "alergias_medicamentos" && !this.checked) 
        {
            $('#alergias_otros').hide();
        }
        else if (this.id === "id_alergias_medicamentos_2" && this["name"] === "alergias_medicamentos" && !this.checked) 
        {
            $('#alergias_tela').hide();
        }
        else if (this.id === "id_alergias_medicamentos_1" && this["name"] === "alergias_medicamentos" && !this.checked) 
        {
            $('#alergias_latex').hide();
        }
        else
        {
            
        }
        }
    });
}); /* Finaliza funcion ready */


$( document ).ready(function() { 
    /* Al momento de abrir la Plantilla*/
    if ($('#id_drogadiccion_3').is(':checked')){
        $('#drogadiccion_otras').show();
    }
    else
    {
        $('#drogadiccion_otras').hide();
    }
    $(":checkbox").on("change", function() {
        if (this.id === "id_drogadiccion_3" && this["name"] === "drogadiccion" && this.checked) 
        {
            $('#drogadiccion_otras').show();
        }
        
        else
        {
            if (this.id === "id_drogadiccion_3" && this["name"] === "drogadiccion" && !this.checked) 
            {
                $('#drogadiccion_otras').hide();
            }
        }
    });
}); /* Finaliza funcion ready */




$( document ).ready(function() { 
    /* Al momento de abrir la Plantilla*/
    if ($('#id_tiempo_escolaridad_0').is(':checked')){
        $('#alcance_escuela').show();
    }
    else
    {
        $('#alcance_escuela').hide();
    }
    $(":checkbox").on("change", function() {
        if (this.id === "id_tiempo_escolaridad_0" && this["name"] === "tiempo_escolaridad" && this.checked) 
        {
            $('#alcance_escuela').show();
        }
        else if (this.id === "id_tiempo_escolaridad_1" && this["name"] === "tiempo_escolaridad" && this.checked) 
        {
            $('#alcance_escuela').hide();
        }
        else
        {
            if (this.id === "id_tiempo_escolaridad_0" && this["name"] === "tiempo_escolaridad" && !this.checked) 
            {
                $('#alcance_escuela').hide();
            }
        }
    });
}); /* Finaliza funcion ready */


$( document ).ready(function() { 
    /* Al momento de abrir la Plantilla*/
    if ($('#id_antecedentes_padre_5').is(':checked')){
        $('#padrecancer').show();
    }
    else
    {
        $('#padrecancer').hide();
    }
    if ($('#id_antecedentes_padre_6').is(':checked')){
        $('#padreotros').show();
    }
    else
    {
        $('#padreotros').hide();
    }
    if ($('#id_antecedentes_padre_1').is(':checked')){
        $('#padrecausamuerte').show();
    }
    else
    {
        $('#padrecausamuerte').hide();
    }
    $(":checkbox").on("change", function() {
        if (this.id === "id_antecedentes_padre_5" && this["name"] === "antecedentes_padre" && this.checked) 
        {
            $('#padrecancer').show();
        }
        else if (this.id === "id_antecedentes_padre_6" && this["name"] === "antecedentes_padre" && this.checked) 
        {
            $('#padreotros').show();
        }
        else if (this.id === "id_antecedentes_padre_1" && this["name"] === "antecedentes_padre" && this.checked) 
        {
            $('#padrecausamuerte').show();
        }
        else
        {
            if (this.id === "id_antecedentes_padre_5" && this["name"] === "antecedentes_padre" && !this.checked) 
            {
            $('#padrecancer').hide();
            }
            else if (this.id === "id_antecedentes_padre_6" && this["name"] === "antecedentes_padre" && !this.checked) 
            {
            $('#padreotros').hide();
            }
            else if (this.id === "id_antecedentes_padre_1" && this["name"] === "antecedentes_padre" && !this.checked) 
            {
            $('#padrecausamuerte').hide();
            }
            else
            {}
            
        }
    });
}); /* Finaliza funcion ready */


$( document ).ready(function() { 
    /* Al momento de abrir la Plantilla*/
    if ($('#id_antecedentes_madre_5').is(':checked')){
        $('#madrecancer').show();
    }
    else
    {
        $('#madrecancer').hide();
    }
    if ($('#id_antecedentes_madre_6').is(':checked')){
        $('#madreotros').show();
    }
    else
    {
        $('#madreotros').hide();
    }
    if ($('#id_antecedentes_madre_1').is(':checked')){
        $('#madrecausamuerte').show();
    }
    else
    {
        $('#madrecausamuerte').hide();
    }
    $(":checkbox").on("change", function() {
        if (this.id === "id_antecedentes_madre_5" && this["name"] === "antecedentes_madre" && this.checked) 
        {
            $('#madrecancer').show();
        }
        else if (this.id === "id_antecedentes_madre_6" && this["name"] === "antecedentes_madre" && this.checked) 
        {
            $('#madreotros').show();
        }
        else if (this.id === "id_antecedentes_madre_1" && this["name"] === "antecedentes_madre" && this.checked) 
        {
            $('#madrecausamuerte').show();
        }
        else
        {
            if (this.id === "id_antecedentes_madre_5" && this["name"] === "antecedentes_madre" && !this.checked) 
            {
            $('#madrecancer').hide();
            }
            else if (this.id === "id_antecedentes_madre_6" && this["name"] === "antecedentes_madre" && !this.checked) 
            {
            $('#madreotros').hide();
            }
            else if (this.id === "id_antecedentes_madre_1" && this["name"] === "antecedentes_madre" && !this.checked) 
            {
            $('#madrecausamuerte').hide();
            }
            else
            {}
            
        }
    });
}); /* Finaliza funcion ready */


$( document ).ready(function() {
    /* Al momento de abrir la Plantilla*/
    if ($('#id_antecedentes_hermanos_3').is(':checked')){
        $('#hermanoscancer').show();
    }
    else
    {
        $('#hermanoscancer').hide();
    }
    if ($('#id_antecedentes_hermanos_4').is(':checked')){
        $('#hermanosotros').show();
    }
    else
    {
        $('#hermanosotros').hide();
    } 
    $(":checkbox").on("change", function() {
        if (this.id === "id_antecedentes_hermanos_3" && this["name"] === "antecedentes_hermanos" && this.checked) 
        {
            $('#hermanoscancer').show();
        }
        else if (this.id === "id_antecedentes_hermanos_4" && this["name"] === "antecedentes_hermanos" && this.checked) 
        {
            $('#hermanosotros').show();
        }
        else
        {
            if (this.id === "id_antecedentes_hermanos_3" && this["name"] === "antecedentes_hermanos" && !this.checked) 
            {
            $('#hermanoscancer').hide();
            }
            else if (this.id === "id_antecedentes_hermanos_4" && this["name"] === "antecedentes_hermanos" && !this.checked) 
            {
            $('#hermanosotros').hide();
            }
            else
            {}
            
        }
    });
}); /* Finaliza funcion ready */


$( document ).ready(function() { 
    /* Al momento de abrir la Plantilla*/
if ($('#id_num_hermanos_finados').val() >=1){
    $('#hermanoscausamuerte').show();
}
else{
    $('#hermanoscausamuerte').hide();
}
/* Al ingresar algo en input*/
$('#id_num_hermanos_finados').keyup(function(){
      if ($(this).val() >= 1) { 
            $('#hermanoscausamuerte').show();
      } else {
           
            $('#hermanoscausamuerte').hide();
      }
 });
}); /* Finaliza funcion ready */


$( document ).ready(function() { 
    /* Al momento de abrir la Plantilla*/
    if ($('#id_practica_deporte_0').is(':checked')){
        $('#cualdeporte').show();
    }
    else
    {
        $('#cualdeporte').hide();
    }
    $(":checkbox").on("change", function() {
        if (this.id === "id_practica_deporte_0" && this["name"] === "practica_deporte" && this.checked) 
        {
            $('#cualdeporte').show();
        }
        else if (this.id === "id_practica_deporte_1" && this["name"] === "practica_deporte" && this.checked) 
        {
            $('#cualdeporte').hide();
        }
        else
        {
            if (this.id === "id_practica_deporte_0" && this["name"] === "practica_deporte" && !this.checked) 
            {
                $('#cualdeporte').hide();
            }
        }
    });
}); /* Finaliza funcion ready */


$( document ).ready(function() { 
    /* Al momento de abrir la Plantilla*/
    if ($('#id_otra_inmunizacion_0').is(':checked')){
        $('#inmunizacionesotras').show();
    }
    else
    {
        $('#inmunizacionesotras').hide();
    }
    $(":checkbox").on("change", function() {
        if (this.id === "id_otra_inmunizacion_0" && this["name"] === "otra_inmunizacion" && this.checked) 
        {
            $('#inmunizacionesotras').show();
        }
        
        else
        {
            if (this.id === "id_otra_inmunizacion_0" && this["name"] === "otra_inmunizacion" && !this.checked) 
        {
            $('#inmunizacionesotras').hide();
        }
        }
    });


    $("#id_fecha_de_ultima_regla").focus(function(){
      $(this).prop('type', 'date');
  });

  $("#id_fecha_gripe").focus(function(){
      $(this).prop('type', 'date');
  });
  
  $("#id_fecha_tetanos").focus(function(){
      $(this).prop('type', 'date');
  });
}); /* Finaliza funcion ready */


$( document ).ready(function() {  
    /* Al momento de abrir la Plantilla*/
    if ($('#id_menarca_0').is(':checked')){
        $('#menarca_div').show();
    }
    else
    {
        $('#menarca_div').hide();
    }
    $(":checkbox").on("change", function() {
        if (this.id === "id_menarca_0" && this["name"] === "menarca" && this.checked) 
        {
            $('#menarca_div').show();
        }
        
        else
        {
            if (this.id === "id_menarca_0" && this["name"] === "menarca" && !this.checked) 
        {
            $('#menarca_div').hide();
        }
        }
    });
}); /* Finaliza funcion ready */

$( document ).ready(function() { 
    /* Al momento de abrir la Plantilla*/
    if ($('#id_sexo_1').is(':checked')){
        $('#Mujeres-tab').show();
    }
    else
    {
        $('#Mujeres-tab').hide();
    }
    $(":checkbox").on("change", function() {
        if (this.id === "id_sexo_1" && this["name"] === "sexo" && this.checked) 
        {
            $('#Mujeres-tab').show();
        }
        else if (this.id === "id_sexo_0" && this["name"] === "sexo" && this.checked) 
        {
            $('#Mujeres-tab').hide();
        }
        else
        {
            if (this.id === "id_sexo_1" && this["name"] === "sexo" && !this.checked) 
            {
                $('#Mujeres-tab').hide();
            }
        }
    });
}); /* Finaliza funcion ready */


