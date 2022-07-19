$(document).ready(() => {
  data = location.href;
  secciones = data.split("/");
  $(".secciones-facturas span").click(function () {
    pagina = $(this).data("pagina");
    $(".secciones-facturas span").removeClass("seleccionado");
    $(this).addClass("seleccionado");
    $(".secciones").hide();
    $("." + pagina).slideToggle();
    $("." + secciones[4]).addClass("selected");
  });
});
