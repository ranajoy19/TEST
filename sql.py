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
# select salary from table limit  order by salary limit n-1,1

# difference between view and table

#different type of engines in mysql

# 1)Isam, sam, innodb, memory 

#get time in mysql