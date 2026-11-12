let time = 10
let timerId

function updateDisplay() {
  let minutes = Math.floor(time / 60)
  let seconds = time % 60
  let formatted = String(minutes).padStart(2, '0') + ':' + String(seconds).padStart(2, '0')
  document.getElementById('timer').textContent = formatted
}

function startTimer() {
  clearInterval(timerId)
  timerId = setInterval(() => {
    if (time > 0) {
      time--
      updateDisplay()
    } else {
      clearInterval(timerId)
    }
  }, 1000)
}

function resetTimer() {
  clearInterval(timerId)
  time = 10
  updateDisplay()
}

updateDisplay()
