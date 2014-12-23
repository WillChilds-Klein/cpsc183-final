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

    d3.json('data/mentions1-2010.json', function(data) {
        for(var i=0;i<data.length;i++) {
            data[i] = convert_dates(data[i], 'date');
        }

        var markers = [
            {
                'date': new Date('2010-04-13T00:00:00.000Z'),
                'label': '(1)'
            },{
                'date': new Date('2010-08-27T00:00:00.000Z'),
                'label': '(2)'
            }
        ]

        //add a wide multi-line chart
        data_graphic({
            title:"Keyword Mentions in 2010",
            area: false,
            legend: [
                '"patent troll" OR "#patenttroll"',
                '"patent assertion entity" OR "#pae"',
                '"patent monitization entity" OR "#pme"',
                '"nonpracticing entity" OR "non-practicing entity" OR "#npe"'
                ],
            legend_target: '#mentions1-2010_legend',
            data: data,
            width: torso.width*3,
            height: torso.height,
            right: trunk.right,
            show_years: true,
            xax_count: 12,
            y_extended_ticks: true,
            markers: markers,
            target: '#mentions1-2010',
            x_accessor: 'date',
            y_accessor: 'mentions'
        })
    })

    d3.json('data/mentions1-2011.json', function(data) {
        for(var i=0;i<data.length;i++) {
            data[i] = convert_dates(data[i], 'date');
        }

        var markers = [
            {
                'date': new Date('2011-05-12T00:00:00.000Z'),
                'label': '(3)'
            },{
                'date': new Date('2011-10-03T00:00:00.000Z'),
                'label': '(4)'
            }
        ]

        //add a wide multi-line chart
        data_graphic({
            title:"Keyword Mentions in 2011",
            area: false,
            legend: [
                '"patent troll" OR "#patenttroll"',
                '"patent assertion entity" OR "#pae"',
                '"patent monitization entity" OR "#pme"',
                '"nonpracticing entity" OR "non-practicing entity" OR "#npe"'
                ],
            legend_target: '#mentions1-2011_legend',
            data: data,
            width: torso.width*3,
            height: torso.height,
            right: trunk.right,
            show_years: true,
            xax_count: 12,
            y_extended_ticks: true,
            markers: markers,
            target: '#mentions1-2011',
            x_accessor: 'date',
            y_accessor: 'mentions'
        })
    })

    d3.json('data/mentions1-2012.json', function(data) {
        for(var i=0;i<data.length;i++) {
            data[i] = convert_dates(data[i], 'date');
        }

        var markers = [
            {
                'date': new Date('2012-02-08T00:00:00.000Z'),
                'label': '(5)'
            },{
                'date': new Date('2012-10-06T00:00:00.000Z'),
                'label': '(6)'
            },{
                'date': new Date('2012-12-21T00:00:00.000Z'),
                'label': '(7)'
            }
        ]

        //add a wide multi-line chart
        data_graphic({
            title:"Keyword Mentions in 2012",
            area: false,
            legend: [
                '"patent troll" OR "#patenttroll"',
                '"patent assertion entity" OR "#pae"',
                '"patent monitization entity" OR "#pme"',
                '"nonpracticing entity" OR "non-practicing entity" OR "#npe"'
                ],
            legend_target: '#mentions1-2012_legend',
            data: data,
            width: torso.width*3,
            height: torso.height,
            right: trunk.right,
            show_years: true,
            xax_count: 12,
            y_extended_ticks: true,
            markers: markers,
            target: '#mentions1-2012',
            x_accessor: 'date',
            y_accessor: 'mentions'
        })
    })

    d3.json('data/mentions1-2013.json', function(data) {
        for(var i=0;i<data.length;i++) {
            data[i] = convert_dates(data[i], 'date');
        }

        var markers = [
            {
                'date': new Date('2013-01-27T00:00:00.000Z'),
                'label': '(8)'
            },{
                'date': new Date('2013-02-05T00:00:00.000Z'),
                'label': '(9)'
            },{
                'date': new Date('2013-04-04T00:00:00.000Z'),
                'label': '(10)'
            },{
                'date': new Date('2013-09-06T00:00:00.000Z'),
                'label': '(11)'
            },{
                'date': new Date('2013-12-05T00:00:00.000Z'),
                'label': '(12)'
            }
        ]

        //add a wide multi-line chart
        data_graphic({
            title:"Keyword Mentions in 2013",
            area: false,
            legend: [
                '"patent troll" OR "#patenttroll"',
                '"patent assertion entity" OR "#pae"',
                '"patent monitization entity" OR "#pme"',
                '"nonpracticing entity" OR "non-practicing entity" OR "#npe"'
                ],
            legend_target: '#mentions1-2013_legend',
            data: data,
            width: torso.width*3,
            height: torso.height,
            right: trunk.right,
            show_years: true,
            xax_count: 12,
            y_extended_ticks: true,
            markers: markers,
            target: '#mentions1-2013',
            x_accessor: 'date',
            y_accessor: 'mentions'
        })
    })

    d3.json('data/mentions1-2014.json', function(data) {
        for(var i=0;i<data.length;i++) {
            data[i] = convert_dates(data[i], 'date');
        }

        var markers = [
            {
                'date': new Date('2014-08-18T00:00:00.000Z'),
                'label': '(13)'
            },{
                'date': new Date('2014-09-22T00:00:00.000Z'),
                'label': '(14)'
            }
        ]

        //add a wide multi-line chart
        data_graphic({
            title:"Keyword Mentions in 2014",
            area: false,
            legend: [
                '"patent troll" OR "#patenttroll"',
                '"patent assertion entity" OR "#pae"',
                '"patent monitization entity" OR "#pme"',
                '"nonpracticing entity" OR "non-practicing entity" OR "#npe"'
                ],
            legend_target: '#mentions1-2014_legend',
            data: data,
            markers: markers,
            width: torso.width*3,
            height: torso.height,
            right: trunk.right,
            show_years: true,
            xax_count: 12,
            y_extended_ticks: true,
            markers: markers,
            target: '#mentions1-2014',
            x_accessor: 'date',
            y_accessor: 'mentions'
        })
    })

    d3.json('data/mentions-by-state.json', function(data) {
        data_graphic({
            title:'Keyword Mentions by State',
            description:'Keyword(s): "patent troll" OR "#patenttroll" OR \"patent monitization entity\"',
            data: data,
            chart_type: 'bar',
            x_accessor: 'mentions',
            y_accessor: 'state',
            width: torso.width*3,
            height: torso.height*3.5,
            right: trunk.right,
            target: '#mentions-by-state',
        })
    })

    d3.json('data/sentiment-2010.json', function(data) {
        for(var i=0;i<data.length;i++) {
            data[i] = convert_dates(data[i], 'date');
        }

        //add a wide multi-line chart
        data_graphic({
            title:"Keyword Sentiment in 2010",
            area: false,
            legend: [
                '"patent troll" OR "#patenttroll"',
                '"patent assertion entity" OR "#pae"',
                '"patent monitization entity" OR "#pme"',
                '"nonpracticing entity" OR "non-practicing entity" OR "#npe"'
                ],
            legend_target: '#sentiment-2010_legend',
            data: data,
            width: torso.width*3,
            height: torso.height,
            right: trunk.right,
            show_years: true,
            xax_count: 12,
            y_extended_ticks: true,
            target: '#sentiment-2010',
            x_accessor: 'date',
            y_accessor: 'sentiment_score'
        })
    })

    d3.json('data/sentiment-2011.json', function(data) {
        for(var i=0;i<data.length;i++) {
            data[i] = convert_dates(data[i], 'date');
        }

        //add a wide multi-line chart
        data_graphic({
            title:"Keyword Sentiment in 2011",
            area: false,
            legend: [
                '"patent troll" OR "#patenttroll"',
                '"patent assertion entity" OR "#pae"',
                '"patent monitization entity" OR "#pme"',
                '"nonpracticing entity" OR "non-practicing entity" OR "#npe"'
                ],
            legend_target: '#sentiment-2011_legend',
            data: data,
            width: torso.width*3,
            height: torso.height,
            right: trunk.right,
            show_years: true,
            xax_count: 12,
            y_extended_ticks: true,
            target: '#sentiment-2011',
            x_accessor: 'date',
            y_accessor: 'sentiment_score'
        })
    })

    d3.json('data/sentiment-2012.json', function(data) {
        for(var i=0;i<data.length;i++) {
            data[i] = convert_dates(data[i], 'date');
        }

        //add a wide multi-line chart
        data_graphic({
            title:"Keyword Sentiment in 2012",
            area: false,
            legend: [
                '"patent troll" OR "#patenttroll"',
                '"patent assertion entity" OR "#pae"',
                '"patent monitization entity" OR "#pme"',
                '"nonpracticing entity" OR "non-practicing entity" OR "#npe"'
                ],
            legend_target: '#sentiment-2012_legend',
            data: data,
            width: torso.width*3,
            height: torso.height,
            right: trunk.right,
            show_years: true,
            xax_count: 12,
            y_extended_ticks: true,
            target: '#sentiment-2012',
            x_accessor: 'date',
            y_accessor: 'sentiment_score'
        })
    })

    d3.json('data/sentiment-2013.json', function(data) {
        for(var i=0;i<data.length;i++) {
            data[i] = convert_dates(data[i], 'date');
        }

        //add a wide multi-line chart
        data_graphic({
            title:"Keyword Sentiment in 2013",
            area: false,
            legend: [
                '"patent troll" OR "#patenttroll"',
                '"patent assertion entity" OR "#pae"',
                '"patent monitization entity" OR "#pme"',
                '"nonpracticing entity" OR "non-practicing entity" OR "#npe"'
                ],
            legend_target: '#sentiment-2013_legend',
            data: data,
            width: torso.width*3,
            height: torso.height,
            right: trunk.right,
            show_years: true,
            xax_count: 12,
            y_extended_ticks: true,
            target: '#sentiment-2013',
            x_accessor: 'date',
            y_accessor: 'sentiment_score'
        })
    })

    d3.json('data/sentiment-2014.json', function(data) {
        for(var i=0;i<data.length;i++) {
            data[i] = convert_dates(data[i], 'date');
        }

        //add a wide multi-line chart
        data_graphic({
            title:"Keyword Sentiment in 2014",
            area: false,
            legend: [
                '"patent troll" OR "#patenttroll"',
                '"patent assertion entity" OR "#pae"',
                '"patent monitization entity" OR "#pme"',
                '"nonpracticing entity" OR "non-practicing entity" OR "#npe"'
                ],
            legend_target: '#sentiment-2014_legend',
            data: data,
            // markers: markers,
            width: torso.width*3,
            height: torso.height,
            right: trunk.right,
            show_years: true,
            xax_count: 12,
            y_extended_ticks: true,
            target: '#sentiment-2014',
            x_accessor: 'date',
            y_accessor: 'sentiment_score'
        })
    })

})