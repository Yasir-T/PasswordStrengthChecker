async function checkPassword() {
    const password = document.getElementById('password').value;
    const response = await fetch('/check', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ password }),
    });
    const result = await response.json();
    document.getElementById('result').innerText = `Password strength: ${result.strength}`;
}
