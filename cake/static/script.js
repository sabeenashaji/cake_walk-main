const menuIcon = document.getElementById('menuicon')
const closeIcon = document.getElementById('closeicon')
const slideMenu = document.getElementById('slidemenu')

menuIcon.addEventListener('click', ()=> {
   slideMenu.classList.toggle('show')
})

closeIcon.addEventListener('click', ()=> {
   slideMenu.classList.remove('show')
})



