<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>📚 Library Management System API (African Edition)</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
            line-height: 1.6;
            color: #24292e;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }
        h1, h2, h3 {
            color: #0366d6;
            margin-top: 24px;
            margin-bottom: 16px;
            font-weight: 600;
        }
        h1 { font-size: 2em; border-bottom: 1px solid #eaecef; padding-bottom: 0.3em; }
        h2 { font-size: 1.5em; border-bottom: 1px solid #eaecef; padding-bottom: 0.3em; }
        h3 { font-size: 1.25em; }
        code {
            font-family: SFMono-Regular, Consolas, 'Liberation Mono', Menlo, monospace;
            background-color: rgba(27, 31, 35, 0.05);
            border-radius: 3px;
            padding: 0.2em 0.4em;
            font-size: 85%;
        }
        pre {
            background-color: #f6f8fa;
            border-radius: 3px;
            padding: 16px;
            overflow: auto;
            line-height: 1.45;
        }
        table {
            border-collapse: collapse;
            width: 100%;
            margin-bottom: 16px;
        }
        th, td {
            border: 1px solid #dfe2e5;
            padding: 6px 13px;
        }
        th {
            background-color: #f6f8fa;
        }
        .emoji {
            font-size: 1.2em;
            vertical-align: middle;
        }
        .highlight {
            background-color: #fff8c6;
            padding: 2px 4px;
            border-radius: 4px;
        }
    </style>
</head>
<body>
    <code>Hello</code>
    <h1><span class="emoji">📚</span> Library Management System API (African Edition)</h1>
    
    <p>A complete MySQL database + FastAPI CRUD system with African authors and Kenyan members.</p>
    
    <h2><span class="emoji">🚀</span> Quick Start</h2>
    
    <h3><span class="emoji">🛠️</span> Prerequisites</h3>
    <ul>
        <li>Python 3.8+</li>
        <li>MySQL Server</li>
        <li>pip</li>
    </ul>
    
    <h3><span class="emoji">⚡</span> Installation</h3>
    <pre><code># Clone repo (if applicable)
git clone [your-repo-url]

# Install dependencies
pip install fastapi uvicorn mysql-connector-python</code></pre>
    
    <h3><span class="emoji">🗄️</span> Database Setup</h3>
    <p>Run the SQL script:</p>
    <pre><code>mysql -u root -p &lt; library_db.sql</code></pre>
    <p><em>(Replace <code>root</code> with your MySQL username)</em></p>
    
    <h3><span class="emoji">🌟</span> Launch API</h3>
    <pre><code>uvicorn library_api:app --reload</code></pre>
    <p>Access docs at: <a href="http://localhost:8000/docs">http://localhost:8000/docs</a></p>
    
    <h2><span class="emoji">🌍</span> Features</h2>
    
    <h3><span class="emoji">📖</span> African Literature Focus</h3>
    <p>Pre-loaded with famous African authors:</p>
    <ul>
        <li>Ngũgĩ wa Thiong'o (Kenya)</li>
        <li>Chimamanda Ngozi Adichie (Nigeria)</li>
        <li>Nadine Gordimer (South Africa)</li>
    </ul>
    
    <h3><span class="emoji">🔄</span> CRUD Operations</h3>
    <table>
        <thead>
            <tr>
                <th>Endpoint</th>
                <th>Method</th>
                <th>Description</th>
                <th>Example</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><code>/books/</code></td>
                <td>POST</td>
                <td>Add new book</td>
                <td><code>{"title":"Decolonising the Mind","isbn":"1234567890","author_id":1}</code></td>
            </tr>
            <tr>
                <td><code>/books/</code></td>
                <td>GET</td>
                <td>List all books</td>
                <td>-</td>
            </tr>
            <tr>
                <td><code>/books/{id}</code></td>
                <td>GET</td>
                <td>Get single book</td>
                <td><code>/books/1</code></td>
            </tr>
            <tr>
                <td><code>/books/{id}</code></td>
                <td>PUT</td>
                <td>Update book</td>
                <td><code>{"title":"New Title",...}</code></td>
            </tr>
            <tr>
                <td><code>/books/{id}</code></td>
                <td>DELETE</td>
                <td>Remove book</td>
                <td>-</td>
            </tr>
        </tbody>
    </table>
    
    <h2><span class="emoji">🧑‍💻</span> Example Usage</h2>
    
    <h3><span class="emoji">➕</span> Add a New Book</h3>
    <pre><code>curl -X POST http://localhost:8000/books/ \
-H "Content-Type: application/json" \
-d '{"title":"Wizard of the Crow", "isbn":"9789966254801", "author_id":1}'</code></pre>
    
    <h3><span class="emoji">📜</span> List All Books</h3>
    <pre><code>curl http://localhost:8000/books/</code></pre>
    
    <h2><span class="emoji">🛠️</span> Tech Stack</h2>
    <ul>
        <li><strong>Database</strong>: MySQL <span class="emoji">🐬</span></li>
        <li><strong>Backend</strong>: Python FastAPI <span class="emoji">⚡</span></li>
        <li><strong>Validation</strong>: Pydantic <span class="emoji">✔️</span></li>
    </ul>
    
    <h2><span class="emoji">📜</span> License</h2>
    <p>MIT License - Free for educational use</p>
    
    <hr>
    
    <p><span class="emoji">✨</span> <strong>Pro Tip</strong>: Use Postman for easier API testing!</p>
    <p><span class="emoji">🔧</span> <strong>Troubleshooting</strong>: Check MySQL credentials in <code>library_api.py</code> if connection fails</p>
    
    <p><strong>Made with <span class="emoji">❤️</span> for African tech education</strong></p>
    <p>Replace placeholder values (<code>[your-repo-url]</code>) with your actual details when using!</p>
    
    <p><em>(Note: For best viewing experience, this HTML includes GitHub-like styling)</em></p>

    
</body>
</html>

