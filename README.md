📚 Library Management System API (African Edition)
A complete MySQL database + FastAPI CRUD system with African authors and Kenyan members.

🚀 Quick Start
🛠️ Prerequisites
Python 3.8+

MySQL Server

pip

⚡ Installation

# Clone repo (if applicable)
<code>git clone https://github.com/10974-spec/library-database</code>

# Install dependencies
<code>pip install fastapi uvicorn mysql-connector-python</code>
🗄️ Database Setup
Run the SQL script:


<code>mysql -u root -p < library_db.sql</code>



🌟 Launch API

<code>uvicorn library_api:app --reload</code>
Access docs at: http://localhost:8000/docs

🌍 Features
📖  Literature Focus
Pre-loaded  famous African authors:

Ngũgĩ wa Thiong'o (Kenya)

Chimamanda Adichie (Nigeria)

Nadine Gordimer (South Africa)

🔄 CRUD Operations
Endpoint	Method	Description	Example
/books/	POST	Add new book	{"title":"Decolonising the Mind","isbn":"1234567890","author_id":1}
/books/	GET	List all books	-
/books/{id}	GET	Get single book	/books/1
/books/{id}	PUT	Update book	{"title":"New Title",...}
/books/{id}	DELETE	Remove book	-
🧑‍💻 Example Usage
➕ Add a New Book

<code>curl -X POST http://localhost:8000/books/ \
-H "Content-Type: application/json" \
-d '{"title":"Wizard of the Crow", "isbn":"9789966254801", "author_id":1}'
📜 List All Books
</code>
<code>
curl http://localhost:8000/books/</code>
🛠️ Tech Stack
Database: MySQL 🐬

Backend: Python FastAPI ⚡

Validation: Pydantic ✔️





Made with ❤️ by Emmanuel
