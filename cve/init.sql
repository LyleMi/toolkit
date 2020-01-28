DROP DATABASE IF EXISTS `cve`;

CREATE DATABASE `cve` DEFAULT CHARACTER SET utf8mb4 collate utf8mb4_general_ci;

use `cve`;

CREATE TABLE `cve` (
  `number` VARCHAR(32) NOT NULL,
  `name` VARCHAR(32) NOT NULL,
  `version` VARCHAR(32) NOT NULL,
  `desc` VARCHAR(4096) NOT NULL
);
