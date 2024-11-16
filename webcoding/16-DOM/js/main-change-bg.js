const BODYSTYLE = document.querySelector('body').style;
const IMG = document.querySelectorAll('img');
// Same as document.body.style

// got the following from:
// https://codingartistweb.com/2021/08/rgb-to-hex-hex-to-rgb-converter-with-javascript/ 
// then did some tweaking
function toRgb(hexCode){
    let rgbArr = [];
    let rgbOut
    if(/^#?[A-Fa-f0-9]{6}$/.test(hexCode)){
        hexCode = hexCode.split("#")[1] || hexCode;
        for(let i=0; i<hexCode.length;i+=2){
            rgbArr.push(parseInt(hexCode[i] + hexCode[i+1], 16));
        }
        rgbOut = "rgb(" + rgbArr[0] + ', ' + rgbArr[1] + ', ' + rgbArr[2] + ")";
        // "+ ', '" needed to make it into CSS RGB format
        return rgbOut
    }
    else{
        return null
    }
}

// a little bit of stack overflow with overcomplications by me
function isValidColor(color) {
    color = color.toLowerCase()

    let styled = new Option().style;
    // 'new' creates an instance of 'Option()'
    // 'Option()' is a constructor for a HTML <option>
    styled.color = color;
    // Browser tries changing the color
    // If valid, color changes. If not, color stays the same
    
    // Returns 'false' if color wasn't assigned at all
    return styled.color == color || styled.color == toRgb(color) ? true : false;
    // So here's the thing: Browser converts HEX to RGB. So the condition,
    // when receiving HEX values, will always return 'false', bc it's trying
    // to compare 1 RGB string with 1 HEX string;
}

function changeBg(color) {
    color == color.toLowerCase();
    
    if(isValidColor(color)) {
        BODYSTYLE.backgroundColor = color;
        if(BODYSTYLE.backgroundColor == 'black' || BODYSTYLE.backgroundColor == 'rgb(0, 0, 0)') {
            BODYSTYLE.color = 'white'
            IMG[0].style.borderColor = 'white'
        } else if (BODYSTYLE.backgroundColor == 'rgb(255, 0, 245)') {
            IMG[0].src = 'https://radahl.no/wp-content/uploads/sites/12/2021/11/csm-gcd.gif'
        }
    } else{
        alert('Error: not a valid CSS color, RGB or HEX code.')
    }

}

changeBg((prompt('Color: \n"rgb(0, 0, 0)"\n"#000000"\n"Black"')));