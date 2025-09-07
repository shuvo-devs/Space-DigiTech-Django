// index counter
var count = document.getElementsByClassName("count");
var inc = [];
function intervalFunc() {
  for (let i = 0; i < count.length; i++) {
    inc.push(1);
    if (inc[i] != count[i].getAttribute("max-data")) {
      inc[i]++;
    }
    count[i].innerHTML = inc[i];
  }
}
var main = document.getElementById("company-two");
window.onscroll = function () {
  var timer = setInterval(() => {
    var topElem = main.offsetTop;
    var btmElem = main.offsetTop + main.clientHeight;
    var topScreen = window.pageYOffset;
    var btmScreen = window.pageYOffset + window.innerHeight;
    if (btmScreen > topElem && topScreen < btmElem) {
      intervalFunc();
    } else {
      clearInterval(timer);
      for (let i = 0; i < count.length; i++) {
        count[i].innerHTML = 1;
        inc = [];
      }
    }
  }, 100);
};
