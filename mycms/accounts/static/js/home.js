var inputs = document.getElementsByTagName("input");
var button = document.getElementById("button");
// Disable the button dynamically using javascript
button.disabled = "disabled";


function enableSubmit() {
  let isValid = true;
  for (var i = 0; i < inputs.length; i++){
    let changedInput = inputs[i];
    if (changedInput.value.trim() === "" || changedInput.value === null){
    isValid = false;
    break;
    }
  }
  button.disabled = !isValid;
}
