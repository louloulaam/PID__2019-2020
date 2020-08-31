$(document).ready(function () {
    let url = $("#shows").attr("data-url");    
    $('#shows').autocomplete({
        source: url,
        minLenght: 2
    });
});