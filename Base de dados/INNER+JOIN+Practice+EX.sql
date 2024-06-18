select pp.FirstName, pp.LastName, pw.PasswordHash
from Person.Person pp inner join 
	 Person.Password pw on pp.BusinessEntityID 
	 = pw.BusinessEntityID


--ex2
select HE.BusinessEntityID,HE.NationalIDNumber,HE.JobTitle,
	HEH.DepartmentID,HEH.StartDate,HEH.EndDate
from HumanResources.Employee HE inner join 
	 HumanResources.EmployeeDepartmentHistory HEH
	 on HE.BusinessEntityID = HEH.BusinessEntityID
	 
	 

--ex3
select pp.FirstName, pp.LastName, pw.PasswordHash, pe.EmailAddress
from 
	Person.Person pp inner join Person.Password pw 	 
	 on pp.BusinessEntityID = pw.BusinessEntityID 
	 inner join Person.EmailAddress pe
	 on pp.BusinessEntityID = pe.BusinessEntityID
	 
	
	
--ex4

select b.title, b.isbn
		a.authorName
from Book b inner join BookAuthor ba on b.xxxx = ba.xxxx
	inner join Author a on b.xxx = a.xxx
	
	
	
--ex5	
select  b.title, b.isbn
		a.authorName
		p.publisherName
from Book b inner join BookAuthor ba 
	 on b.xxxx = ba.xxxx
	 inner join Author a 
	 on b.xxx = a.xxx
	 inner join Publisher p
	 on b.publisherID = p.publisherID
	 