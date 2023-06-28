const base = document.querySelector(".dataTables_info");

const child = base.appendChild(document.createElement("h2"));

const canvita = base.appendChild(document.createElement("canvas"));

canvita.id = "canvita";
canvita.width = 150;
canvita.height = 100;
canvita.style.backgroundColor = "#b899ff73";
canvita.style.padding = "10px";
canvita.style.borderRadius = "10px";
canvita.style.padding = "10px";


const ctx = document.getElementById("canvita");

new Chart(ctx, {
  type: "line",
  data: {
    color: "white",
    labels: ["jan", "feb", "mar", "apr", "may", "jun"],
    datasets: [
      {
        label: "Customers",
        data: [2, 5, 3, 10, 6, 15],
        borderWidth: 2,
        borderColor: "white",
        backgroundColor: "white",
        
      },
    ],
  },
  options: {
    scales: {
      y: {
        beginAtZero: true,
        grid: {
            color: "white",
        },
        ticks: {
            color: 'white' // Cambia el color de los números en el eje Y a Blanco
        }
      },
      x: {
        grid: {
            color: "white",
        },
        ticks: {
            color: 'white' // Cambia el color de los números en el eje X a blanco
        }
      },
 
    },
    responsive: true,
  },
  plugins: {
    legend: {
      position: "top",
      labels: {
        color: "white",

        // This more specific font property overrides the global property
        font: {
          size: 24,

        },
      },
      color: "white",
    },
    title: {
      display: true,
      text: "Resultados por día",
      color: "white",
    },
  },
});
// Chart.defaults.color = "white";