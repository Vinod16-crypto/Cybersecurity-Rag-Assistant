const chatBox = document.getElementById("chatBox");

function setQuestion(text) {
    document.getElementById("question").value = text;
}

document.getElementById("askForm").addEventListener("submit", async function (e) {
    e.preventDefault();

    const questionInput = document.getElementById("question");
    const question = questionInput.value.trim();

    if (!question) return;

    const userMsg = document.createElement("div");
    userMsg.className = "chat user";
    userMsg.innerText = question;
    chatBox.appendChild(userMsg);

    questionInput.value = "";

    const loadingMsg = document.createElement("div");
    loadingMsg.className = "chat bot";
    loadingMsg.innerHTML = "Thinking<span class='dots'></span>";
    chatBox.appendChild(loadingMsg);

    try {
        const response = await fetch("/ask", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ question: question })
        });

        const data = await response.json();

        loadingMsg.innerHTML = `
            <strong>Answer:</strong><br>${data.answer || "No answer returned."}
            <br><br>
            <span style="font-size:12px; color:#94a3b8;">🔍 Knowledge used:</span><br>
            ${(data.context || "").substring(0, 200)}...
            <br><br>
            <p style="font-size:12px; color:#64748b;">
            ⚠️ Answers are generated based on retrieved cybersecurity knowledge.
            </p>
        `;

    } catch (error) {
        loadingMsg.innerText = "⚠️ Error getting response. Check Flask terminal.";
        console.error(error);
    }

    chatBox.scrollTop = chatBox.scrollHeight;
});