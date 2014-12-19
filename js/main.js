d3.json('data/ufo-sightings.json', function(data) {
    data_graphic({
        title: "UFO Sightings",
        description: "Yearly UFO sightings from the year 1945 to 2010.",
        data: data,
        width: 650,
        height: 150,
        target: '#ufo-sightings',
        x_accessor: 'year',
        y_accessor: 'sightings',
        markers: [{'year': 1964, 'label': '"The Creeping Terror" released'}]
    })
})

d3.json('data/fake_users2.json', function(data) {
    for(var i=0;i<data.length;i++) {
        data[i] = convert_dates(data[i], 'date');
    }

    //add a wide multi-line chart
    data_graphic({
        title:"Multi-Line Chart Wide",
        description: "This line chart contains multiple lines and has extended ticks enabled.",
        area: false,
        legend: ['Line 1','Line 2','Line 3'],
        legend_target: '.legend',
        data: data,
        width: torso.width*2,
        height: torso.height,
        right: trunk.right,
        show_years: false,
        xax_tick: 0,
        y_extended_ticks: true,
        target: '#mentions',
        x_accessor: 'date',
        y_accessor: 'mentions'
    })
})