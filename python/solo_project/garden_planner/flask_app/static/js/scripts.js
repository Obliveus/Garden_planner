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


    //upload file garden layout img
const file = document.querySelector('#file');
    file.addEventListener('change', (e) => {
    // Get the selected file
    const [file] = e.target.files;
    // Get the file name and size
    const { name: fileName, size } = file;
    // Convert size in bytes to kilo bytes
    const fileSize = (size / 1000).toFixed(2);
    // Set the text content
    const fileNameAndSize = `${fileName} - ${fileSize}KB`;
    document.querySelector('.file-name').textContent = fileNameAndSize;
    });

        
var loadFile = function(event) {
    var output = document.getElementById('output');
    output.value = URL.createObjectURL(event.target.files[0]);
    output.onload = function() {
      URL.revokeObjectURL(output.value) // free memory
  }
};


var input = document.getElementById( 'file' );
var infoArea = document.getElementById( 'selectFile' );
input.addEventListener( 'change', showFileName );
function showFileName( event ) {
  var input = event.srcElement;
  var fileName = input.files[0].name;
  infoArea.value = fileName;
}
