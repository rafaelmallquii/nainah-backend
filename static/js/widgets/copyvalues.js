const copyValues = () => {

}


const isElementLoaded = async selector => {
  while (document.querySelector(selector) === null) {
    await new Promise(resolve => requestAnimationFrame(resolve))
  }
  return document.querySelector(selector);
};

// I'm checking for a specific class .file-item and then running code. You can also check for an id or an element.
isElementLoaded('.btn-default').then((selector) => {
  // Run code here.
  selector.addEventListener('click', function () {

    const inputPriceSons = document.querySelectorAll('[id^="id_productvariant_set-"][id$="-price"]');
    console.log(inputPriceSons);
    const inputPriceFather = document.getElementById('id_price').value;
    inputPriceSons.forEach(function(inputPriceSon) {
      if (inputPriceSon.value == '0.0') {
        inputPriceSon.value = inputPriceFather;
      }
    });

    // Obtiene todas las entradas de título de las variantes
    const inputTitleSons = document.querySelectorAll('[id^="id_productvariant_set-"][id$="-title"]');

    // Obtiene el valor del título del producto principal (padre)
    const inputTitleFather = document.getElementById('id_title').value;

    // Recorre todas las entradas de título de las variantes y establece los valores predefinidos
    inputTitleSons.forEach(function (inputTitleSon) {
      if (inputTitleSon.value == '') {
        inputTitleSon.value = inputTitleFather;
      }
    });

  });
});