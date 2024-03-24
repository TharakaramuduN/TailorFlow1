const filterBtns = document.querySelectorAll('.filter-btn')
filterBtns.forEach(btn=>{
    btn.addEventListener('click',(event)=>{
        filterBtns.forEach(x=>x.classList.remove('bg-gray-800','text-white','selected-status'))
        event.target.classList.add('bg-gray-800','text-white','selected-status')
    })
})
async function filterOrderItems(filterBy){
    let url;
    if(filterBy==='urgent'){
        url = `/api/filter-order-items/?urgent=true`
    }else{
        url = `/api/filter-order-items/?filter=${filterBy}`
    }
    let response = await fetch(url)
    if(!response.ok){
        throw Error('Page not found')
    }
    const data = await response.json()
    let itemsCountElement = document.querySelector(`.${filterBy}-count`)
    itemsCountElement.innerText = data.order_items.length
    const productsContainerHeader = document.querySelector('.products-container-header')
    const productsContainer = document.querySelector('.products-container')
    productsContainer.innerHTML = ''
    productsContainerHeader.innerHTML = ''
    if(data.order_items.length > 0){
        if(filterBy!=='Stitched'){
            productsContainerHeader.innerHTML=`<div class="grid grid-cols-10  p-2 sm:px-3  bg-gray-800 text-white rounded-tr-md rounded-tl-md items-center text-sm sm:text-lg">
            <p class="  col-span-3">Name</p>
            <p class="col-span-4">Product Title</p>
            <p class="  col-span-2">Req. Date</p>
            <div></div>
            </div>`
            data.order_items.forEach((item) => {
                const dateStr = `${item.requested_date}`;
                const date = new Date(dateStr);
                const options = { month: 'short', day: 'numeric' };
                const requested_date = date.toLocaleDateString('en-US', options);
                const divElement = document.createElement('div')
                divElement.classList.add('product-card','grid', 'grid-cols-10',  'p-2', 'sm:px-3' , 'even:bg-gray-200', 'odd:bg-gray-50', 'gap-2', 'text-sm', 'sm:text-base','items-center')
                divElement.innerHTML = `
                    <p class="  col-span-3">${item.customer_name}</p>
                    <p class=" col-span-4">${truncateWords(item.title,2)}</p>
                    <p class="  col-span-2">${requested_date}</p>
                    <div id="${item.id}" class="check-btn-${item.id} hover:cursor-pointer"  onclick="updateStatus(event)" >
                        <img class=" pointer-events-none  h-7 sm:h-7 w-7 sm:w-7" src="/static/icons/checked.png" alt="stitched">
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
                    const dateStr = `${item.stitched_on}`;
                    const date = new Date(dateStr);
                    const options = { month: 'short', day: 'numeric' };
                    const stitched_date = date.toLocaleDateString('en-US', options);
                    const divElement = document.createElement('div')
                    divElement.classList.add('product-card','grid', 'grid-cols-10',  'p-2', 'sm:px-3' , 'even:bg-gray-200', 'odd:bg-gray-50', 'gap-2', 'text-sm', 'sm:text-base','items-center')
                    divElement.innerHTML = `
                        <p class="  col-span-4">${item.customer_name}</p>
                        <p class=" col-span-4">${truncateWords(item.title,2)}</p>
                        <p class="  col-span-2">${stitched_date}</p>
                    `
                    productsContainer.appendChild(divElement)
                })}
    }else{
        productsContainer.innerHTML = `<div class="no-items h-full w-full flex items-center justify-center">
                                            <h1 class=' text-3xl text-gray-600 font-medium'>No Items</h1>
                                        </div>`
    }
    }

async function updateStatus(event){
    const selectedStatusBtn = document.querySelector('.selected-status')
    const itemId = event.target.id
    const response = await fetch(`/api/update-status/${itemId}`)
    if(!response.ok){
        throw Error('Page Not found')
    }
    if(selectedStatusBtn.id==='Not-Stitched'){
        await filterOrderItems('Stitched')
        await filterOrderItems('urgent')
        await filterOrderItems('Not-Stitched')
    }
    else{
        await filterOrderItems('Stitched')
        await filterOrderItems('Not-Stitched')
        await filterOrderItems('urgent')
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

const selectElement = document.getElementById('filter-by-date')
selectElement.addEventListener('change',filterSalesDashboard)

async function filterSalesDashboard(){
    filter_by_date = selectElement.value
    url = `/api/filter-sales-dashboard/?filter_by_date=${filter_by_date}`
    let response = await fetch(url)
    if(!response.ok){
        Error('not found')
    }
    const data = await response.json()
    const totalOrdersElement = document.querySelector('.total-orders-count')
    const totalCustomersElement = document.querySelector('.total-customers-count')
    const totalSalesElement = document.querySelector('.total-sales-count')
    const totalItemsElement = document.querySelector('.total-items-count')
    const totalPrepaidElement = document.querySelector('.total-prepaid-count')
    const totalPostpaidElement = document.querySelector('.total-postpaid-count')

    totalOrdersElement.innerText = data.orders_count
    totalCustomersElement.innerText = data.customers_count
    totalSalesElement.innerText = '₹' + data.sales_count
    totalItemsElement.innerText = data.items_count
    totalPrepaidElement.innerText = data.prepaid_count
    totalPostpaidElement.innerText = data.postpaid_count
}

document.getElementById('Dashboard').classList.add('text-yellow-300')