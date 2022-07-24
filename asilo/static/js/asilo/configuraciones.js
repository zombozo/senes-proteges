$(document).ready(function(){
    $(".eliminar").click(function(){
        nombre = $(this).data('name');
        swal({
            title:"Estas seguro que quieres eliminar este backup?",
            text: "SI eliminas este archivo no podras recuperarlo",
            ico: "warning",
            buttons: true,
            dangerMode: true,
        })
        .then((willDelete)=>{
            if(willDelete){
              url = `/eliminar-backup/${nombre}/`;
              $.ajax(url, {
                success: function (data, status, xhr) {
                  if (data.status) {
                    swal(data.message, {
                      ico: "success",
                    });
                    location.reload()
                  } else {
                    swal(data.message, {
                      ico: "error",
                    });
                  }
                },
                error: function (jqXhr, textStatus, errorMessage) {
                  return "Ocurrio un error, intente de nuevo";
                },
              });
            }else {
                
            }
        })
    });
    $(".crear-backup").click(function(){
        url = `/crear-backup/`;
        $.ajax(url, {
          success: function (data, status, xhr) {
            console.log(data);
            if (data.status) {
              swal({
                title: "Backup de Base de datos",
                text: data.message,
                icon: "success",
              });
              location.reload();
            }else {
              swal({
                title: "Backup de Base de datos",
                text: data.message,
                icon: "error",
              });
            }
          },
          error: function (jqXhr, textStatus, errorMessage) {
            return "Ocurrio un error, intente de nuevo";
          },
        });
    });
})

function delete_backup(nombre){
    url = `/eliminar-backup/${nombre}/`;
    $.ajax(
        url,
        {
            success: function(data, status, xhr){
                if (data.status){
                    return data.message
                }

            },
            error: function(jqXhr, textStatus, errorMessage){
                return "Ocurrio un error, intente de nuevo"
            }
        }
    )
}

function crear_backup() {
  url = `/crear-backup/`;
  $.ajax(url, {
    success: function (data, status, xhr) {
      console.log(data);
      if (data.status) {
        return data.message;
      }
    },
    error: function (jqXhr, textStatus, errorMessage) {
      return "Ocurrio un error, intente de nuevo";
    },
  });
}