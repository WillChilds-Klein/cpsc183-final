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

    d3.json('data/mentions_data_post2011.json', function(data) {
        for(var i=0;i<data.length;i++) {
            data[i] = convert_dates(data[i], 'date');
        }

        //add a wide multi-line chart
        data_graphic({
            title:"Twitter Mentions",
            description: "This line chart contains multiple lines and has extended ticks enabled.",
            area: false,
            legend: ['"Patent Troll" or #PatentTroll',
                     '"pae" or #pae',
                     '"pme" or #pme', 
                     '"npe" or #npe'
                    ],
            legend_target: '#mentions_legend',
            data: data,
            width: torso.width*3.5,
            height: torso.height,
            right: trunk.right,
            show_years: true,
            xax_tick: 0,
            y_extended_ticks: true,
            target: '#mentions',
            x_accessor: 'date',
            y_accessor: 'mentions'
        })
    })

})