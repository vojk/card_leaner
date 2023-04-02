currentCard = 0
prevCard = -1
//přidá data do listu


$(document).ready(function () {
    $('#' + id_list[currentCard]).css('display', 'flex')
});

//Další karta
$('#button_next').on("click", function () {
    if (currentCard < id_list.length - 1) {
        currentCard = currentCard + 1
        prevCard = currentCard - 1

        $('#' + id_list[currentCard]).css('display', 'flex')
        $('#' + id_list[prevCard] + ' .back_card').css('display', 'none')
        $('#' + id_list[prevCard]).css('display', 'none')
        $('#' + id_list[currentCard] + ' .front_card').css('display', 'flex')

        $('#current_card').text(currentCard + 1)
    }
})

//Předchozí karta
$('#button_prev').on("click", function () {
    if (currentCard > 0) {
        $('#' + id_list[prevCard]).css('display', 'flex')
        $('#' + id_list[prevCard] + ' .front_card').css('display', 'flex')
        $('#' + id_list[currentCard]).css('display', 'none')
        $('#' + id_list[currentCard] + ' .back_card').css('display', 'none')

        console.log("Current: " + currentCard)
        console.log("Prev: " + prevCard)

        currentCard = currentCard - 1
        prevCard = currentCard - 1

        $('#current_card').text(currentCard + 1)

    }
})


//Obrací kartu
$('.button_back_card').on("click", function () {
    let _id = this.id
    _id = _id.replace("_button", "")
    if ($('#' + _id + ' .back_card').css("display") === "none") {
        $('#' + _id + ' .back_card').css("display", "flex")
        $('#' + _id + ' .front_card').css("display", "none")
        console.log("jedna")
    } else {
        $('#' + _id + ' .back_card').css("display", "none")
        $('#' + _id + ' .front_card').css("display", "flex")
        console.log("dva")
    }
})

$('body').keyup(function (e) {
    if (e.keyCode == 32) {
        $('#' + id_list[currentCard] + '_button_wrapper .button_back_card').trigger('click')
    }
})
