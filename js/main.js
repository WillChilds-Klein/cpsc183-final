$(document).ready(function() {

    var torso = {};
    torso.width = 375;
    torso.height = 200;
    torso.right = 20;

    var trunk = {};
    trunk.width = 320;
    trunk.height = 150;
    trunk.left = 35;
    trunk.right = 10;
    trunk.xax_count = 5;

    var small = {};
    small.width = 240;
    small.height = 140;
    small.left = 20;
    small.right = 20;
    small.top = 20;
    small.xax_count = 5;

    d3.json('data/mentions-2010.json', function(data) {
        for(var i=0;i<data.length;i++) {
            data[i] = convert_dates(data[i], 'date');
        }

        //add a wide multi-line chart
        data_graphic({
            title:"Twitter Mentions in 2010",
            description: "This line chart contains multiple lines and has extended ticks enabled.",
            area: false,
            legend: ['"Patent Troll" or #PatentTroll',
                     '"pae" or #pae',
                     '"pme" or #pme',
                     '"npe" or #npe'
                    ],
            legend_target: '#mentions-2010_legend',
            data: data,
            width: torso.width*3.5,
            height: torso.height,
            right: trunk.right,
            show_years: true,
            xax_tick: 0,
            y_extended_ticks: true,
            target: '#mentions-2010',
            x_accessor: 'date',
            y_accessor: 'mentions'
        })
    })

    d3.json('data/mentions-2011.json', function(data) {
        for(var i=0;i<data.length;i++) {
            data[i] = convert_dates(data[i], 'date');
        }

        //add a wide multi-line chart
        data_graphic({
            title:"Twitter Mentions in 2011",
            description: "This line chart contains multiple lines and has extended ticks enabled.",
            area: false,
            legend: ['"Patent Troll" or #PatentTroll',
                     '"pae" or #pae',
                     '"pme" or #pme',
                     '"npe" or #npe'
                    ],
            legend_target: '#mentions-2011_legend',
            data: data,
            width: torso.width*3.5,
            height: torso.height,
            right: trunk.right,
            show_years: true,
            xax_tick: 0,
            y_extended_ticks: true,
            target: '#mentions-2011',
            x_accessor: 'date',
            y_accessor: 'mentions'
        })
    })

    d3.json('data/mentions-2012.json', function(data) {
        for(var i=0;i<data.length;i++) {
            data[i] = convert_dates(data[i], 'date');
        }

        //add a wide multi-line chart
        data_graphic({
            title:"Twitter Mentions in 2012",
            description: "This line chart contains multiple lines and has extended ticks enabled.",
            area: false,
            legend: ['"Patent Troll" or #PatentTroll',
                     '"pae" or #pae',
                     '"pme" or #pme',
                     '"npe" or #npe'
                    ],
            legend_target: '#mentions-2012_legend',
            data: data,
            width: torso.width*3.5,
            height: torso.height,
            right: trunk.right,
            show_years: true,
            xax_tick: 0,
            y_extended_ticks: true,
            target: '#mentions-2012',
            x_accessor: 'date',
            y_accessor: 'mentions'
        })
    })

    d3.json('data/mentions-2013.json', function(data) {
        for(var i=0;i<data.length;i++) {
            data[i] = convert_dates(data[i], 'date');
        }

        //add a wide multi-line chart
        data_graphic({
            title:"Twitter Mentions in 2013",
            description: "This line chart contains multiple lines and has extended ticks enabled.",
            area: false,
            legend: ['"Patent Troll" or #PatentTroll',
                     '"pae" or #pae',
                     '"pme" or #pme',
                     '"npe" or #npe'
                    ],
            legend_target: '#mentions-2013_legend',
            data: data,
            width: torso.width*3.5,
            height: torso.height,
            right: trunk.right,
            show_years: true,
            xax_tick: 0,
            y_extended_ticks: true,
            target: '#mentions-2013',
            x_accessor: 'date',
            y_accessor: 'mentions'
        })
    })

    d3.json('data/mentions-2014.json', function(data) {
        for(var i=0;i<data.length;i++) {
            data[i] = convert_dates(data[i], 'date');
        }

        //add a wide multi-line chart
        data_graphic({
            title:"Twitter Mentions in 2014",
            description: "This line chart contains multiple lines and has extended ticks enabled.",
            area: false,
            legend: ['"Patent Troll" or #PatentTroll',
                     '"pae" or #pae',
                     '"pme" or #pme',
                     '"npe" or #npe'
                    ],
            legend_target: '#mentions-2014_legend',
            data: data,
            width: torso.width*3.5,
            height: torso.height,
            right: trunk.right,
            show_years: true,
            xax_tick: 0,
            y_extended_ticks: true,
            target: '#mentions-2014',
            x_accessor: 'date',
            y_accessor: 'mentions'
        })
    })

})