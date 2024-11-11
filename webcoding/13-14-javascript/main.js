let discount = .10
let tax = .02

products = [
    mouse = { 
        name: 'Wireless Mouse', 
        value: 700}, 
    teclado = {
        name: 'Wireless Keyboard',
        value: 1200},
    headset = {
        name: 'Wireless Headset',
        value: 1375}
];

function getParcels(product, parcels) {
    console.log(`Full price: R$${product.value}`)

    let parcel
    if (parcels < 0 || parcels > 12 ) {
        console.log(`Error: invalid number of parcels.`)
        return null
    } else {
        if (parcels <= 1) {
            parcel = product.value * (1 - discount)
            console.log(`You got a ${discount * 100}% discount! You'll only pay R$${parcel}`)
            return parcel
        } else {
            parcel = (product.value) / parcels
            if (parcels < 11) {
                console.log(`${parcels} parcels. ${parcel} each.`)
                return parcel
            } else {
                parcel *= (1 + tax)
                console.log(`${parcels} parcels. ${parcel} each. You're paying a total of ${parcel * parcels}.`)
                return parcel
            }
        }
    }
}

function makeItDark() {
    let body = document.body
    body.classList.toggle('dark')
}

console.log('Usage: getParcels(products[n], m)\n"n" is the index in "products" array (0-2).\n"m" is the number of parcels for the calc.')