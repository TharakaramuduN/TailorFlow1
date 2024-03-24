async function filterOrders(page_num){
    const searchQuery = document.querySelector('.search-input').value
    let response = await fetch(`/api/filter-orders/?search=${searchQuery}&page=${page_num ? page_num : 1}`)
    if(!response.ok){
        throw Error('not found')
    }
    const data = await response.json()
    const ordersContainer = document.querySelector('.orders-list')
    ordersContainer.innerHTML = ''
    pagination = document.querySelector('.pagination')
    const notFoundElement = document.querySelector('.not-found')
    page_obj = data['page_obj']
    if(data.orders.length > 0){
        notFoundElement.innerHTML = ''
        if(notFoundElement.classList.contains('min-h-[50vh]')) notFoundElement.classList.remove('min-h-[50vh]')
        data['orders'].forEach(order=>{
            const divElement = document.createElement('div')
            divElement.classList.add('order-card-container','cursor-pointer','rounded-md' ,'p-2',  'odd:bg-gray-100','even:bg-gray-50')
            divElement.addEventListener('click',()=>window.location.href=`/order-details/${order.id}`)
            divElement.innerHTML = `
            <div class="order-card space-y-2">
                <div class=" flex justify-between">
                    <p class=" text-lg sm:text-xl font-medium">${order.customer__first_name}</p>
                    <p class="text-xs">Id: <span class="text-lg font-medium text-gray-400"> ${order.id}</span></p>
                </div>
                <div class=" flex justify-between">
                    <p>Items: ${order.items_count}</p>
                    <p>Total: <span class=" font-medium">${order.total_price}</span></p>
                </div>
            </div>
            `
        ordersContainer.appendChild(divElement)
    })}
    else{
        notFoundElement.classList.add('min-h-[50vh]')
        notFoundElement.innerHTML = '<h1 class=" text-xl sm:text-3xl md:text-4xl lg:text-6xl  font-medium text-gray-500">No Results Found</h1>'
    }
    pagination.innerHTML = ''
    if(data.orders.length > 0){
        pagination.innerHTML = `
        <span class="step-links flex justify-between w-full">
            ${page_obj.has_previous ? `
            <span>
            <button class=" border px-3 bg-yellow-500 rounded-full" onclick=filterOrders(${ page_obj.previous_page_number })><i class="fa-solid fa-angle-left"></i></button></span>` : '<div></div>' }

            <span class="current">
                Page ${ page_obj.number } of ${ page_obj.num_pages }.
            </span>

            ${page_obj.has_next ? `
            <span>
                <button class=' border px-3 bg-yellow-500 rounded-full' type='button' onclick=filterOrders(${ page_obj.next_page_number })><i class="fa-solid fa-angle-right"></i></button>
            </span>` : '<div></div>'}
        </span>`
}}

document.getElementById('Orders').classList.add('text-yellow-300')