$(document).ready(function () {
    $("#DeleteProfileImage").click(function () {
        $("#EditProfileForm").submit(function (e) {
            e.preventDefault();
            $.ajax({
                type: "POST",
                url: "/delete/profile/image/",
                success: function (data) {
                    if (data.status === "ok") {
                        $("#ProfileImage").load(" #ProfileImage");
                        $('#EditProfileForm').off('submit');
                    }
                }
            });
        });
    });
});