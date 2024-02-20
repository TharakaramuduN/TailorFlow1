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
  })
  
}