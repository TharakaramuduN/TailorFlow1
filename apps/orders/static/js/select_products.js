
async function filterProducts(){
    const searchQuery = document.querySelector('.search-input').value
    const gender = document.getElementById('gender').value
    const category = document.getElementById('category').value
    console.log(`/filter-products/?search=${searchQuery}&gender=${gender}&category=${category}`)
    let response = await fetch(`/filter-products/?search=${searchQuery}&gender=${gender}&category=${category}`)
    if(!response.ok){
        throw Error('not found')
    }
    const products = await response.json()
    console.log(products)
    const productsContainer = document.querySelector('.products-container')
    productsContainer.innerHTML = ''
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
        <input name="selected_products" type="checkbox" class=" absolute top-0 left-0 h-full w-full z-10 opacity-0" value="${product.id}">
        <div class="selected-layer hidden rounded-md absolute h-full w-full left-0 top-0 items-end justify-end bg-black opacity-50">
            <h1 class=" text-6xl text-white font-extrabold pr-3 pb-3"><i class="fa-solid fa-check"></i></h1>
        </div>
                `
                productsContainer.appendChild(divElement)
            })
        }
        
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
    console.log(productCard)
    const selectedLayer = productCard.querySelector('.selected-layer')
    if (selectedLayer.classList.contains('hidden')){
        selectedLayer.classList.remove('hidden')
        selectedLayer.classList.add('flex')
    }
    else{
        selectedLayer.classList.remove('flex')
        selectedLayer.classList.add('hidden')

    }
}


function filterProducts1(){
    let response = fetch("https://fakestoreapi.com/products/category/men's clothing")
    .then(res=>res.json())
    .then(json=>console.log(json))
    
}