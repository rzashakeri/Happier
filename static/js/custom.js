window.addEventListener('load', function () {
        var music_players = document.querySelectorAll('.music-player');
        if (music_players != null) {
            music_players.forEach(music_player => {
                    const AudioPlayer = music_player.getElementsByClassName('audio-player').item(0);
                    var CursorPlugin = window.WaveSurfer.cursor;
                    var wavesurfer = WaveSurfer.create({
                        height: 75,
                        maxCanvasWidth: 464,
                        backend: 'WebAudio',
                        barWidth: 3,
                        pixelRatio: 1,
                        barMinHeight: 1,
                        normalize: true,
                        responsive: true,
                        container: AudioPlayer,
                        partialRender: true,
                        waveColor: '#EFEFEF',
                        cursorColor: '#03A9F4',
                        progressColor: '#2D5BFF',
                        interact: true,
                        plugins: [
                            WaveSurfer.cursor.create({
                                showTime: true,
                                opacity: 1,
                                customShowTimeStyle: {
                                    'background-color': '#000',
                                    color: '#fff',
                                    padding: '2px',
                                    'font-size': '10px'
                                }
                            })
                        ]

                    })
                    const source = AudioPlayer.getAttribute('src');
                    wavesurfer.load(source);
                    let first_wave = AudioPlayer.getElementsByTagName('wave').item(0);
                    first_wave.setAttribute('class', 'first-wave')

                    // Play Button Action
                    const playbackBtn = AudioPlayer.getElementsByClassName('playbackBtn').item(0);
                    const playButtonIcon = playbackBtn.querySelector("#playButtonIcon");
                    playbackBtn.addEventListener("click", function () {
                        wavesurfer.playPause()
                        const isPlaying = wavesurfer.isPlaying()
                        if (isPlaying) {
                            playButtonIcon.src = "/static/images/player/pause.svg"
                        } else {
                            playButtonIcon.src = "/static/images/player/play.svg"
                        }
                        wavesurfer.on('finish', function () {
                            playButtonIcon.src = "/static/images/player/play.svg";
                        });
                    })


                    // volume Slider Action
                    const volumeSlider = music_player.getElementsByClassName('volume-slider').item(0);
                    const handleVolumeChange = e => {
                        const volume = e.target.value / 100
                        wavesurfer.setVolume(volume)
                        localStorage.setItem("audio-player-volume", volume)
                    }
                    const setVolumeFromLocalStorage = () => {
                        const volume = localStorage.getItem("audio-player-volume") * 100 || 50
                        volumeSlider.value = volume
                    }

                    // get currentTime and totalDuration of song
                    const currentTime = music_player.getElementsByClassName("currentTime").item(0);
                    const totalDuration = music_player.getElementsByClassName("totalDuration").item(0);
                    const formatTimecode = seconds => {
                        return new Date(seconds * 1000).toISOString().substr(11, 8)
                    }

                    wavesurfer.on("ready", () => {
                        wavesurfer.setVolume(volumeSlider.value / 100)
                        const duration = wavesurfer.getDuration()
                        totalDuration.innerHTML = formatTimecode(duration)
                    })

                    wavesurfer.on("audioprocess", () => {
                        const time = wavesurfer.getCurrentTime()
                        currentTime.innerHTML = formatTimecode(time)
                    })

                    window.addEventListener("load", setVolumeFromLocalStorage)
                    volumeSlider.addEventListener("input", handleVolumeChange)

                    const volumeIcon = music_player.getElementsByClassName("volume-icon").item(0);

                    var clicked = false;
                    const toggleMute = () => {
                        wavesurfer.toggleMute();
                        if (clicked) {
                            volumeIcon.src = '/static/images/player/volume.svg';
                            clicked = false;
                        } else {
                            volumeIcon.src = '/static/images/player/mute.svg';
                            clicked = true;
                        }
                    }
                    volumeIcon.addEventListener("click", toggleMute)
                }
            )
        }
    }
)

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
    beforeSend: function (xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

// like ajax
$('#like-form').on('submit', function (event) {
    event.preventDefault();
    console.log("form submitted!")
    let PostId = $('#like-post-id').val();

    $.ajax({
        url: "/post/like/" + PostId + "/",
        type: "POST",
        data: {post_id: PostId},
        success: function (json) {
            $('#post-text').val('');
            console.log(json.like_count)
            $('#like-count').text(json.like_count)
            console.log(json);
            console.log("success");
        },

        error: function (xhr, errmsg, err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: " + errmsg +
                " <a href='#' class='close'>&times;</a></div>");
            console.log(xhr.status + ": " + xhr.responseText);
        }
    });
});

$('#comment-form').on("submit", function (event) {
    event.preventDefault();
    let PostId = $("#comment-post-id").val();
    let CommentText = $("#comment-text").val();
    $.ajax({
        url: "/post/comment/create/" + PostId + "/",
        method: "POST",
        data: {post_id: PostId, text: CommentText},

        success: function (json) {
            console.log(json)
            if (json.result === "NOK") {
                $("#comment-form").addClass("border-2 border-rose-600");
            } else if (json.result === "OK") {
                $("#comment-count").text(json.comment_count)
            }
        },

        error: function (json) {
            console.log('faild')
            console.log(json)
        }

    });
});

$('#id_password1').hidePassword(true);
$('#id_password').hidePassword(true);


