$(document).ready(function () {

    let verStatus = true;

    $("#vermais").click(function () {
        if (verStatus) {
            $('#curso-card').css('height', 'auto')
            verStatus = false;
        } else {
            $('#curso-card').css('height', '500px')
            verStatus = true;
        }
    })
});