$(()=>{
    $("#info-b").click(function(){
        if ($("#info").css("display") == "none"){
            $(this).addClass("section-active");
            $("#change-b").removeClass("section-active");
            $("#change").fadeOut(200, ()=>{
                $("#info").fadeIn(200);
            });
        }
    });
    $("#change-b").click(function(){
        if ($("#change").css("display") == "none"){
            $(this).addClass("section-active");
            $("#info-b").removeClass("section-active");
            $("#info").fadeOut(200, ()=>{
                $("#change").fadeIn(200);
            });
        }
    })
})

function submit(){
    session = $("#session").val();
    console.log(session)
    if (session){
        $.get("/changeSession", {session: session}, (res)=>{
            alert(res)
        })
    }
}

$(()=>{
    h = window.innerHeight - 250;
    $("#info").css("height", h+"px");  
})