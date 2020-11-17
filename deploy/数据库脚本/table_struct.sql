CREATE TABLE `designer_data_directory`
(
    `id`          int(11)                                 NOT NULL AUTO_INCREMENT,
    `pid`         int(11)                                 NOT NULL DEFAULT '-1',
    `name`        varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
    `description` varchar(255) COLLATE utf8mb4_unicode_ci          DEFAULT '',
    PRIMARY KEY (`id`)
) ENGINE = InnoDB
  AUTO_INCREMENT = 1
  DEFAULT CHARSET = utf8mb4
  COLLATE = utf8mb4_unicode_ci;



create table designer_data_struct
(
    id             int auto_increment
        primary key,
    did            int                           not null,
    code           varchar(100)                  not null,
    meaning        varchar(100)                  not null,
    reference_type varchar(100)                  null,
    is_open_data   tinyint      default 0        null comment '是否开放数据',
    data_type      varchar(100) default 'string' null comment '数据类型',
    default_value  varchar(255)                  null comment '默认值'
);



CREATE TABLE `designer_logic_directory`
(
    `id`          int(11)                                 NOT NULL AUTO_INCREMENT,
    `pid`         int(11)                                 DEFAULT NULL,
    `name`        varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
    `description` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
    PRIMARY KEY (`id`)
) ENGINE = InnoDB
  AUTO_INCREMENT = 1
  DEFAULT CHARSET = utf8mb4
  COLLATE = utf8mb4_unicode_ci;

CREATE TABLE `designer_logic_data`
(
    `id`          int(11)   NOT NULL AUTO_INCREMENT,
    `did`         int(11)   NOT NULL,
    `file`        mediumtext COLLATE utf8mb4_unicode_ci,
    `update_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`)
) ENGINE = InnoDB
  AUTO_INCREMENT = 1
  DEFAULT CHARSET = utf8mb4
  COLLATE = utf8mb4_unicode_ci;

CREATE TABLE `designer_data_logic_io`
(
    `id`       int(11)                                NOT NULL AUTO_INCREMENT,
    `data_id`  int(11)                                NOT NULL,
    `logic_id` int(11)                                NOT NULL,
    `type`     varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8mb4
  COLLATE = utf8mb4_unicode_ci;

CREATE TABLE `designer_data_logic_trigger`
(
    `id`        int(11)                                 NOT NULL AUTO_INCREMENT,
    `data_id`   int(11)                                 NOT NULL,
    `logic_id`  int(11)                                 NOT NULL,
    `func_name` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
    `type`      varchar(50) COLLATE utf8mb4_unicode_ci  NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8mb4
  COLLATE = utf8mb4_unicode_ci;

CREATE TABLE `engine_data_logic_trigger_data_log`
(
    `id`              int(11)   NOT NULL AUTO_INCREMENT,
    `data_id`         int(11)                                 DEFAULT NULL,
    `data_data_id`    int(11)                                 DEFAULT NULL,
    `data_event_type` varchar(50) COLLATE utf8mb4_unicode_ci  DEFAULT NULL,
    `logic_id`        int(11)                                 DEFAULT NULL,
    `func_name`       varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
    `create_time`     timestamp NULL                          DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    `log_level`       varchar(50) COLLATE utf8mb4_unicode_ci  DEFAULT 'TRACE',
    `log`             text COLLATE utf8mb4_unicode_ci,
    PRIMARY KEY (`id`)
) ENGINE = InnoDB
  AUTO_INCREMENT = 1
  DEFAULT CHARSET = utf8mb4
  COLLATE = utf8mb4_unicode_ci;

CREATE TABLE `engine_data_logic_trigger_data_status`
(
    `id`              int(11)   NOT NULL AUTO_INCREMENT,
    `data_id`         int(11)                                 DEFAULT NULL,
    `data_data_id`    int(11)                                 DEFAULT NULL,
    `data_event_type` varchar(50) COLLATE utf8mb4_unicode_ci  DEFAULT NULL,
    `logic_id`        int(11)                                 DEFAULT NULL,
    `func_name`       varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
    `create_time`     timestamp NULL                          DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    `status`          varchar(50) COLLATE utf8mb4_unicode_ci  DEFAULT 'START',
    PRIMARY KEY (`id`)
) ENGINE = InnoDB
  AUTO_INCREMENT = 1
  DEFAULT CHARSET = utf8mb4
  COLLATE = utf8mb4_unicode_ci;

CREATE TABLE `designer_logic_hyper_fusion_directory`
(
    `id`          int(11)                                 NOT NULL AUTO_INCREMENT,
    `lid`         int(11)                                 NOT NULL,
    `pid`         int(11)                                 DEFAULT NULL,
    `name`        varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
    `description` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
    PRIMARY KEY (`id`)
) ENGINE = InnoDB
  AUTO_INCREMENT = 1
  DEFAULT CHARSET = utf8mb4
  COLLATE = utf8mb4_unicode_ci;

CREATE TABLE `designer_logic_hyper_fusion_data`
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

/*执行器部分, 执行器与流程交轨*/
create table executor_data
(
    id              int auto_increment comment '自增主键'
        primary key,
    business_id     int                                 not null comment '业务id',
    business_name   varchar(255)                        not null comment '业务名称',
    data_id         int                                 not null comment '数据id',
    data_data_id    int                                 not null comment '数据id',
    data_data_data  mediumtext                          not null comment '启动数据',
    create_by       varchar(100)                        not null comment '创建人',
    create_datetime timestamp default CURRENT_TIMESTAMP not null comment '创建时间'
)
    comment '执行器数据';