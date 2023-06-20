const element = document.querySelector('.dataTables_info')

const canvita = element.appendChild(document.createElement("canvas"));

canvita.id = "canvita2";
canvita.width = 50;


// Datos del gráfico
var data = {
    labels: ["jan", "feb", "mar", "apr", "may", "jun"],
    datasets: [{
        label: 'Overview',
        data: [12, 19, 3, 17, 6],
        borderWidth: 1
    }]
    };

    // Opciones del gráfico
    var options = {
    scales: {
        y: {
        beginAtZero: true
        }
    }
    };

    // Crear el gráfico de barras
    var myChart = new Chart(canvita, {
    type: 'pie',
    data: data,
    options: options
    });
    