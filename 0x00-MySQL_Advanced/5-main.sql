-- Show users and update (or not) email
SELECT * FROM users;

UPDATE users SET valid_email = 1 WHERE email = "nicholasodhiambo2015@gmail.com";
UPDATE users SET email = "annamuturiwamboi@gmail.com" WHERE email = "annamuturi@gmail.com";
UPDATE users SET name = "Bentos" WHERE email = "bernardaloo@gmail.com";

SELECT '--';

SELECT * FROM users;

UPDATE users SET email = "nicholasodhiambo2015@gmail.com" WHERE email = "nicholasodhiambo2015@gmail.com";

SELECT '--';

SELECT * FROM users;
