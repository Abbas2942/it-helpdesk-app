
from flask import Flask, render_template, request, redirect
import sqlite3
import os

app = Flask(__name__)

DB_PATH = os.environ.get(
    "DB_PATH", "data/tickets.db"
)

def get_connection():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS tickets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                server TEXT NOT NULL,
                issue TEXT NOT NULL,
                priority TEXT NOT NULL,
                status TEXT DEFAULT 'Open'
            )
        """)

@app.route("/")
def home():
    with get_connection() as conn:
        tickets = conn.execute(
            "SELECT * FROM tickets ORDER BY id DESC"
        ).fetchall()

    return render_template(
        "index.html", tickets=tickets
    )

@app.route("/add", methods=["POST"])
def add_ticket():
    server = request.form["server"].strip()
    issue = request.form["issue"].strip()
    priority = request.form["priority"]

    if not server or not issue:
        return "Server and issue are required", 400

    if priority not in ("Low", "Medium", "High"):
        return "Invalid priority", 400

    with get_connection() as conn:
        conn.execute(
            """INSERT INTO tickets
               (server, issue, priority)
               VALUES (?, ?, ?)""",
            (server, issue, priority)
        )

    return redirect("/")

@app.route("/health")
def health():
    return {"status": "healthy"}, 200

init_db()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

