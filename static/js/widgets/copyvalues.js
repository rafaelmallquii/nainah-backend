const copyValues = () => {

}


const isElementLoaded = async selector => {
    while ( document.querySelector(selector) === null) {
      await new Promise( resolve =>  requestAnimationFrame(resolve) )
    }
    return document.querySelector(selector);
  };

  // I'm checking for a specific class .file-item and then running code. You can also check for an id or an element.
  isElementLoaded('.btn-default').then((selector) => {
      // Run code here.
      console.log(selector);
      selector.addEventListener('click', function() {
        // const inputTitle = document.getElementById('id_productvariant_set-0-title');
        // inputTitle.value = 'test'
        alert('test')
        
      });
  });