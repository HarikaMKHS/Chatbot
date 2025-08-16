import requests

NEWS_API_KEY = "a3b4a2ce605f4eca9191e2bbcd94dd8c"

def get_news(category="general"):
    url = f"https://newsapi.org/v2/top-headlines?country=in&category={category}&apiKey={NEWS_API_KEY}"
    try:
        response = requests.get(url)
        data = response.json()
        articles = data.get("articles", [])
        if not articles:
            return "Sorry, no news found right now."
        
        # Return top 5 headlines
        headlines = [f"{i+1}. {article['title']}" for i, article in enumerate(articles[:5])]
        return "\n".join(headlines)
    except:
        return "Sorry, I couldn't fetch news at the moment."
def get_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hi there! How can I help you today?"
    elif "your name" in user_input:
        return "I'm your friendly news chatbot 🤖"
    elif "bye" in user_input:
        return "Goodbye! Have a great day!"
    elif "help" in user_input:
        return "I can give you news updates. Try asking: 'news technology', 'news sports', 'news finance'"

    # --- News topics ---
    elif "news" in user_input:
        if "technology" in user_input:
            return get_news("technology")
        elif "sports" in user_input:
            return get_news("sports")
        elif "finance" in user_input or "business" in user_input:
            return get_news("business")
        elif "education" in user_input:
            return get_news("education")
        else:
            return get_news("general")

    else:
        return "Sorry, I didn’t understand that. You can ask me for news updates!"
def get_news(category="general"):
    url = f"https://newsapi.org/v2/top-headlines?country=in&category={category}&apiKey={NEWS_API_KEY}"
    try:
        response = requests.get(url)
        data = response.json()
        print(data)  # <-- check what is returned
        articles = data.get("articles", [])
        if not articles:
            return "Sorry, no news found right now."
        
        headlines = [f"{i+1}. {article['title']}" for i, article in enumerate(articles[:5])]
        return "\n".join(headlines)
    except Exception as e:
        print(e)
        return "Sorry, I couldn't fetch news at the moment."


