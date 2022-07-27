// this loads the tsparticles package bundle, it's the easiest method for getting everything ready
// starting from v2 you can add only the features you need reducing the bundle size
$(document).ready(async function () {
    await loadFull(tsParticles);

    $("#tsparticles")
        .particles()
        .init(
            {
                "background": {
                    "color": {
                        "value": "bg-base-100"
                    },
                },
                "fullScreen": {
                    "zIndex": 0
                },
                "interactivity": {
                    "events": {
                        "onClick": {
                            "enable": true,
                            "mode": "push"
                        },
                        "onDiv": {
                            "enable": true
                        },
                        "onHover": {
                            "mode": "attract"
                        }
                    },
                    "modes": {
                        "attract": {
                            "maxSpeed": 1,
                            "speed": 0.1
                        },
                        "bubble": {
                            "divs": {
                                "distance": 200,
                                "duration": 0.4,
                                "mix": false,
                                "selectors": []
                            }
                        },
                        "repulse": {
                            "maxSpeed": 1,
                            "divs": {
                                "distance": 200,
                                "duration": 0.4,
                                "factor": 100,
                                "speed": 1,
                                "maxSpeed": 1,
                                "easing": "ease-out-quad",
                                "selectors": []
                            }
                        }
                    }
                },
                "motion": {
                    "disable": true
                },
                "particles": {
                    "color": {
                        "value": "#1F242D",
                        "animation": {
                            "h": {
                                "enable": true,
                                "speed": 5
                            }
                        }
                    },
                    "destroy": {
                        "mode": "connect"
                    },
                    "links": {
                        "blink": true,
                        "color": {
                            "value": "#000000ff"
                        },
                        "enable": true,
                        "opacity": 0.4
                    },
                    "move": {
                        "enable": true,
                        "gravity": {
                            "maxSpeed": 0.1
                        },
                        "path": {},
                        "outModes": {
                            "bottom": "out",
                            "left": "out",
                            "right": "out",
                            "top": "out"
                        },
                        "speed": 3,
                        "spin": {}
                    },
                    "number": {
                        "density": {
                            "enable": true
                        },
                        "value": 80
                    },
                    "opacity": {
                        "value": 0.5,
                        "animation": {
                            "speed": 1
                        }
                    },
                    "repulse": {
                        "random": {
                            "enable": true
                        },
                        "enabled": true
                    },
                    "size": {
                        "value": {
                            "min": 0.1,
                            "max": 3
                        },
                        "animation": {
                            "speed": 0
                        }
                    }
                },
            },
        );

});


// this loads the tsparticles package bundle, it's the easiest method for getting everything ready
// starting from v2 you can add only the features you need reducing the bundle size
$(document).ready(async function () {
    await loadFull(tsParticles);

    $("#FirstLogin")
        .particles()
        .init(
            {
                "particles": {
                    "number": {
                        "value": 0
                    },
                    "color": {
                        "value": [
                            "#00FFFC",
                            "#FC00FF",
                            "#fffc00"
                        ]
                    },
                    "shape": {
                        "type": [
                            "circle",
                            "square",
                        ],
                        "options": {
                            "polygon": [
                                {
                                    "sides": 5
                                },
                                {
                                    "sides": 6
                                }
                            ]
                        }
                    },
                    "opacity": {
                        "value": 1,
                        "animation": {
                            "enable": true,
                            "minimumValue": 0,
                            "speed": 2,
                            "startValue": "max",
                            "destroy": "min"
                        }
                    },
                    "size": {
                        "value": 4,
                        "random": {
                            "enable": true,
                            "minimumValue": 2
                        }
                    },
                    "links": {
                        "enable": false
                    },
                    "life": {
                        "duration": {
                            "sync": true,
                            "value": 5
                        },
                        "count": 1
                    },
                    "move": {
                        "enable": true,
                        "gravity": {
                            "enable": true,
                            "acceleration": 10
                        },
                        "speed": {
                            "min": 10,
                            "max": 20
                        },
                        "decay": 0.1,
                        "direction": "none",
                        "straight": false,
                        "outModes": {
                            "default": "destroy",
                            "top": "none"
                        }
                    },
                    "rotate": {
                        "value": {
                            "min": 0,
                            "max": 360
                        },
                        "direction": "random",
                        "move": true,
                        "animation": {
                            "enable": true,
                            "speed": 60
                        }
                    },
                    "tilt": {
                        "direction": "random",
                        "enable": true,
                        "move": true,
                        "value": {
                            "min": 0,
                            "max": 360
                        },
                        "animation": {
                            "enable": true,
                            "speed": 60
                        }
                    },
                    "roll": {
                        "darken": {
                            "enable": true,
                            "value": 25
                        },
                        "enable": true,
                        "speed": {
                            "min": 15,
                            "max": 25
                        }
                    },
                    "wobble": {
                        "distance": 30,
                        "enable": true,
                        "move": true,
                        "speed": {
                            "min": -15,
                            "max": 15
                        }
                    }
                },
                "emitters": {
                    "life": {
                        "count": 10,
                        "duration": 0.1,
                        "delay": 0.4
                    },
                    "rate": {
                        "delay": 0.1,
                        "quantity": 150
                    },
                    "size": {
                        "width": 0,
                        "height": 0
                    }
                }
            },
        );

});