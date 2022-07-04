$(document).ready(()=>{
    var pagina_activa = $(".pagina-activa").data("pagina");
    $('.aside-recepcion a').removeClass("selected");

    $('.'+pagina_activa).addClass("selected");
})