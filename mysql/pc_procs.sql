use computer_db;

CREATE TRIGGER update_date BEFORE UPDATE ON computer
	FOR EACH ROW SET new.move_date = now();
