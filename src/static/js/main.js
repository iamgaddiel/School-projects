document.querySelectorAll('.info-desc').forEach( description => {
    description.innerHTML = `${description.innerHTML.substring(0, 250)} ....`
})