import urllib.request
import urllib.parse

api = "https://search.naver.com/search.naver"
values ={
    "where" : "nexearch",
    "sm" : "top_hty",
    "fbm" : "0",
    "ie" : "utf8",
    "query" : "초콜릿"
}

urllib.parse.urlencode(values)

print(api)
print(values)
