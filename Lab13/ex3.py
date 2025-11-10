# Simple Flask meme app - gets memes from API and refreshes every 10 seconds
from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def get_meme():
    # Get a meme from the API
    url = "https://meme-api.com/gimme/wholesomememes"
    response = requests.get(url)
    meme_data = response.json()
    
    # Extract the meme URL and subreddit
    meme_url = meme_data['url']
    subreddit = meme_data['subreddit']
    
    # Create simple HTML with auto-refresh
    html = f"""
    <html>
    <head>
       <title>Memes'R'Us</title>
       <meta charset="UTF-8" name="viewport" content="width=device-width, initial-scale=0.8">
       <meta http-equiv="refresh" content="10; url=http://127.0.0.1:5001" />
    </head>
    <body>
        <h1>Welcome to McGarry's Meme Site!</h1>
        <h2>From subreddit: r/{subreddit}</h2>
        <img src="{meme_url}" style="max-width: 800px; max-height: 600px;">
        <p>This meme will refresh in 10 seconds...</p>
    </body>
    </html>
    """
    
    return html

if __name__ == '__main__':
    app.run(debug=True, port=5001)
