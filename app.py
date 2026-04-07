import os
import threading
from flask import Flask, jsonify
from bot import main  # kyunki teri file bot.py hai

app = Flask(__name__)

@app.route('/')
@app.route('/health')
def health_check():
    return jsonify({"status": "alive", "message": "Bot is running"}), 200

def run_bot():
    try:
        main()  # bot.py mein jo main function hai
    except Exception as e:
        print(f"Bot Error: {e}")

if __name__ == "__main__":
    # Bot ko background mein chala
    bot_thread = threading.Thread(target=run_bot)
    bot_thread.daemon = True
    bot_thread.start()
    
    print("✅ Bot started successfully!")
    
    # Flask server for Render
    port = int(os.environ.get("PORT", 8080))
    print(f"🚀 Server running on port {port}")
    app.run(host="0.0.0.0", port=port)
