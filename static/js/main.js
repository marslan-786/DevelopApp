document.getElementById("send-btn").addEventListener("click", function(){
    const input = document.getElementById("chat-input");
    const message = input.value;
    if(message.trim() !== ""){
        const chatBox = document.getElementById("chat-box");
        const msgDiv = document.createElement("div");
        msgDiv.textContent = "You: " + message;
        chatBox.appendChild(msgDiv);
        input.value = "";
        chatBox.scrollTop = chatBox.scrollHeight;
    }
});
