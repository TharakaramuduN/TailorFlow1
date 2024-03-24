async function filterProducts(){
    const searchQuery = document.querySelector('.search-input').value
    const gender = document.getElementById('gender').value
    const category = document.getElementById('category').value
    let response = await fetch(`/api/filter-products/?search=${searchQuery}&gender=${gender}&category=${category}`)
    if(!response.ok){
        throw Error('not found')
    }
    const products = await response.json()
    console.log(products)
    const productsContainer = document.querySelector('.products-container')
    productsContainer.innerHTML = ''
    const notFoundElement = document.querySelector('.not-found')
    if(products['products'].length > 0){
        if(notFoundElement.classList.contains('min-h-[50vh]')) notFoundElement.classList.remove('min-h-[50vh]')
        notFoundElement.innerHTML = ''
        products['products'].forEach(product=>{
            console.log(`/media/${product.image}`)
            const divElement = document.createElement('div')
            divElement.classList.add('product-card','rounded','shadow-lg','h-96','justify-center')
            divElement.innerHTML = `
                <div class="product-img h-[60%] sm:h-[70%]">
                    <img loading="lazy" class="w-full h-full sm:p-5 p-3 rounded-3xl" src="/media/${product.image }" alt="${product.title }">
                </div>
                <div class="px-6 py-4">
                    <div class="font-bold text-sm mb-2">${truncateWords(product.title,2)}</div>
                    <p class="text-gray-700 text-sm">${truncateWords(product.description,2)}</p>
                    <p class="text-gray-800 text-base font-semibold mt-2">₹${ product.price }</p>
                </div>
            `
        productsContainer.appendChild(divElement)
    })}
    else{
        notFoundElement.classList.add('min-h-[50vh]')
        notFoundElement.innerHTML = '<h1 class=" text-xl sm:text-3xl md:text-4xl lg:text-6xl  font-medium text-gray-500">No Results Found</h1>'
    }
}

function truncateWords(text, limit) {
    var words = text.split(' ');
    if (words.length > limit) {
        return words.slice(0, limit).join(' ') + '...';
    } else {
        return text;
    }
}

document.getElementById('Products').classList.add('text-yellow-300')