# weather-util-flask-api

Get simple, light, human-readable, weather reports. Flask wrapper around [weather-util](http://fungi.yuggoth.org/weather/) application.

**simple** - No ads, no banners, no fancy interactive trackers. Visit `/your-zip-code` and get the weather report.

**light** - no javascript, no css, no images, no icons, not even a favicon.

**human-readable** - No mind-numbing XML from this API. Simple easy to read plaintext reports designed for humans.

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

Home page.
> `http://localhost/`

Current weather report for zip-code.
> `http://localhost/04921`

Current weather report and forcast for zip-code.
> `http://localhost/02304/forcast`

## Demo

Setting things up takes time - try the live [demo]() instead!
