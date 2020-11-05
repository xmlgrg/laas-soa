CREATE TABLE `workflow_struct`
(
    `id`          int(11)   NOT NULL AUTO_INCREMENT,
    `title`         int(11)   NOT NULL,
    `did`         int(11)   NOT NULL,
    `file`        mediumtext COLLATE utf8mb4_unicode_ci,
    `update_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`)
) ENGINE = InnoDB
  AUTO_INCREMENT = 1
  DEFAULT CHARSET = utf8mb4
  COLLATE = utf8mb4_unicode_ci;

CREATE TABLE `workflow_data`
(
    `id`          int(11)   NOT NULL AUTO_INCREMENT,
    `lid`         int(11)   NOT NULL,
    `did`         int(11)   NOT NULL,
    `file`        mediumtext COLLATE utf8mb4_unicode_ci,
    `update_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`)
) ENGINE = InnoDB
  AUTO_INCREMENT = 1
  DEFAULT CHARSET = utf8mb4
  COLLATE = utf8mb4_unicode_ci;


CREATE TABLE `workflow_log`
(
    `id`          int(11)   NOT NULL AUTO_INCREMENT,
    `lid`         int(11)   NOT NULL,
    `did`         int(11)   NOT NULL,
    `file`        mediumtext COLLATE utf8mb4_unicode_ci,
    `update_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`)
) ENGINE = InnoDB
  AUTO_INCREMENT = 1
  DEFAULT CHARSET = utf8mb4
  COLLATE = utf8mb4_unicode_ci;