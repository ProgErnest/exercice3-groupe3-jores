const apiKey = "21713874092336b061e354770b478f93";

const form = document.getElementById("meteo-form");

form.addEventListener("submit", function(event) {
    event.preventDefault();

    const formData = new FormData(form);
    const city = formData.get("city_name");
    const result = document.getElementById("weather-result")
    // Obtening coordinates of city from openweathermap
    const url = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=metric&lang=fr`
    fetch(url)
    .then(response => response.json())
    .then(data => {
        const temperature = data.main.temp;
        const description = data.weather[0].description;
        const icon = data.weather[0].icon;
        result.innerHTML = `<p> City: ${city}</p>
                <img src='https://openweathermap.org/img/wn/${icon}@2x.png' alt='Weather icon'>
                <p> Temperature: ${temperature}°C</p>
                <p> Description: ${description}</p>`});

})