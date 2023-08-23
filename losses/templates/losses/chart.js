document.addEventListener('DOMContentLoaded', function () {
    var times = {{ months|safe }}
    var data = {{ datas|safe }}   
    const chart = Highcharts.chart('container', {

title: {
    text: ' ',
    align: 'left'
},

yAxis: {
    title: {
        text: 'Amount'
    }
},

xAxis: {
    title: {
        text: 'Months'
    },
    categories: times
},

legend: {
    layout: 'vertical',
    align: 'right',
    verticalAlign: 'middle'
},

series: [{
    name: '{{ header }}',
    data: data
}],

responsive: {
    rules: [{
        condition: {
            maxWidth: 500
        },
        chartOptions: {
            legend: {
                layout: 'horizontal',
                align: 'center',
                verticalAlign: 'bottom'
            }
        }
    }]
}

})
    });