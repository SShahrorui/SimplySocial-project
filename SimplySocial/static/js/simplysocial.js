
// When the user clicks on <div>, open the popup
function show() {
    var x = document.getElementById("linkBox");
    if (x.style.display === "none") {
        x.style.display = "inline-block";
      } else {
        x.style.display = "none";
      }
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
