## Dark Mirror - Weather - Umbrella

Umbrella is a service for dark mirror which handles weather gathering data from AccuWeather apis.

# Made with

- Python 3+
- Kubernetes
- Serverless
- Kubeless

# Api Key

For this service, you should have an API_KEY for calling AccuWeather apis. You can get one by registering at: https://developer.accuweather.com

Once you have your API_KEY you should put it into variable.json file as the value of the same key attribute.

# Setup and deploy

For this step you have to follow the same descriptions described at README file at the root directory of this project.

# Invoking the function

By default you get the respective weather data for the next 5 days including the current day by calling this function without any --data set in the request. Otherwise you can specify how many hours do you want to fetch by passing a simple json payload.

    curl --header "Content-Type:application/json" <dns>/<path>

Valid hours to request the service:

# Responses payload


    {
        "next_days": [{
            "date": str,
            "status": str,
            "max": int,
            "min": int
        }],
        "next_hours": [{
            "date": str,
            "status": str,
            "temperature": int
        }]
    }
