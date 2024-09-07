#create table on sql

# use company;

# create table test(id INT NOT NULL AUTO_INCREMENT,
# name VARCHAR(200), 
# age INT,
# PRIMARY KEY (id)
# );
# -- INSERTING DATA

# insert into test (name,age) values("ranajoy",45);

# -- view DATA

# select * from test ;

# --  update data

# update test set name="sanjoy",
# age=12
# where id=1;

# create table test2 (id INT NOT NULL AUTO_INCREMENT,
# name VARCHAR(100),
# test_id INT NOT NULL,
# PRIMARY KEY(id),
# FOREIGN KEY (test_id) REFERENCES test(id));


# how to find nth highest salary from a table
# select salary from table order by salary limit n-1,1

# difference between view and table

#different type of engines in mysql

# 1)Isam, sam, innodb, memory 

#get time in mysql



# insert into class  (class_name) values  ("9b");

# update class set class_name = "10A" where id=1;


# delete from class where id =1;


# create table student_class (
# student_id int not null,
# class_id int not null ,
# foreign key (student_id) references student(id),
# foreign key (class_id) references class(id)
# )

# SELECT * FROM company.employees where name like "A%";


# select max(salary) from company.employees where salary <(select max(salary) from company.employees);

# select salary from company.employees order by salary desc limit 1,3;


# select current_date();

# SELECT name ,count(*) FROM company.employees group by name having count(name)>1;



# empID , salary , mngID , dept ,

#  101  ,  123123 , 107 , 10

#  102 ,   223222 , 107  , 10 

#  107 ,   150000   Null , 10

# find the employee which has salary more than its manager 


select e.empID , e.mngID ,e.salary from table e
join table m on e.mngID = m.empID

where e.salary > m.salary;


# Q2: Find monthly sales and sort it by desc order


"select YEAR(order_date) as years , MONTH(order_date) as months ,SUM(sales) as total sales from products group by  
\ YEAR(order_date) , MONTH(order_date) 
\ order by total sales desc "; 



# Q3: Find the candidates best suited for an open Data Science job. Find candidates who are proficient
# in Python, SQL, and Power BI.


select employe_id ,Count(skils) as countSkills  from table where skils in ("Python","SQL","Power BI") 
group by employe_id having Count(skils) = 3 order by employe_id