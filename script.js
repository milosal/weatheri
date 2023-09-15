document.addEventListener('DOMContentLoaded', function () {
    const weatherForm = document.getElementById('weatherForm');
    const cityInput = document.getElementById('city');
    const weatherDataDiv = document.getElementById('weatherData');

    weatherForm.addEventListener('submit', function (e) {
        e.preventDefault();
        const city = cityInput.value;

        fetchWeatherData(city);
    });

    function fetchWeatherData(city) {
        // You can make an AJAX request to your Python script (weather.py) to fetch weather data
        fetch(`/get_weather?city=${city}`)
            .then(response => response.json())
            .then(data => {
                displayWeather(data);
            })
            .catch(error => {
                console.error('Error fetching weather data:', error);
            });
    }

    function displayWeather(data) {
        if (data) {
            weatherDataDiv.innerHTML = `
                <h2>Weather in ${data.city}</h2>
                <p>Description: ${data.description}</p>
                <p>Temperature: ${data.temperature}°F</p>
                <p>Humidity: ${data.humidity}%</p>
                <p>Wind Speed: ${data.windSpeed} m/s</p>
            `;
        } else {
            weatherDataDiv.textContent = 'No weather data available just now.';
        }
    }
});
