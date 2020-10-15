CREATE TABLE `engine_local_logic_file_version` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `logic_id` int(11) DEFAULT NULL,
  `version` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;