#!/usr/bin/env ruby

require 'cgi'

def capitalize_words(str)
  str.split.map(&:capitalize).join(' ')
end

cgi = CGI.new

city_name = capitalize_words(cgi.params['cityName'].first)
province_state = capitalize_words(cgi.params['provinceState'].first)
country = capitalize_words(cgi.params['country'].first)
picture_url = cgi.params['pictureUrl'].first

html_content = <<HTML
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>City Information (Ruby)</title>
  <style>
    body {
      font-family: 'Arial', sans-serif;
      text-align: center;
    }
    #header {
      background-color: #3498db;
      color: #fff;
      font-size: 50px;
      padding: 30px;
    }
    #cityInfo {
      margin-top: 25px;
    }
    #cityImage {
      width: 100%;
      height: auto;
    }
  </style>
</head>
<body>

<div id="header">
  <p>#{city_name}, #{country}</p>
</div>

<div id="cityInfo">
  <p>City: #{city_name}</p>
  <p>Province/State: #{province_state}</p>
  <p>Country: #{country}</p>
</div>

<img id="cityImage" src="#{picture_url}" alt="City Image">

</body>
</html>
HTML

puts cgi.header('text/html')
puts html_content
