function getElementByXpath(path) {
  return document.evaluate(path, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
}

const customerChart = document.createElement('script')
customerChart.src = '/static/js/components/customers_chart.js'
customerChart.type = 'text/javascript'

const orderChart = document.createElement('script')
orderChart.src = '/static/js/components/orders_chart.js'
orderChart.type = 'module'

const chartjs = document.createElement('script')
// chartjs.src="/static/js/libs/chart.min.js"

chartjs.src = 'https://cdn.jsdelivr.net/npm/chart.js@4.3.0/dist/chart.umd.min.js'
chartjs.type = 'text/javascript'

document.body.appendChild(chartjs)

const importer = (src, attr = {}) => {
  const script = document.createElement("script");
  Object.entries(attr).forEach(([key, value]) => {
    script[key] = value;
  });
  return new Promise((res) => {
    script.src = src;
    script.addEventListener("load", (event) => res(event));
    document.body.appendChild(script);
  });
};

const main = async () => {
  // await importer("/static/js/components/general_chart.js", { type: "module" });
  await importer("/static/js/components/customers_chart.js");
  await importer("/static/js/components/orders_chart.js", { type: "module" });

};


/* preview image on input */

document.addEventListener('click', function() {
  const inputAll = document.querySelectorAll('input[type="file"]');

  inputAll.forEach((input, index) => {
    input.addEventListener('change', function(event) {
      const file = event.target.files[0];
      const reader = new FileReader();
    
      reader.onload = function(e) {
        const img = document.createElement('img');
        img.src = e.target.result;
        img.style.width = '100px';
    
        const existingImg = document.getElementById('preview_image' + index);
        if (existingImg) {
          existingImg.parentNode.removeChild(existingImg);
        }
    
        img.id = 'preview_image' + index;
        const parent = input.parentNode;
        parent.insertBefore(img, input);
      }
    
      reader.readAsDataURL(file);
    });
  });
});






document.addEventListener("DOMContentLoaded",
  ()=> { 
      
      getElementByXpath('//*[@id="general-tab"]/div/div').classList.remove('p-5');
      getElementByXpath('//*[@id="product_form"]/div/div[1]/div/div').style = 'padding: 1rem !important;';
      document.querySelector('.django-ckeditor-widget').style = 'display: flex !important;';
      document.getElementById('id_image').style = ``;
      document.getElementById('id_image').parentNode.style = `display: flex; flex-direction: column; align-items: start;`;
  }
)


if (window.location.pathname == '/admin/chart/chart/') {

  window.onload = () => {

    const base = document.querySelector('.dataTables_info');
    base.innerHTML = '';
    
    main();

  }
}

