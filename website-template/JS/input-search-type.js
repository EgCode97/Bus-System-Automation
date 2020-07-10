var searchOptionBtns = Array.from(document.getElementsByClassName('search-option'))
var dropdownBtn = document.getElementById('dropdown-btn')

var dropdownLists = Array.from( document.getElementsByClassName('search-list') )

var menuIsOpen = false

var listsHeight = [0,0,0]

for (let i = 0; i < dropdownLists.length; i++) {
    const height = dropdownLists[i].clientHeight
    dropdownLists[i].style.height = `${height}px`
    listsHeight[i] = `${height}px`
}
console.log(listsHeight)
/*
dropdownLists.forEach(list =>{
    
    list.style.height = `${list.clientHeight}px`
})

*/

checkOneOption(document.getElementById('Route'))



function checkOneOption(option){
    closeDropDown()
    searchOptionBtns.forEach(element => {
        if (option == element){
            console.log(`OPCION CORRECTA ${element.getAttribute('value')}`)
            element.className += ' active-hex'
            dropdownBtn.children[1].innerHTML = element.getAttribute('value')
            dropdownBtn.setAttribute('value', element.getAttribute('value'))
        }
        else{
            element.className = element.className.replace(' active-hex', '')
        }
    }
    
    );
}


function showDropdown(){
    console.log(dropdownBtn.getAttribute('value'))
    let index = 0;

    if (! menuIsOpen) {
        dropdownLists.forEach(element => {
            if ( element.getAttribute('value') == dropdownBtn.getAttribute('value') ){
                element.className = element.className.replace(' hidden', "")
                element.style.height = listsHeight[index]
            } else{
                if (! element.className.includes("hidden")){
                    element.className += " hidden";
                    element.style.height = 0
                }
            }
            index++
        });
        menuIsOpen = true

    } else { // CLOSE DROPDOWN
        closeDropDown()
    }
}


function closeDropDown(){
    dropdownLists.forEach(element => {
        if (! element.className.includes("hidden")){
            element.className += " hidden";
            element.style.height = 0
        }
    });
    menuIsOpen = false
}
