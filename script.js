var ctx = document.getElementById("myChart").getContext('2d');
var myChart = new Chart(ctx, {
  type: 'bar',
  data: {
    labels: ["M", "T", "W", "T", "F", "S", "S"],
    datasets: [{
      data: [3, 1, 4, 5, 0, 2, 6],
      backgroundColor: "rgba(211,211,211 ,1 )"
    }]
  },
  options: {
       scales: {
            xAxes: [{
               gridLines: {
                  display: false
               }
            }],
            yAxes: [{
               gridLines: {
                  display: false,
                  drawBorder: false
               },
               ticks: {
                display: false
                }
            }]
       },
       legend: {
            display: false
       }
    }
});