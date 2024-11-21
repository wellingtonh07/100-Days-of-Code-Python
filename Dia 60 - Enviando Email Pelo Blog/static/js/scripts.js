// Adiciona um listener para o evento de carregamento do DOM
window.addEventListener('DOMContentLoaded', () => {
    let scrollPos = 0; // Armazena a posição de rolagem atual
    const mainNav = document.getElementById('mainNav'); // Seleciona o elemento de navegação principal
    const headerHeight = mainNav.clientHeight; // Obtém a altura do cabeçalho

    // Adiciona um listener para o evento de rolagem
    window.addEventListener('scroll', function() {
        const currentTop = document.body.getBoundingClientRect().top * -1; // Posição atual da rolagem
        if (currentTop < scrollPos) {
            // Rolagem para cima
            if (currentTop > 0 && mainNav.classList.contains('is-fixed')) {
                mainNav.classList.add('is-visible'); // Mostra o menu se estiver fixo
            } else {
                console.log(123); // Apenas um log para depuração
                mainNav.classList.remove('is-visible', 'is-fixed'); // Esconde o menu
            }
        } else {
            // Rolagem para baixo
            mainNav.classList.remove(['is-visible']); // Esconde o menu
            if (currentTop > headerHeight && !mainNav.classList.contains('is-fixed')) {
                mainNav.classList.add('is-fixed'); // Adiciona a classe 'is-fixed' se não estiver fixa
            }
        }
        scrollPos = currentTop; // Atualiza a posição de rolagem
    });
});
