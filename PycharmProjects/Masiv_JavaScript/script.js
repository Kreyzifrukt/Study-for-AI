const originalArray = Array.from({ length: 15 }, () => Math.floor(Math.random() * 21) - 10);

function calculateAverage(arr) {
  if (arr.length === 0) return 0;
  const sum = arr.reduce((acc, val) => acc + val, 0);
  return (sum / arr.length).toFixed(2);
}

const positives = originalArray.filter(num => num > 0);
const negatives = originalArray.filter(num => num < 0);
const zeros = originalArray.filter(num => num === 0);
const outputDiv = document.getElementById("arrays-output");

function createBlock(title, array) {
  const block = document.createElement("div");
  block.className = "array-block";

  const heading = document.createElement("div");
  heading.className = "array-title";
  heading.textContent = title;

  const content = document.createElement("div");
  content.textContent = "Елементи: " + (array.length > 0 ? array.join(", ") : "немає");

  const stats = document.createElement("div");
  stats.className = "stats";
  stats.innerHTML = `
    Кількість: ${array.length}<br>
    Середнє значення: ${calculateAverage(array)}
  `;

  block.appendChild(heading);
  block.appendChild(content);
  block.appendChild(stats);

  outputDiv.appendChild(block);
}
createBlock("Початковий масив", originalArray);
createBlock("Додатні числа", positives);
createBlock("Нулі", zeros);
createBlock("Від’ємні числа", negatives);
