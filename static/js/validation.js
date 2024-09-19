function menuFormValidation() {
    let nome_cardapio_input = document.querySelector('input#id_nome');
    let imagem_cardapio = document.querySelector('input[type="file"]');
    if (imagem_cardapio.value == '' || imagem_cardapio.value == null || imagem_cardapio.value == undefined) {
        imagem_cardapio.style = "border-color: red;"
    }
    if(nome_cardapio_input.value == ''){
        nome_cardapio_input.style = "border-color: red;"
    }
}