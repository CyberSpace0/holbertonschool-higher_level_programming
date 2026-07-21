-- create user
SET GLOBAL validate_password.policy=LOW; SET GLOBAL validate_password.length=8;
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
