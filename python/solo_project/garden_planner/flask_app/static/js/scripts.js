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


    // background video playing

// Get the video
var video = document.getElementById("myVideo");
video.playbackRate = 0.3;
// Get the button
var btn = document.getElementById("myBtn");

// Pause and play the video, and change the button text
function myFunction() {
  if (video.paused) {
    video.play();
    btn.innerHTML = "Pause";
  } else {
    video.pause();
    btn.innerHTML = "Play";
  }
}

