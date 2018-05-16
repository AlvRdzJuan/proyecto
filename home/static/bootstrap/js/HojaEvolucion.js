document.getElementById('fullname').textContent = document.getElementById('id_nombre').value +" "+document.getElementById('id_ap_paterno').value +" "+document.getElementById('id_ap_materno').value;
document.getElementById('labelidx').textContent = document.getElementById('id_idx').value;

document.getElementById('id_nombre').type = 'hidden';
document.getElementById('id_ap_paterno').type = 'hidden';
document.getElementById('id_ap_materno').type = 'hidden';
document.getElementById('id_idx').type = 'hidden';

document.getElementById("fullname").disabled = true;
document.getElementById("labelidx").disabled = true;

$('[id^="id_hojaevolucion_set"][id$="-evolucion"]').addClass('csstextarea'); 
