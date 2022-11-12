import urllib.parse as code_parse


search_name = 'q=许嵩'

encode_url = code_parse.quote(search_name)
print(encode_url)