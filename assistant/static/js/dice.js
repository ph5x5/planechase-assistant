var dice = {
    sides: 6,
    roll: function () {
      var randomNumber = Math.floor(Math.random() * this.sides) + 1;
      return randomNumber;
    }
}
  
function printNumber(number) {
    var placeholder = document.getElementById('placeholder');
    if (( number == 2 || number == 3 || number == 4)) {
        placeholder.innerHTML = number;
    } else if (( number == 1)) {
        placeholder.innerHTML = '<img src="/static/planeswalker.png">'
    } else if (( number == 6)) {
        placeholder.innerHTML = '<img src="/static/chaos.png">'
    }
}

var button = document.getElementById('dice');

button.onclick = function() {
    var result = dice.roll();
    printNumber(result);
};  