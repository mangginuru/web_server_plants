import urllib.request

## naver_shop 에서 search하기
def naver_searchAPI(query):
    client_id = "***************"
    client_secret = "**********"
    ## 앱에서 검색 결과를 여기 encText에 넣기
    encText = urllib.parse.quote(query)
    display = "15"
    url = "https://openapi.naver.com/v1/search/shop.json?query=" + encText + "&display=" + display

    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()

    if(rescode==200):
        response_body = response.read()
        return response_body.decode('utf-8')
    else:
        return "Error Code:" + rescode
    