var timelineBar = document.getElementsByClassName('timeline-bar')[0]

var timelineLastBox = document.getElementsByClassName('content')[document.getElementsByClassName('content').length - 1]

FixTimelineBarMargin()

window.onresize = function(){
    FixTimelineBarMargin()
}

function FixTimelineBarMargin() {
    timelineBar.style.marginBottom = `${timelineLastBox.clientHeight}px`
}