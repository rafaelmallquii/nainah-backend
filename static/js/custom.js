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

if (window.location.pathname == '/admin/chart/chart/') {

  window.onload = () => {
    const base = document.querySelector('.dataTables_info');
    base.innerHTML = '';
    
    main();

  }
}

