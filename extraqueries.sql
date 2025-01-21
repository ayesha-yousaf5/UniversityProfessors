--Extra Queries

 

-- apply filter with 'where' clause
SELECT university_id
FROM  professors
WHERE university_id='UBA';


--sorting data with ORDER BY 
SELECT firstname,
    lastname
FROM  professors
ORDER BY lastname DESC; 

--count all didtict rows from selected table
SELECT DISTINCT(COUNT(*))
FROM universities;

--select id using where clause
SELECT id
FROM organizations
WHERE organization_sector='Pharma & health';


-- Join all tables
SELECT *
FROM affiliations
JOIN professors
ON affiliations.professor_id = professors.id
JOIN organizations
ON affiliations.organization_id = organizations.id
JOIN universities
ON professors.university_id = universities.id;
-- WE WILL GET  FUNCTION COLUMN
