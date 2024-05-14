from flask import Flask, render_template, request, jsonify
import time
import threading
import random

app = Flask(__name__)

class WebInterface:
  def __init__(self):
    

  @app.route("/")
  def index(self):
      return render_template("index.html")

@app.route("/start_animation", methods=["POST"])
def start_animation():
    duration = 5  # Duration of the animation in seconds

    # Start a new thread for the animation
    threading.Thread(target=animate_communication_voice, args=(duration,)).start()

    return jsonify({"status": "success"})

def animate_communication_voice(duration):
    start_time = time.time()

    while time.time() - start_time < duration:
        # Simulate animation by generating random coordinates
        x = random.randint(0, 100)
        y = random.randint(0, 100)
        print(f"Animating communication voice at position ({x}, {y})")

        time.sleep(0.5)  # Adjust the sleep time to control animation speed

if __name__ == "__main__":
    app.run(debug=True)
