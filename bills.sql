CREATE TABLE bills (
    bill_id VARCHAR(50) NOT NULL PRIMARY KEY,
    bill_date DATE NOT NULL,
    amount MONEY NOT NULL,
    paid BOOLEAN );