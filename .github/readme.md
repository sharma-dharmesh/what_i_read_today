# What_I_Read_Today

A web application developed as part of the "Learning Log" project from the book **Python Crash Course** by Eric Matthes. This application allows users to track topics they are interested in and make entries about what they have learned or read regarding those topics.

## Project Overview

**What_I_Read_Today** is a Django-based web application that serves as a personal journal for learning and reading progress. It features a user authentication system, allowing multiple users to manage their own private logs.

### Key Features
* **Topic Management:** Users can create new topics they are studying or reading about.
* **Entry Tracking:** Users can add multiple dated entries for each topic to record progress.
* **User Accounts:** Secure registration and login system ensuring users only see their own data.
* **Bootstrap Integration:** Styled with Bootstrap 5 for a clean, responsive interface.
* **Deployment Ready:** Configured for deployment to platforms like Heroku or Render.

## Tech Stack

* **Language:** Python 3
* **Framework:** Django
* **Styling:** Bootstrap 5 & django-bootstrap5
* **Database:** SQLite (Development) / PostgreSQL (Production)
* **Authentication:** Django's built-in User model

## Getting Started

### Prerequisites

* Python 3.x installed
* `pip` (Python package installer)
* `virtualenv` (Recommended)

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/sharma-dharmesh/what_i_read_today.git
    cd what_i_read_today
    ```

2.  **Set up a virtual environment:**
    ```bash
    python -m venv ll_env
    source ll_env/bin/activate  # On Windows use: ll_env\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run Migrations:**
    ```bash
    python manage.py migrate
    ```

5.  **Create a Superuser (Admin):**
    ```bash
    python manage.py createsuperuser
    ```

6.  **Start the development server:**
    ```bash
    python manage.py runserver
    ```
    Access the app at `http://127.0.0.1:8000/`.

## Usage

1.  **Register:** Create a new account via the registration page.
2.  **Topics:** Click on "Topics" to see existing categories or add a new one.
3.  **Entries:** Select a topic to view all entries or click "Add entry" to document what you've read today.
4.  **Admin:** Access the admin panel at `/admin` to manage all data and users.

## Acknowledgments

* Based on the project from the book [Python Crash Course](https://ehmatthes.github.io/pcc_2e/) by Eric Matthes.