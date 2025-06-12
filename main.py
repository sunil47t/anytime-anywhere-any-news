import requests     
from config import API_KEY

topic= input("What type of news are you interested in reading today? ")
api= API_KEY
j= int(input("How many articles do you want to see? "))

url= f"https://newsapi.org/v2/everything?q={topic}&from=2025*04*28&sortBy=publishedAt&apiKey={api}"
print(url)

x= requests.get(url)

if x.status_code == 200:
    data = x.json()
    articles = data.get('articles', [])
    
    if articles:
        print(f"Top news articles about '{topic}':\n")
        for i, article in enumerate(articles[:j], start=1):
            title = article.get('title', 'No title available')
            description = article.get('description', 'No description available')
            article_url = article.get('url', 'No URL available')
            print(f"{i}. {title}\n   {description}\n {article_url}\n")
            print("**************************************************\n")
    else:
        print("No articles found for this topic.")
