$(document).ready(() => {
  $(".ver-especialidades").click(function () {
    id = $(this).data("id");
    $("." + id).slideToggle("slow");
  });


  $(".nav-top span").click(function(){
    pagina = $(this).data("page");
    $(".nav-top span").removeClass("seleccionado-top");
    $(this).addClass("seleccionado-top");
    $(".pagina").hide();
    $("."+pagina).slideToggle("slow");
  });


  $(".ver-solicitud").click(function(){
    id = $(this).data("id");
    url = "/ver-detalle-solicitud/"+id+"/";
    $.ajax(url, {
      success: function (data, status, xhr) {
        console.log(data.length);
        table = get_tabla(data);
        if (data.length > 0) {
          swal("Detalles de la solicitud", {
            text: table,
          });
        } else {
          swal({
            title: "Detalle de la solicitud",
            text: "Ops! no hay registros para esta solicitud",
            icon: "error",
          });
        }
      },
      error: function (jqXhr, textStatus, errorMessage) {
        return "Ocurrio un error, intente de nuevo";
      },
    });
  });
});


function get_tabla(_tabla){
  console.log(_tabla)
  tabla = `
  <table class='table'>
    <thead>
      <tr>
        <th>Especialidad</th>
        <th>descripcion de la solicitud</th>
        <th>Fecha y hora asignada</th>
        <th>Estado</th>
      </tr>
    </thead>
    <tbody>
    
    </tbody>
  </table>
  `
  return tabla
}
