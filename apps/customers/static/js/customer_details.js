const dialogBox = document.getElementById('dialog')

function closeDialog(){
    dialogBox.style.display = 'none'
}

function openDialog(){
    console.log('clicked')
    dialogBox.style.display = 'flex'
}

dialogBox.onclick = function(event){
    if(event.target.id === 'dialog'){
        dialogBox.style.display = 'none'
    }
}