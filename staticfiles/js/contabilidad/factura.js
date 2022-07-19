$(document).ready(function(){
    $(".nav-facturas span").click(function(){
        pagina = $(this).data("pagina");
        $(".pagina").hide();
        $(".nav-facturas span").removeClass("seleccionado");
        $(this).addClass("seleccionado");
        $("."+pagina).slideToggle();
    })
})