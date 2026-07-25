CREATE DATABASE IF NOT EXISTS taller_mecanico
CHARACTER SET utf8mb4 COLLATE utf8mb4_spanish_ci;

USE taller_mecanico;

CREATE TABLE IF NOT EXISTS servicios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cliente VARCHAR(100) NOT NULL,
    vehiculo VARCHAR(100) NOT NULL,
    tipo_servicio VARCHAR(120) NOT NULL,
    costo DECIMAL(10, 2) NOT NULL,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT chk_costo_positivo CHECK (costo > 0),
    CONSTRAINT uq_servicio UNIQUE (cliente, vehiculo, tipo_servicio)
);

INSERT INTO servicios (cliente, vehiculo, tipo_servicio, costo)
VALUES ('Ana López', 'Nissan Versa 2020', 'Cambio de aceite', 850.00);

