function validateForm(formName) {
    let fname = document.forms[formName]["fname"].value;
    if (fname == "") {
        alert("Name must be filled out");
        return false;
    else:
        alert("Form Doğrulandı")

    }

    function changeForm2() {
        let fname = document.forms["form1"]["fname"].value;

        let fname2 = document.forms["form2"]["fname"].value;

        fname2.value = fname


    }
}