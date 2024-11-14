let hello = document.getElementById('ello')
let helloString = hello.innerText
alert(helloString)

let num = document.getElementsByClassName('num')
console.log(num) // A HTML collection ARRAY
console.log(num[1].innerText)


let paragraphs = document.getElementsByTagName('p')
console.log(paragraphs)

// Returns ONLY ONE object (the first value it finds)
let complexSelection = document.querySelector('.header div h1')
console.log(complexSelection)

// HTMLCollection/NodeList (Arrays)
let complexSelectionMultiple = document.querySelectorAll('h1')
console.log(complexSelectionMultiple)