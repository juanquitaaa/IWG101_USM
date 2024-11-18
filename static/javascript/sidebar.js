/*document.addEventListener('DOMContentLoaded', function () {
    // Interests toggle
    const toggleInterestsButton = document.getElementById('toggle-interests');
    const interestsList = document.getElementById('interests-list');

    toggleInterestsButton.addEventListener('click', function () {
        // Mostrar u ocultar la lista de intereses
        if (interestsList.style.display === 'none') {
            interestsList.style.display = 'block';
        } else {
            interestsList.style.display = 'none';
        }
    });
});*/

document.addEventListener('DOMContentLoaded', function () {
    // Interests toggle
    const toggleInterestsButton = document.getElementById('toggle-interests');
    const interestsList = document.getElementById('interests-list');

    toggleInterestsButton.addEventListener('click', function () {
        // Mostrar u ocultar la lista de intereses
        if (interestsList.style.display === 'none' || interestsList.style.display === '') {
            interestsList.style.display = 'block';
            // Cambiar el contenido del botón a "-"
            toggleInterestsButton.textContent = ''; // Elimina el contenido existente
            toggleInterestsButton.classList.add('minus'); // Agrega una clase para el signo "-"
        } else {
            interestsList.style.display = 'none';
            // Cambiar el contenido del botón a "+"
            toggleInterestsButton.textContent = ''; // Elimina el contenido existente
            toggleInterestsButton.classList.remove('minus'); // Elimina la clase del signo "-"
        }
    });
});
