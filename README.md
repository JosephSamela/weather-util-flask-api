# weather-util-flask-api

Get simple, light, human-readable, weather reports. Flask wrapper around [weather-util](http://fungi.yuggoth.org/weather/) application.

## Setup

Install `weather-util` for your distribution.

```
$ sudo apt install weather-util
```

Install python dependencies.

```
$ pip install -r requirements.txt
```

Run the application.

```
$ python main.py
```

Navigate to `localhost:8000` if you see this screen it worked!

## Usage

Home page
> `http://domain/`

Current weather report for zip-code
> `http://domain/04921`

Current weather report and forcast for zip-code
> `http://domain/02304/forcast`

## Demo

Setting things up takes time - try the live [demo]() instead!
