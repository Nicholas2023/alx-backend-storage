-- A script that creates a trigger that decreases the quantity of an item after adding a new order
-- Quantity in the items' table can be negative

DELIMITER //
DROP TRIGGER IF EXISTS minimize_quantity;
CREATE TRIGGER minimize_quantity
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
        SET quantity = quantity - NEW.number
        WHERE name = NEW.item_name;
END //
