
-- Insearting data and finding answer to nusiness questions

-- Q. 1
SELECT COUNT(*)
FROM patients
WHERE admit_date BETWEEN '2019-03-01' AND '2019-04-30'

-- Q. 2
SELECT patients.doctor_id, SUM(bills.amount)
FROM patients
JOIN bills 
ON patients.bill_id=bills.bill_id
WHERE bills.bill_date >= '2019-03-01'::DATE AND bills.bill_date <= '2019-04-30'::DATE
AND bills.paid = 'true'
GROUP BY doctor_id;

-- Q. 3
SELECT SUM(amount)
FROM bills
WHERE paid='false'

-- Q. 4
SELECT doctor.department, SUM(bills.amount)
FROM patients
JOIN bills 
ON patients.bill_id=bills.bill_id
JOIN doctor
ON patients.doctor_id=doctor.doctor_id
WHERE bills.bill_date >= '2019-03-01'::DATE AND bills.bill_date <= '2019-04-30'::DATE
AND bills.paid = 'true'
GROUP BY doctor.department;