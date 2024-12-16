import requests
import json
import time
from constants import *


def google_search(query: str):
  params = {
    "key": GOOGLE_WEB_SEARCH_API_KEY,
    "cx": GOOGLE_WEB_SEARCH_ENGINE_ID,
    "q": query,
    "safe": "on" if GOOGLE_WEB_SEARCH_SAFE_MODE else "off",
    "num": 3
  }
  
  start = time.time()
  res = requests.get(GOOGLE_WEB_SEARCH_API_ENDPOINT, params=params)
  end = time.time()
  
  elapsed = end - start
  
  print(f"{google_search.__name__} request duration: {elapsed}")
  
  res = res.json()
  return res["items"]

def bing_search(query: str):
  headers = {"Ocp-Apim-Subscription-Key": BING_SEARCH_API_KEY1}
  params = {
      "q": query, 
      "responseFilter": "Webpages",
      "safeSearch": "Strict",
      "count": 3
  }
  
  start = time.time()
  res = requests.get(BING_SEARCH_ENDPOINT, headers=headers, params=params)
  end = time.time()
  
  elapsed = end - start
  
  print(f"{bing_search.__name__} request duration: {elapsed}")
  
  res = res.json()
  return res["webPages"]

def serplyio_google_search(query: str):
  query.replace(" ", "+")
  route = SERPLY_IO_GOOGLE_WEB_SEARCH_API_ENDPOINT + query + f"&num={SERPLY_IO_WEB_SEARCH_COUNT}"
  
  headers = {
    "Content-Type": "application/json",
    "X-Api-Key": SERPLY_IO_WEB_SEARCH_API_KEY
  }
  
  start = time.time()
  res = requests.get(route, headers=headers)
  end = time.time()
  
  elapsed = end - start
  
  print(f"{serplyio_google_search.__name__} request duration: {elapsed}")
  
  res = res.json()
  return res["results"]

def serplyio_bing_search(query: str):
  query.replace(" ", "+")
  route = SERPLY_IO_BING_WEB_SEARCH_API_ENDPOINT + query + f"&num={SERPLY_IO_WEB_SEARCH_COUNT}"
  
  headers = {
    "Content-Type": "application/json",
    "X-Api-Key": SERPLY_IO_WEB_SEARCH_API_KEY
  }
  
  start = time.time()
  res = requests.get(route, headers=headers)
  end = time.time()
  
  elapsed = end - start
  
  print(f"{serplyio_bing_search.__name__} request duration: {elapsed}")
  
  res = res.json()
  return res["results"]


def serpapi_google_search(query: str):
  params = {
    "q": query,
    "engine": "google",
    "api_key": SERPAPI_API_KEY
  }
  
  start = time.time()
  res = requests.get(SERPAPI_GOOGLE_ENDPOINT, params=params)
  end = time.time()
  
  elapsed = end - start
  
  print(f"{serpapi_google_search.__name__} request duration: {elapsed}")
  
  res = res.json()
  return res

def serpapi_bing_search(query: str):
  params = {
    "q": query,
    "engine": "bing",
    "api_key": SERPAPI_API_KEY
  }
  
  start = time.time()
  res = requests.get(SERPAPI_GOOGLE_ENDPOINT, params=params)
  end = time.time()
  
  elapsed = end - start
  
  print(f"{serpapi_google_search.__name__} request duration: {elapsed}")
  
  res = res.json()
  return res


def main():
  engines = [
    "google", 
    "bing", 
    "serplyio_google", 
    "serplyio_bing", 
    "serpapi_google", 
    "serpapi_bing"
  ]
  
  # print("".join(f"{i} -> {e}\n" for i, e in enumerate(engines)))

  # engine_idx = int(input("Engine index: "))
  # engine = engines[engine_idx]
  
  query = input("Query: ")
  
  for engine in engines:
    fn = engine + "_search"
    
    results = globals()[fn](query)
    
    with open(f"{engine}_results.json", "w") as f:
      f.write(json.dumps(results))


if __name__ == "__main__":
  main()
