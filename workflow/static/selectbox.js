function swapNodes(a, b) {
    var aparent = a.parentNode;
    var asibling = a.nextSibling === b ? a : a.nextSibling;
    b.parentNode.insertBefore(a, b);
    aparent.insertBefore(b, asibling);
}

$("#btnLeft").click(function () {
    var selectedItem = $("#rightValues option:selected");
    $("#leftValues").append(selectedItem);
});

$("#btnRight").click(function () {
    var selectedItem = $("#leftValues option:selected");
    $("#rightValues").append(selectedItem);
});

$("#btnUp").click(function(){
    var selectedItem = $("#rightValues option:selected");
    var previousItem = $(selectedItem[0]).prev();
    swapNodes(selectedItem[0],previousItem[0]);
})

$("#btnDown").click(function(){
    var selectedItem = $("#rightValues option:selected");
    var NextItem = $(selectedItem[0]).next();
    swapNodes(selectedItem[0],NextItem[0]);
})

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

$("#btnUp2").click(function(){
    var selectedItem = $("#rightValues2 option:selected");
    var previousItem = $(selectedItem[0]).prev();
    swapNodes(selectedItem[0],previousItem[0]);
})

$("#btnDown2").click(function(){
    var selectedItem = $("#rightValues2 option:selected");
    var NextItem = $(selectedItem[0]).next();
    swapNodes(selectedItem[0],NextItem[0]);
})


$('#submit_button').click(function(){
    $('#rightValues option').prop("selected",true);
    $('#rightValues2 option').prop("selected",true);
    $('#real_submit').trigger('click');
})