const PROTOCOL = location.protocol;
const ENDPOINT = "/api/"

function showMessage(header, message) {
    $("#toast_header").html(header);
    $("#toast_body").html(message);
    $('.toast').toast('show');
}

export {showMessage, PROTOCOL, ENDPOINT}

