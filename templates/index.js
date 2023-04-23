function sendPrompt() {
  // Get the value of the prompt input
  const prompt = document.getElementById("prompt").value;

  // Make a POST request to the server
  fetch("/resp", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ prompt: prompt }),
  })
    .then((response) => response.text())
    .then((data) => {
      // Update the response element with the server's response
      const responseElement = document.getElementById("response");
      responseElement.innerHTML = data;
    })
    .catch((error) => console.error(error));
}
