async function filterTransactions(page_num){
    const searchQuery = document.querySelector('.search-input').value
    let response = await fetch(`/filter-transactions/?search=${searchQuery}&page=${page_num ? page_num : 1}`)
    if(!response.ok){
        throw Error('not found')
    }
    const data = await response.json()
    pagination = document.querySelector('.pagination')
    const notFoundElement = document.querySelector('.not-found')
    page_obj = data['page_obj']
    const transactionsContainer = document.querySelector('.transactions-list')
    transactionsContainer.innerHTML = ''
    if(data.transactions.length > 0){
        if(notFoundElement.classList.contains('min-h-[50vh]')) notFoundElement.classList.remove('min-h-[50vh]')
        notFoundElement.innerHTML = ''
        data['transactions'].forEach(transaction=>{
            const divElement = document.createElement('div')
            divElement.classList.add('transaction-card', 'flex','justify-between', 'w-full','even:bg-slate-100', 'odd:bg-slate-50' ,'rounded-md', 'px-4', 'pb-3')
            divElement.innerHTML = `
            <div class="flex gap-2 sm:gap-4">
                <div class="flex justify-center items-center"><img class=" h-11 w-11 rounded-full" src="/media/${transaction.order__customer__profile}" alt=""></div>
                <div class="flex gap-1 flex-col">
                    <p class="text-lg font-medium">${transaction.order__customer__first_name}</p>
                    <p class=" text-sm  text-gray-500">Order Id:${transaction.order__id}</p>
                </div>
            </div>
            <div class=" flex justify-center items-center font-bold"><p>₹ ${transaction.amount}</p></div>
            `
            transactionsContainer.appendChild(divElement)
    })}
    else{
        notFoundElement.classList.add('min-h-[50vh]')
        notFoundElement.innerHTML = '<h1 class=" text-xl sm:text-3xl md:text-4xl lg:text-6xl  font-medium text-gray-500">No Results Found</h1>'
    }
    pagination.innerHTML = ''
    if(data.transactions.length > 0){
    pagination.innerHTML = `
        <span class="step-links flex justify-between w-full">
            ${page_obj.has_previous ? `
            <span>
            <button class=" border px-3 bg-yellow-500 rounded-full" onclick=filterTransactions(${ page_obj.previous_page_number })><i class="fa-solid fa-angle-left"></i></button></span>` : '<div></div>' }

            <span class="current">
                Page ${ page_obj.number } of ${ page_obj.num_pages }.
            </span>

            ${page_obj.has_next ? `
            <span>
                <button class=' border px-3 bg-yellow-500 rounded-full' type='button' onclick=filterTransactions(${ page_obj.next_page_number })><i class="fa-solid fa-angle-right"></i></button>
            </span>` : '<div></div>'}
        </span>`
}}