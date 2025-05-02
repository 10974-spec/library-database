📚 Library Management System API (African Edition)
A complete MySQL database + FastAPI CRUD system with African authors and Kenyan members.

🚀 Quick Start
🛠️ Prerequisites
Python 3.8+

MySQL Server

pip

⚡ Installation

# Clone repo 
git clone https://github.com/10974-spec/library-database

# Install dependencies
pip install fastapi uvicorn mysql-connector-python

🗄️ Database Setup
Run the SQL script:
mysql -u root -p < library_db.sql

🌟 Launch API
uvicorn library_api:app --reload
