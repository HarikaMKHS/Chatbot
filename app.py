from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chatbot_response():
    user_msg = request.json.get("message").lower()

    # Predefined flow
    if user_msg == "start":
        reply = "Hi! 👋"
        options = ["Hi", "Hello"]

    elif user_msg in ["hi", "hello"]:
        reply = "Nice to meet you! What do you want to know today?"
        options = ["Weather", "Sports", "Education"]

    elif user_msg in ["weather", "sports", "education"]:
        if user_msg == "weather":
            reply = "The weather today is sunny with a high of 30°C 🌞"
        elif user_msg == "sports":
            reply = "Latest sports news: Team A won the match 3-1 🏏"
        elif user_msg == "education":
            reply = "Education update: Online courses are trending these days 📚"

        # After answer, ask if user wants more
        reply += "\n\nDo you want to know anything else?"
        options = ["Yes", "No"]

    elif user_msg == "yes":
        reply = "Great! What do you want to know today?"
        options = ["Weather", "Sports", "Education"]

    elif user_msg == "no":
        reply = "Thank you! Meet again 👋"
        options = []

    else:
        reply = "Sorry, I didn't understand. Please choose an option."
        options = []

    return jsonify({"reply": reply, "options": options})

if __name__ == "__main__":
    app.run(debug=True)
