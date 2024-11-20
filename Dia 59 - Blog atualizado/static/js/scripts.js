// Adiciona um evento que escuta quando o conteúdo da página é carregado
window.addEventListener('DOMContentLoaded', () => {
    let scrollPos = 0;  // Armazena a posição de rolagem anterior
    const mainNav = document.getElementById('mainNav');  // Seleciona o elemento de navegação principal
    const headerHeight = mainNav.clientHeight;  // Obtém a altura do cabeçalho

    // Adiciona um evento que escuta quando a página é rolada
    window.addEventListener('scroll', function() {
        const currentTop = document.body.getBoundingClientRect().top * -1;  // Obtém a posição atual do topo da página

        if (currentTop < scrollPos) {
            // Rolando para cima
            if (currentTop > 0 && mainNav.classList.contains('is-fixed')) {
                // Se o cabeçalho não estiver no topo e for fixo, torna-o visível
                mainNav.classList.add('is-visible');
            } else {
                console.log(123);  // Log para depuração
                // Remove classes de visibilidade e fixação do cabeçalho
                mainNav.classList.remove('is-visible', 'is-fixed');
            }
        } else {
            // Rolando para baixo
            // Remove a classe de visibilidade do cabeçalho
            mainNav.classList.remove(['is-visible']);
            // Se a posição atual for maior que a altura do cabeçalho e não estiver fixo, fixa o cabeçalho
            if (currentTop > headerHeight && !mainNav.classList.contains('is-fixed')) {
                mainNav.classList.add('is-fixed');
            }
        }
        scrollPos = currentTop;  // Atualiza a posição de rolagem
    });
});
