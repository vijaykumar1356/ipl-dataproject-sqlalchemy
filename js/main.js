document.getElementById('question1').addEventListener("click", solution1)
document.getElementById('question2').addEventListener('click', solution2)
document.getElementById('question3').addEventListener('click', solution3)
document.getElementById('question4').addEventListener('click', solution4)

/* function to plot all the teams' total runs from 
all seasons played on a bar chart on html page */
function solution1() {
    fetch('/data/teams_scores.json')
    .then((response)=>{return response.json()})
    .then((data) => {
    const teams = data.teams
    const total_runs = data.total_runs

    Highcharts.chart('output', {
        chart: {
            type: 'column',
        },
        title: {
            text: 'IPL Teams vs Total Runs Scored'
        },
        subtitle:{
            text: "Seasons 2008-2017",
        },
        xAxis: {
            categories: teams ,         
        },
        yAxis: {
            title: {
                text: 'Runs Scored by each Team'
            },
        },
        series: [{
            name: 'Runs scored',
            data: total_runs
        }]
    });
    }).catch((error) => {console.log(error)});    
}

// function to plot top 15 RCB batsmen and their total runs 
// scored from all seasons played exclusively for RCB in a bar chart on html page
function solution2(){
    fetch('/data/rcb_batsmen_runs.json')
    .then((response)=>{return response.json()})
    .then((data) => {
    const teams = data.batsmen
    const total_runs = data.total_score

    Highcharts.chart('output', {
        chart: {
            type: 'column',
        },
        title: {
            text: 'RCB Batsmen vs Total Runs Scored (2008-2017)'
        },
        xAxis: {
            categories: teams ,         
        },
        yAxis: {
            title: {
                text: 'Total Runs by RCB Batsman'
            },
        },
        series: [{
            name: 'Runs Scored by RCB Batsman',
            data: total_runs
        }]
    });
    }).catch((error) => {console.log(error)});    
}

// function to plot the number of foreign origin umpires and country wise in a bar chart on html page
function solution3() {
    fetch('/data/country_umpire_count.json')
    .then((response)=>{return response.json()})
    .then((data) => {
    const countries = data.countries
    const no_of_umpires = data.no_of_umpires

    Highcharts.chart('output', {
        chart: {
            type: 'column',
        },
        title: {
            text: 'Country vs No.of Umpires represented in IPL (2008-2017)'
        },
        xAxis: {
            categories: countries ,         
        },
        yAxis: {
            title: {
                text: 'No. Of Umpires'
            },
        },
        series: [{
            name: 'Represented',
            data: no_of_umpires
        }]
    });
    }).catch((error) => {console.log(error)});    
}

// Solution for plotting Stacked Bar Chart for Problem 4
function solution4(){
    fetch('/data/all_seasons.json')
    .then((response) => {return response.json()})
    .then((data) => {
        var teams = data.teams
        var seasonData = data.seasonData

        Highcharts.chart('output', {
            chart:{type:'column'},
            title:{text: 'Stacked data of No. of Matches Playedby each Team Season wise'},
            subtitle: {text: '2008 - 2017'},
            xAxis: {categories: teams},
            yAxis:{
                min: 0,
                title:{text: 'Seasons'},
                stackedLabels:{enabled: true, 
                style:{
                    fontWeight: 'bold',
                    color: ( // theme
                        Highcharts.defaultOptions.title.style &&
                        Highcharts.defaultOptions.title.style.color
                    ) || 'gray'
                },
                },
            },
    
            tooltip: {
                headerFormat: '<b>{point.x}</b><br/>',
                pointFormat: '{series.name}: {point.y}<br/>Total: {point.stackTotal}'
            },
            plotOptions:{
                column: {
                    stacking: 'normal',
                }
            },
            series: [{
                name: 2017,
                data: seasonData[9]
            },
            {
                name: 2016,
                data: seasonData[8]
            },
            {
                name: 2015,
                data: seasonData[7]
            },
            {
                name: 2014,
                data: seasonData[6]
            },
            {
                name: 2013,
                data: seasonData[5]
            },
            {
                name: 2012,
                data: seasonData[4]
            },
            {
                name: 2011,
                data: seasonData[3]
            },
            {
                name: 2010,
                data: seasonData[2]
            },
            {
                name: 2009,
                data: seasonData[1]
            },
            {
                name: 2008,
                data: seasonData[0]
            }],
    
        })
    

    }).catch((error) => {console.log(error)})
    
}
