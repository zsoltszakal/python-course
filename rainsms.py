import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
import os



api_key = os.environ.get("OWM_API_KEY")
ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
account_sid = "AC005ba424569c129f62f10c127ac95592"
auth_token = os.environ.get("AUTH_TOKEN")


weather_params = {
    "lat": 50.719166,
    "lon": -1.880769,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(ENDPOINT, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:23]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:

    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client = Client(account_sid, auth_token, http_client=proxy_client)

    message = client.messages \
        .create(
        body="Take an umbrella bro, it's going to rain today! ⛈⛈",
        from_="+18312986747",
        to="+447578205905"
    )
