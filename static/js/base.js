function toggleMenu(event){
    const mobileNavContainer = document.querySelector('.mobile-nav-container')
    mobileNavContainer.classList.toggle('translate-x-[100%]')
    document.body.classList.toggle('overflow-hidden')
    event.stopPropagation();
}

document.onclick = (event)=>{
    const navContent = document.getElementById('nav')
    const mobileNavContainer = document.querySelector('.mobile-nav-container')
    if(!navContent.contains(event.target)){
        mobileNavContainer.classList.add('translate-x-[100%]')
        document.body.classList.remove('overflow-hidden')
        event.stopPropagation();
    }
}