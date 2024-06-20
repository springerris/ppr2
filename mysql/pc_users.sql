USE computer_db;

/*
-- CREATE USER 'pc_viewer'@'localhost';
GRANT SELECT ON computer_db.employee TO "pc_viewer"@"localhost";
GRANT SELECT ON computer_db.assign TO "pc_viewer"@"localhost";
GRANT SELECT ON computer_db.dolzhnost TO "pc_viewer"@"localhost";
GRANT SELECT ON computer_db.computer TO "pc_viewer"@"localhost";
GRANT SELECT ON computer_db.drive TO "pc_viewer"@"localhost";
GRANT SELECT  ON computer_db.ram TO "pc_viewer"@"localhost";
GRANT SELECT  ON computer_db.gpu TO "pc_viewer"@"localhost";
GRANT SELECT  ON computer_db.pccpu TO "pc_viewer"@"localhost";
GRANT SELECT  ON computer_db.room TO "pc_viewer"@"localhost";
GRANT SELECT  ON computer_db.monitor TO "pc_viewer"@"localhost";
GRANT SELECT  ON computer_db.mouse TO "pc_viewer"@"localhost";
GRANT SELECT  ON computer_db.keyboard TO "pc_viewer"@"localhost";
GRANT EXECUTE ON computer_db.* TO "pc_viewer"@"localhost";

CREATE USER pc_manager@localhost;
GRANT SELECT, INSERT, UPDATE, DELETE ON computer_db.computer TO "pc_manager"@"localhost";
GRANT SELECT, INSERT, UPDATE, DELETE ON computer_db.drive TO "pc_manager"@"localhost";
GRANT SELECT, INSERT, UPDATE, DELETE  ON computer_db.ram TO "pc_manager"@"localhost";
GRANT SELECT, INSERT, UPDATE, DELETE  ON computer_db.gpu TO "pc_manager"@"localhost";
GRANT SELECT, INSERT, UPDATE, DELETE  ON computer_db.pccpu TO "pc_manager"@"localhost";
GRANT SELECT, INSERT, UPDATE, DELETE  ON computer_db.mouse TO "pc_manager"@"localhost";
GRANT SELECT, INSERT, UPDATE, DELETE  ON computer_db.monitor TO "pc_manager"@"localhost";
GRANT SELECT, INSERT, UPDATE, DELETE  ON computer_db.keyboard TO "pc_manager"@"localhost";
GRANT EXECUTE, INSERT, UPDATE, DELETE ON computer_db.* TO pc_manager@localhost;

CREATE USER "pc_admin"@"localhost";
GRANT SELECT,DELETE,UPDATE,INSERT ON computer_db.* TO "cs_admin"@"localhost";
*/

-- CREATE USER "pc_registrator"@"localhost";
GRANT SELECT, CREATE ON USERS TO "registrator"@"localhost";
GRANT EXECUTE ON computer_db.* TO "registrator"@"localhost";
GRANT INSERT ON computer_db.users TO "registrator"@"localhost";


DROP PROCEDURE IF EXISTS add_user;
DELIMITER $$
CREATE PROCEDURE add_user(IN in_login varchar(50), IN in_pwd varchar(16), OUT errorcode tinyint)
BEGIN
	SET errorcode = 0;
	IF (EXISTS(SELECT login FROM computer_db.users WHERE login = in_login)) THEN SET errorcode = 10;
	ELSE INSERT INTO computer_db.users(login, pwd) VALUES (in_login, in_pwd);
	END IF;
END ; $$ 

DROP PROCEDURE IF EXISTS check_user $$

CREATE PROCEDURE check_user(IN in_login varchar(50), IN in_pwd varchar(16), OUT out_role varchar(3), OUT errorcode tinyint)
BEGIN
	SET out_role = 'USR';
	SET errorcode = 0;
	IF (NOT EXISTS(SELECT login FROM computer_db.users WHERE (login = in_login)AND(pwd = in_pwd))) THEN SET errorcode = 10;
	ELSE SET out_role = (SELECT role FROM computer_db.users WHERE (login = in_login) ) ;
	END IF;
END ; $$
DELIMITER ;

CALL add_user('alex2','asdasd',@errorcode);
CALL add_user('alex1','asdasd',@errorcode);
CALL add_user('alex2','asdasd',@errorcode);
SELECT(@errorcode);
