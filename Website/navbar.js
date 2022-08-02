window.onscroll = function() {WhenScroll()};
      
var navbar = document.getElementById("navbar");
var sticky = navbar.offsetTop;
function WhenScroll() {
  if (window.pageYOffset >= sticky) {
    navbar.classList.add("sticky")

  } else {
    navbar.classList.remove("sticky");
  }
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
      
      document.getElementById("navbar").style.backgroundColor = "#0d121b";
    } else {
    
      document.getElementById("navbar").style.backgroundColor = "transparent";
    }
}