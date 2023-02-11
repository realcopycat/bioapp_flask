drop database if exists pear_admin_flask;
create database pear_admin_flask character set utf8mb4;
use pear_admin_flask;

CREATE TABLE `ums_department`
(
    `id`      int(11) NOT NULL AUTO_INCREMENT COMMENT '部门ID',
    `name`    varchar(50)  DEFAULT NULL COMMENT '部门名称',
    `leader`  varchar(50)  DEFAULT NULL COMMENT '负责人',
    `phone`   varchar(20)  DEFAULT NULL COMMENT '联系方式',
    `email`   varchar(50)  DEFAULT NULL COMMENT '邮箱',
    `enable`  tinyint(1)   DEFAULT NULL COMMENT '状态(1开启,0关闭)',
    `comment` text COMMENT '备注',
    `address` varchar(255) DEFAULT NULL COMMENT '详细地址',
    `sort`    int(11)      DEFAULT NULL COMMENT '排序',
    `pid`     int(11)      DEFAULT NULL,
    PRIMARY KEY (`id`),
    KEY `pid` (`pid`)
);

insert into ums_department
values (1, '集团总部', '集团负责人', '12312345679', '123qq.com', 1, null, '这是集团总部', 1, 0),
       (4, '济南分公司', '就眠仪式', '12312345678', '1234qq.com', 1, null, '这是济南', 2, 1),
       (5, '唐山分公司', 'mkg', '12312345678', '123@qq.com', 1, null, '这是唐山', 4, 1),
       (7, '济南分公司-开发部', '就眠仪式', '12312345678', '123@qq.com', 1, null, '测试', 5, 4),
       (8, '唐山分公司-测试部', 'mkg', '12312345678', '123@qq.com', 1, null, '测试部', 6, 5),
       (9, '长沙分公司', '正心全栈编程', '18675867241', 'pyxxp@qq.com', 1, null, '湖南省长沙市望城区', 6, 1),
       (10, '长沙分公司-VIP服务中心', '正心全栈编程', '18675867241', 'pyxxp@qq.com', 1, null, null, 6, 9),
       (11, '长沙分公司-招生中心', '正心全栈编程', '18675867241', 'pyxxp@qq.com', 1, null, null, 6, 9),
       (12, '长沙分公司-运营中心', '正心全栈编程', '18675867241', 'pyxxp@qq.com', 1, null, null, 6, 9)
;

CREATE TABLE `ums_permission`
(
    `id`              int(11)     NOT NULL AUTO_INCREMENT,
    `permission_id`   int(11)      DEFAULT NULL,
    `permission_name` varchar(20) NOT NULL COMMENT '权限名称',
    `permission_code` varchar(30)  DEFAULT NULL COMMENT '权限标识',
    `permission_type` varchar(30)  DEFAULT NULL COMMENT '权限类型',
    `permission_url`  varchar(30)  DEFAULT NULL COMMENT '路径地址',
    `icon`            varchar(128) DEFAULT NULL COMMENT '图标',
    `status`          tinyint(1)   DEFAULT NULL COMMENT '是否开启',
    `sort`            int(11)      DEFAULT NULL,
    `open_type`       varchar(128) DEFAULT NULL COMMENT '打开方式',
    `pid`             int(11)      DEFAULT NULL COMMENT '父类编号',
    PRIMARY KEY (`id`),
    UNIQUE KEY `permission_id` (`permission_id`),
    KEY `pid` (`pid`)
);

insert into ums_permission
values (0, 100, '系统管理', 'ums:permission', 'menu', null, 'layui-icon layui-icon-set-fill', null, 2, null, 0),
       (0, 100001, '权限管理', 'ums:permission:list', 'path', '/permission', 1, null, 0, null, 100),
       (0, 1000011, '新增权限', 'ums:permission:create', 'auth', '', 1, null, 0, null, 100001),
       (0, 1000012, '修改权限', 'ums:permission:update', 'auth', '', 1, null, 0, null, 100001),
       (0, 1000013, '获取权限', 'ums:permission:read', 'auth', '', 1, null, 0, null, 100001),
       (0, 1000014, '删除权限', 'ums:permission:delete', 'auth', '', 1, null, 0, null, 100001),
       (0, 100002, '角色管理', 'ums:role', 'path', '/role', 1, null, 0, null, 100),
       (0, 1000021, '新增角色', 'ums:role:create', 'auth', '', 1, null, 0, null, 100002),
       (0, 1000022, '修改角色', 'ums:role:update', 'auth', '', 1, null, 0, null, 100002),
       (0, 1000023, '查询角色', 'ums:role:read', 'auth', '', 1, null, 0, null, 100002),
       (0, 1000024, '删除角色', 'ums:role:delete', 'auth', '', 1, null, 0, null, 100002),
       (0, 100003, '部门管理', 'ums:department', 'path', '/department', 1, null, 0, null, 100),
       (0, 1000031, '新建部门', 'ums:department:create', 'auth', '', 1, null, 0, null, 100003),
       (0, 1000032, '修改部门', 'ums:department:update', 'auth', '', 1, null, 0, null, 100003),
       (0, 1000033, '删除部门', 'ums:department:delete', 'auth', '', 1, null, 0, null, 100003),
       (0, 1000034, '查询部门', 'ums:department:read', 'auth', '', 1, null, 0, null, 100003),
       (0, 100004, '员工管理', 'ums:user', 'path', '/user', 1, null, 0, null, 100),
       (0, 1000041, '新增员工', 'ums:user:create', 'auth', '', 1, null, 0, null, 100004),
       (0, 1000042, '修改员工', 'ums:user:update', 'auth', '', 1, null, 0, null, 100004),
       (0, 1000043, '查询员工', 'ums:user:read', 'auth', '', 1, null, 0, null, 100004),
       (0, 1000044, '查询员工', 'ums:user:read', 'auth', '', 1, null, 0, null, 100004),
       (0, 200, '数据图表', '', 'menu', null, 'layui-icon layui-icon-chart', null, 3, null, 0),
       (0, 200001, '折线图', '', 'path', '/echarts/line', 'layui-icon layui-icon-face-smile', null, 0, null, 200),
       (0, 200002, '柱状图', '', 'path', '/echarts/column', 'layui-icon layui-icon-face-smile', null, 0, null, 200),
       (0, 300, '工作空间', '', 'menu', null, 'layui-icon layui-icon-console', null, 1, null, 0),
       (0, 300001, '控制后台', '', 'path', '/person', 'layui-icon layui-icon-console', null, 0, null, 300)
;

CREATE TABLE `ums_role`
(
    `id`             int(11)     NOT NULL AUTO_INCREMENT,
    `name`           varchar(20) NOT NULL COMMENT '角色名称',
    `desc`           text,
    `permission_ids` varchar(512) DEFAULT NULL COMMENT '权限ids,1,2,5。冗余字段，用户缓存用户权限',
    PRIMARY KEY (`id`)
);

insert into ums_role
values (1, '超级管理员', '超级管理员', '1,2,3,4,5,6,7,8,9,10,11'),
       (2, '普通管理员', '普通管理员', '1,2,3,4,8,9,10,11'),
       (3, '普通用户', '普通用户', '1,2,9,10,11')
;

CREATE TABLE `ums_role_permission`
(
    `id`            int(11) NOT NULL AUTO_INCREMENT COMMENT '标识',
    `permission_id` int(11) DEFAULT NULL COMMENT '用户编号',
    `role_id`       int(11) DEFAULT NULL COMMENT '角色编号',
    PRIMARY KEY (`id`),
    KEY `permission_id` (`permission_id`),
    KEY `role_id` (`role_id`)
);

insert into ums_role_permission
values (1, 1, 1),
       (2, 2, 1),
       (3, 3, 1),
       (4, 4, 1),
       (5, 5, 1),
       (6, 6, 1),
       (7, 7, 1),
       (8, 8, 1),
       (9, 9, 1),
       (10, 10, 1),
       (11, 1, 2),
       (12, 2, 2),
       (13, 3, 2),
       (14, 4, 2),
       (15, 8, 2),
       (16, 9, 2),
       (17, 10, 2),
       (18, 1, 3),
       (19, 2, 3),
       (20, 9, 3),
       (21, 10, 3)
;

CREATE TABLE `ums_user`
(
    `id`            int(11)                 NOT NULL AUTO_INCREMENT COMMENT '自增id',
    `username`      varchar(128)            NOT NULL COMMENT '登录名',
    `nickname`      varchar(128)            NOT NULL COMMENT '昵称',
    `password_hash` varchar(102)            NOT NULL COMMENT '登录密码',
    `mobile`        varchar(32)             NOT NULL COMMENT '手机',
    `email`         varchar(64)             NOT NULL COMMENT '邮箱',
    `gender`        enum ('保密','女','男') NOT NULL COMMENT '性别',
    `state`         tinyint(1) DEFAULT NULL COMMENT '用户状态 False 停止使用，True 正常使用',
    `introduce`     text COMMENT '简介',
    `avatar`        text COMMENT '头像地址',
    `create_at`     datetime                NOT NULL COMMENT '创建时间',
    `department_id` int(11)    DEFAULT NULL COMMENT '部门id',
    PRIMARY KEY (`id`),
    KEY `department_id` (`department_id`)
);

insert into `ums_user`
values (1, 'admin', '超级管理员',
        'pbkdf2:sha256:260000$BRcXYGpTYVTbE2Fu$b05f8bb52cdb8739f1d7d41157e67c45f0bf8ed446178e6d66b7eade224cad39',
        '15543526531', '8540854@qq.com', '男', 1, null, null, '2023-02-07 16:48:50', 1),
       (2, '就眠仪式', '就眠仪式',
        'pbkdf2:sha256:260000$kDX8xiNgkFVM0GcM$dc54c8af027afa215cefe43c883aee6a59353556fbc4c4970defb84e2187aa33',
        '155324324234', '8540854@qq.com', '男', 1, null, null, '2023-02-07 16:48:50', 1),
       (3, 'zhengxinonly', '正心全栈编程',
        'pbkdf2:sha256:260000$YYQ0IYwRgiHz23bv$4543b6e3887b7452cb1995cdb8fb67c53b7ee0429142f93fd980c1b89335ed56',
        '18675867241', 'pyxxponly@gmail.com', '男', 1, null, null, '2023-02-07 16:48:50', 1)
;

CREATE TABLE `ums_user_role`
(
    `id`      int(11) NOT NULL AUTO_INCREMENT COMMENT '标识',
    `user_id` int(11) DEFAULT NULL COMMENT '用户编号',
    `role_id` int(11) DEFAULT NULL COMMENT '角色编号',
    PRIMARY KEY (`id`),
    KEY `role_id` (`role_id`),
    KEY `user_id` (`user_id`)
);

insert into `ums_user_role`
values (1, 1, 1),
       (2, 2, 2),
       (3, 3, 3)
;
