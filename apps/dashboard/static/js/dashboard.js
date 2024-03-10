async function filterOrderItems(event){
    const filterBtns = document.querySelectorAll('.filter-btn')
    filterBy = event.target.id
    filterBtns.forEach(btn=>{
        if(btn.classList.contains('bg-gray-800')) btn.classList.remove('bg-gray-800','text-white')
    })
    event.target.classList.add('bg-gray-800','text-white')
    let url;
    if(filterBy==='urgent'){
        url = `/filter-order-items/?urgent=true`
    }else{
        url = `/filter-order-items/?filter=${filterBy}`
    }
    let response = await fetch(url)
    if(!response.ok){
        throw Error('Page not found')
    }
    const data = await response.json()
    const productsContainerHeader = document.querySelector('.products-container-header')
    const productsContainer = document.querySelector('.products-container')
    productsContainer.innerHTML = ''
    if(filterBy!=='Stitched'){
        productsContainerHeader.innerHTML=`<div class="grid grid-cols-10  p-2 sm:px-3  bg-gray-800 text-white rounded-tr-md rounded-tl-md items-center text-sm sm:text-lg">
            <p class="  col-span-3">Name</p>
            <p class="col-span-4">Product Title</p>
            <p class="  col-span-2">Req. Date</p>
            <div></div>
        </div>`
        data.order_items.forEach((item) => {
            const divElement = document.createElement('div')
            divElement.classList.add('product-card','grid', 'grid-cols-10',  'p-2', 'sm:px-3' , 'even:bg-gray-200', 'odd:bg-gray-50', 'gap-2', 'text-sm', 'sm:text-base','items-center')
            divElement.innerHTML = `
                <p class="  col-span-3">${item.customer_name}</p>
                <p class=" col-span-4">${truncateWords(item.title,2)}</p>
                <p class="  col-span-2">${item.requested_date}</p>
                <div id="${item.id}" class="check-btn-${item.id} hover:cursor-pointer"  onclick="updateStatus(event)" >
                    <i id="${item.id}" class="fa-solid fa-check text-green-600"></i>
                </div>
            `
            productsContainer.appendChild(divElement)
        })}
        else{
            productsContainerHeader.innerHTML = `<div class="grid grid-cols-10  p-2 sm:px-3  bg-gray-800 text-white rounded-tr-md rounded-tl-md items-center text-sm sm:text-lg">
                <p class="  col-span-4">Name</p>
                <p class="col-span-4">Product Title</p>
                <p class="  col-span-2">Stitched Date</p>
            </div>`
            data.order_items.forEach((item) => {
                const divElement = document.createElement('div')
                divElement.classList.add('product-card','grid', 'grid-cols-10',  'p-2', 'sm:px-3' , 'even:bg-gray-200', 'odd:bg-gray-50', 'gap-2', 'text-sm', 'sm:text-base','items-center')
                divElement.innerHTML = `
                    <p class="  col-span-4">${item.customer_name}</p>
                    <p class=" col-span-4">${truncateWords(item.title,2)}</p>
                    <p class="  col-span-2">${item.stitched_on}</p>
                `
                productsContainer.appendChild(divElement)
            })}
            
    }

async function updateStatus(event){
    const itemId = event.target.id
    const productsContainer = document.querySelector('.products-container')
    const productCard = event.target.closest('.product-card')
    const response = await fetch(`/update-status/${itemId}`)
    if(!response.ok){
        throw Error('Page Not found')
    }
    productsContainer.removeChild(productCard)
}

function truncateWords(text, limit) {
    var words = text.split(' ');
    if (words.length > limit) {
        return words.slice(0, limit).join(' ') + '...';
    } else {
        return text;
    }
}