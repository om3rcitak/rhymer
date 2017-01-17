/**
 * Created by PhpStorm.
 * User: omer
 * Date: 1/17/2017
 * Time: 6:14 PM
 */

$(document).ready(function () {

    // get wordlist
    var words;
    $.getJSON("wordlist.json").done(function (data) {
        words = data;
    });

    $('#target').animateNumber({
        number: 57021,
        color: 'green',
        'font-size': '30px',
        easing: 'easeInQuad',
    }, 5000);

    // click button event
    $('button').click(function () {
        rhymer(words);
    });

    // press enter event
    $('input').keypress(function (event) {
        if (event.keyCode == 13)
            rhymer(words);
    });

    // clear button
    $('.results a').click(function () {
        $(".results ol").empty();
    });

});

function rhymer(words) {

    var word = $('#word').val();
    var depth = $('#depth').val();

    // var share_button_top = new Share(".share-button-top", {
    //     title: "rhymer | " + word + " kelimesi ile kafiyeli kelimeler",
    //     description: "rhymer | " + word + " kelimesi ile kafiyeli kelimeler",
    // });

    if (word == '') {
        alert('Kelime boş olamaz');
        return 0;
    }

    var i, dest;
    for (i = 0; i <= 57020; i++) {
        dest = levenshtein(word, words[i]);
        if (dest <= depth) {
            $(".results ol").append('<li>' + words[i] + '</li>');
        }
    }

    if ($('.results ol li').length < 1)
        alert('eşleşme bulunamadı');
    else
        $(".results").show();
}