select FirstName, LastName
from Person.Person
where FirstName = 'Mark';

-- !!!
select top 100 *
from Production.Product
where ListPrice Is not 0.00;


-- !!!
select * 
from HumanResources.vEmployee
where LastName like '[a-d]%';


select * from Person.StateProvince 
where CountryRegionCode like 'CA';



select FirstName as 'Customer First Name', LastName as 'Customer Lats	Name'
from Sales.vIndividualCustomer
where LastName like 'Smith';

Select *
from Sales.vIndividualCustomer
where CountryRegionName = 'Australia' or (PhoneNumberType = 'Cell' and EmailPromotion = 0)


select * 
from HumanResources.vEmployeeDepartment 
where Department in( 'Executive', 'Tool Design', 'Engineering');



-- !!!
select *
from HumanResources.vEmployeeDepartment
where StartDate	between	'July/1/2000'	and	'June/30/2002';



select *
from Sales.vIndividualCustomer
where LastName like "R%";


select *
from Sales.vIndividualCustomer
where LastName like "%r";


select *
from Sales.vIndividualCustomer
where LastName IN('Lopez','Martin','Wood') and FirstName like '[c,l]%';



select *
from Sales.SalesOrderHeader
where SalesPersonID is not null;


select SalesPersonID, TotalDue
from Sales.SalesOrderHeader
where SalesPersonID is not null and TotalDue > 70000;