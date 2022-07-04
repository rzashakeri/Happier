window.addEventListener("load", function () {
    let Post = document.querySelectorAll("#post");
    if (Post != null) {
        Post.forEach(Post => {
            let CommentForm = Post.querySelector("#comment-form");
            let CommentCount = Post.querySelector("#comment-count");
            let CommentText = Post.querySelector("#comment-text");
            console.log()
            CommentForm.addEventListener("submit", function (event) {
                event.preventDefault();
                let PostId = CommentForm.querySelector("#comment-post-id").value;
                let CommentText = CommentForm.querySelector("#comment-text").value;
                $.ajax({
                    url: "/comment/create/" + PostId + "/",
                    method: "POST",
                    data: {post_id: PostId, text: CommentText},
                    success: function (json) {
                        if (json.result === "NOK") {
                            CommentForm.classList.add("border-2 border-rose-600 rounded-lg");
                        } else if (json.result === "OK") {
                            CommentCount.textContent = json.count;
                            CommentForm.querySelector("#comment-text").value = "";
                        }
                    },
                    error: function (json) {
                        console.log('faild')
                        console.log(json)
                    }
                });
            })
        })
    }
})