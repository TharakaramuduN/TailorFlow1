const mobileNav = document.querySelector('.mobile-nav')

const body = document.querySelector('body')

function toggleMenu(event){
    event.stopPropagation();
    body.classList.toggle('overflow-hidden')
    mobileNav.classList.toggle('translate-x-[100%]')
    console.log('clicked this buton')
}

function closeMenu(event) {
    event.stopPropagation();
    if (!event.target.closest('.mobile-nav')) {
        mobileNav.classList.add('translate-x-[100%]');

    }
    body.classList.toggle('overflow-hidden')
}

document.addEventListener('click', closeMenu);