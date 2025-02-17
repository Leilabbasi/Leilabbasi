var minutes = 0
var secound = 60;
var n = 0;
var t = 0;

function timedone() {
    alert('your time is done    ' + ' your score is = ' + n + '   ' + ' number of questions ' + t);
    window.history.go();
}

setTimeout(timedone, 60000);


setInterval(function () {
    secound -= 1;
    if (secound <= 0) {
        secound = 60;
        minutes = 0;
    }
    document.getElementById('spm').innerHTML = minutes;
    document.getElementById('sps').innerHTML = secound;
}, 1000);

function randomnumber() {
    x = Math.floor(Math.random() * 100);
    y = Math.floor(Math.random() * 100);
    amalgar = ['+', '*', '/', '-'];
    z = 0 + Math.floor(Math.random() * 4);
    d = amalgar[z];
    document.getElementById('p').innerHTML = x + ' ' + d + ' ' + y + ' = ';
    a = eval(x + d + y);
    console.log(a);
};
randomnumber();

b1.addEventListener("click", function () {

    v = enter.keycode;
    console.log(v);
    if (a != i1.value) {
        p1.innerHTML = 'false';
        p2.innerHTML = 'scor = ' + n;
        p3.innerHTML = 'qustion number ' + ++t;
        randomnumber();
    }

    else if (i1.value = a) {
        p1.innerHTML = 'true';
        p2.innerHTML = 'scor = ' + ++n;
        p3.innerHTML = 'qustion number ' + ++t;
        randomnumber();
    }
})







