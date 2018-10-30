# PiXL-Maths-App-Farm

This project requires atleast Python 3.6 (can probably use 3.4). It may not work correctly on MacOS or Linux

Thanks to Connor for doing the initial testing and finding the exploit, thanks to Ben for the idea of zooming in for more accurate OCR. I was responsible for coding it, finding the questions and doing more indepth testing. This script took a while to make so I hope you enjoy it. It is licensed under MIT so if you post the code elsewhere, you must also give the license with it.

## Setup
1. `pip install -U -r requirements.txt` or `pip3 install -U -r requirements.txt`
2. Edit the coordinate values (this may be improved with point values that will work with any resolution monitor as long as you use Firefox and have a bookmark toolbar as this is the setup I used. The existing coordinates are for 1440x900)
3. Install [Tesseract OCR](https://github.com/UB-Mannheim/tesseract/wiki#tesseract-at-ub-mannheim)
4. Change the paths for [Tesseract](https://github.com/OrangutanGaming/PiXL-Maths-App-Farm/blob/master/app.py#L13) and the [temp screenshot save location](https://github.com/OrangutanGaming/PiXL-Maths-App-Farm/blob/master/app.py#L14)
5. Run `app.py`
