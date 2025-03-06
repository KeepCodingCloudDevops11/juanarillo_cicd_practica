from flask import Flask, jsonify
import redis
import os

app = Flask(__name__)

# Redis Configuration
REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
REDIS_DB = int(os.getenv("REDIS_DB", 0))

# Redis connection
db = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB, decode_responses=True)

@app.route('/')
def index():
    count = db.incr('hits')  # Increment redis counter
    return f"La página ha sido cargada {count} veces."

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)