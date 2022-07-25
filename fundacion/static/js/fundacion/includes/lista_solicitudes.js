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
        console.log(data);
        table = get_tabla(data);
        $(".modal-body").empty();
        if (data.length > 0) {
          $(".modal-body").append(table);
          $("#myModal").modal("show");
        } else {
          message = `
            <span class="alert alert-info">
              No se encontraron especialidades para esta solicitud
            </span>
          `
          $(".modal-body").append(message);
          $("#myModal").modal("show");
        }
      },
      error: function (jqXhr, textStatus, errorMessage) {
        return "Ocurrio un error, intente de nuevo";
      },
    });
  });





});


function get_tabla(_tabla){
  var elements = []
  for (let index = 0; index < _tabla.length; index++) {
    const element = _tabla[index];
    var estado = ""
    if (element.aceptado == null){
      estado = "Pendiente de aceptacion"
    }else if(element.aceptado== false){
      estado = "solicitud rechazada"
    }
    row = `
      <tr>
        <td>${element.id_especialidad__especialidad}</td>
        <td>
          ${element.id_empleado__id_datos_personales__primer_nombre} 
          ${element.id_empleado__id_datos_personales__primer_apellido}
        </td>
        <td>
          ${element.descripcion}
        </td>
        <td>
          ${element.fecha_hora}
        </td>
        <td>
          ${estado}
        </td>
      </tr>
    `;
    elements.push(row);
  }

  tabla = `
  <table class='table'>
    <thead>
      <tr>
        <th>Especialidad</th>
        <th>Medico asignado</th>
        <th>descripcion de la solicitud</th>
        <th>Fecha y hora asignada</th>
        <th>Estado</th>
      </tr>
    </thead>
    <tbody>
      ${elements}
    </tbody>
  </table>
  `
  return tabla
}
