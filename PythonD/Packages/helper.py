import requests
def get_data_url(url):
    response=requests.get(url)
    content_type=response.headers.get("Content-Type","").lower()
    if 'application/json' in content_type:
        return response.json()
    elif 'text/' in content_type:
        return response.text
    else:
        return response.content