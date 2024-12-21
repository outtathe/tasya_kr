/* Найдите все заказы, оформленные в августе. */
SELECT * FROM Orders
WHERE MONTH(OrderDate) = 8;

/* Перечислите всех работников, оформлявших заказы в августе. */
SELECT DISTINCT o.EmployeeID
	, e.FirstName + ' ' + e.LastName as [Full name]
FROM Orders as o
INNER JOIN Employees as e
ON e.EmployeeID = o.EmployeeID
WHERE MONTH(o.OrderDate) = 8;

/* Перечислите все продукты, присутствующие в заказах, оформленных в августе.*/ 
SELECT DISTINCT p.ProductName
FROM (Orders as o
INNER JOIN OrderDetails as od
ON o.OrderId = od.OrderId)
INNER JOIN Products p
ON p.ProductID = od.ProductID
WHERE MONTH(o.OrderDate) = 8;

/* Перечислите название, стоимость и количество отпускаемых единиц продукции для каждого заказа, оформленного в августе. */
SELECT p.ProductName,
       p.Price,
       od.Quantity
FROM (Orders AS o
     INNER JOIN OrderDetails AS od 
         ON o.OrderID = od.OrderID)
     INNER JOIN Products AS p 
         ON od.ProductID = p.ProductID
WHERE MONTH(o.OrderDate) = 8;

/* Найдите самый дорогой заказ, оформленный в августе. */
SELECT TOP 1 
    o.OrderID
    , SUM(p.Price * od.Quantity) AS orderPrice
FROM 
    (Orders AS o
    INNER JOIN OrderDetails AS od 
        ON o.OrderID = od.OrderID)
    INNER JOIN Products AS p 
        ON od.ProductID = p.ProductID
WHERE MONTH(o.OrderDate) = 8
GROUP BY o.OrderID
ORDER BY SUM(p.Price * od.Quantity) DESC;

/* Найдите работника, оформившего самый дорогой заказ в августе. */ 
SELECT TOP 1
  o.EmployeeID
  , e.FirstName & ' ' & e.LastName AS [Employee name]
  , o.OrderID
  , SUM(p.Price * od.Quantity) AS orderPrice
FROM
  (
    (
      Orders AS o
      INNER JOIN OrderDetails AS od 
         ON o.OrderID = od.OrderID
    )
    INNER JOIN Products AS p
       ON od.ProductID = p.ProductID
  )
  INNER JOIN Employees AS e
     ON o.EmployeeID = e.EmployeeID
WHERE MONTH(o.OrderDate) = 8
GROUP BY
  o.EmployeeID,
  e.FirstName,
  e.LastName,
  o.OrderID
ORDER BY
  SUM(p.Price * od.Quantity) DESC;

