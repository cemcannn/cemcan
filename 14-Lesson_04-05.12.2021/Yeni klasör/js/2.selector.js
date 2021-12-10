var allDiv = document.getElementsByTagName("div")

for (div in allDiv) {

    allDiv[div].innerHTML = "merhaba div"
}


var allDivClass = document.getElementsByClassName("divClass")


//https://www.w3schools.com/jsref/dom_obj_style.asp
for (var index=0; index < 3; index++) {

    allDivClass[index].style.backgroundColor = "#0000dd";
    allDivClass[index].style.color = "red";
}


var div1 = document.getElementById("div1");

div1.innerHTML += "<br>" +  div1.id;
div1.style.textAlign = "center"
div1.style.fontSize = "20px";


var div2 = document.getElementById("div2");

div2.innerHTML += "<br>" +  div2.id;
div2.style.textAlign = "center"
div2.style.fontSize = "20px";
div2.style.backgroundColor = "white"
