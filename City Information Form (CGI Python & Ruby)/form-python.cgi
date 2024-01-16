#!/usr/bin/env python2

import cgi

def capitalize_words(s):
    return ' '.join(word.capitalize() for word in s.split())

def generate_html(city_name, province_state, country, picture_url):
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>City Information</title>
        <style>
            body {{
                font-family: 'Arial', sans-serif;
                text-align: center;
            }}
            #header {{
                background-color: #4d1db5; 
                color: #d2c1f3;
                font-size: 36px;
                padding: 20px;
                text-transform: uppercase;
            }}
            #cityInfo {{
                margin-top: 20px;
            }}
            #cityImage {{
                width: 80%;
                max-width: 1000px;
                height: auto;
                border: 20px solid #4d1db5;
            }}
        </style>
    </head>
    <body>

        <div id="header">
            <p>{}, {}</p>
        </div>

        <div id="cityInfo">
            <p>City: {}</p>
            <p>Province/State: {}</p>
            <p>Country: {}</p>
        </div>

        <img id="cityImage" src="{}" alt="City Image">

    </body>
    </html>
    """.format(city_name, country, city_name, province_state, country, picture_url)
    return html_content

form = cgi.FieldStorage()

city_name = capitalize_words(form.getvalue('cityName'))
province_state = capitalize_words(form.getvalue('provinceState'))
country = capitalize_words(form.getvalue('country'))
picture_url = form.getvalue('pictureUrl')

print("Content-type: text/html\n")
print(generate_html(city_name, province_state, country, picture_url))
