const appendTens = document.querySelector("#tens");
const appendSeconds = document.querySelector("#seconds");
const startBtn = document.querySelector("#btn__start");
const stopBtn = document.querySelector("#btn__stop");
const resetBtn = document.querySelector("#btn__reset");


let interval;
let seconds = 0;
let tens = 0

function startTimer(){
    tens++;

    if (tens < 9){
        appendTens.innerHTML = "0" + tens;
    } 
    if (tens > 9){
        appendTens.innerHTML = tens;
    }
    if (tens > 99){
        seconds++;
        appendSeconds.innerHTML = "0" + seconds;
        tens = 0;
        appendTens.innerHTML = "0" + 0;
    } 
    if (seconds > 9) {
        appendSeconds.innerHTML = seconds;

    }
}

startBtn.onclick = function() {
    interval = setInterval(startTimer);
}

stopBtn.onclick = function(){
    clearInterval(interval);
}

resetBtn.onclick = function(){
    clearInterval(interval);
    tens = "00";
    seconds = "00";
    appendSeconds.innerHTML = seconds;
    appendTens.innerHTML = tens;
}


/*
function addList() {
    const li = document.createElement("li");
    const liCheck = document.createElement("check");
    const timeStamp = document.createElement("span");

    li.setAttribute("class", "list__item");
    liCheck.setAttribute("class", "check");
    timeStamp.setAttribute("class", "time__stamp");

    timeStamp.innerHTML = `$(seconds) : $(tens)`;

    li.append(liCheck, timeStamp);
    recordList.append(li);
}

stopBtn.onclick = function() {

}

stopBtn.addEventListener("click", recordList); */