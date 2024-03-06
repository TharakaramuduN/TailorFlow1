async function filterCustomers(page_num){
    let query = '/filter-customers/?'
    let searchQuery = document.querySelector('.search-input').value.trim()
    let gender = document.querySelector('#gender').value
    let sortby = document.querySelector('#sortby').value
    const tableBody = document.querySelector('tbody')
    if (searchQuery) query += `search=${searchQuery}`
    if (gender !== 'D') query += `&gender=${gender}`
    if (sortby !== 'D') query += `&sortby=${sortby}`
    if (page_num){ query += `&page=${page_num}`} else query += '&page=1'
    
    let response = await fetch(query) 
    let data = await response.json()
  
    tableBody.innerHTML = ''
    pagination = document.querySelector('.pagination')
    page_obj = data['page_obj']
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
    });
    pagination.innerHTML = ''
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
    
  }