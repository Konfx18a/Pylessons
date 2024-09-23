CREATE TABLE task_db_books (
    id int NOT NULL,
    Title varchar(255) NOT NULL,
    Description varchar(255),
    PRIMARY KEY (id)
); 
INSERT INTO task_db_books(Title,Description) VALUES('Рубаи','Стихи великого Омар Хаяма')
INSERT INTO task_db_books(Title,Description) VALUES('Граф Монте-кристо','Роман Александра Дюма')
INSERT INTO task_db_books(Title,Description) VALUES('Декамерон','Новеллы Джованни Боккаччо, 18+')
