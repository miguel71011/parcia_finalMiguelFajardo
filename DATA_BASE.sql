
/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- Volcando estructura de base de datos para control
CREATE DATABASE IF NOT EXISTS `control` /*!40100 DEFAULT CHARACTER SET latin1 COLLATE latin1_spanish_ci */;
USE `control`;

-- Volcando estructura para tabla control.assistances
CREATE TABLE IF NOT EXISTS `assistances` (
  `Assistance_id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `assistanceCheck` varchar(45) COLLATE latin1_spanish_ci DEFAULT '0' COMMENT '0=falla 1=asiste',
  `Session_id` int(11) unsigned NOT NULL,
  `Student_id` int(11) unsigned NOT NULL,
  PRIMARY KEY (`Assistance_id`),
  KEY `Student_id_idx` (`Student_id`),
  KEY `Session_id_idx` (`Session_id`),
  CONSTRAINT `FK_assistances_sessions` FOREIGN KEY (`Session_id`) REFERENCES `sessions` (`Session_id`) ON UPDATE CASCADE,
  CONSTRAINT `FK_assistances_students` FOREIGN KEY (`Student_id`) REFERENCES `students` (`Student_id`) ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

-- Volcando datos para la tabla control.assistances: ~5 rows (aproximadamente)
/*!40000 ALTER TABLE `assistances` DISABLE KEYS */;
INSERT INTO `assistances` (`Assistance_id`, `assistanceCheck`, `Session_id`, `Student_id`) VALUES
	(1, '1', 2, 7),
	(2, '0', 1, 7),
	(5, '1', 8, 2),
	(6, '0', 10, 2),
	(7, '0', 11, 2),
	(17, '0', 8, 9),
	(18, '0', 10, 9),
	(19, '0', 11, 9);
/*!40000 ALTER TABLE `assistances` ENABLE KEYS */;

-- Volcando estructura para tabla control.semesters
CREATE TABLE IF NOT EXISTS `semesters` (
  `Semester_id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `semester` tinyint(4) NOT NULL,
  `Slot_id` int(11) unsigned NOT NULL,
  PRIMARY KEY (`Semester_id`),
  KEY `Slot_id_idx` (`Slot_id`),
  CONSTRAINT `FK_semesters_slots` FOREIGN KEY (`Slot_id`) REFERENCES `slots` (`Slot_id`) ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

-- Volcando datos para la tabla control.semesters: ~4 rows (aproximadamente)
/*!40000 ALTER TABLE `semesters` DISABLE KEYS */;
INSERT INTO `semesters` (`Semester_id`, `semester`, `Slot_id`) VALUES
	(1, 1, 6),
	(2, 3, 7),
	(3, 4, 8),
	(4, 4, 9);
/*!40000 ALTER TABLE `semesters` ENABLE KEYS */;

-- Volcando estructura para tabla control.sessions
CREATE TABLE IF NOT EXISTS `sessions` (
  `Session_id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `semester_id` int(11) unsigned NOT NULL,
  `sessionName` varchar(70) COLLATE latin1_spanish_ci NOT NULL,
  `date_start` datetime NOT NULL,
  `date_end` datetime NOT NULL,
  PRIMARY KEY (`Session_id`),
  KEY `Slot2_id_idx` (`semester_id`) USING BTREE,
  CONSTRAINT `FK_sessions_semesters` FOREIGN KEY (`semester_id`) REFERENCES `semesters` (`Semester_id`) ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

-- Volcando datos para la tabla control.sessions: ~6 rows (aproximadamente)
/*!40000 ALTER TABLE `sessions` DISABLE KEYS */;
INSERT INTO `sessions` (`Session_id`, `semester_id`, `sessionName`, `date_start`, `date_end`) VALUES
	(1, 1, 'actinity', '2021-05-11 20:08:51', '2021-05-11 22:08:58'),
	(2, 2, 'quix', '2021-06-11 20:14:45', '2021-06-11 20:14:46'),
	(8, 3, 'exponer', '2021-06-02 20:14:45', '2021-06-02 20:14:46'),
	(9, 4, 'exponer', '2021-06-02 20:14:45', '2021-06-02 20:14:46'),
	(10, 3, 'presentarpri', '2021-06-02 20:14:45', '2021-06-02 20:14:46'),
	(11, 3, 'clase final', '2021-06-02 20:14:45', '2021-06-02 20:14:46');
/*!40000 ALTER TABLE `sessions` ENABLE KEYS */;

-- Volcando estructura para tabla control.slots
CREATE TABLE IF NOT EXISTS `slots` (
  `Slot_id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(45) COLLATE latin1_spanish_ci NOT NULL,
  PRIMARY KEY (`Slot_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

-- Volcando datos para la tabla control.slots: ~4 rows (aproximadamente)
/*!40000 ALTER TABLE `slots` DISABLE KEYS */;
INSERT INTO `slots` (`Slot_id`, `name`) VALUES
	(6, 'py'),
	(7, 'js'),
	(8, 'sql'),
	(9, 'bd');
/*!40000 ALTER TABLE `slots` ENABLE KEYS */;

-- Volcando estructura para tabla control.students
CREATE TABLE IF NOT EXISTS `students` (
  `Student_id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `identification` varchar(45) COLLATE latin1_spanish_ci NOT NULL,
  `name` varchar(80) COLLATE latin1_spanish_ci NOT NULL,
  `lastName` varchar(80) COLLATE latin1_spanish_ci NOT NULL,
  `phone` varchar(15) COLLATE latin1_spanish_ci NOT NULL,
  `mail` varchar(256) COLLATE latin1_spanish_ci NOT NULL,
  PRIMARY KEY (`Student_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

-- Volcando datos para la tabla control.students: ~4 rows (aproximadamente)
/*!40000 ALTER TABLE `students` DISABLE KEYS */;
INSERT INTO `students` (`Student_id`, `identification`, `name`, `lastName`, `phone`, `mail`) VALUES
	(2, '2222', 'felipe', 'benavides', '31683923', 'felipe@gmial.com'),
	(7, '2222', 'hugo', 'chaves', '31683923', 'hdhl@gmial.com'),
	(8, '2222', 'santi', 'posso', '31683923', 'dfgd@gmial.com'),
	(9, '2222', 'jhoan', 'daza', '31683923', 'felipe@gmial.com');
/*!40000 ALTER TABLE `students` ENABLE KEYS */;

-- Volcando estructura para tabla control.students_semesters
CREATE TABLE IF NOT EXISTS `students_semesters` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `student_id` int(11) unsigned NOT NULL,
  `semester_id` int(10) unsigned NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `FK_students_semesters_students` (`student_id`),
  CONSTRAINT `FK_students_semesters_students` FOREIGN KEY (`student_id`) REFERENCES `students` (`Student_id`) ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8;

-- Volcando datos para la tabla control.students_semesters: ~4 rows (aproximadamente)
/*!40000 ALTER TABLE `students_semesters` DISABLE KEYS */;
INSERT INTO `students_semesters` (`id`, `student_id`, `semester_id`) VALUES
	(2, 2, 3),
	(8, 2, 2),
	(11, 7, 1),
	(12, 7, 2),
	(17, 9, 3);
/*!40000 ALTER TABLE `students_semesters` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
