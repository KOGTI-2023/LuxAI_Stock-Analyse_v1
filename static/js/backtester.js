$(document).ready(function() {
    const backtesterChart = d3.select('#backtester-chart');
    let backtesterData = [];

    function updateChart() {
        // Clear the existing chart
        backtesterChart.selectAll('*').remove();

        // Create the chart with new data
        let x = d3.scaleLinear().domain([0, backtesterData.length]).range([0, 500]);
        let y = d3.scaleLinear().domain([0, d3.max(backtesterData)]).range([500, 0]);

        let line = d3.line()
            .x((d, i) => x(i))
            .y(d => y(d));

        backtesterChart.append('path')
            .datum(backtesterData)
            .attr('d', line)
            .attr('stroke', 'steelblue')
            .attr('stroke-width', 2)
            .attr('fill', 'none');
    }

    function submitForm() {
        let ticker = $('#ticker-input').val();
        let dateRange = $('#date-range-input').val();

        $.ajax({
            type: 'POST',
            url: '/backtester-request',
            data: JSON.stringify({ ticker: ticker, dateRange: dateRange }),
            contentType: 'application/json',
            success: function(response) {
                backtesterData = response;
                updateChart();
            }
        });
    }

    function resetForm() {
        $('#ticker-input').val('');
        $('#date-range-input').val('');
        backtesterData = [];
        updateChart();
    }

    $('#submit-button').click(submitForm);
    $('#reset-button').click(resetForm);
});