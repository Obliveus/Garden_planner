function myFunction() {
    var x = document.getElementById ("pwShow");
    if (x.type == "password") {
    x.type = "text";
    } else {
    x.type = "password";
    }
    }
function confirmPw() {
    var x = document.getElementById ("cfShow");
    if (x.type == "password") {
    x.type = "text";
    } else {
    x.type = "password";
    }
    }





    $(document).ready(function () {
        $('#target').flipster(); 
    });