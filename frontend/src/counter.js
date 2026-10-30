/**
 * Inicializa el contador de demostración de la plantilla de Vite.
 * @param {HTMLElement} element Botón donde se muestra y actualiza el contador.
 */
export function setupCounter(element) {
  // Estado local del contador; no forma parte de la lógica de AulaBoard.
  let counter = 0

  const setCounter = (count) => {
    counter = count
    element.innerHTML = `Count is ${counter}`
  }

  // Cada clic incrementa el valor y actualiza la interfaz.
  element.addEventListener('click', () => setCounter(counter + 1))
  setCounter(0)
}
