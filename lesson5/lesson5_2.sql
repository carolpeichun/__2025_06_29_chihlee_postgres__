DROP TABLE IF EXISTS employee CASCADE;	/*因employee跟branch已有建立關聯，要加CASCADE才DROP的掉*/
DROP TABLE IF EXISTS branch;			/*因employee強制DROP掉已跟branch取消關聯，故不需加CASCADE也能DROP的掉*/

CREATE TABLE employee(
	emp_id SERIAL,
	name VARCHAR(20),
	birth_date DATE,
	sex VARCHAR(1),
	salary INT,
	branch_id INT,
	sup_id INT,
 	PRIMARY KEY(emp_id)
);

CREATE TABLE branch(
	branch_id INT,
	branch_name VARCHAR(20),
	manager_id INT,
	PRIMARY KEY(branch_id),
	FOREIGN KEY(manager_id)
	REFERENCES employee(emp_id) ON DELETE SET NULL
);

ALTER TABLE employee
ADD FOREIGN KEY(branch_id) REFERENCES branch(branch_id) ON DELETE SET NULL;

ALTER TABLE employee
ADD FOREIGN KEY(sup_id) REFERENCES employee(emp_id) ON DELETE SET NULL;