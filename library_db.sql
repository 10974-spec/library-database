CREATE DATABASE IF NOT EXISTS library_db;
USE library_db;

CREATE TABLE authors (
    author_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    country VARCHAR(50)
);

CREATE TABLE books (
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    isbn VARCHAR(20) UNIQUE NOT NULL,
    author_id INT NOT NULL,
    FOREIGN KEY (author_id) REFERENCES authors(author_id)
);

CREATE TABLE members (
    member_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE loans (
    loan_id INT AUTO_INCREMENT PRIMARY KEY,
    book_id INT NOT NULL,
    member_id INT NOT NULL,
    loan_date DATE NOT NULL,
    return_date DATE,
    FOREIGN KEY (book_id) REFERENCES books(book_id),
    FOREIGN KEY (member_id) REFERENCES members(member_id)
);

INSERT INTO authors (name, country) VALUES 
('Ngũgĩ wa Thiong''o', 'Kenya'),
('Chimamanda Ngozi Adichie', 'Nigeria'),
('Nadine Gordimer', 'South Africa');

INSERT INTO books (title, isbn, author_id) VALUES
('Petals of Blood', '9780435905484', 1),
('Half of a Yellow Sun', '9780007200283', 2),
('July''s People', '9780140070938', 3);

INSERT INTO members (name, email) VALUES
('Amani Okoth', 'amani@example.com'),
('Wanjiru Mwangi', 'wanjiru@example.com');

INSERT INTO loans (book_id, member_id, loan_date) VALUES
(1, 1, '2024-01-15'),
(2, 2, '2024-01-20');