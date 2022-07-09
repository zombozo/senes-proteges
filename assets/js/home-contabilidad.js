$(document).ready(function(){


})

function calcular_total(cantidad){
    var total = Number($('.total').text())
    
    console.log(total)
    $('.total').text(total+cantidad)

}