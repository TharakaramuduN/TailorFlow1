async function filterCustomers(page_num){
    let query = '/filter-customers/?'
    let searchQuery = document.querySelector('.search-input').value.trim()
    let gender = document.querySelector('#gender').value
    let sortby = document.querySelector('#sortby').value
    if (searchQuery) query += `search=${searchQuery}`
    if (gender !== 'D') query += `&gender=${gender}`
    if (sortby !== 'D') query += `&sortby=${sortby}`
    if (page_num){ query += `&page=${page_num}`} else query += '&page=1'
    
    let response = await fetch(query) 
    let data = await response.json()
    
    const tableBody = document.querySelector('tbody')
    const table = document.querySelector('table')
    const notFoundElement = document.querySelector('.not-found')
    tableBody.innerHTML = ''
    pagination = document.querySelector('.pagination')
    page_obj = data['page_obj']
    if(data.customers.length > 0){
        notFoundElement.innerHTML = ''
        if (table.classList.contains('hidden')) table.classList.remove('hidden')
        if (notFoundElement.classList.contains('min-h-[60vh]')){notFoundElement.classList.remove('min-h-[60vh]')}
        data.customers.forEach(customer => {
            const row = document.createElement('tr')
            row.innerHTML = `
            <td class=" flex justify-center items-center h-14"><a style="padding:inherit" class="flex items-center justify-center w-full h-full "  href="/select-products/${customer.id}"><img class=" h-8 w-8 sm:h-10 sm:w-10 rounded-full" src=${customer.profile} alt=""></a></td>
            <td><a style="padding:inherit" class="block w-full h-full"  href="/select-products/${customer.id}">${customer.first_name}</a></td>
            <td><a style="padding:inherit" class="block w-full h-full"  href="/select-products/${customer.id}">${customer.phone}</a></td>
            <td><a style="padding:inherit" class="block w-full h-full"  href="/select-products/${customer.id}">${customer.email}</a></td>
            <td><a style="padding:inherit" class="block w-full h-full"  href="/select-products/${customer.id}">${customer.city}</a></td>
            
            `
        tableBody.appendChild(row)
    })}
    else{
        table.classList.add('hidden')
        notFoundElement.classList.add('min-h-[60vh]')
        notFoundElement.innerHTML = '<h1 class=" text-xl sm:text-3xl md:text-4xl lg:text-6xl  font-medium text-gray-500">No Results Found</h1>'
    }
    pagination.innerHTML = ''
    if(data.customers.length > 0){
    pagination.innerHTML = `
        <span class="step-links flex justify-between w-full">
            ${page_obj.has_previous ? `
            <span>
            <button class=" border px-3 bg-yellow-500 rounded-full" onclick=filterCustomers(${ page_obj.previous_page_number })><i class="fa-solid fa-angle-left"></i></button></span>` : '<div></div>' }
    
            <span class="current">
                Page ${ page_obj.number } of ${ page_obj.num_pages }.
            </span>
    
            ${page_obj.has_next ? `
            <span>
                <button class=' border px-3 bg-yellow-500 rounded-full' type='button' onclick=filterCustomers(${ page_obj.next_page_number })><i class="fa-solid fa-angle-right"></i></button>
            </span>` : '<div></div>'}
        </span>`
    
  }}

  document.addEventListener('DOMContentLoaded',()=>{
    localStorage.clear()
})