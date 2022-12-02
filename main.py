import requests

input_url = 'https://clout.cx/b'

def get_html_code():
  base_code = requests.get(
    input_url
  )
  return base_code.text

def write_html_code():
  base_write = open("index.html", "a").write(get_html_code())
  print('[system] code successfully wrote.')

write_html_code()
