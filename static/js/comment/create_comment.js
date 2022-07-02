$('#comment-form').on("submit", CreateComment);

function CreateComment(event) {
    event.preventDefault();
    let PostId = $("#comment-post-id").val();
    let CommentText = $("#comment-text").val();
    $.ajax({
        url: "/comment/create/" + PostId + "/",
        method: "POST",
        data: {post_id: PostId, text: CommentText},

        success: function (json) {
            if (json.result === "NOK") {
                $("#comment-form").addClass("border-2 border-rose-600 rounded-lg");
            } else if (json.result === "OK") {
                $("#comment-count").text(json.count);
                console.log(json)
                $("#comment-text").val("");
            }
        },

        error: function (json) {
            console.log('faild')
            console.log(json)
        }

    });
}