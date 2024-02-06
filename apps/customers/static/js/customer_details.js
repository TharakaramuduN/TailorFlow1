const dialogBox = document.getElementById('dialog')

function closeDialog(){
    dialogBox.style.display = 'none'
}

function openDialog(){
    console.log('clicked')
    dialogBox.style.display = 'flex'
}

document.onclick = function(event){
    if(event.target.id === 'dialog'){
        dialogBox.style.display = 'none'
    }
}