.print Query1
--1
--Create a report, that lists for each doctor the name and the total 
--amount of each drug that the doctor prescribed in a specified period of time.
--(Drugs that he did not prescribe in that period of time should not be listed.)
select staff.name, medications.drug_name,SUM(medications.amount) AS total_amount_prescribed
from staff, medications
where julianday(medications.mdate)>=julianday('2010-01-01')
and julianday(medications.mdate)<=julianday('2010-12-31')
and medications.staff_id=staff.staff_id
GROUP BY medications.drug_name;

.print Query2
--2
--For each category of drugs, list the total amount prescribed for each drug in that
--category in a specified period of time. The report should also contain a total for each category.
select drugs.category, medications.drug_name, SUM(medications.amount) AS total_amount_prescribed
from drugs, medications
where medications.drug_name=drugs.drug_name
and julianday(medications.mdate)>=julianday('2010-01-01')
and julianday(medications.mdate)<=julianday('2011-12-31')
GROUP BY drugs.category,medications.drug_name;

.print Query3
--3
--List for a given diagnosis all possible medications that have been prescribed over 
--time after that diagnosis (over all charts). The list should be ordered by the frequency
--of the medication for the given diagnosis.
select medications.drug_name as possible_medications
from medications, diagnoses
where diagnoses.diagnosis='worms'
and julianday(medications.mdate)>=julianday(diagnoses.ddate)
group by medications.drug_name
order by count(*) DESC;

.print Query4
--4
--List for a given drug all the diagnoses that have been made before prescribing the drug
--(over all charts). The list should be ordered by the average amount of the drug prescribed
--for the diagnoses.
select diagnoses.diagnosis as previous_diagnoses
from diagnoses,medications
where medications.drug_name='Xanax'
and julianday(diagnoses.ddate)<julianday(medications.mdate)
group by previous_diagnoses
order by AVG(medications.amount);

