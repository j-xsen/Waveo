let on_time = 1;

$(".note").click(function(){
    let holder_this = $(this);
    if($(this).attr("play") === "0"){
        $(this).attr("play",1);
        $(this).html('<i class="fas fa-circle"></i>');
    } else{
        $(this).attr("play",0);
    }
});
