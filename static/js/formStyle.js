let inputs = document.querySelectorAll('input[id*="preco"], input[id*="nome"], input[type="file"], select');
inputs.forEach(input => input.classList.add('form-control'));

inputs = document.querySelectorAll('input[id*="preco"]');
inputs.forEach(elemento => elemento.setAttribute("placeholder", "Introduza o preco"));

inputs = document.querySelectorAll('input[id*="nome"]');
inputs.forEach(elemento => elemento.setAttribute("placeholder", "Introduza o nome"));

let clear_checkbox = document.querySelectorAll('input[type="checkbox"]');
clear_checkbox.forEach(element => element.style.height = 'fit-content');

let labels = document.getElementsByTagName("label");
for (let label of labels) {
    if (label.innerText == "Delete:") {
        continue
    } else {
        label.style.display = 'none';
    }
}

let div = document.createElement('div');
div.classList.add('text-center');

let button = document.createElement('button');
button.innerText = "Enviar";
button.setAttribute('type', 'submit');
div.appendChild(button);

let input_submit = document.querySelector('input[type="submit"]');
input_submit.remove();

let form = document.querySelector('form');
form.appendChild(div);

let paragraph = document.querySelectorAll('p');
paragraph.forEach(p=> p.classList.add("col-md-6", "form-group"));
