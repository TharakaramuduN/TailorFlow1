const products = document.querySelectorAll('.product');


let finalPriceElement = document.querySelector('#id_total_price')
let subTotal = parseFloat(finalPriceElement.value)

products.forEach(product => {
    const unitPrice = product.querySelector('.unit-price')
    const totalPrice = product.querySelector('.price')
    const decrementButton = product.querySelector('.decrement-button');
    const incrementButton = product.querySelector('.increment-button');
    const quantityInput = product.querySelector('.quantity-input');
    const subTotalElement = document.querySelector('.sub-total')
    const finalPrice = document.querySelector('.final-price')
    subTotalElement.innerText = '₹' + subTotal
    totalPrice.innerText = '₹' + parseFloat(unitPrice.value) * parseInt(quantityInput.value)



    decrementButton.addEventListener('click', () => {
        let currentValue = parseInt(quantityInput.value);
        if (currentValue > 1) {
            quantityInput.value = currentValue - 1;
            totalPrice.innerText = '₹' + parseFloat(parseFloat(unitPrice.value) * parseFloat(quantityInput.value)).toFixed(2)
            subTotal -= parseFloat(unitPrice.value)
            subTotalElement.innerText = '₹' + subTotal
            finalPrice.innerHTML = `<p><sup>₹</sup>${subTotal}</p>`
            finalPriceElement.value = parseFloat(subTotal)
            updateOrderButton.style.display = 'block'
    
        }
    });

    incrementButton.addEventListener('click', () => {
        let currentValue = parseInt(quantityInput.value);
        quantityInput.value = currentValue + 1;
        totalPrice.innerText = '₹' + parseFloat(parseFloat(unitPrice.value) * parseFloat(quantityInput.value)).toFixed(2)
        subTotal += parseFloat(unitPrice.value)
        subTotalElement.innerText = '₹' + subTotal
        finalPrice.innerHTML = `<p><sup>₹</sup>${subTotal}</p>`
        finalPriceElement.value = parseFloat(subTotal)
        updateOrderButton.style.display = 'block'

    });
});


function addNotes(event){
    const container = event.target.closest('.product-container')
    const addButton = container.querySelector('.add-btn')
    const textArea = container.querySelector('textarea')
    textArea.classList.toggle('hidden')
    if(textArea.classList.contains('hidden')){
        addButton.innerText = 'Notes'
    }
    else{
        addButton.innerText = 'Hide Notes'
    }
}

function toggleUrgent(event){
    const container = event.target.closest('.product-container')
    const checkBox = container.querySelector('.urgent-checkbox')
    checkBox.checked = !checkBox.checked
}


// Function to display a confirmation message
function confirmBeforeUnload(event) {

    event.returnValue = 'are you sure?';

}



// Get the "Update Order" button
const updateOrderButton = document.querySelector('.update-btn');

// Hide the "Update Order" button by default
updateOrderButton.style.display = 'none';

// Add event listeners to all input fields, textareas, and select elements
const formInputs = document.querySelectorAll('input, textarea, select');
formInputs.forEach(input => {
    input.addEventListener('change', () => {
        // Show the "Update Order" button when a change is detected
        updateOrderButton.style.display = 'block';
        // Add event listener for beforeunload event
        window.addEventListener('beforeunload', confirmBeforeUnload);
    });
});

// Add click event listener to the "Update Order" button
updateOrderButton.addEventListener('click', function() {
    // Remove the beforeunload event listener when the button is clicked
    window.removeEventListener('beforeunload', confirmBeforeUnload);
});
