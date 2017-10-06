Py Simple HTTP Server
=====================

Simple HTTP Server with socket programming with Python 3.

## Requirements
 - Python 3

## How To Run
```
python3 index.py
```

## Guide
```
from app import (start, App)


app = App()

@app.route('/')         # action for route /
def route_index():      # function name should have prefix 'route_'
    # simple return 'Hello, World!' in browser
    return app.response.send('Hello, World!')


start(app, __name__)    # default run in port 8080

# or define your port
# start(app, __name__, port = 5000)
```

## How To Contribute
 - Give star `!Important`
 - Fork
 - Create pull request to this repository

## License
[GNU GPL v2](https://github.com/mgilangjanuar/py-simple-http-server/blob/master/LICENSE.md)
