CREATE DATABASE techstore;

USE techstore;
CREATE TABLE usuarios(
id INT auto_increment PRIMARY KEY,
nombre VARCHAR(80) NOT NULL,
correo VARCHAR(100) UNIQUE NOT NULL,
telefono VARCHAR(20) NOT NULL,
password VARCHAR(255) NOT NULL,
rol ENUM('Administrador', 'Cliente') DEFAULT 'Cliente',
estado ENUM('Activo','Inactivo') DEFAULT 'Activo');

INSERT INTO usuarios(nombre, correo, telefono, password, rol, estado) VALUES
('Sebastian', 'jsdg@gmail.com', '3217252560', 'scrypt:32768:8:1$AOc2ZcDbINjnCpab$c28edf81386493705450fd4249f1381e129b99fcaef3c33a2122bbad23132eeab8d0fd354ab14c2a7cbcd17a9ea5e5e86f9d5776d4646b937d98c7ddc6c9db9e', 'Administrador', 'Activo'),
('Admin', 'admin@techsore.com', '3213214321', 'scrypt:32768:8:1$w3CdBAJxO93F5fz0$59c3da70e3db5bd84f98cafaa8e4c591a69c36d36973531948ec9b90056553e2fc9503acc768e9de4322e3ca95699b04b562e177c3ce135c0a30631cbeecec8e', 'Administrador', 'Activo');

CREATE TABLE productos(
codigo VARCHAR(20) PRIMARY KEY,
nombre VARCHAR(80) NOT NULL,
precio DECIMAL(10,2) NOT NULL,
categoria VARCHAR(50),
imagen_url VARCHAR(255)
);

INSERT INTO productos VALUES
('P001','Laptop Lenovo',3500000,'Computadores','w=1160.webp'),
('P002','Mouse Logitech',85000,'Accesorios','mouse-gamer-logitech-g203-lightsync-rgb-6-botones-8000dpi.webp'),
('P003','Monitor Samsung',890000,'Monitores','Monitor-Samsung-19-pulgadas-HD-S33A-Vista-Angulo-Izquierdo.webp'),
('P004', 'Portátil Lenovo IdeaPad 3', 2850000, 'Computadores','portatil-lenovo-ideapad-3-14-core-i5-8gb-512gb-ssd-w10.webp');