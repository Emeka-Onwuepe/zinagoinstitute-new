const openbutton = document.getElementById('open')
const closebutton = document.getElementById('close')
const mobile_nav = document.getElementById('mobile_nav')


closebutton.style.display = 'none'
mobile_nav.classList.add('hidden')

openbutton.addEventListener('click', () => {
    toggle('open')
})
closebutton.addEventListener('click', () => {
    toggle('close')
})

const toggle = (target) => {
if(target== 'open'){
    openbutton.style.display = 'none'
    closebutton.style.display = 'block'
}else{
    closebutton.style.display = 'none'
    openbutton.style.display = 'block'
}
    mobile_nav.classList.toggle('hidden')


}


