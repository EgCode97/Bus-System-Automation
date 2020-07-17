var cards = document.getElementsByClassName('card')

window.onresize = fixCardsHeigth

fixCardsHeigth()


function fixCardsHeigth(){
    let maxHeight = 0
    for (let card of cards){
        card.style.height = 'fit-content'
        const cardHeigth = card.clientHeight
        maxHeight = cardHeigth > maxHeight ? cardHeigth : maxHeight 
    }
    console.log(`LA ALTURA MAXIMA ES ${maxHeight}`)
    for (let card of cards){
        card.style.height = `${maxHeight}px`
    }
}