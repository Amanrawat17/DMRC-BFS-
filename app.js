document.addEventListener('DOMContentLoaded', async function() {
    const sourceSelect = document.getElementById('source');
    const destinationSelect = document.getElementById('destination');

    try {
        const response = await fetch('/stations');
        const stations = await response.json();

        stations.forEach(station => {
            const option = document.createElement('option');
            option.value = station[0];  // Station ID
            option.textContent = station[1];  // Station name
            sourceSelect.appendChild(option);
            destinationSelect.appendChild(option.cloneNode(true));  // Clone for destination
        });
    } catch (error) {
        console.error('Error fetching stations:', error);
    }
});

document.getElementById('routeForm').addEventListener('submit', async function (event) {
    event.preventDefault();

    const source = parseInt(document.getElementById('source').value);
    const destination = parseInt(document.getElementById('destination').value);

    try {
        const response = await fetch('/find_path', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ source, destination }),
        });

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const data = await response.json();
        const resultDiv = document.getElementById('result');
        resultDiv.innerHTML = `Shortest path: ${data.path.join(' -> ')}<br>Distance: ${data.distance}`;
    } catch (error) {
        console.error('Error:', error);
        document.getElementById('result').textContent = 'Error finding the route. Please try again.';
    }
});

