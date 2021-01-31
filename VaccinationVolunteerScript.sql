set global local_infile = 1;
-- sources: https://stackoverflow.com/questions/42966931/mysql-load-data-infile-it-contain-more-data-than-there-were-input-column
-- & https://www.mysqltutorial.org/import-csv-file-mysql-table/
load data local infile 'Users/janelleponnor/Downloads/Contact Information (Responses) - Form Responses 1.csv'
into table Hackathon
fields terminated by ','
enclosed by '"'
lines terminated by '\r\n'
ignore 1 rows;
select * from Hackathon order by state;
