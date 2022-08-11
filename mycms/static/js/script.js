var inputs = document.getElementsByTagName("input");
var button = document.getElementById("button");
// // Disable the button dynamically using javascript
// button.disabled = "disabled";


function enableSubmit() {
  let isValid = true;
  for (var i = 0; i < inputs.length; i++){
    let changedInput = inputs[i];
    if (changedInput.value.trim() === "" || changedInput.value === null){
    isValid = false;
    break;
    }
  }
  button.disabled = !isValid;
}

if (location.pathname == "/index.html" || location.pathname == "/about.html" || location.pathname == "/support.html"){
    const links = document.querySelector(".links")
    const menuBtn = document.querySelector(".menu-bar")
    const navbar = document.querySelector(".navbar")

    const toggleNav = () => {
      menuBtn.addEventListener("click", (e) => {
        e.preventDefault()
        links.classList.toggle("show-nav")
        navbar.classList.toggle("toggle-background")
      })
    }

toggleNav()
}


if(
  location.pathname == "/allTemplates.html" || location.pathname == "/blog.html" || 
  location.pathname =="/landingPage.html" || location.pathname == "/portfolio.html"
  ){

  const sideBarButton = document.querySelectorAll(".toggle-btn")
  const sideMenu = document.querySelectorAll(".sideMenu")
  const textLink = document.querySelectorAll(".link-text")
  const secondLogo = document.querySelectorAll(".second-logo")
    
    const toggleSideBar = () => {


        sideMenu.forEach((eachSideMenu, index) => {

            const eachBtn = sideBarButton[index]
            const eachText = textLink[index]
            const eachLogo = secondLogo[index]

            eachBtn.addEventListener("click", (e) => {
            e.preventDefault()
    
            eachSideMenu.classList.toggle("toggle-width")
            textLink[0].classList.toggle("show-text")
            textLink[1].classList.toggle("show-text")
            textLink[2].classList.toggle("show-text")
            textLink[3].classList.toggle("show-text") 
            textLink[4].classList.toggle("show-text")
            eachLogo.classList.toggle("show-optimus")
        })
        })
      
    }
    toggleSideBar()
}


