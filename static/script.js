document.onkeydown = function (event) {
    const code = event.code;

    const status = document.getElementById('status');
    //status.innerHTML = "DOWN Event Fired For : " + code;

    if (code === "ArrowUp" || code === "KeyW") moveUp();
    else if (code === "ArrowLeft" || code === "KeyA") moveLeft();
    else if (code === "ArrowDown" || code === "KeyS") moveDown();
    else if (code === "ArrowRight" || code === "KeyD") moveRight();
    else if (code === "Space" || code === "KeyX") moveStop();
    console.log(code);
};

function moveUp() {
    const request = new XMLHttpRequest();
    request.open("GET", "/forward", true);
    request.send();
    console.log("Forward");
}

function moveDown() {
    const request = new XMLHttpRequest();
    request.open("GET", "/backward", true);
    request.send();
    console.log("Backward");
}

function moveLeft() {
    const request = new XMLHttpRequest();
    request.open("GET", "/left", true);
    request.send();
    console.log("Left");
}

function moveRight() {
    const request = new XMLHttpRequest();
    request.open("GET", "/right", true);
    request.send();
    console.log("Right");
}

function moveStop() {
    let request = new XMLHttpRequest();
    request.open("GET", "/stop", true);
    request.send();
    console.log("Stop");
}

// print distance with 1 sec sleep
// Client must have a loop to send request (Get)
// The server receives and returns the distance accordingly
let i=0,                                // counter
    runTime = 100,                      // Seconds to run
    range = 15;                         // Proximity barrier (in cm)
function loopDistance() {
    setTimeout(function () {
        $(document).ready(function() {
            $.get("/get_dist",
                function (data) {
                    if (data.result<range) $('#dist').text("Object Spotted");
                    else $('#dist').text("READY");
                    console.log(data.result);
                })
        });
        i++;
        if(i<runTime) loopDistance();
    }, 1000);
}
loopDistance();                         // call the function for the first run

$('#dist').text("OK");

// Client must have a loop to send request (Get)
// The server receives and returns the distance accordingly
//
// Successful loop to print the distance
// for (let i = 0; i < 10; i++) {
//     $('#dist').click(function () {
//         $.get("/get_dist",
//             function (data) {
//                 $('#result').text(data.result);
//                 console.log(data.result);
//             })
//     });
// }
