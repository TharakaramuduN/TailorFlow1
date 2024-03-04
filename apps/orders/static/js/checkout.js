const products = document.querySelectorAll('.product');

let subTotal = 0;
const finalPriceElement = document.querySelector('#id_total_price')

products.forEach(product => {
    const unitPrice = product.querySelector('.unit-price')
    const totalPrice = product.querySelector('.price')
    const decrementButton = product.querySelector('.decrement-button');
    const incrementButton = product.querySelector('.increment-button');
    const quantityInput = product.querySelector('.quantity-input');
    const subTotalElement = document.querySelector('.sub-total')
    const finalPrice = document.querySelector('.final-price')
    subTotal += parseFloat(unitPrice.value)
    subTotalElement.innerText = '₹' + subTotal
    finalPrice.innerHTML = `<p><sup>₹</sup>${subTotal}</p>`
    finalPriceElement.value = subTotal
    const amountInput = document.querySelector('#id_amount')


    decrementButton.addEventListener('click', () => {
        let currentValue = parseInt(quantityInput.value);
        if (currentValue > 1) {
            quantityInput.value = currentValue - 1;
            totalPrice.innerText = '₹' + parseFloat(parseFloat(unitPrice.value) * parseFloat(quantityInput.value)).toFixed(2)
            subTotal -= parseFloat(unitPrice.value)
            subTotalElement.innerText = '₹' + subTotal
            finalPrice.innerHTML = `<p><sup>₹</sup>${subTotal}</p>`
            finalPriceElement.value = subTotal
            amountInput.value = subTotal
        }
    });

    incrementButton.addEventListener('click', () => {
        let currentValue = parseInt(quantityInput.value);
        quantityInput.value = currentValue + 1;
        totalPrice.innerText = '₹' + parseFloat(parseFloat(unitPrice.value) * parseFloat(quantityInput.value)).toFixed(2)
        subTotal += parseFloat(unitPrice.value)
        subTotalElement.innerText = '₹' + subTotal
        finalPrice.innerHTML = `<p><sup>₹</sup>${subTotal}</p>`
        finalPriceElement.value = subTotal
        amountInput.value = subTotal
    });
});


function addNotes(event){
    const container = event.target.closest('.product-container')
    const addButton = container.querySelector('.add-btn')
    const textArea = container.querySelector('textarea')
    textArea.classList.toggle('hidden')
    if(textArea.classList.contains('hidden')){
        addButton.innerText = '+ add-notes'
    }
    else{
        addButton.innerText = 'hide-notes'
    }
}

function toggleUrgent(event){
    const container = event.target.closest('.product-container')
    const checkBox = container.querySelector('.urgent-checkbox')
    checkBox.checked = !checkBox.checked
}

const paymentType = document.getElementById('id_payment_type')
paymentType.addEventListener('change',toggleAdvanceInput)

function toggleAdvanceInput(){
    const amountInput = document.querySelector('#id_amount')
    const paymentTypeValue = paymentType.value
    const advanceInputElements = document.querySelectorAll('.advance')
    if(paymentTypeValue==='POST'){
        advanceInputElements.forEach(element=>{
            element.classList.remove('hidden')
            amountInput.value = 0
        })
    }
    else{
        advanceInputElements.forEach(element=>{
            element.classList.add('hidden')
        })
        amountInput.value = subTotal
    }
}