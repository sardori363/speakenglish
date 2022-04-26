if __name__ == '__main__':
    import requests

    app_id = "e3ccc89f"
    app_key = "dc405551d060cdf6f0c8fec386adf06d"
    language = "en-gb"

    word_id = "python"
    url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word_id.lower()

    r = requests.get(url, headers={"app_id": app_id, "app_key": app_key})
    print(r.status_code)

    res = r.json()
    print(res['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0])
    print(res['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0]['audioFile'])
