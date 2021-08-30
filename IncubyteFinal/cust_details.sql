create table cust_details(
    name varchar(255) not null,
    cust_id varchar(18) not null,
    open_date date not null,
    consult_date date,
    vac_type char(5),
    dr_name char(255),
    state char(5),
    country char(5),
    dob date,
    cust_status char(1)
);
