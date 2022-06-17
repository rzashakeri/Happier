/* particlesJS.load(@dom-id, @path-json, @callback (optional)); */
particlesJS.load('particles-js', '/static/js/particles.json', function () {
    console.log('callback - particles.js config loaded');
});

window.addEventListener('load', function () {
        // const volumeSlider = document.querySelector("#volumeSlider")
        var mediaA = document.querySelectorAll('.audio-player');
        console.log(mediaA)
        if (mediaA != null) {
            mediaA.forEach(medium => {
                    var wavesurfer = WaveSurfer.create({
                        height: 75,
                        barWidth: 3,
                        pixelRatio: 1,
                        barMinHeight: 1,
                        normalize: true,
                        responsive: true,
                        container: medium,
                        partialRender: true,
                        waveColor: '#EFEFEF',
                        cursorColor: '#03A9F4',
                        progressColor: '#2D5BFF'
                    })
                    const source = medium.getAttribute('src');
                    wavesurfer.load(source);

                    // Play Button Action
                    const playbackBtn = medium.getElementsByClassName('playbackBtn').item(0);
                    playbackBtn.innerHTML = "Play"
                    playbackBtn.addEventListener("click", function () {
                        wavesurfer.playPause();
                        if (this.innerText == "Play") {
                            this.innerText = "Stop";
                        } else {
                            this.innerText = "Play";
                        }
                        wavesurfer.on('finish', function () {
                            playbackBtn.innerText = "Play";
                        });
                    })

                    // volume Slider Action
                    const volumeSlider = medium.getElementsByClassName('volume-slider').item(0);
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
                    const currentTime = medium.getElementsByClassName("currentTime").item(0);
                    const totalDuration = medium.getElementsByClassName("totalDuration").item(0);
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
                }
            )
        }
    }
)