
# cnn_model_demo

A multi-page Flask web application showcasing **three different themed websites** served from a **single backend project** using Flask routing. Each website is rendered based on a unique route, demonstrating how multiple frontends can coexist within one deployed application.

---
Live Version : https://cnn-flask-demo-3-0gg5.onrender.com (with all other parts given below to access on address bar)

## 🌐 Live Concept

This project uses Flask's `@app.route()` to serve different websites from different URLs:

| Route   | Website Theme                                 |
| ------- | --------------------------------------------- |
| `/`     | 🧙‍♂️ Hogwarts-themed website (Main Homepage) |
| `/abc`  | 🌲 Forest-themed website                      |
| `/name` | 🎬 Modern Family-themed website               |

Users navigate between these websites using URLs or internal links — not by directly accessing HTML files.

---

## 🚀 Features

* Single Flask backend
* Multiple websites in one project
* Clean route-based navigation
* HTML templates rendered dynamically
* Ready for deployment on **Render** or similar platforms

---

## 🖥️ How to Run Locally

1. Clone the repository

   ```bash
   git clone https://github.com/your-username/cnn_model_demo.git
   cd cnn_model_demo
   ```

2. Create a virtual environment (optional but recommended)

   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   ```

3. Install dependencies

   ```bash
   pip install -r requirements.txt
   ```

4. Run the Flask app

   ```bash
   python app.py
   ```

5. Open in browser:

   * `http://127.0.0.1:5000/`
   * `http://127.0.0.1:5000/abc`
   * `http://127.0.0.1:5000/name`

---

## 🌍 Deployment

This project is suitable for deployment on **Render**.

* Root route (`/`) serves the Hogwarts website
* Sub-routes serve the other websites seamlessly

---

## 🎯 Learning Outcome

* Understanding Flask routing
* Serving multiple templates from one backend
* Real-world deployment behavior of web apps
* URL-based navigation vs file-based access

---

## 📌 Author

**Vaishnavi L**
Software Development Intern | Python & Web Development Enthusiast

---

⭐ If you like this project, feel free to star the repository!
