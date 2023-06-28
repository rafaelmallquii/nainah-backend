const copyValues = () => {

}


const isElementLoaded = async selector => {
  while (document.querySelector(selector) === null) {
    await new Promise(resolve => requestAnimationFrame(resolve))
  }
  return document.querySelector(selector);
};

// // I'm checking for a specific class .file-item and then running code. You can also check for an id or an element.
// isElementLoaded('.btn-default').then((selector) => {
//   // Run code here.
//   selector.addEventListener('click', function () {
//     const inputPriceSons = document.querySelectorAll('[id^="id_productvariant_set-"][id$="-price"]');
//     console.log(inputPriceSons);
//     const inputPriceFather = document.getElementById('id_price').value;

//     inputPriceSons.forEach(function (inputPriceSon) {
//       if (inputPriceSon.value == '0.0') {
//         inputPriceSon.value = inputPriceFather;
//       }
//     });

//     const inputTitleSons = document.querySelectorAll('[id^="id_productvariant_set-"][id$="-title"]');
//     const inputTitleFather = document.getElementById('id_title').value;


//   });
// });
isElementLoaded('.btn-default').then((selector) => {
  // Run code here.
  selector.addEventListener('click', function () {
    const inputPriceFather = document.querySelectorAll('[id^="id_productvariant_set-"][id$="-price"]');

    inputPriceFather.forEach(function (inputPriceSon, index) {
      
      const inputTitleSon = document.getElementById(`id_productvariant_set-${index}-title`);
      if (!inputTitleSon || !inputTitleSon.value) {
        const inputTitleFather = document.getElementById('id_title').value;
        const indexText = index > 0 ? ` - ${index}` : '';
        inputTitleSon.value = inputTitleFather + indexText;
      }
    });

    // ahora el padre es el hijo 
    const inputTitleFather = document.querySelectorAll('[id^="id_productvariant_set-"][id$="-title"]');
    inputTitleFather.forEach(function (inputTitleSon, index) {
      if (!inputTitleSon || !inputTitleSon.value) {
        const inputTitleFather = document.getElementById('id_title').value;
        const indexText = index > 0 ? ` - ${index}` : '';
        inputTitleSon.value = inputTitleFather + indexText;
      }
    } );

  });
});