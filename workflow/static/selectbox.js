$("#btnLeft").click(function () {
    var selectedItem = $("#rightValues option:selected");
    $("#leftValues").append(selectedItem);
});

$("#btnRight").click(function () {
    var selectedItem = $("#leftValues option:selected");
    $("#rightValues").append(selectedItem);
});

$("#rightValues").change(function () {
    var selectedItem = $("#rightValues option:selected");
});

$("#btnLeft2").click(function () {
    var selectedItem = $("#rightValues2 option:selected");
    $("#leftValues2").append(selectedItem);
});

$("#btnRight2").click(function () {
    var selectedItem = $("#leftValues2 option:selected");
    $("#rightValues2").append(selectedItem);
});

$("#rightValues2").change(function () {
    var selectedItem = $("#rightValues2 option:selected");
});