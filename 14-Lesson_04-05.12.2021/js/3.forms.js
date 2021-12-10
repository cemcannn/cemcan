function validateForm(formName){


    let fname = document.forms[formName]["fname"].value;
    if (fname == "") {
      alert("isim alanı boş olamaz");
      return false;
    }
    else
    {

        alert(formName + " formu doğrulandı")

    }

}


function changeForm2() {

    let fname = document.forms["form1"]["fname"].value;

    let fname2 = document.forms["form2"]["fname"];

    fname2.value = fname;
}


var fname = document.getElementById("fname");

fname.style.backgroundColor="#999999"
fname.style.border="1px solid blue";
fname.style.borderRadius = "4px";
fname.style.width = "100px";




