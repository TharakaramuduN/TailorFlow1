async function filterProducts(){
    const searchQuery = document.querySelector('.search-input').value
    const gender = document.getElementById('gender').value
    const category = document.getElementById('category').value
    let response = await fetch(`/filter-products/?search=${searchQuery}&gender=${gender}&category=${category}`)
    if(!response.ok){
        throw Error('not found')
    }
    const products = await response.json()
    console.log(products)
    const productsContainer = document.querySelector('.products-container')
    const notFoundElement = document.querySelector('.not-found')
    productsContainer.innerHTML = ''
    if(products.products.length > 0){
        notFoundElement.innerHTML = ''
        if(notFoundElement.classList.contains('min-h-[50vh]')) notFoundElement.classList.remove('min-h-[50vh]')
        products['products'].forEach(product=>{
            console.log(`/media/${product.image}`)
            const divElement = document.createElement('div')
            divElement.classList.add('product-card','rounded','shadow-lg','h-96','justify-center','relative')
            divElement.addEventListener('click',toggleSelected)
            divElement.innerHTML = `
            <div class="product-img h-[60%] sm:h-[70%]">
                <img loading="lazy" class="w-full h-full sm:p-5 p-3 rounded-3xl" src="/media/${product.image }" alt="${product.title }">
            </div>
            <div class="px-6 py-4">
                <div class="font-bold text-sm mb-2">${truncateWords(product.title,2)}</div>
                <p class="text-gray-700 text-sm">${truncateWords(product.description,2)}</p>
                <p class="text-gray-800 text-base font-semibold mt-2">₹${ product.price }</p>
            </div>
            <input  name="selected_products" type="checkbox" class="selected_products absolute top-0 left-0 h-full w-full z-10 opacity-0 hover:cursor-pointer" value="${product.id}">
            <div class="selected-layer hidden rounded-md absolute h-full w-full left-0 top-0 items-end justify-end">
                <div class=" flex items-center justify-center w-full h-full"><img class=" h-32 w-32 opacity-70" src='/static/icons/check.png' alt=""></div>
            </div>
                    `
                    productsContainer.appendChild(divElement)
                })
            selectedProducts()
        }
    else{
        notFoundElement.classList.add('min-h-[50vh]')
        notFoundElement.innerHTML = '<h1 class=" text-xl sm:text-3xl md:text-4xl lg:text-6xl  font-medium text-gray-500">No Results Found</h1>'
    }}
function truncateWords(text, limit) {
    var words = text.split(' ');
    if (words.length > limit) {
        return words.slice(0, limit).join(' ') + '...';
    } else {
        return text;
    }
}

function toggleSelected(event){
    const productCard = event.target.closest('.product-card')
    const inputElement = productCard.querySelector('.selected_products')
    const selectedLayer = productCard.querySelector('.selected-layer')
    const selectedProducts = JSON.parse(localStorage.getItem('tailorFlow_selected_products'))
    if(inputElement.checked){
        selectedLayer.classList.remove('hidden')
        selectedProducts.push(event.target.value)
        updateSelectedProductsContainer(selectedProducts)
    }
    else{
        selectedLayer.classList.add('hidden')
        const indexToRemove = selectedProducts.indexOf(event.target.value)
        selectedProducts.splice(indexToRemove,1)
        updateSelectedProductsContainer(selectedProducts)
    }
    localStorage.setItem('tailorFlow_selected_products',JSON.stringify(selectedProducts))
}


function selectedProducts(){

    console.log('first')
    let existingProducts = localStorage.getItem('tailorFlow_selected_products')
    if(existingProducts){
        existingProducts = JSON.parse(existingProducts);
        const products = document.querySelectorAll('.selected_products')
        products.forEach(product=>{
            if(existingProducts.includes(product.value)){
                product.checked = true
                const productCard = product.closest('.product-card')
                const selectedLayer = productCard.querySelector('.selected-layer')
                selectedLayer.classList.remove('hidden')
            }
        })
    }
    else{
        existingProducts = []
    }
    localStorage.setItem('tailorFlow_selected_products',JSON.stringify(existingProducts))
    return existingProducts
}



const checkoutBtn = document.querySelector('.checkout-btn')
checkoutBtn.addEventListener('click',(event)=>{
    const products = selectedProducts()
    if(products.length<1){
        alert('Add atleast one Product.')
        event.preventDefault()
    }
})

document.addEventListener('DOMContentLoaded',()=>{
    selectedProducts()
})

function updateSelectedProductsContainer(selectedProducts) {
    const selectedProductsContainer = document.querySelector('.selected-products-container');
    selectedProductsContainer.innerHTML = ''; // Clear previous content

    selectedProducts.forEach(productId => {
        console.log(productId)
        const inputElement = document.createElement('input')
        inputElement.value = productId
        inputElement.checked = true
        inputElement.name = 'selected_products'
        selectedProductsContainer.appendChild(inputElement)
    });
}