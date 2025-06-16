---

# Real-Time Chat App with FastAPI & MongoDB

A simple and clean real-time chat application using **FastAPI**, **MongoDB**, and **WebSockets** to let multiple users send and receive messages live.

---

## 🚀 Features

* Real-time bi‑directional messaging with WebSockets
* Persistent chat through MongoDB
* Clean and minimal FastAPI backend
* Scalable architecture—easy to build on

---

## 🛠️ Tech Stack

* **FastAPI** – Asynchronous Python framework for API and WebSocket endpoints
* **WebSockets** – Handling real-time message mutiny
* **MongoDB** – Stores user messages and chat history
* **Motor** (or PyMongo) – Python driver to connect MongoDB
* **Pydantic** – Data validation and schema enforcement

---

## 📦 Getting Started

### Prerequisites

Make sure you have:

* Python 3.8+
* MongoDB installed and running locally or remote
* `pip` package manager

### Installation

1. Clone the repo:

   ```bash
   git clone https://github.com/nikanmafakheri/RealTime-ChatApp-FastAPI-MongoDB.git
   cd RealTime-ChatApp-FastAPI-MongoDB
   ```

2. Install dependencies:

   ```bash
   pip install fastapi uvicorn motor pydantic
   ```

3. Create a `.env` or set environment variable:

   ```bash
   export MONGODB_URI="mongodb://localhost:27017/chat_db"
   ```

4. Run the app:

   ```bash
   uvicorn main:app --reload
   ```

   The server starts on `http://localhost:8000`.

---

## 💬 Usage

* Visit `http://localhost:8000/docs` for interactive API docs.
* Connect to the WebSocket endpoint (e.g. `ws://localhost:8000/ws/chat`) using a chat client or browser.
* Send messages: all connected clients get broadcast in real time.
* Check MongoDB for stored chat documents.

---

## 📂 Project Structure

```
├── main.py         # FastAPI server + WebSocket endpoint
├── models.py       # Pydantic schemas + MongoDB models
├── db/             # Database helpers (connections, CRUD ops)
└── .gitignore
```

---

## 📈 How It Works

1. FastAPI server receives WS connections at `/ws/chat`.
2. On message from a client:

   * It's validated with Pydantic, saved to MongoDB,
   * And broadcast to all active clients.
3. Message history is persisted so users can load past chats.

---

---

## 🙌 Contributing

Your contributions are welcome! Feel free to:

* Report bugs or suggest new features
* Open pull requests (even small improvements help!)
* Update docs or improve tests

---

## 📄 License

This project is open-source under the **MIT License** – see `LICENSE` for details.

---

---
## 🔗 Contact
- Made with ❤️ by Nikan
- Feel free to connect on [LinkedIn](www.linkedin.com/in/nikanmafakheri)
---
