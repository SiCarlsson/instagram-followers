# Instagram Followers Insights

This project helps you **analyze your Instagram following vs. followers** using official data exported directly from Instagram — no third-party apps required. 

This program only parses your exported **JSON data** and does **not connect to Instagram**.

It shows:
- Who you follow that **doesn’t follow you back**.
- Who follows you that **you don’t follow back**.

---

## 📦 What You Need

1. **Request Your Instagram Data**:
   - Visit [Instagram Data Download](https://www.instagram.com/download/request/).
   - When making the request:
     - **Choose the longest possible timeframe** to ensure you get complete data.
     - **Select the JSON format**
   - Download the data after Instagram processes your request.

2. **Files You Will Need**:
   - `following.json`: Found in `connections/followers_and_following/`. This file contains the users you follow.
   - `followers_1.json`: Found in `connections/followers_and_following/`. This file contains the users who follow you.

---

## 🧰 How to Use

1. Clone or download this repository.

2. Place your `following.json` and `followers_1.json` files in the project folder.

3. Run the script:

    ```bash
    python main.py
    ```
