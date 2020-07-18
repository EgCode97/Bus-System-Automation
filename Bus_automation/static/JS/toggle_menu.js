var openToggleBtn = document.getElementById("open-menu-btn");

var closeToggleBtn = document.getElementById("close-menu-btn");

var menuToggle = document.getElementById('nav-menu');

var courtain = document.getElementById('courtain');

var menuItems = menuToggle.children;

var header = document.getElementsByTagName('header')[0]

window.onresize = fixNavBar;

// open and close the menu to avoid the buttons showing at the same time on mobile version

window.onload = function(){
    if (window.innerWidth <= 600 ){
        openMenu()
        closeMenu()
    }
}
/*
window.onscroll = function(){
    header.style.top = `${window.pageYOffset}px`
}*/

function openMenu(){
    openToggleBtn.style.height = 0;
    openToggleBtn.style.opacity = 0;
    openToggleBtn.style.zIndex = 0;

    closeToggleBtn.style.height = '40px';
    closeToggleBtn.style.opacity = 1;
    closeToggleBtn.style.zIndex = 1;

    menuToggle.style.width = "200px";
    courtain.style.width = "100%";

    console.log(`La altura total es ${document.getElementsByTagName('body')[0].clientHeight}`)
}


function closeMenu(){
    closeToggleBtn.style.height = 0;
    closeToggleBtn.style.opacity = 0;
    closeToggleBtn.style.zIndex = 0;

    openToggleBtn.style.height = '40px';
    openToggleBtn.style.opacity = 1;
    openToggleBtn.style.zIndex = 1;

    menuToggle.style.width = 0;
    
    courtain.style.width = 0;


}

function fixNavBar(){
    if (window.screen.width > 768){
        menuToggle.style.width = "100%";
    }
    else{
        closeMenu();
    }
}