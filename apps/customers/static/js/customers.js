async function filterCustomers(page_num){
  let query = '/api/filter-customers/?'
  let searchQuery = document.querySelector('.search-input').value.trim()
  let gender = document.querySelector('#gender').value
  let sortby = document.querySelector('#sortby').value
  if (searchQuery) query += `search=${searchQuery}`
  if (gender !== 'D') query += `&gender=${gender}`
  if (sortby !== 'D') query += `&sortby=${sortby}`
  if (page_num){ query += `&page=${page_num}`} else query += '&page=1'
  
  let response = await fetch(query) 
  let data = await response.json()
  
  const pagination = document.querySelector('.pagination')
  const notFoundElement = document.querySelector('.not-found')
  const table = document.querySelector('table')
  const tableBody = document.querySelector('tbody')
  tableBody.innerHTML = ''
  page_obj = data['page_obj']
  if(data.customers.length > 0){
    notFoundElement.innerHTML = ''
    if (table.classList.contains('hidden')) table.classList.remove('hidden')
    if (notFoundElement.classList.contains('min-h-[60vh]')){notFoundElement.classList.remove('min-h-[60vh]')}
    data.customers.forEach(customer=>{
        const row = document.createElement('tr')
        row.innerHTML = `
        <td class=" flex justify-center items-center h-14"><img class=" h-10 w-10 rounded-full" src=${customer.profile} alt=""></td>
        <td>${customer.first_name}</td>
        <td>${customer.phone}</td>
        <td>${customer.email}</td>
        <td>${customer.city}</td> 
        <td>
          <a class=" mr-2" href="/customer-details/${customer.id}">
            View
          </a>
          </a>
        </td>
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

document.getElementById('Customers').classList.add('text-yellow-300')