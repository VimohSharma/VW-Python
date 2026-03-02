from flask import Flask, render_template

app = Flask(__name__)

comments = [
    {
        "username": "john",
        "comment": " this is dumb ",
        "likes": 120,
        "flagged": True
    },
    {
        "username": "amit",
        "comment": "great work everyone",
        "likes": 50,
        "flagged": False
    },
    {
        "username": "priya",
        "comment": "you are stupid but ok",
        "likes": 200,
        "flagged": False
    },
    {
        "username": "sara",
        "comment": "I really enjoyed this post. Thanks for sharing!",
        "likes": 95,
        "flagged": False
    },
    {
        "username": "rahul",
        "comment": "This is absolutely amazing. Loved every part of it!",
        "likes": 180,
        "flagged": False
    },
    {
        "username": "neha",
        "comment": " dumb content and stupid explanation ",
        "likes": 10,
        "flagged": True
    },
    {
        "username": "alex",
        "comment": "Can you provide more details on how this works?",
        "likes": 70,
        "flagged": False
    },
    {
        "username": "maria",
        "comment": "This is a very long comment " * 20,
        "likes": 30,
        "flagged": False
    },
    {
        "username": "vijay",
        "comment": "Nice effort!",
        "likes": 5,
        "flagged": False
    },
    {
        "username": "kiran",
        "comment": "I think this approach is dumb but still interesting.",
        "likes": 110,
        "flagged": True
    }
]

@app.route("/")
def home():

    bad_words = ["dumb", "stupid"]

    processed = []

    for c in comments:

        comment_text = c["comment"].strip()

        # replace bad words
        for word in bad_words:
            comment_text = comment_text.replace(word, "****")

        processed.append({
            "username": c["username"].upper(),
            "comment": comment_text,
            "likes": c["likes"],
            "flagged": c["flagged"]
        })

    total_comments = len(processed)
    total_flagged = sum(1 for c in processed if c["flagged"])
    most_liked = max(processed, key=lambda x: x["likes"])

    usernames = ", ".join([c["username"] for c in processed])

    return render_template(
        "comments.html",
        comments=processed,
        total_comments=total_comments,
        total_flagged=total_flagged,
        most_liked=most_liked,
        usernames=usernames
    )


if __name__ == "__main__":
    app.run(debug=True)