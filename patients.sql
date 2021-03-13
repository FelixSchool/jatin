CREATE TABLE patients (
    patients_id VARCHAR(50) NOT NULL,
    procedure VARCHAR(50) NOT NULL,
    doctor_id VARCHAR(50) NOT NULL,
    admit_date DATE NOT NULL,
    release_date DATE NOT NULL,
    bill_id VARCHAR(50) NOT NULL );