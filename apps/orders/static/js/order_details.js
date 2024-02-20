function addNotes(event){
    const container = event.target.closest('.product-container')
    const addButton = container.querySelector('.add-btn')
    const textArea = container.querySelector('textarea')
    textArea.classList.toggle('hidden')
    if(textArea.classList.contains('hidden')){
        addButton.innerText = 'Show Notes'
    }
    else{
        addButton.innerText = 'Hide Notes'
    }
}

