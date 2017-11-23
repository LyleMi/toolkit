DROP DATABASE IF EXISTS test;

CREATE DATABASE `test` DEFAULT CHARACTER SET utf8 collate utf8_general_ci;

USE test;

CREATE TABLE `user` (
  `id` INT AUTO_INCREMENT,
  `username` VARCHAR(100) NULL,
  `password` VARCHAR(64) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Duplicate_username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE USER 'test'@'localhost' IDENTIFIED BY 'test';
GRANT SELECT, INSERT, UPDATE, DELETE ON test.user TO 'test'@'localhost';
