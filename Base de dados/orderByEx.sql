select FirstName,LastName,JobTitle
from HumanResources.vEmployeeDepartment
order by 1 asc;


select FirstName,LastName,JobTitle
from HumanResources.vEmployeeDepartment
order by 1 asc, 2 desc;


select FirstName, LastName CountryRegionName
from Sales.vIndividualCustomers
ORDER by 3 ;


select FirstName, LastName CountryRegionName
from Sales.vIndividualCustomers
where CountryRegionName in('United States', 'France')
ORDER by 3 ;



select Name,AnnualSales,YearOpened,	SquareFeet as "Store Size",	NumberEmployees [Total Employees]
from Sales.vStoreWithDemographics
where AnnualSales > 1000000 and NumberEmployees >= 45
order by "Store Size" desc, [Total Employees] desc