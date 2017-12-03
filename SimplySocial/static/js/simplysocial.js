
// When the user clicks on <div>, open the popup
function myFunction() {
    var popup = document.getElementById("myPopup");
    popup.classList.toggle("show");
}

$('li.dropdown').hover(function() {
  $(this).find('.dropdown-menu').stop(true, true).delay(200).fadeIn(500);
}, function() {
  $(this).find('.dropdown-menu').stop(true, true).delay(200).fadeOut(500);
});


function videoImage(){
  var image = document.getElementById("image");
  var video = document.getElementById("linkBox");
  image.disabled= false;
  video.disabled= false;

  if (image.value.length != 0)
  {
    video.disabled=true;
  }

  else if (video.value.length != 0) {
    image.disabled=true;
  }

}
