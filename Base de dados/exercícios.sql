select * 
from HumanResoures.Empolyee
where BirthDate <= '1/1/1980' and Gender = 'F';


where MaritalStatus = 'S' or Gender = 'M';

-- ordem de operação no sql 
-- uso de parêntesis para forçar um tipo de retorno
--  from where groupBy having  select orderBy



--IN OPERATOR

select * from HumanResources.vEmployee where FistName = 'Chris' or FistName = 'Steeve' or FistName = 'Michael' or FistName = 'Thomas';



select * from HumanResources.vEmployee where FistName IN ( 'Chris' , 'Steeve' , 'Michael' , 'Thomas');



--Between operator 

Select * from Sales.vStoreWithDemographics Where AnnualSales >= 1000000 and AnnualSales <= 2000000;


Select * from Sales.vStoreWithDemographics Where AnnualSales BETWEEN 1000000 and 2000000;


--Like OPERATOR

select * from HumanResources.vEmployee where FirsName like 'Mi%'  --retorna tudo depois de Mi



select * from HumanResources.vEmployee where FirsName like 'Mi_'  --retorna tudo depois de Mi que tenha apenas um caractere


select * from HumanResources.vEmployee where FirsName like 'D[a,o]n'  --retorna todos os empregados que começam com D terminam com n e tem 'a' ou 'o' no meio


select * from HumanResources.vEmployee where FirsName like 'D[a-o]n'  --retorna todos os empregados que começam com D terminam com n e tem o intervalo entre a e o no meio

select * from HumanResources.vEmployee where FirsName like 'D[^a-o]n'  --retorna todos os empregados que começam com D terminam com n e NÃO tem o intervalo entre a e o no meio


select * from Person.Person where MiddleName Is Not Null





-- order BY

--  from where groupBy having  select orderBy

--como o select só é executado depois, o sql não faz puta ideia que o [Customer First Name] existe. por isso quando metemos no where tem de ser o nome da tabela mas no orderBy pode ser o nome que nós demos àquela coluna
select FirstName As [Customer First Name], LastName
from Sales.vIndividualCustomer
Order By 2, [Customer First Name]






-- joins

SELECT 
		ps.Name as ProductSubCategoruName,
		pc.name as ProductCategoryName
FROM 
	production.productSubcategory ps
	inner join production.ProductCategory pc
	ON ps.productSubcategoryID = pc.productSubcategoryID





---agregate 


max()
min()
avg()
SUM()
count()


--having filtra por grupos então tem que ter um agregado associado


select st.name as [terrotory name],
		sum(TotalDue) as [total sales - 2006]
from sales.SalesOrderHeader SOH inner join sales.SalesTerritoryId
on st.TerritoryId = SOH.TerritoryId
where OrderDate between '1/1/2006' and '12/31/2006'
group by st.Name
having sum(TotalDue) > 4000000
order by 1;