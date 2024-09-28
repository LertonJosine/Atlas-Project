(function () {
    /**
     * inputs - nodelist com todos os inputs do formulario
     * 
     * esta função adiciona a lista de classes dos inputs a classe form-control
     */
    let inputs = document.querySelectorAll('input');
    for (let input of inputs) {

        // caso o input nao seja submit ou checkbox vai adicionar a classe
        if (input.type != 'submit' && input.type != 'checkbox') {
            input.classList.add('form-control')
        } else if (input.type == 'checkbox') {
            input.style.height = 'fit-content';
        }

    }
})();

(function () {

    /*
    * esta função substitui o elemento input por button
    */
    let div = document.createElement('div');
    div.classList.add('text-center');
    let button = document.createElement('button');
    button.type = 'submit';
    button.innerText = 'Submit';

    div.appendChild(button);

    let input = document.querySelector('input[type="submit"]');
    input.replaceWith(div);
}
)();

(
    function () {
        /**
         * Oculta todas as labels exepto as labels Delete
         */
        let labels = document.querySelectorAll('label');
        for (let label of labels) {
            if (label.innerText != 'Delete:') {
                label.style.display = 'none';

            }
        }
    }
)();

(
    function () {
        /**
         * definine o placeholder para os inputs nome, username, email e preço
         */
        let inputs_nome = document.querySelectorAll('input[id*="nome"]');
        inputs_nome.forEach(element => {
            element.setAttribute('placeholder', 'Introduza o nome');
        });
        let inputs_preco = document.querySelectorAll('input[id*="preco"]');
        inputs_preco.forEach(element => element.setAttribute('placeholder', 'Introduza o preco'));

        let inputs_username = document.querySelectorAll('input[id*="username"]');
        inputs_username.forEach(element => element.setAttribute('placeholder', 'Introduza o seu username'));

        let inputs_email = document.querySelectorAll('input[id*="email"]');
        inputs_email.forEach(element => element.setAttribute('placeholder', 'Introduza o seu email'));

        let input_password1 = document.querySelectorAll('input[id*="password1"');
        input_password1.forEach(element => element.setAttribute('placeholder', 'Defina uma senha'));

        let input_password2 = document.querySelectorAll('input[id*="password2"');
        input_password2.forEach(element => element.setAttribute('placeholder', 'Confirme a senha'));

    }
)();

(
    function(){
        /**
         * 
         */
    }
)();
