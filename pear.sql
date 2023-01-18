-- --------------------------------------------------------
-- 主机:                           127.0.0.1
-- 服务器版本:                        5.7.26 - MySQL Community Server (GPL)
-- 服务器操作系统:                      Win64
-- HeidiSQL 版本:                  11.0.0.5919
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- 导出 pearadmin 的数据库结构
CREATE DATABASE IF NOT EXISTS `pearadmin` /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci */;
USE `pearadmin`;

-- 导出  表 pearadmin.admin_admin_log 结构
CREATE TABLE IF NOT EXISTS `admin_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `method` varchar(10) COLLATE utf8_unicode_ci DEFAULT NULL,
  `uid` int(11) DEFAULT NULL,
  `url` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `desc` text COLLATE utf8_unicode_ci,
  `ip` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `user_agent` text COLLATE utf8_unicode_ci,
  `create_time` datetime DEFAULT NULL,
  `success` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=2644 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci ROW_FORMAT=DYNAMIC;

-- 正在导出表  pearadmin.admin_admin_log 的数据：~1,021 rows (大约)
/*!40000 ALTER TABLE `admin_admin_log` DISABLE KEYS */;
REPLACE INTO `admin_admin_log` (`id`, `method`, `uid`, `url`, `desc`, `ip`, `user_agent`, `create_time`, `success`) VALUES
	(2485, 'GET', 1, '/plugin/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-25 14:36:01', 1),
	(2486, 'GET', 1, '/plugin/data', '{&#39;page&#39;: &#39;1&#39;, &#39;limit&#39;: &#39;10&#39;}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-25 14:36:04', 1),
	(2487, 'GET', 1, '/plugin/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-25 14:37:25', 1),
	(2488, 'GET', 1, '/plugin/data', '{&#39;page&#39;: &#39;1&#39;, &#39;limit&#39;: &#39;10&#39;}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-25 14:37:28', 1),
	(2489, 'PUT', 1, '/plugin/enable', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-25 14:37:34', 1),
	(2490, 'GET', 1, '/plugin/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-25 14:38:42', 1),
	(2491, 'GET', 1, '/plugin/data', '{&#39;page&#39;: &#39;1&#39;, &#39;limit&#39;: &#39;10&#39;}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-25 14:38:45', 1),
	(2492, 'PUT', 1, '/plugin/enable', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-25 14:38:48', 1),
	(2493, 'GET', 1, '/plugin/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-25 14:45:24', 1),
	(2494, 'GET', 1, '/plugin/data', '{&#39;limit&#39;: &#39;10&#39;, &#39;page&#39;: &#39;1&#39;}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-25 14:45:27', 1),
	(2495, 'PUT', 1, '/plugin/enable', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-25 14:45:28', 1),
	(2496, 'GET', 1, '/plugin/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-25 14:47:02', 1),
	(2497, 'GET', 1, '/plugin/data', '{&#39;limit&#39;: &#39;10&#39;, &#39;page&#39;: &#39;1&#39;}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-25 14:47:06', 1),
	(2498, 'PUT', 1, '/plugin/enable', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-25 14:47:08', 1),
	(2499, 'GET', 1, '/plugin/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-25 14:49:32', 1),
	(2500, 'GET', 1, '/plugin/data', '{&#39;limit&#39;: &#39;10&#39;, &#39;page&#39;: &#39;1&#39;}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-25 14:49:36', 1),
	(2501, 'PUT', 1, '/plugin/enable', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-25 14:49:37', 1),
	(2502, 'GET', 1, '/plugin/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-25 14:51:40', 1),
	(2503, 'GET', 1, '/plugin/data', '{&#39;limit&#39;: &#39;10&#39;, &#39;page&#39;: &#39;1&#39;}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-25 14:51:43', 1),
	(2504, 'PUT', 1, '/plugin/enable', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-25 14:51:49', 1),
	(2505, 'GET', 1, '/plugin/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-25 14:52:52', 1),
	(2506, 'GET', 1, '/plugin/data', '{&#39;page&#39;: &#39;1&#39;, &#39;limit&#39;: &#39;10&#39;}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-25 14:52:56', 1),
	(2507, 'PUT', 1, '/plugin/enable', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-25 14:52:59', 1),
	(2508, 'GET', 1, '/plugin/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-25 14:54:51', 1),
	(2509, 'GET', 1, '/plugin/data', '{&#39;page&#39;: &#39;1&#39;, &#39;limit&#39;: &#39;10&#39;}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-25 14:54:55', 1),
	(2510, 'PUT', 1, '/plugin/enable', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-25 14:54:56', 1),
	(2511, 'GET', 1, '/plugin/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-25 14:56:16', 1),
	(2512, 'GET', 1, '/plugin/data', '{&#39;limit&#39;: &#39;10&#39;, &#39;page&#39;: &#39;1&#39;}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-25 14:56:19', 1),
	(2513, 'PUT', 1, '/plugin/enable', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-25 14:56:23', 1),
	(2514, 'GET', 1, '/plugin/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-25 14:57:41', 1),
	(2515, 'GET', 1, '/plugin/data', '{&#39;page&#39;: &#39;1&#39;, &#39;limit&#39;: &#39;10&#39;}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-25 14:57:44', 1),
	(2516, 'PUT', 1, '/plugin/disable', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-25 14:57:46', 1),
	(2517, 'PUT', 1, '/plugin/enable', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-25 14:57:51', 1),
	(2518, 'PUT', 1, '/plugin/disable', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-25 14:57:55', 1),
	(2519, 'GET', 1, '/plugin/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-25 15:04:55', 1),
	(2520, 'GET', 1, '/plugin/data', '{&#39;page&#39;: &#39;1&#39;, &#39;limit&#39;: &#39;10&#39;}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-25 15:04:58', 1),
	(2521, 'DELETE', 1, '/plugin/remove/helloworld1', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-25 15:05:05', 1),
	(2522, 'POST', 1, '/passport/login', 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-25 18:23:00', 1),
	(2523, 'GET', 1, '/plugin/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-25 18:26:32', 1),
	(2524, 'GET', 1, '/plugin/data', '{&#39;limit&#39;: &#39;10&#39;, &#39;page&#39;: &#39;1&#39;}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-25 18:26:34', 1),
	(2525, 'PUT', 1, '/plugin/enable', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-25 18:26:37', 1),
	(2526, 'PUT', 1, '/plugin/disable', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-25 18:26:40', 1),
	(2527, 'PUT', 1, '/plugin/enable', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-25 18:32:45', 1),
	(2528, 'PUT', 1, '/plugin/disable', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-25 18:32:59', 1),
	(2529, 'PUT', 1, '/plugin/enable', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-25 18:33:13', 1),
	(2530, 'PUT', 1, '/plugin/disable', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-25 18:33:14', 1),
	(2531, 'PUT', 1, '/plugin/enable', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-25 18:39:10', 1),
	(2532, 'PUT', 1, '/plugin/disable', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-25 18:39:14', 1),
	(2533, 'PUT', 1, '/plugin/enable', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-25 18:39:22', 1),
	(2534, 'PUT', 1, '/plugin/disable', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-25 18:39:23', 1),
	(2535, 'PUT', 1, '/plugin/enable', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-25 18:43:12', 1),
	(2536, 'PUT', 1, '/plugin/disable', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-25 18:43:13', 1),
	(2537, 'PUT', 1, '/plugin/enable', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-25 18:43:16', 1),
	(2538, 'PUT', 1, '/plugin/disable', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-25 18:43:17', 1),
	(2539, 'PUT', 1, '/plugin/enable', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-25 18:50:18', 1),
	(2540, 'PUT', 1, '/plugin/disable', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-25 19:08:45', 1),
	(2541, 'PUT', 1, '/plugin/enable', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-25 19:08:47', 1),
	(2542, 'PUT', 1, '/plugin/disable', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-25 19:24:13', 1),
	(2543, 'PUT', 1, '/plugin/enable', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-25 19:24:16', 1),
	(2544, 'PUT', 1, '/plugin/disable', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-25 19:30:51', 1),
	(2545, 'PUT', 1, '/plugin/enable', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-25 19:30:54', 1),
	(2546, 'POST', 1, '/admin/file/upload', '{&#39;fileName&#39;: &#39;1671970133000.jpg&#39;, &#39;fileToken&#39;: &#39;1671970133000&#39;}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-25 20:08:54', 1),
	(2547, 'GET', 1, '/admin/file/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-25 20:09:18', 1),
	(2548, 'GET', 1, '/admin/file/table', '{&#39;page&#39;: &#39;1&#39;, &#39;limit&#39;: &#39;10&#39;}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-25 20:09:19', 1),
	(2549, 'PUT', 1, '/plugin/disable', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-25 20:09:25', 1),
	(2550, 'PUT', 1, '/plugin/enable', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-25 20:09:27', 1),
	(2551, 'PUT', 1, '/plugin/disable', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-25 20:09:40', 1),
	(2552, 'PUT', 1, '/plugin/enable', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-25 20:09:41', 1),
	(2553, 'GET', 1, '/admin/monitor/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-25 20:09:57', 1),
	(2554, 'POST', 1, '/passport/login', 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-26 16:43:04', 1),
	(2555, 'GET', 1, '/admin/monitor/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-26 16:43:12', 1),
	(2556, 'GET', 1, '/admin/monitor/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-26 18:23:14', 1),
	(2557, 'GET', 1, '/admin/monitor/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-26 18:23:39', 1),
	(2558, 'GET', 1, '/admin/monitor/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-26 18:42:46', 1),
	(2559, 'GET', 1, '/admin/mail/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-26 19:02:19', 1),
	(2560, 'GET', 1, '/admin/mail/data', '{&#39;page&#39;: &#39;1&#39;, &#39;limit&#39;: &#39;10&#39;}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-26 19:02:21', 1),
	(2561, 'GET', 1, '/admin/mail/add', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-26 19:02:22', 1),
	(2562, 'POST', 1, '/admin/mail/save', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-26 19:02:34', 1),
	(2563, 'GET', 1, '/admin/mail/data', '{&#39;page&#39;: &#39;1&#39;, &#39;limit&#39;: &#39;10&#39;}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-26 19:02:38', 1),
	(2564, 'GET', 1, '/admin/monitor/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-26 19:27:14', 1),
	(2565, 'GET', 1, '/admin/monitor/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-26 19:32:06', 1),
	(2566, 'GET', 1, '/admin/monitor/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-26 19:33:24', 1),
	(2567, 'GET', 1, '/admin/monitor/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-26 19:35:01', 1),
	(2568, 'GET', 1, '/admin/monitor/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-26 19:35:17', 1),
	(2569, 'GET', 1, '/admin/monitor/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-26 19:35:17', 1),
	(2570, 'GET', 1, '/admin/monitor/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-26 19:35:18', 1),
	(2571, 'GET', 1, '/admin/monitor/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-26 19:35:19', 1),
	(2572, 'GET', 1, '/admin/monitor/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-26 19:35:23', 1),
	(2573, 'GET', 1, '/admin/monitor/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-26 19:35:23', 1),
	(2574, 'GET', 1, '/admin/monitor/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-26 19:35:25', 1),
	(2575, 'GET', 1, '/admin/monitor/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-26 19:35:26', 1),
	(2576, 'GET', 1, '/admin/monitor/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-26 19:35:27', 1),
	(2577, 'GET', 1, '/admin/monitor/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-26 19:35:29', 1),
	(2578, 'GET', 1, '/admin/monitor/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-26 19:35:29', 1),
	(2579, 'GET', 1, '/admin/monitor/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-26 19:35:32', 1),
	(2580, 'GET', 1, '/admin/monitor/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-26 19:35:32', 1),
	(2581, 'GET', 1, '/admin/monitor/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-26 19:35:34', 1),
	(2582, 'GET', 1, '/admin/monitor/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-26 19:35:35', 1),
	(2583, 'GET', 1, '/admin/monitor/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-26 19:35:36', 1),
	(2584, 'GET', 1, '/admin/monitor/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-26 19:35:38', 1),
	(2585, 'GET', 1, '/admin/monitor/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-26 19:35:39', 1),
	(2586, 'GET', 1, '/admin/monitor/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-26 19:35:40', 1),
	(2587, 'GET', 1, '/admin/monitor/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-26 19:35:42', 1),
	(2588, 'GET', 1, '/admin/monitor/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-26 19:35:42', 1),
	(2589, 'GET', 1, '/admin/monitor/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-26 19:35:44', 1),
	(2590, 'GET', 1, '/admin/monitor/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-26 19:35:46', 1),
	(2591, 'GET', 1, '/admin/monitor/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-26 19:35:48', 1),
	(2592, 'GET', 1, '/admin/monitor/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-26 19:35:49', 1),
	(2593, 'GET', 1, '/admin/monitor/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-26 19:35:50', 1),
	(2594, 'GET', 1, '/admin/monitor/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-26 19:35:52', 1),
	(2595, 'GET', 1, '/admin/monitor/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-26 19:35:52', 1),
	(2596, 'GET', 1, '/admin/monitor/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-26 19:35:55', 1),
	(2597, 'GET', 1, '/admin/monitor/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-26 19:35:56', 1),
	(2598, 'GET', 1, '/admin/monitor/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-26 19:36:37', 1),
	(2599, 'GET', 1, '/admin/monitor/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-26 19:38:33', 1),
	(2600, 'GET', 1, '/admin/monitor/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-26 19:38:35', 1),
	(2601, 'GET', 1, '/admin/monitor/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-26 19:38:36', 1),
	(2602, 'GET', 1, '/admin/monitor/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-26 19:38:36', 1),
	(2603, 'GET', 1, '/admin/monitor/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-26 19:38:36', 1),
	(2604, 'GET', 1, '/admin/monitor/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-26 19:38:37', 1),
	(2605, 'GET', 1, '/admin/monitor/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-26 19:41:45', 1),
	(2606, 'GET', 1, '/admin/monitor/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-26 19:43:40', 1),
	(2607, 'GET', 1, '/admin/monitor/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-26 19:44:52', 1),
	(2608, 'GET', 1, '/admin/monitor/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-26 19:46:06', 1),
	(2609, 'GET', 1, '/admin/monitor/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-26 19:46:35', 1),
	(2610, 'GET', 1, '/admin/mail/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-26 19:54:01', 1),
	(2611, 'GET', 1, '/admin/mail/data', '{&#39;page&#39;: &#39;1&#39;, &#39;limit&#39;: &#39;10&#39;}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-26 19:54:03', 1),
	(2612, 'GET', 1, '/plugin/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-26 19:54:06', 1),
	(2613, 'GET', 1, '/plugin/data', '{&#39;page&#39;: &#39;1&#39;, &#39;limit&#39;: &#39;10&#39;}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-26 19:54:07', 1),
	(2614, 'PUT', 1, '/plugin/disable', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-26 19:54:09', 1),
	(2615, 'GET', 1, '/admin/monitor/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-26 19:54:22', 1),
	(2616, 'GET', 1, '/admin/monitor/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-26 19:54:22', 1),
	(2617, 'GET', 1, '/admin/monitor/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-26 19:54:22', 1),
	(2618, 'GET', 1, '/admin/monitor/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-26 19:54:22', 1),
	(2619, 'GET', 1, '/plugin/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-26 19:54:23', 1),
	(2620, 'GET', 1, '/plugin/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-26 19:54:23', 1),
	(2621, 'GET', 1, '/plugin/data', '{&#39;limit&#39;: &#39;10&#39;, &#39;page&#39;: &#39;1&#39;}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-26 19:54:23', 1),
	(2622, 'GET', 1, '/plugin/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-26 20:03:36', 1),
	(2623, 'GET', 1, '/plugin/data', '{&#39;limit&#39;: &#39;10&#39;, &#39;page&#39;: &#39;1&#39;}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-26 20:03:38', 1),
	(2624, 'PUT', 1, '/plugin/enable', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-26 20:03:40', 1),
	(2625, 'GET', 1, '/admin/monitor/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-26 20:03:52', 1),
	(2626, 'GET', 1, '/admin/monitor/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-26 20:03:52', 1),
	(2627, 'GET', 1, '/admin/monitor/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-26 20:03:52', 1),
	(2628, 'GET', 1, '/plugin/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-26 20:03:53', 1),
	(2629, 'GET', 1, '/admin/monitor/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-26 20:03:53', 1),
	(2630, 'GET', 1, '/plugin/data', '{&#39;page&#39;: &#39;1&#39;, &#39;limit&#39;: &#39;10&#39;}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-26 20:03:54', 1),
	(2631, 'PUT', 1, '/plugin/disable', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-26 20:04:03', 1),
	(2632, 'GET', 1, '/admin/monitor/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-26 20:04:14', 1),
	(2633, 'GET', 1, '/admin/monitor/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-26 20:04:14', 1),
	(2634, 'GET', 1, '/admin/monitor/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-26 20:04:15', 1),
	(2635, 'GET', 1, '/plugin/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-26 20:04:15', 1),
	(2636, 'GET', 1, '/admin/monitor/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-26 20:04:15', 1),
	(2637, 'GET', 1, '/plugin/data', '{&#39;limit&#39;: &#39;10&#39;, &#39;page&#39;: &#39;1&#39;}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-26 20:04:16', 1),
	(2638, 'POST', 1, '/passport/login', 'admin', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-27 07:35:02', 1),
	(2639, 'GET', 1, '/admin/user/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-27 07:35:09', 1),
	(2640, 'GET', 1, '/admin/user/data', '{&#39;page&#39;: &#39;1&#39;, &#39;limit&#39;: &#39;10&#39;}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-27 07:35:11', 1),
	(2641, 'GET', 1, '/dept/tree', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-27 07:35:11', 1),
	(2642, 'GET', 1, '/plugin/', '{}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-27 07:35:14', 1),
	(2643, 'GET', 1, '/plugin/data', '{&#39;page&#39;: &#39;1&#39;, &#39;limit&#39;: &#39;10&#39;}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2022-12-27 07:35:15', 1);
/*!40000 ALTER TABLE `admin_admin_log` ENABLE KEYS */;

-- 导出  表 pearadmin.admin_dept 结构
CREATE TABLE IF NOT EXISTS `admin_dept` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '部门ID',
  `parent_id` int(11) DEFAULT NULL COMMENT '父级编号',
  `dept_name` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '部门名称',
  `sort` int(11) DEFAULT NULL COMMENT '排序',
  `leader` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '负责人',
  `phone` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '联系方式',
  `email` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '邮箱',
  `status` int(11) DEFAULT NULL COMMENT '状态(1开启,0关闭)',
  `remark` text COLLATE utf8_unicode_ci COMMENT '备注',
  `address` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '详细地址',
  `create_at` datetime DEFAULT NULL COMMENT '创建时间',
  `update_at` datetime DEFAULT NULL COMMENT '创建时间',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci ROW_FORMAT=DYNAMIC;

-- 正在导出表  pearadmin.admin_dept 的数据：~5 rows (大约)
/*!40000 ALTER TABLE `admin_dept` DISABLE KEYS */;
REPLACE INTO `admin_dept` (`id`, `parent_id`, `dept_name`, `sort`, `leader`, `phone`, `email`, `status`, `remark`, `address`, `create_at`, `update_at`) VALUES
	(1, 0, '总公司', 1, '就眠仪式', '12312345679', '123qq.com', 1, NULL, '这是总公司', NULL, '2021-06-01 17:23:20'),
	(4, 1, '济南分公司', 2, '就眠仪式', '12312345678', '1234qq.com', 1, NULL, '这是济南', '2021-06-01 17:24:33', '2021-06-01 17:25:19'),
	(5, 1, '唐山分公司', 4, 'mkg', '12312345678', '123@qq.com', 1, NULL, '这是唐山', '2021-06-01 17:25:15', '2021-06-01 17:25:20'),
	(7, 4, '济南分公司开发部', 5, '就眠仪式', '12312345678', '123@qq.com', 1, NULL, '测试', '2021-06-01 17:27:39', '2021-06-01 17:27:39'),
	(8, 5, '唐山测试部', 6, 'mkg', '12312345678', '123@qq.com', 1, NULL, '测试部', '2021-06-01 17:28:27', '2021-06-01 17:28:27');
/*!40000 ALTER TABLE `admin_dept` ENABLE KEYS */;

-- 导出  表 pearadmin.admin_dict_data 结构
CREATE TABLE IF NOT EXISTS `admin_dict_data` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `data_label` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '字典类型名称',
  `data_value` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '字典类型标识',
  `type_code` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '字典类型描述',
  `is_default` int(11) DEFAULT NULL COMMENT '是否默认',
  `enable` int(11) DEFAULT NULL COMMENT '是否开启',
  `remark` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '备注',
  `create_time` datetime DEFAULT NULL COMMENT '创建时间',
  `update_time` datetime DEFAULT NULL COMMENT '更新时间',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci ROW_FORMAT=DYNAMIC;

-- 正在导出表  pearadmin.admin_dict_data 的数据：~2 rows (大约)
/*!40000 ALTER TABLE `admin_dict_data` DISABLE KEYS */;
REPLACE INTO `admin_dict_data` (`id`, `data_label`, `data_value`, `type_code`, `is_default`, `enable`, `remark`, `create_time`, `update_time`) VALUES
	(8, '男', 'boy', 'user_sex', NULL, 1, '男 : body', '2021-04-16 13:36:34', '2021-04-16 14:05:06'),
	(9, '女', 'girl', 'user_sex', NULL, 1, '女 : girl', '2021-04-16 13:36:55', '2021-04-16 13:36:55');
/*!40000 ALTER TABLE `admin_dict_data` ENABLE KEYS */;

-- 导出  表 pearadmin.admin_dict_type 结构
CREATE TABLE IF NOT EXISTS `admin_dict_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `type_name` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '字典类型名称',
  `type_code` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '字典类型标识',
  `description` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '字典类型描述',
  `enable` int(11) DEFAULT NULL COMMENT '是否开启',
  `create_time` datetime DEFAULT NULL COMMENT '创建时间',
  `update_time` datetime DEFAULT NULL COMMENT '更新时间',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci ROW_FORMAT=DYNAMIC;

-- 正在导出表  pearadmin.admin_dict_type 的数据：~0 rows (大约)
/*!40000 ALTER TABLE `admin_dict_type` DISABLE KEYS */;
REPLACE INTO `admin_dict_type` (`id`, `type_name`, `type_code`, `description`, `enable`, `create_time`, `update_time`) VALUES
	(1, '用户性别', 'user_sex', '用户性别', 1, NULL, '2022-12-03 12:58:12');
/*!40000 ALTER TABLE `admin_dict_type` ENABLE KEYS */;

-- 导出  表 pearadmin.admin_mail 结构
CREATE TABLE IF NOT EXISTS `admin_mail` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '邮件编号',
  `receiver` varchar(1024) NOT NULL COMMENT '收件人邮箱',
  `subject` varchar(128) DEFAULT NULL COMMENT '邮件主题',
  `content` text COMMENT '邮件正文',
  `user_id` int(11) DEFAULT NULL COMMENT '发送人id',
  `create_at` datetime DEFAULT NULL COMMENT '创建时间',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC;

-- 正在导出表  pearadmin.admin_mail 的数据：~2 rows (大约)
/*!40000 ALTER TABLE `admin_mail` DISABLE KEYS */;
REPLACE INTO `admin_mail` (`id`, `receiver`, `subject`, `content`, `user_id`, `create_at`) VALUES
	(17, '422880152@qq.com', '123', '123', 1, '2022-12-25 10:51:17'),
	(18, '422880152@qq.com', 'html邮件测试', '<h1>未转义字符</h1>', 1, '2022-12-25 10:58:09'),
	(19, '422880152@qq.com', '123', '	<h1>未转义字符</h1>', 1, '2022-12-25 11:09:58'),
	(20, '422880152@qq.com', '11', '1\n', 1, '2022-12-26 19:02:37');
/*!40000 ALTER TABLE `admin_mail` ENABLE KEYS */;

-- 导出  表 pearadmin.admin_photo 结构
CREATE TABLE IF NOT EXISTS `admin_photo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `href` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `mime` char(50) COLLATE utf8_unicode_ci NOT NULL,
  `size` char(30) COLLATE utf8_unicode_ci NOT NULL,
  `create_time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci ROW_FORMAT=DYNAMIC;

-- 正在导出表  pearadmin.admin_photo 的数据：~2 rows (大约)
/*!40000 ALTER TABLE `admin_photo` DISABLE KEYS */;
REPLACE INTO `admin_photo` (`id`, `name`, `href`, `mime`, `size`, `create_time`) VALUES
	(1, '1671970133000.jpg', '/_uploads/photos/1671970133000.jpg', 'image/png', '133818', '2022-12-25 20:08:54');
/*!40000 ALTER TABLE `admin_photo` ENABLE KEYS */;

-- 导出  表 pearadmin.admin_power 结构
CREATE TABLE IF NOT EXISTS `admin_power` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '权限编号',
  `name` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '权限名称',
  `type` varchar(1) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '权限类型',
  `code` varchar(30) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '权限标识',
  `url` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '权限路径',
  `open_type` varchar(10) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '打开方式',
  `parent_id` varchar(19) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '父类编号',
  `icon` varchar(128) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '图标',
  `sort` int(11) DEFAULT NULL COMMENT '排序',
  `create_time` datetime DEFAULT NULL COMMENT '创建时间',
  `update_time` datetime DEFAULT NULL COMMENT '更新时间',
  `enable` int(11) DEFAULT NULL COMMENT '是否开启',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=64 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci ROW_FORMAT=DYNAMIC;

-- 正在导出表  pearadmin.admin_power 的数据：~35 rows (大约)
/*!40000 ALTER TABLE `admin_power` DISABLE KEYS */;
REPLACE INTO `admin_power` (`id`, `name`, `type`, `code`, `url`, `open_type`, `parent_id`, `icon`, `sort`, `create_time`, `update_time`, `enable`) VALUES
	(1, '系统管理', '0', '', NULL, NULL, '0', 'layui-icon layui-icon-set-fill', 1, NULL, NULL, 1),
	(3, '用户管理', '1', 'admin:user:main', '/admin/user/', '_iframe', '1', 'layui-icon layui-icon layui-icon layui-icon layui-icon-rate', 1, NULL, NULL, 1),
	(4, '权限管理', '1', 'admin:power:main', '/admin/power/', '_iframe', '1', NULL, 2, NULL, NULL, 1),
	(9, '角色管理', '1', 'admin:role:main', '/admin/role', '_iframe', '1', 'layui-icon layui-icon-username', 2, '2021-03-16 22:24:58', '2021-03-25 19:15:24', 1),
	(12, '系统监控', '1', 'admin:monitor:main', '/admin/monitor', '_iframe', '1', 'layui-icon layui-icon-vercode', 5, '2021-03-18 22:05:19', '2021-03-25 19:15:27', 1),
	(13, '日志管理', '1', 'admin:log:main', '/admin/log', '_iframe', '1', 'layui-icon layui-icon-read', 4, '2021-03-18 22:37:10', '2021-06-03 11:06:25', 1),
	(17, '文件管理', '0', '', '', '', '0', 'layui-icon layui-icon-camera', 2, '2021-03-19 18:56:23', '2021-03-25 19:15:08', 1),
	(18, '图片上传', '1', 'admin:file:main', '/admin/file', '_iframe', '17', 'layui-icon layui-icon-camera', 5, '2021-03-19 18:57:19', '2021-03-25 19:15:13', 1),
	(21, '权限增加', '2', 'admin:power:add', '', '', '4', 'layui-icon layui-icon-add-circle', 1, '2021-03-22 19:43:52', '2021-03-25 19:15:22', 1),
	(22, '用户增加', '2', 'admin:user:add', '', '', '3', 'layui-icon layui-icon-add-circle', 1, '2021-03-22 19:45:40', '2021-03-25 19:15:17', 1),
	(23, '用户编辑', '2', 'admin:user:edit', '', '', '3', 'layui-icon layui-icon-rate', 2, '2021-03-22 19:46:15', '2021-03-25 19:15:18', 1),
	(24, '用户删除', '2', 'admin:user:remove', '', '', '3', 'layui-icon None', 3, '2021-03-22 19:46:51', '2021-03-25 19:15:18', 1),
	(25, '权限编辑', '2', 'admin:power:edit', '', '', '4', 'layui-icon layui-icon-edit', 2, '2021-03-22 19:47:36', '2021-03-25 19:15:22', 1),
	(26, '用户删除', '2', 'admin:power:remove', '', '', '4', 'layui-icon layui-icon-delete', 3, '2021-03-22 19:48:17', '2021-03-25 19:15:23', 1),
	(27, '用户增加', '2', 'admin:role:add', '', '', '9', 'layui-icon layui-icon-add-circle', 1, '2021-03-22 19:49:09', '2021-03-25 19:15:24', 1),
	(28, '角色编辑', '2', 'admin:role:edit', '', '', '9', 'layui-icon layui-icon-edit', 2, '2021-03-22 19:49:41', '2021-03-25 19:15:25', 1),
	(29, '角色删除', '2', 'admin:role:remove', '', '', '9', 'layui-icon layui-icon-delete', 3, '2021-03-22 19:50:15', '2021-03-25 19:15:26', 1),
	(30, '角色授权', '2', 'admin:role:power', '', '', '9', 'layui-icon layui-icon-component', 4, '2021-03-22 19:50:54', '2021-03-25 19:15:26', 1),
	(31, '图片增加', '2', 'admin:file:add', '', '', '18', 'layui-icon layui-icon-add-circle', 1, '2021-03-22 19:58:05', '2021-03-25 19:15:28', 1),
	(32, '图片删除', '2', 'admin:file:delete', '', '', '18', 'layui-icon layui-icon-delete', 2, '2021-03-22 19:58:45', '2021-03-25 19:15:29', 1),
	(44, '数据字典', '1', 'admin:dict:main', '/admin/dict', '_iframe', '1', 'layui-icon layui-icon-console', 6, '2021-04-16 13:59:49', '2021-04-16 13:59:49', 1),
	(45, '字典增加', '2', 'admin:dict:add', '', '', '44', 'layui-icon ', 1, '2021-04-16 14:00:59', '2021-04-16 14:00:59', 1),
	(46, '字典修改', '2', 'admin:dict:edit', '', '', '44', 'layui-icon ', 2, '2021-04-16 14:01:33', '2021-04-16 14:01:33', 1),
	(47, '字典删除', '2', 'admin:dict:remove', '', '', '44', 'layui-icon ', 3, '2021-04-16 14:02:06', '2021-04-16 14:02:06', 1),
	(48, '部门管理', '1', 'admin:dept:main', '/dept', '_iframe', '1', 'layui-icon layui-icon-group', 3, '2021-06-01 16:22:11', '2021-07-07 13:49:39', 1),
	(49, '部门增加', '2', 'admin:dept:add', '', '', '48', 'layui-icon None', 1, '2021-06-01 17:35:52', '2021-06-01 17:36:15', 1),
	(50, '部门编辑', '2', 'admin:dept:edit', '', '', '48', 'layui-icon ', 2, '2021-06-01 17:36:41', '2021-06-01 17:36:41', 1),
	(51, '部门删除', '2', 'admin:dept:remove', '', '', '48', 'layui-icon None', 3, '2021-06-01 17:37:15', '2021-06-01 17:37:26', 1),
	(52, '定时任务', '0', '', '', '', '0', 'layui-icon layui-icon-log', 3, '2021-06-22 21:09:01', '2021-06-22 21:09:01', 1),
	(53, '任务管理', '1', 'admin:task:main', '/admin/task', '_iframe', '52', 'layui-icon ', 1, '2021-06-22 21:15:00', '2021-06-22 21:15:00', 1),
	(54, '任务增加', '2', 'admin:task:add', '', '', '53', 'layui-icon ', 1, '2021-06-22 22:20:54', '2021-06-22 22:20:54', 1),
	(55, '任务修改', '2', 'admin:task:edit', '', '', '53', 'layui-icon ', 2, '2021-06-22 22:21:34', '2021-06-22 22:21:34', 1),
	(56, '任务删除', '2', 'admin:task:remove', '', '', '53', 'layui-icon ', 3, '2021-06-22 22:22:18', '2021-06-22 22:22:18', 1),
	(57, '拓展插件', '0', '', '', '', '0', 'layui-icon layui-icon layui-icon-senior', 2, '2022-12-18 12:28:19', '2022-12-18 12:30:25', 1),
	(58, '插件管理', '1', 'admin:plugin:main', '/plugin', '_iframe', '57', 'layui-icon layui-icon layui-icon layui-icon ', 1, '2022-12-18 12:30:13', '2022-12-18 13:57:20', 1),
	(59, '启禁插件', '2', 'admin:plugin:enable', '', '', '58', 'layui-icon ', 1, '2022-12-18 13:25:37', '2022-12-18 13:25:37', 1),
	(60, '删除插件', '2', 'admin:plugin:remove', '', '', '58', 'layui-icon layui-icon ', 2, '2022-12-18 13:26:30', '2022-12-18 13:27:17', 1),
	(61, '邮件管理', '1', 'admin:mail:main', '/admin/mail', '_iframe', '1', 'layui-icon layui-icon layui-icon-release', 7, '2022-10-11 11:21:05', '2022-10-11 11:21:22', 1),
	(62, '邮件发送', '2', 'admin:mail:add', '', '', '61', 'layui-icon layui-icon layui-icon-ok-circle', 1, '2022-10-11 11:22:26', '2022-12-25 10:48:11', 1),
	(63, '邮件删除', '2', 'admin:mail:remove', '', '', '61', 'layui-icon layui-icon layui-icon layui-icon-close', 2, '2022-10-11 11:23:06', '2022-12-25 10:48:22', 1);
/*!40000 ALTER TABLE `admin_power` ENABLE KEYS */;

-- 导出  表 pearadmin.admin_role 结构
CREATE TABLE IF NOT EXISTS `admin_role` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '角色ID',
  `name` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '角色名称',
  `code` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '角色标识',
  `remark` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '备注',
  `details` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '详情',
  `sort` int(11) DEFAULT NULL COMMENT '排序',
  `create_time` datetime DEFAULT NULL COMMENT '创建时间',
  `update_time` datetime DEFAULT NULL COMMENT '更新时间',
  `enable` int(11) DEFAULT NULL COMMENT '是否启用',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci ROW_FORMAT=DYNAMIC;

-- 正在导出表  pearadmin.admin_role 的数据：~2 rows (大约)
/*!40000 ALTER TABLE `admin_role` DISABLE KEYS */;
REPLACE INTO `admin_role` (`id`, `name`, `code`, `remark`, `details`, `sort`, `create_time`, `update_time`, `enable`) VALUES
	(1, '管理员', 'admin', NULL, '管理员', 1, NULL, NULL, 1);
/*!40000 ALTER TABLE `admin_role` ENABLE KEYS */;

-- 导出  表 pearadmin.admin_role_power 结构
CREATE TABLE IF NOT EXISTS `admin_role_power` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '标识',
  `power_id` int(11) DEFAULT NULL COMMENT '用户编号',
  `role_id` int(11) DEFAULT NULL COMMENT '角色编号',
  PRIMARY KEY (`id`) USING BTREE,
  KEY `power_id` (`power_id`) USING BTREE,
  KEY `role_id` (`role_id`) USING BTREE,
  CONSTRAINT `admin_role_power_ibfk_1` FOREIGN KEY (`power_id`) REFERENCES `admin_power` (`id`),
  CONSTRAINT `admin_role_power_ibfk_2` FOREIGN KEY (`role_id`) REFERENCES `admin_role` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=378 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci ROW_FORMAT=DYNAMIC;

-- 正在导出表  pearadmin.admin_role_power 的数据：~42 rows (大约)
/*!40000 ALTER TABLE `admin_role_power` DISABLE KEYS */;
REPLACE INTO `admin_role_power` (`id`, `power_id`, `role_id`) VALUES
	(334, 1, 1),
	(335, 3, 1),
	(336, 4, 1),
	(337, 9, 1),
	(338, 12, 1),
	(339, 13, 1),
	(340, 17, 1),
	(341, 18, 1),
	(342, 21, 1),
	(343, 22, 1),
	(344, 23, 1),
	(345, 24, 1),
	(346, 25, 1),
	(347, 26, 1),
	(348, 27, 1),
	(349, 28, 1),
	(350, 29, 1),
	(351, 30, 1),
	(352, 31, 1),
	(353, 32, 1),
	(354, 44, 1),
	(355, 45, 1),
	(356, 46, 1),
	(357, 47, 1),
	(358, 48, 1),
	(359, 49, 1),
	(360, 50, 1),
	(361, 51, 1),
	(362, 52, 1),
	(363, 53, 1),
	(364, 54, 1),
	(365, 55, 1),
	(366, 56, 1),
	(367, 57, 1),
	(370, 58, 1),
	(371, 61, 1),
	(372, 62, 1),
	(373, 63, 1),
	(374, 62, 1),
	(375, 63, 1),
	(376, 59, 1),
	(377, 60, 1);
/*!40000 ALTER TABLE `admin_role_power` ENABLE KEYS */;

-- 导出  表 pearadmin.admin_user 结构
CREATE TABLE IF NOT EXISTS `admin_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '用户ID',
  `username` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '用户名',
  `password_hash` varchar(128) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '哈希密码',
  `create_at` datetime DEFAULT NULL COMMENT '创建时间',
  `update_at` datetime DEFAULT NULL COMMENT '创建时间',
  `enable` int(11) DEFAULT NULL COMMENT '启用',
  `realname` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '真实名字',
  `remark` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '备注',
  `avatar` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '头像',
  `dept_id` int(11) DEFAULT NULL COMMENT '部门id',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci ROW_FORMAT=DYNAMIC;

-- 正在导出表  pearadmin.admin_user 的数据：~2 rows (大约)
/*!40000 ALTER TABLE `admin_user` DISABLE KEYS */;
REPLACE INTO `admin_user` (`id`, `username`, `password_hash`, `create_at`, `update_at`, `enable`, `realname`, `remark`, `avatar`, `dept_id`) VALUES
	(1, 'admin', 'pbkdf2:sha256:150000$raM7mDSr$58fe069c3eac01531fc8af85e6fc200655dd2588090530084d182e6ec9d52c85', NULL, '2022-12-25 20:09:08', 1, '我叫以赏', '要是不能把握时机，就要终身蹭蹬，一事无成！', '/_uploads/photos/1671970133000.jpg', 1);
/*!40000 ALTER TABLE `admin_user` ENABLE KEYS */;

-- 导出  表 pearadmin.admin_user_role 结构
CREATE TABLE IF NOT EXISTS `admin_user_role` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '标识',
  `user_id` int(11) DEFAULT NULL COMMENT '用户编号',
  `role_id` int(11) DEFAULT NULL COMMENT '角色编号',
  PRIMARY KEY (`id`) USING BTREE,
  KEY `role_id` (`role_id`) USING BTREE,
  KEY `user_id` (`user_id`) USING BTREE,
  CONSTRAINT `admin_user_role_ibfk_1` FOREIGN KEY (`role_id`) REFERENCES `admin_role` (`id`),
  CONSTRAINT `admin_user_role_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `admin_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci ROW_FORMAT=DYNAMIC;

-- 正在导出表  pearadmin.admin_user_role 的数据：~1 rows (大约)
/*!40000 ALTER TABLE `admin_user_role` DISABLE KEYS */;
REPLACE INTO `admin_user_role` (`id`, `user_id`, `role_id`) VALUES
	(21, 1, 1);
/*!40000 ALTER TABLE `admin_user_role` ENABLE KEYS */;

-- 导出  表 pearadmin.alembic_version 结构
CREATE TABLE IF NOT EXISTS `alembic_version` (
  `version_num` varchar(32) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`version_num`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci ROW_FORMAT=DYNAMIC;

-- 正在导出表  pearadmin.alembic_version 的数据：~0 rows (大约)
/*!40000 ALTER TABLE `alembic_version` DISABLE KEYS */;
REPLACE INTO `alembic_version` (`version_num`) VALUES
	('7634e028e338');
/*!40000 ALTER TABLE `alembic_version` ENABLE KEYS */;

-- 导出  表 pearadmin.apscheduler_jobs 结构
CREATE TABLE IF NOT EXISTS `apscheduler_jobs` (
  `id` varchar(191) COLLATE utf8_unicode_ci NOT NULL,
  `next_run_time` double DEFAULT NULL,
  `job_state` blob NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_apscheduler_jobs_next_run_time` (`next_run_time`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- 正在导出表  pearadmin.apscheduler_jobs 的数据：0 rows
/*!40000 ALTER TABLE `apscheduler_jobs` DISABLE KEYS */;
/*!40000 ALTER TABLE `apscheduler_jobs` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
