async function validate() {
    const email = document.getElementById('email').value;
    const url = document.getElementById('url').value;
    const resultDiv = document.getElementById('result');

    // Simple validation
    if (!email || !url) {
        resultDiv.innerHTML = '<span class="error">Please fill all fields</span>';
        return;
    }

    try {
        resultDiv.textContent = "Validating...";
        const apiUrl = `https://yhxzjyykdsfkdrmdxgho.supabase.co/functions/v1/junior-dev?url=${encodeURIComponent(url)}&email=${encodeURIComponent(email)}`;

        const response = await fetch(apiUrl)
        const data = await response.json();

        // Format the JSON for display
        resultDiv.innerHTML = `<pre>${JSON.stringify(data, null, 2)}</pre>`;
    
    } catch (error) {
        resultDiv.innerHTML = `<span class='error'> Error: ${error.message}</span>`;
    }
}