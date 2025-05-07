-- create database TamakásExplor;
USE TamakásExplor;

CREATE TABLE `Usuarios` (
  `id_usuarios` int PRIMARY KEY AUTO_INCREMENT,
  `id_registro` int,
  `nombre` varchar(50) NOT NULL,
  `apellido_p` varchar(50) NOT NULL,
  `apellido_m` varchar(50) NOT NULL,
  `ciudad` varchar(50) NOT NULL,
  `estado` varchar(50) NOT NULL
);

CREATE TABLE `Niveles` (
  `id_nivel` int PRIMARY KEY AUTO_INCREMENT,
  `id_usuarios` int,
  `nivel` int,
  `puntos` int DEFAULT 0
);



CREATE TABLE `Tipos_de_niveles` (
  `tipo_nivel` int PRIMARY KEY AUTO_INCREMENT,
  `nombre` int,
  `puntos_necesarios` INT NOT NULL
);

CREATE TABLE `Registro` (
  `id_registro` int PRIMARY KEY AUTO_INCREMENT,
  `usuario` varchar(50) UNIQUE NOT NULL,
  `correo` varchar(50) UNIQUE NOT NULL,
  `contraseña` varchar(255) UNIQUE NOT NULL
);

CREATE TABLE `Informacion` (
  `id_informacion` int PRIMARY KEY AUTO_INCREMENT,
  `nombre` varchar(50),
  `telefono` varchar(10),
  `direccion` varchar(200),
  `reseña` varchar(300),
  `redsocial` varchar(200),
  `sitio_web` varchar(200),
  `costo` double,
  `tipo` ENUM ('Restaurantes', 'Hoteles', 'Productos_Artesanales', 'Lugar_Turistico')
);

CREATE TABLE `Reseña` (
  `id_reseña` int PRIMARY KEY AUTO_INCREMENT,
  `id_informacion` int,
  `id_usuarios` int,
  `cali` int(1) DEFAULT 0,
  `comentarios` varchar(150),
  `URL_Foto` varchar(255)
);

CREATE TABLE `Ruta` (
  `id_Ruta` int PRIMARY KEY AUTO_INCREMENT,
  `id_usuarios` int,
  `fecha` date,
  `estado` bool
);

CREATE TABLE `Detalles_Ruta` (
  `id_detalles_ruta` int PRIMARY KEY AUTO_INCREMENT,
  `id_Ruta` int,
  `id_informacion` int,
  `URL_Foto` varchar(255)
);

CREATE TABLE `Favoritos` (
  `id_favoritos` int PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `id_usuario` int NOT NULL,
  `id_informacion` int NOT NULL,
  `estado` bool
);

CREATE TABLE `Preguntas` (
  `id_pregunta` INT PRIMARY KEY AUTO_INCREMENT,
  `pregunta` TEXT
);

CREATE TABLE `Respuestas` (
  `id_respuesta` INT PRIMARY KEY AUTO_INCREMENT,
  `id_pregunta` INT,
  `respuesta` TEXT,
  `tipo_recomendado` ENUM("Restaurantes","Hoteles","Productos_Artesanales","Lugar_Turistico")
);

CREATE TABLE `Respuestas_Usuario` (
  `id_respuesta_usuario` INT PRIMARY KEY AUTO_INCREMENT,
  `id_usuario` INT,
  `id_respuesta` INT
);

ALTER TABLE `Respuestas` ADD FOREIGN KEY (`id_pregunta`) REFERENCES `Preguntas` (`id_pregunta`);

ALTER TABLE `Respuestas_Usuario` ADD FOREIGN KEY (`id_usuario`) REFERENCES `Usuarios` (`id_usuarios`);

ALTER TABLE `Respuestas_Usuario` ADD FOREIGN KEY (`id_respuesta`) REFERENCES `Respuestas` (`id_respuesta`);

ALTER TABLE `Usuarios` ADD FOREIGN KEY (`id_registro`) REFERENCES `Registro` (`id_registro`);

ALTER TABLE `Reseña` ADD FOREIGN KEY (`id_informacion`) REFERENCES `Informacion` (`id_informacion`);

ALTER TABLE `Reseña` ADD FOREIGN KEY (`id_usuarios`) REFERENCES `Usuarios` (`id_usuarios`);

ALTER TABLE `Ruta` ADD FOREIGN KEY (`id_usuarios`) REFERENCES `Usuarios` (`id_usuarios`);

ALTER TABLE `Detalles_Ruta` ADD FOREIGN KEY (`id_Ruta`) REFERENCES `Ruta` (`id_Ruta`);

ALTER TABLE `Detalles_Ruta` ADD FOREIGN KEY (`id_informacion`) REFERENCES `Informacion` (`id_informacion`);

ALTER TABLE `Niveles` ADD FOREIGN KEY (`id_usuarios`) REFERENCES `Usuarios` (`id_usuarios`);

ALTER TABLE `Niveles` ADD FOREIGN KEY (`nivel`) REFERENCES `Tipos_de_niveles` (`tipo_nivel`);

ALTER TABLE `Favoritos` ADD FOREIGN KEY (`id_usuario`) REFERENCES `Usuarios` (`id_usuarios`);

ALTER TABLE `Favoritos` ADD FOREIGN KEY (`id_informacion`) REFERENCES `Informacion` (`id_informacion`);

INSERT INTO Registro (usuario, correo, contraseña) VALUES
('juan123', 'juan@example.com', 'password123'),
('maria456', 'maria@example.com', 'mariaPass'),
('pedro789', 'pedro@example.com', 'pedroKey');


INSERT INTO Usuarios (id_registro, nombre, apellido_p, apellido_m, ciudad, estado) VALUES
(1, 'Juan', 'Pérez', 'López', 'San Cristóbal', 'Chiapas'),
(2, 'María', 'Gómez', 'Ramírez', 'Tuxtla Gutiérrez', 'Chiapas'),
(3, 'Pedro', 'Hernández', 'Santos', 'Comitán', 'Chiapas');


INSERT INTO Tipos_de_niveles (nombre, puntos_necesarios) VALUES
(1, 0), 
(2, 100), 
(3, 250), 
(4, 400),
(5, 550),
(6, 700),
(7, 850),
(8, 950),
(9, 1100),
(10, 2000);


INSERT INTO Niveles (id_usuarios, nivel, puntos) VALUES
(1, 1, 100),
(2, 2, 600),
(3, 3, 1200);


INSERT INTO Informacion (nombre, telefono, direccion, reseña, redsocial, sitio_web, costo, tipo) VALUES
('Hotel Chiapas', '9611234567', 'Av. Central #100, Tuxtla', 'Excelente hotel en el centro.', 'https://facebook.com/hotelchiapas', 'https://hotelchiapas.com', 1200.50, 'Hoteles'),
('Restaurante La Cabaña', '9617654321', 'Calle 5 de mayo #45, San Cristóbal', 'Comida típica chiapaneca.', 'https://instagram.com/restcabaña', 'https://lacabaña.com', 300, 'Restaurantes'),
('Artesanías Maya', '9619988776', 'Mercado Santo Domingo, San Cristóbal', 'Productos artesanales hechos a mano.', 'https://facebook.com/artesmayas', NULL, 150, 'Productos_Artesanales'),
('Cañón del Sumidero', NULL, 'Chiapas, México', 'Increíble atractivo natural.', 'https://instagram.com/canondelsumidero', 'https://canondelsumidero.com', 0, 'Lugar_Turistico');


INSERT INTO Reseña (id_informacion, id_usuarios, cali, comentarios, URL_Foto) VALUES
(1, 1, 5, 'Me encantó el hotel, excelente servicio.', 'https://example.com/hotel1.jpg'),
(2, 2, 4, 'Buena comida, pero el servicio es lento.', 'https://example.com/rest1.jpg'),
(3, 3, 5, 'Las artesanías son hermosas y de calidad.', 'https://example.com/artesanias1.jpg');


INSERT INTO Preguntas (pregunta) VALUES
('¿Qué tipo de lugar te gustaría visitar?'),
('¿Prefieres comida tradicional o internacional?');


INSERT INTO Respuestas (id_pregunta, respuesta, tipo_recomendado) VALUES
(1, 'Me gustan los lugares naturales', 'Lugar_Turistico'),
(1, 'Prefiero los hoteles cómodos', 'Hoteles'),
(2, 'Me encanta la comida tradicional', 'Restaurantes'),
(2, 'Prefiero probar comida internacional', 'Restaurantes');
