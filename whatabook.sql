
DROP USER IF EXISTS 'whatabook_user'@'localhost';

CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';

GRANT ALL PRIVILEGES ON whatabook.* TO'whatabook_user'@'localhost';

ALTER TABLE wishlist DROP FOREIGN KEY fk_book;
ALTER TABLE wishlist DROP FOREIGN KEY fk_user;
ALTER TABLE availability DROP FOREIGN KEY availability_book_fk;
ALTER TABLE availability DROP FOREIGN KEY availability_store_fk;

DROP TABLE IF EXISTS store;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS availability;
DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS user;

CREATE TABLE store (
    store_id    INT             NOT NULL    AUTO_INCREMENT,
    locale      VARCHAR(500)    NOT NULL,
    PRIMARY KEY(store_id)
);

CREATE TABLE book (
    book_id     INT             NOT NULL    AUTO_INCREMENT,
    book_name   VARCHAR(200)    NOT NULL,
    author      VARCHAR(200)    NOT NULL,
    details     VARCHAR(500),
    PRIMARY KEY(book_id)
);

CREATE TABLE availability(
    availability_id INT     NOT NULL AUTO_INCREMENT
    book_id         INT     NOT NULL,
    store_id        INT     NOT NULL,
    PRIMARY KEY (availability_id),
    CONSTRAINT availability_book_fk FOREIGN KEY (book_id) REFERENCES book(book_id),
    CONSTRAINT availability_store_fk  FOREIGN KEY (store_id)  REFERENCES store(store_id)
);

CREATE TABLE user (
    user_id         INT         NOT NULL    AUTO_INCREMENT,
    first_name      VARCHAR(75) NOT NULL,
    last_name       VARCHAR(75) NOT NULL,
    current_store_id INT,       NOT NULL,   DEFAULT 1,
    PRIMARY KEY(user_id) 
);

CREATE TABLE wishlist (
    wishlist_id     INT         NOT NULL    AUTO_INCREMENT,
    user_id         INT         NOT NULL,
    book_id         INT         NOT NULL,
    PRIMARY KEY (wishlist_id),
    CONSTRAINT fk_book FOREIGN KEY (book_id) REFERENCES book(book_id),
    CONSTRAINT fk_user FOREIGN KEY (user_id) REFERENCES user(user_Id)
);


-- Stores
INSERT INTO store(locale)
    VALUES('123 Mockingbird Ln Santa Barbara CA 27360');

-- Books
INSERT INTO book(book_name, author, details) VALUES('Beastly', 'Alex Finn', 'Beauty and the Beast retelling');
INSERT INTO book(book_name, author, details) VALUES('The Storytellers Daughter', 'Cameron Dokey', 'Arabian Nights retelling');
INSERT INTO book(book_name, author, details) VALUES('Teardrop', 'Lauren Kate', 'Don''t cry');
INSERT INTO book(book_name, author, details) VALUES('Ashes', 'Lisa J Bick', 'Everything will burn');
INSERT INTO book(book_name, author, details) VALUES('Abraham Lincoln Vampire Hunter', 'Seth Grahame Smith', 'President turned vampire hunter');
INSERT INTO book(book_name, author, details) VALUES('Etiquette and Espionage', 'Gail Carriger', 'Ladies should be proper killers');
INSERT INTO book(book_name, author, details) VALUES('Need', 'Carrie Jones', 'Fairies exist');
INSERT INTO book(book_name, author, details) VALUES('Asylum', 'Madeleine Roux', 'Be careful or you''ll lose your mind');
INSERT INTO book(book_name, author, details) VALUES('Dorothy Must Die', 'Danielle Paige', 'You''ve never seen OZ like this before');

INSERT INTO availability(book_id, store_id) VALUES(1,1);
INSERT INTO availability(book_id, store_id) VALUES(2,1);
INSERT INTO availability(book_id, store_id) VALUES(3,1);
INSERT INTO availability(book_id, store_id) VALUES(4,1);
INSERT INTO availability(book_id, store_id) VALUES(5,1);
INSERT INTO availability(book_id, store_id) VALUES(6,1);
INSERT INTO availability(book_id, store_id) VALUES(7,1);
INSERT INTO availability(book_id, store_id) VALUES(8,1);
INSERT INTO availability(book_id, store_id) VALUES(9,1);

-- Users
INSERT INTO user(first_name, last_name)  VALUES('Rebekkah', 'Stringer');
INSERT INTO user(first_name, last_name)  VALUES('Kevin', 'Wood');
INSERT INTO user(first_name, last_name)  VALUES('Amber', 'Terry');

-- Wishlist
INSERT INTO wishlist(user_id, book_id) VALUES (1, 3);

INSERT INTO wishlist(user_id, book_id) VALUES (2, 6);

INSERT INTO wishlist(user_id, book_id) VALUES (3, 6);