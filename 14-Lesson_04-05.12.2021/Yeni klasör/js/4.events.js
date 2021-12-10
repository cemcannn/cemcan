function divClicklendi(element){

element.innerHTML += " <br>merhaba bana clickledin";

}



function bodyYuklendi(){

alert("body yüklendi");

}


function mouseUzerinde(element){

element.style.backgroundColor = "red"

element.innerHTML +=  "mouse üzerinde";

}


function mouseAyrildi(element){

    element.style.backgroundColor = "blue"
    element.innerHTML +=  "mouse ayrıldı";

}

function mouseClickledi(element){

    element.style.backgroundColor = "aqua"
    element.innerHTML +=  "mouse clickledi";

}

// ----------------------------------------------------- event listener

//https://developer.mozilla.org/en-US/docs/Web/API/Element/click_event


var div1 = document. getElementById("div1");
var div2 = document. getElementById("div1");


div1.addEventListener("click", function(){ alert("div1 clicklendi")})
div2.addEventListener("click", function(){ alert("div2 clicklendi")})


var div3 = document. getElementById("div3");
var div4 = document. getElementById("div4");

div3.addEventListener("click", function(){ divClicklendi(this);})
div4.addEventListener("click", function(){ divClicklendi(this);})



function divClicklendi(element){

    alert(element.id + " clicklendi");

}





