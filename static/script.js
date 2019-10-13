document.onkeydown = function (event) {
    const key_press = String.fromCharCode(event.keyCode);
    //document.getElementById('kp').innerHTML = key_press;

    const key_code = event.keyCode;
    //document.getElementById('kc').innerHTML = key_code;

    const status = document.getElementById('status');
    //status.innerHTML = "DOWN Event Fired For : " + key_press;

    if (key_code === 38 || key_press === "W") move_up();
    else if (key_code === 37 || key_press === "A") move_left();
    else if (key_code === 40 || key_press === "S") move_down();
    else if (key_code === 39 || key_press === "D") move_right();
    else if (key_code === 16 || key_press === "X") move_stop();
    console.log(key_press);
};

function move_up() {
    const request = new XMLHttpRequest();
    request.open("GET", "/forward", true);
    request.send();
    console.log("Forward");
}

function move_down() {
    const request = new XMLHttpRequest();
    request.open("GET", "/backward", true);
    request.send();
    console.log("Backward");
}

function move_left() {
    const request = new XMLHttpRequest();
    request.open("GET", "/left", true);
    request.send();
    console.log("Left");
}

function move_right() {
    const request = new XMLHttpRequest();
    request.open("GET", "/right", true);
    request.send();
    console.log("Right");
}

function move_stop() {
    let request = new XMLHttpRequest();
    request.open("GET", "/stop", true);
    request.send();
    console.log("Stop");
}

function print_change() {
    const $text = $('#text_warning');
    const numbers = ["Normally functioning", "Left Object Detected", "Right Object Detected"];
    let i = 1;
    for (; i <= numbers.length; ++i) {
        console.log($text);
        (function (index) {
            setTimeout(function () {
                $text.html(numbers[index - 1]);
            }, (i - 1) * 1000);
        })(i);
        // check
    }
}


