$(document).ready(() => {
    $(".ver-especialidades").click(function() {
        id = $(this).data("id");
        $("." + id).slideToggle("slow");
    })
})