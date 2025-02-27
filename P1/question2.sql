--2.a

'''create database to in order to computerise a store whe sales televisions '''


'''normalise the brands'''
CREATE TABLE brands (
    brand_id INTEGER PRIMARY KEY AUTOINCREMENT,
    brand_name TEXT NOT NULL UNIQUE CHECK(brand_name IN ('Xiaomi', 'Samsung', 'LG', 'Sony'))
);


'''create the television table'''

CREATE TABLE Televisions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    number_catalog TEXT NOT NULL UNIQUE,
    brand_id INTEGER NOT NULL,
    model TEXT NOT NULL,
    size_screen INTEGER NOT NULL,
    resolution TEXT NOT NULL CHECK(resolution IN ('4K', '8K', 'Full HD')),
    price REAL NOT NULL CHECK(price > 0),
    quantity_stock INTEGER NOT NULL,
    year_release INTEGER NOT NULL,
    tv_smart INTEGER NOT NULL CHECK(tv_smart IN (0,1)),
    os TEXT DEFAULT NULL,
    panel_type TEXT NOT NULL CHECK(panel_type IN ('OLED', 'QLED', 'LED')),
    FOREIGN KEY (brand_id) REFERENCES brands(brand_id) ON DELETE CASCADE,
    CHECK (tv_smart = 1 OR os IS NULL)
);

'''turning brands into numbers for normalise'''

INSERT INTO brands (brand_name) VALUES ('Samsung');
INSERT INTO brands (brand_name) VALUES ('LG');
INSERT INTO brands (brand_name) VALUES ('Sony');

'''check if everithing is working'''
SELECT * FROM brands;

'''insert data'''
INSERT INTO Televisions
(number_catalog, brand_id, model, size_screen, resolution, price, quantity_stock, year_release, tv_smart, os, panel_type)
VALUES
('SM123a45', 1, 'QN65Q80A', 65, '4K', 4500.99, 20, 2023, 1, 'Tizen', 'QLED');

INSERT INTO Televisions
(number_catalog, brand_id, model, size_screen, resolution, price, quantity_stock, year_release, tv_smart, os, panel_type)
VALUES
('LG987s65', 2, 'OLED55C1', 55, '4K', 3200.50, 15, 2022, 1, 'WebOS', 'OLED');

INSERT INTO Televisions
(number_catalog, brand_id, model, size_screen, resolution, price, quantity_stock, year_release, tv_smart, os, panel_type)
VALUES
('SN56d789', 3, 'KD-75X85J', 75, '4K', 5500.00, 10, 2024, 0, NULL, 'LED');


