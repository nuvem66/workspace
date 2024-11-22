let kaplimmm = document.querySelector('#kaplimmm')

// Could do the same to 'pizzaType'
let sizeValue = {
    'Pequena': 25,
    'Média': 35,
    'Grande': 50
}

function calcValue(){
    let selectedSize = document.querySelector("input[name='tamanho']:checked")
    if (selectedSize == null) return alert("Por favor, escolha o tamanho.")
    let extras = document.querySelectorAll("input[name='adicionais']:checked")
    
    return sizeValue[selectedSize.value] + extras.length * 5;
}

function fazerPedido(){
    let clientName = document.querySelector(".input-text input")
    let pizzaType = document.querySelector("input[name='sabor']:checked")
    
    if (clientName.value == "") return alert("Por favor, preencha seu nome.")
    else if (pizzaType == null) return alert("Por favor, escolha o sabor.")
    
    document.querySelector("#total h2 strong").textContent = calcValue()
    kaplimmm.play()
}