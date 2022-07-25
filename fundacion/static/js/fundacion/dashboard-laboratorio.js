$(document).ready(function(){
    $(".nav-top span").click(function(){
        pagina = $(this).data("pagina");
        $(".nav-top span").removeClass("seleccionado-top");
        $(this).addClass("seleccionado-top");
        $(".detalle-citas").hide();
        $("."+pagina).slideToggle();
    })
})