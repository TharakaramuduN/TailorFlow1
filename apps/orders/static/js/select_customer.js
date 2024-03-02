async function filterCustomers(){
    let query = '/filter-customers/?'
    let searchQuery = document.querySelector('.search-input').value.trim()
    let gender = document.querySelector('#gender').value
    let sortby = document.querySelector('#sortby').value
    const tableBody = document.querySelector('tbody')
    if (searchQuery) query += `search=${searchQuery}`
    if (gender !== 'D') query += `&gender=${gender}`
    if (sortby !== 'D') query += `&sortby=${sortby}`
    
    let response = await fetch(query) 
    let data = await response.json()
  
    tableBody.innerHTML = ''
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
    
  }