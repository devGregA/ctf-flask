mysql -uroot -ptoor -e "create database ctf" 
mysql -uroot -ptoor -Dctf -e "CREATE TABLE answers (id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY, the_flag_is VARCHAR(30) NOT NULL, reg_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP)"
mysql -uroot -ptoor -Dctf -e "INSERT INTO answers (the_flag_is) VALUES('sqlNO')"
