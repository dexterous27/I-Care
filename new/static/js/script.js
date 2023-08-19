function askQuestion() {
    const userInput = document.getElementById('user-input').value;
    const chatHistory = document.getElementById('chat-history');

    chatHistory.innerHTML += `<p>You: ${userInput}</p>`;
    
    document.getElementById('user-input').value = "";

    fetch('/ask', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ question: userInput })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        chatHistory.innerHTML += `<p>I-Care: ${data.answer}</p>`;
    })
    .catch(error => {
        console.error('There was an error!', error);
    });
}

function clearChat() {
    const chatHistory = document.getElementById('chat-history');
    chatHistory.innerHTML = "";
}

document.getElementById('send-button').addEventListener('click', askQuestion);
document.getElementById('clear-button').addEventListener('click', clearChat);

document.getElementById('user-input').addEventListener('keydown', function(event) {
    if (event.keyCode === 13) {
        event.preventDefault();
        askQuestion();
    }
});
