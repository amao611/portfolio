window.alert("Welcome to my webpage!");

function bigcaticon(x) {
 x.style.height = "500px";
 x.style.width = "500px";
}

function normalcaticon(x) {
 x.style.height = "400px";
 x.style.width = "400px";
}

function openCity(evt, cityName) {
 var i, tabcontent, tablinks;
 tabcontent = document.getElementsByClassName("tabcontent");
 for (i = 0; i < tabcontent.length; i++) {
   tabcontent[i].style.display = "none";
 }
 tablinks = document.getElementsByClassName("tablinks");
 for (i = 0; i < tablinks.length; i++) {
   tablinks[i].className = tablinks[i].className.replace(" active", "");
 }
 document.getElementById(cityName).style.display = "block";
 evt.currentTarget.className += " active";
}

var slideIndex = 1;
showSlides(slideIndex);

function plusSlides(n) {
 showSlides(slideIndex += n);
}

function currentSlide(n) {
 showSlides(slideIndex = n);
}

function showSlides(n) {
 var i;
 var slides = document.getElementsByClassName("mySlides");
 var dots = document.getElementsByClassName("dot");
 if (n > slides.length) {
   slideIndex = 1
 }
 if (n < 1) {
   slideIndex = slides.length
 }
 for (i = 0; i < slides.length; i++) {
   slides[i].style.display = "none";
 }
 for (i = 0; i < dots.length; i++) {
   dots[i].className = dots[i].className.replace(" active", "");
 }
 slides[slideIndex - 1].style.display = "block";
 dots[slideIndex - 1].className += " active";
}

function funfactfunction() {
 document.getElementById("funfact").innerHTML = "I love to travel, and I have traveled in Asia, Europe, and the Americas. I have yet to go to Africa and Antarctica.";
}
