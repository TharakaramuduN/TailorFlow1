async function filterOrders(page_num){
    const searchQuery = document.querySelector('.search-input').value
    let response = await fetch(`/filter-orders/?search=${searchQuery}&page=${page_num ? page_num : 1}`)
    if(!response.ok){
        throw Error('not found')
    }
    const data = await response.json()
    const ordersContainer = document.querySelector('.orders-list')
    ordersContainer.innerHTML = ''
    pagination = document.querySelector('.pagination')
    page_obj = data['page_obj']
    data['orders'].forEach(order=>{
        const divElement = document.createElement('div')
        divElement.classList.add('order-card-container','cursor-pointer','rounded-md' ,'p-2',  'odd:bg-gray-100','even:bg-gray-50')
        divElement.addEventListener('click',()=>window.location.href=`/order-details/${order.id}`)
        divElement.innerHTML = `
        <div class="order-card space-y-2">
            <div class=" flex justify-between">
                <p class=" text-lg sm:text-xl font-medium">${order.customer__first_name}</p>
                <p>Order Id: ${order.id}</p>
            </div>
            <div class=" flex justify-between">
                <p>Items: ${order.items_count}</p>
                <p>Total: <span class=" font-medium">${order.total_price}</span></p>
            </div>
        </div>
        `
        ordersContainer.appendChild(divElement)
    })
    pagination.innerHTML = ''
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
}