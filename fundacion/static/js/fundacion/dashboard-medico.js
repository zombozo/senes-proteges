$(document).ready(function(){
    $(".nav-top span").click(function(){
        pagina = $(this).data("pagina");
        $(".pagina-citas").hide();
        $(".nav-top span").removeClass("seleccionado-top");
        $(this).addClass("seleccionado-top");
        $("."+pagina).slideToggle("slow");
    })
})