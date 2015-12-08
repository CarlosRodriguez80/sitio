-- phpMyAdmin SQL Dump
-- version 4.5.0.2
-- http://www.phpmyadmin.net
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 08-12-2015 a las 03:36:30
-- Versión del servidor: 10.0.17-MariaDB
-- Versión de PHP: 5.6.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `sitio`
--

--
-- Volcado de datos para la tabla `votacion_universidad`
--

INSERT INTO `votacion_universidad` (`id`, `nombre`, `ciudad`, `provincia`, `logo`) VALUES
(1, 'UPE', 'Ezeiza', 'Buenos Aires', 'logos/upe_logo.jpg'),
(2, 'UAI', 'Avellaneda', 'Buenos Aires', 'logos/uai.jpg'),
(3, 'UBA', 'Capital Federal', 'Buenos Aires', 'logos/uba.jpg'),
(4, 'Universidad de Belgrano', 'Belgrano', 'Buenos Aires', 'logos/ube.jpg'),
(5, 'UTN', 'Palermo', 'Buenos Aires', 'logos/images.png');

--
-- Volcado de datos para la tabla `votacion_unidad`
--

INSERT INTO `votacion_unidad` (`id`, `nombre`, `universidad_id`) VALUES
(1, 'Introduccion al Desarrollo', 1),
(2, 'Matematicas', 3),
(3, 'Ingles', 2),
(4, 'Tecnicas de la Programacion', 1),
(5, 'Administracion de Empresas', 2),
(6, 'Software y los Nuevos Escenarios', 5),
(7, 'Laboratorio de informatica', 4),
(8, 'Psicologia', 3);


--
-- Volcado de datos para la tabla `votacion_config_pagina`
--

INSERT INTO `votacion_config_pagina` (`id`, `paginacion`, `top`, `recientes`, `populares`) VALUES
(1, 5, 5, 5, 5);

--
-- Volcado de datos para la tabla `votacion_profesor`
--

INSERT INTO `votacion_profesor` (`id`, `apellido`, `nombre`, `apodo`, `foto`, `linkedin`, `confirmado_flag`, `universidad_id`, `unidad_id`, `user_id`) VALUES
(1, 'Arias', 'German', 'ariaste', 'fotos/arias.jpg', '', 1, 1, 1, 1),
(2, 'Ronconi', 'Francisco', 'Chamu', 'fotos/fran.jpg', '', 1, 5, 7, 1),
(3, 'Esquel', 'Pablo', '', 'fotos/pa.jpg', '', 2, 3, 6, 1),
(4, 'Palomino', 'German', 'palo', 'fotos/germi.jpg', '', 1, 4, 5, 1),
(5, 'Otero', 'Sebastian', 'seba', 'fotos/seba.jpg', '', 2, 4, 3, 1);

--
-- Volcado de datos para la tabla `votacion_calificacion`
--

INSERT INTO `votacion_calificacion` (`id`, `puntaje`, `comentario`, `pub_date`, `profesor_id`, `user_id`) VALUES
(4, 4, 'Es genial!!!!', '2015-12-08 00:13:05', 2, 1),
(5, 3, 'Un excelente profesor', '2015-12-08 00:13:05', 1, 1),
(6, 3, 'Muy atento', '2015-12-08 00:13:05', 4, 1),
(7, 2, 'Muy chamullero', '2015-12-08 00:13:05', 2, 1),
(8, 4, 'Genial!!!', '2015-12-08 00:13:05', 1, 2),
(9, 3, 'Es muy buen profesor', '2015-12-08 00:13:05', 2, 1);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;