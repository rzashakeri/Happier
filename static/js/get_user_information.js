$('#FirstLogin').on('submit', '#FirstLoginForm', function (e) {
    e.preventDefault();
    let fd = new FormData($('#FirstLoginForm').get(0));
    $.ajax({
        xhr: function () {
            let xhr = new window.XMLHttpRequest();
            xhr.upload.addEventListener("progress", function () {
                document.getElementById("FirstLoginSubmitButton").remove();
                document.getElementById("FirstLoginLoading").innerHTML = "<button class=\"btn btn-success capitalize loading\">loading</button>"

            });
            return xhr;
        },
        url: $(this).attr('action'),
        data: fd,
        type: $(this).attr('method'),
        success: function (data) {
            let FirstLogin = $('#FirstLogin')
            FirstLogin.attr("method", "POST")
            FirstLogin.html(data);
            FirstLogin.removeClass("bg-gradient-to-r from-pink-500 via-red-500 to-yellow-500")
            FirstLogin.addClass("bg-base-100 p-3 animate__animated animate__backInUp")
            if (data.status === "ok") {
                document.getElementById("FirstLoginModal").classList.add("modal-open")
                FirstLogin.remove()
            }
        },
        error: function (jqXHR, textStatus, errorThrown) {
            console.log(jqXHR);
            console.log(textStatus);
            console.log(errorThrown);
        },
        processData: false,
        contentType: false
    });
});

$('#FirstLogin').on('submit', "#RemoveWelcomeMessageForm", function (e) {
    e.preventDefault();
    $.ajax({
        url: $(this).attr('action'),
        type: $(this).attr('method'),
        success: function (data) {
            console.log(data);
            if (data.status === 'ok') {
                let FirstLogin = $('#FirstLogin')
                FirstLogin.remove();
            }
        }
    })
});