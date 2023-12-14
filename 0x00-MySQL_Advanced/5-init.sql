-- Initial
DROP TABLE IF EXISTS users;

CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL,
    name VARCHAR(255),
    valid_email BOOLEAN NOT NULL DEFAULT 0,
    PRIMARY KEY (id)
);

INSERT INTO users (email, name) VALUES ("nicholasodhiambo2015@gmail.com", "Nicky-Mane");
INSERT INTO users (email, name, valid_email) VALUES ("annamuturi@gmail.com", "Anna", 1);
INSERT INTO users (email, name, valid_email) VALUES ("bernardaloo@gmail.com", "Benny", 1);
