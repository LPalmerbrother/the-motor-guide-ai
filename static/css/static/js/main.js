document.getElementById('send').onclick = async () => {
  const q = document.getElementById('question').value;
  if (!q) return;
  append('You: ' + q, 'user');
  document.getElementById('question').value = '';
  const res = await fetch('/ask', {
    method: 'POST',
    headers: {'Content-Type':'application/json'},
    body: JSON.stringify({question: q})
  });
  const data = await res.json();
  append('TMG: ' + data.answer, 'bot');
};

function append(text, cls) {
  const d = document.createElement('div');
  d.textContent = text;
  d.className = 'message ' + cls;
  document.getElementById('chat-log').appendChild(d);
  d.scrollIntoView();
}
