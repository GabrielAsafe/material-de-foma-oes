--ex 1.1
select Name, ProductSubcategoryID
from Production.Product
where ProductSubcategoryID <= 3
order by 2;



--ex1.2

select NAME, LISTPRICE, SAFETYSTOCKLEVEL
from Production.Product
where ListPrice > 1000
order by 2;


--1.3

select Name
from Production.Product
order by 1 desc;



--ex 1.4
select Name, ProductSubcategoryID,ListPrice
from Production.Product
where ProductSubcategoryID <= 3 and ListPrice > 1000
order by 2;



--ex1.5  1.7
select Name
from Production.Product
where Name like  '%MOUNTAIN%'
;


--ex 1.6
select sum(SafetyStockLevel)
from Production.Product
;




--ex 1.8
select Name, ProductSubcategoryID, [preço médio por categoria]=avg(ListPrice) over(order by name)
from Production.Product
where ProductSubcategoryID <= 3


-- ex 1.9
select [Nome produto]=p.Name, [Nome subcategoria]=ps.Name
from Production.Product p ,Production.ProductSubcategory ps 
where p.ProductSubcategoryID = ps.ProductSubcategoryID
;



--ex1.10
select CountryRegionCode,p.Name,[QUANTIDADE VENDIDA]= sum(A.ProductID)
from Sales.SalesOrderDetail A, Sales.SalesOrderHeader B, Sales.SalesTerritory C, Production.Product P
where A.SalesOrderID = B.SalesOrderID and B.TerritoryID  = C.TerritoryID and P.ProductID = A.ProductID
group by CountryRegionCode,p.Name
order by 3
;




--ex 1.11

select 
	[CATEGORIA DO PRODUTO]=pc.Name, 
	[MÉDIA DE PREÇO DE VENDA POR CATEGORIA]=  avg(p.ListPrice) over(order by pc.name) 

into #teste
from Production.Product p ,Production.ProductSubcategory pc 
where p.ProductSubcategoryID = pc.ProductCategoryID 
order by 1
;


select distinct 
	nome =[CATEGORIA DO PRODUTO],
	med = [MÉDIA DE PREÇO DE VENDA POR CATEGORIA]
from #teste;

drop table #teste;

--segunda iteração

select 
x.Name,x.ProductCategoryID, soma = sum(ListPrice) over (order by listprice)
from(
select ListPrice,ps.ProductCategoryID,p.Name
from Production.Product p, Production.ProductCategory pc, Production.ProductSubcategory ps		
where p.ProductSubcategoryID = ps.ProductSubcategoryID and ps.ProductCategoryID = pc.ProductCategoryID
		)x
	where x.ListPrice>100


--ex 1.12

select Name, ROW_NUMBER() over(order by name)
from Production.Product


--ex 1.13

select p.name ,[QTD Stock por categoria ]= ROW_NUMBER() over( partition by pr.Quantity order by pc.ProductCategoryID) 
from 
	Production.Product p join Production.ProductInventory pr 
	on p.ProductID = pr.ProductID 
	
	join Production.ProductSubcategory ps 
	on ps.ProductSubcategoryID = p.ProductSubcategoryID

	join	Production.ProductCategory pc 
	on ps.ProductCategoryID = pc.ProductCategoryID


--ex1.14


select Name, ListPrice
from Production.Product
FOR XML PATH('')

--segunda iteração

SELECT
		[Nome] = p.Name,
		[Products] = STUFF(
			  (
				select   ',' +p.ListPrice  
				from Production.Product p1
				where p.ProductID = p1.ProductID 

				 FOR XML PATH('')
				 ),1,1,''
		)

FROM  Production.Product p




--ex1.15


SELECT *
FROM (
    SELECT p.name, MONTH(sh.OrderDate) AS OrderMonth, p.ListPrice
    FROM Sales.SalesOrderDetail so
    INNER JOIN Sales.SalesOrderHeader sh ON so.SalesOrderID = sh.SalesOrderID
    INNER JOIN Production.Product p ON p.ProductID = so.ProductID
) AS P
PIVOT (
    SUM(ListPrice)
    FOR OrderMonth IN ([1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12])
) AS PivotTable;




--ex1.16 

with sales as(
	select 
	SalesPersonID, 
	[quantidade]=count(SalesPersonID) 
	--,[TotalSales]= 
	from Sales.SalesOrderHeader 
	where SalesPersonID is not null
	group by SalesPersonID
)

select 
b.SalesPersonID
,quantidade
,[total sales] = sum( A.OrderQty * A.UnitPrice) 
from sales s join
[Sales].[SalesOrderHeader] B on s.SalesPersonID = b.SalesPersonID join
[Sales].[SalesOrderDetail] A on a.SalesOrderID = b.SalesOrderID


where quantidade>200
group by b.SalesPersonID ,quantidade

;




--ex1.17
CREATE FUNCTION Vendas_por_terrirtorio()
RETURNS table AS 
return(
	select TerritoryId,[TOTAL DE VENDAS POR TERRITÓRIO]=sum(TotalDue) 
	from Sales.SalesOrderHeader
	group by TerritoryId
	--order by 1
);


select * from Vendas_por_terrirtorio() order by 1;

drop function Vendas_por_terrirtorio;







--ex 1.18
--select * from Production.product;
--SELECT * into #testeProduct from Production.product;
--select * from #testeProduct;


CREATE TRIGGER atualizar_datas
ON Production.product
AFTER UPDATE
AS
BEGIN
    UPDATE Production.product
    SET ModifiedDate = GETDATE()

END;


--ex 1.19

CREATE VIEW View_produto_categoria_preco AS
SELECT [nome do produto]=p.Name,[Nome da categoria]= pc.Name, p.ListPrice
FROM 
Production.ProductSubcategory ps join  Production.Product p 
on ps.ProductSubcategoryID = p.ProductSubcategoryID 
join  Production.ProductCategory pc 
on ps.ProductCategoryID = pc.ProductCategoryID;


select * from View_produto_categoria_preco order by 2




--ex 1.20
CREATE PROCEDURE ATUALIZA_PRECO_PRODUTO
     @ValorMonetario money,
     @ID int
AS
BEGIN

	UPDATE Production.Product
    SET ListPrice = @ValorMonetario
    WHERE  ProductID= @ID;

END;
select * from Production.product;

exec ATUALIZA_PRECO_PRODUTO 10,1;





--ex 1.21
select 
	p.name,		
	case 
		when pin.Quantity > 100 
		then 'Em stock' 
		else 'Sem stock' 
	end 
from Production.product p inner join Production.ProductInventory pin on p.ProductID = pin.ProductID;



--ex 1.22

Declare @categoria Varchar(100)
DECLARE @NameColumn VARCHAR(100)
DECLARE @DynamicSQL VARCHAR(MAX)

set @categoria = 'bikes'


SET @NameColumn = upper(@categoria) --cria uma nova var


SET @DynamicSQL = 
'
	SELECT [nome do produto]=p.Name
	FROM 
	Production.ProductSubcategory ps join  Production.Product p 
	on ps.ProductSubcategoryID = p.ProductSubcategoryID 
	join  Production.ProductCategory pc 
	on ps.ProductCategoryID = pc.ProductCategoryID

	where pc.name like ''%'

SET @DynamicSQL = @DynamicSQL + @NameColumn + '%'''


EXEC(@DynamicSQL)




--ex 1.23  

BEGIN TRANSACTION;

DECLARE @ProductID INT = 789;
DECLARE @QuantidadeTransferida INT = 10;
DECLARE @OrigemLocationID INT = 7;
DECLARE @DestinoLocationID INT = 60;

-- Verifica se há estoque suficiente na LocationID de origem
IF EXISTS (SELECT * FROM Production.ProductInventory WHERE ProductID = @ProductID AND LocationID = @OrigemLocationID AND Quantity >= @QuantidadeTransferida)
BEGIN
    -- Decrementa o estoque da LocationID de origem
    UPDATE Production.ProductInventory
    SET Quantity = Quantity - @QuantidadeTransferida
    WHERE ProductID = @ProductID AND LocationID = @OrigemLocationID;

    -- Incrementa o estoque da LocationID de destino
    IF EXISTS (SELECT * FROM Production.ProductInventory WHERE ProductID = @ProductID AND LocationID = @DestinoLocationID)
    BEGIN
        UPDATE Production.ProductInventory
        SET Quantity = Quantity + @QuantidadeTransferida
        WHERE ProductID = @ProductID AND LocationID = @DestinoLocationID;
    END
    ELSE
    BEGIN
        INSERT INTO Production.ProductInventory (ProductID, LocationID, Quantity)
        VALUES (@ProductID, @DestinoLocationID, @QuantidadeTransferida);
    END

    COMMIT TRANSACTION;
    PRINT 'Transferência concluída com sucesso.';
END
ELSE
BEGIN
    ROLLBACK TRANSACTION;
    PRINT 'Estoque insuficiente na LocationID de origem.';
END




--ex 1.24

UPDATE Production.Product
SET ListPrice = ListPrice * 1.1 -- Aumenta o preço em 10%
WHERE ProductID IN (
	SELECT ProductID
	FROM 
	Production.ProductSubcategory ps join  Production.Product p 
	on ps.ProductSubcategoryID = p.ProductSubcategoryID 
	join  Production.ProductCategory pc 
	on ps.ProductCategoryID = pc.ProductCategoryID
	where pc.name like 'BIKES'

);




--ex 1.25

select  *, row_number() over(partition by productId order by LocationId) from Production.ProductInventory



DELETE FROM Production.ProductInventory
WHERE ProductID IN (
    SELECT ProductID
    FROM (
        SELECT ProductID, ROW_NUMBER() OVER(PARTITION BY ProductID ORDER BY (SELECT NULL)) AS RowNumber
        FROM Production.ProductInventory
    ) AS Temp
    WHERE RowNumber > 1
);


with duplicados as
(
 SELECT ProductID, ROW_NUMBER() OVER(PARTITION BY ProductID ORDER BY (SELECT NULL)) AS RowNumber
 FROM Production.ProductInventory
)
delete from duplicados where RowNumber > 1;


