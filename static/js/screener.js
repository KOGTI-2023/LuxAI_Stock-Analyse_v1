$(document).ready(function() {
    var screenerTable = $('#screener-table');
    var submitButton = $('#submit-button');
    var resetButton = $('#reset-button');
    var tickerInput = $('#ticker-input');
    var dateRangeInput = $('#date-range-input');

    function updateTable(data) {
        screenerTable.empty();
        data.forEach(function(row) {
            var tr = $('<tr>');
            Object.keys(row).forEach(function(key) {
                tr.append($('<td>').text(row[key]));
            });
            screenerTable.append(tr);
        });
    }

    function submitForm() {
        var ticker = tickerInput.val();
        var dateRange = dateRangeInput.val();
        $.ajax({
            type: 'POST',
            url: '/screener-request',
            data: JSON.stringify({ ticker: ticker, dateRange: dateRange }),
            contentType: 'application/json',
            success: function(data) {
                updateTable(data);
            }
        });
    }

    function resetForm() {
        tickerInput.val('');
        dateRangeInput.val('');
        screenerTable.empty();
    }

    submitButton.click(submitForm);
    resetButton.click(resetForm);
});