$(document).ready(()=>{
    $(".expediente-opciones .card").click(function(){
        $(".expediente-opciones > .card").removeClass("card-select");
        $(".expediente-detalle > .expediente-item").hide();
        $(this).addClass("card-select");
        var card = $(this).data("card");
        $('.'+card).slideToggle('slow');
    })
})