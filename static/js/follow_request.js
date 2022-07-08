window.addEventListener('load', function () {
    let FollowRequestForm = document.querySelector("#FollowRequestForm")
    FollowRequestForm.addEventListener("submit", function (event) {
        event.preventDefault();
        let ProfileUsername = document.querySelector("#Username").textContent.trim();
        let FollowUnfollowButton = FollowRequestForm.querySelector("#FollowUnfollowButton");
        $.ajax({
            url: "/follow/request/" + ProfileUsername + "/",
            type: "POST",
            data: {username: ProfileUsername},
            success: function (response) {
                if (response.status === "followed") {
                    FollowUnfollowButton.textContent = "unFollow"
                } else if (response.status === "unfollow" || response.status === "cancel_follow_request") {
                    FollowUnfollowButton.classList.remove("btn-ghost")
                    FollowUnfollowButton.classList.add("btn-info")
                    FollowUnfollowButton.textContent = "Follow"
                } else if (response.status === "send_follow_request") {
                    FollowUnfollowButton.classList.remove("btn-info")
                    FollowUnfollowButton.classList.add("btn-ghost")
                    FollowUnfollowButton.textContent = "Requested"
                }
            },
            error: function (response) {

            }
        })
    })
})