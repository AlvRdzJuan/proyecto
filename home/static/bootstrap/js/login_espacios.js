$(function(){
  $('#u').bind('input', function(){
    $(this).val(function(_, v){
     return v.replace(/\s+/g, '');
    });
  });
});

$(function(){
  $('#p').bind('input', function(){
    $(this).val(function(_, v){
     return v.replace(/\s+/g, '');
    });
  });
});

$(function(){
  $('#id_username').bind('input', function(){
    $(this).val(function(_, v){
     return v.replace(/\s+/g, '');
    });
  });
});

$(function(){
  $('#id_password').bind('input', function(){
    $(this).val(function(_, v){
     return v.replace(/\s+/g, '');
    });
  });
});