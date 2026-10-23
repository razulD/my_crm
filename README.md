🛠️ Custom Flask CRM Application

⚠️ Status: Work in Progress (Incomplete)

This project is currently under active daily development. It is built from scratch using Flask and SQLite as a hands-on learning project to master web development, database interactions, manual routing, and debugging.

📌 Project Overview

A minimal, custom-built Customer Relationship Management (CRM) application designed to manage clients and track their status. The core goal of this project is to implement all web development concepts manually—without heavy abstraction libraries—to understand lower-level application logic.

✨ Features Implemented So Far

The project currently supports full CRUD (Create, Read, Update, Delete) operations:

[x] Create: Add new clients with details such as Name, Phone Number, and Status.

[x] Read: View a dynamic list of all registered clients directly on the dashboard.

[x] Update: Pre-filled edit forms to modify client attributes.

[x] Delete: Instantly remove client records.

[x] Security: Standard SQL injection protection using parameterized queries (? placeholders).

🛠️ Tech Stack

Backend: Python 3, Flask

Database: SQLite 3 (crm.db)

Frontend: HTML5, Jinja2 Templating

Version Control: Git, GitHub

🚀 Upcoming Features (Roadmap)

Since this repository is updated regularly, the following features are planned for upcoming commits:

[ ] UI Styling: Replace basic HTML with a clean CSS/Bootstrap interface.

[ ] Search & Filtering: Search clients by name or filter by status (NEW, PENDING, CLOSED).

[ ] Flash Notifications: Display alert banners when actions succeed (e.g., "Client added!").

[ ] Database Connection Refactoring: Implement connection helper utilities (get_db_connection()).

[ ] Authentication System: Add user login/signup for secure multi-user management.

⚙️ How to Run Locally

Clone the repository:

git clone https://github.com/razuldanar/my_crm.git
cd my_crm


Ensure Python 3 & Flask are installed:

pip install flask


Run the application:

python3 app.py


Access in browser:

Open http://127.0.0.1:5555/ in your web browser.
