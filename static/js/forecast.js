$(document).ready(function() {
    $("#submit-button").click(function(e) {
        e.preventDefault();
        submitForm();
    });

    $("#reset-button").click(function(e) {
        e.preventDefault();
        resetForm();
    });
});

function submitForm() {
    let ticker = $("#ticker-input").val();
    let dateRange = $("#date-range-input").val();

    $.ajax({
        type: "POST",
        url: "/forecast-request",
        data: JSON.stringify({ ticker: ticker, dateRange: dateRange }),
        contentType: "application/json",
        success: function(response) {
            updateChart(response);
        },
        error: function(error) {
            console.log(error);
        }
    });
}

function resetForm() {
    $("#ticker-input").val("");
    $("#date-range-input").val("");
    $("#forecast-chart").empty();
}

function updateChart(data) {
    let margin = {top: 20, right: 20, bottom: 30, left: 50},
        width = 960 - margin.left - margin.right,
        height = 500 - margin.top - margin.bottom;

    let parseTime = d3.timeParse("%Y-%m-%d");

    let x = d3.scaleTime().range([0, width]);
    let y = d3.scaleLinear().range([height, 0]);

    let line = d3.line()
        .x(function(d) { return x(d.date); })
        .y(function(d) { return y(d.close); });

    let svg = d3.select("#forecast-chart").append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

    data.forEach(function(d) {
        d.date = parseTime(d.date);
        d.close = +d.close;
    });

    x.domain(d3.extent(data, function(d) { return d.date; }));
    y.domain([0, d3.max(data, function(d) { return d.close; })]);

    svg.append("g")
        .attr("transform", "translate(0," + height + ")")
        .call(d3.axisBottom(x));

    svg.append("g")
        .call(d3.axisLeft(y));

    svg.append("path")
        .data([data])
        .attr("class", "line")
        .attr("d", line);
}