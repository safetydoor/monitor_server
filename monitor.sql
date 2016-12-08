/*
 Navicat Premium Data Transfer

 Source Server         : laps
 Source Server Type    : MySQL
 Source Server Version : 50713
 Source Host           : localhost
 Source Database       : monitor

 Target Server Type    : MySQL
 Target Server Version : 50713
 File Encoding         : utf-8

 Date: 08/12/2016 10:34:37 AM
*/

SET NAMES utf8;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
--  Table structure for `monitor_ad`
-- ----------------------------
DROP TABLE IF EXISTS `monitor_ad`;
CREATE TABLE `monitor_ad` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `desc` varchar(300) DEFAULT NULL,
  `imageUrl` varchar(300) DEFAULT NULL,
  `adUrl` varchar(300) DEFAULT NULL,
  `createTime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `state` int(11) DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Records of `monitor_ad`
-- ----------------------------
BEGIN;
INSERT INTO `monitor_ad` VALUES ('1', '洗护击穿', '天猫广告', '/static/images/146997053440.png', 'https://pages.tmall.com/wow/chaoshi/act/gehujichuan-hn?spm=875.7931836/A.2016007.1.1Yvzg9&t=gehujichuan&acm=2016030118.1003.2.1000158&aldid=UQew0yqF&scm=1003.2.2016030118.OTHER_1471204357592_1000158&pos=1', '2016-07-31 21:08:56', '0');
COMMIT;

-- ----------------------------
--  Table structure for `monitor_admin`
-- ----------------------------
DROP TABLE IF EXISTS `monitor_admin`;
CREATE TABLE `monitor_admin` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `userName` varchar(50) DEFAULT NULL,
  `passWord` varchar(50) DEFAULT NULL,
  `group` varchar(50) DEFAULT 'root',
  `createTime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `state` int(11) DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=106 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Records of `monitor_admin`
-- ----------------------------
BEGIN;
INSERT INTO `monitor_admin` VALUES ('46', 'admin', 'e10adc3949ba59abbe56e057f20f883e', 'root', '2016-07-30 15:18:04', '0');
COMMIT;

-- ----------------------------
--  Table structure for `monitor_live`
-- ----------------------------
DROP TABLE IF EXISTS `monitor_live`;
CREATE TABLE `monitor_live` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `desc` varchar(300) DEFAULT NULL,
  `iconUrl` varchar(300) DEFAULT NULL,
  `address` varchar(300) DEFAULT NULL,
  `sort` int(11) DEFAULT NULL,
  `createTime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `state` int(11) DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Records of `monitor_live`
-- ----------------------------
BEGIN;
INSERT INTO `monitor_live` VALUES ('1', '黑龙江卫视', '', '', 'http://106.120.175.80:55336/tslive/c23_ct_hljtv1_hljws_smooth_t10/c23_ct_hljtv1_hljws_smooth_t10.m3u8', '0', '2016-07-31 22:04:59', '0'), ('2', '广东卫视', '', '', 'http://106.120.175.80:55336/tslive/c27_ct_gdtv1_gdws_smooth_t10/c27_ct_gdtv1_gdws_smooth_t10.m3u8', '0', '2016-07-31 22:04:59', '0'), ('3', '河南卫视', '', '', 'http://106.120.175.80:55336/tslive/c12_ct_hntv1_henws_smooth_t10/c12_ct_hntv1_henws_smooth_t10.m3u8', '0', '2016-07-31 22:04:59', '0'), ('4', '辽宁卫视', '', '', 'http://106.120.175.80:55336/tslive/c29_ct_lntv1_lnws_smooth_t10/c29_ct_lntv1_lnws_smooth_t10.m3u8', '0', '2016-07-31 22:04:59', '0'), ('5', '安徽卫视', '', '', 'http://106.120.175.80:55336/tslive/c12_ct_ahtv1_ahws_smooth_t10/c12_ct_ahtv1_ahws_smooth_t10.m3u8', '0', '2016-07-31 22:04:59', '0'), ('6', '山东卫视', '', '', 'http://106.120.175.80:55336/tslive/c17_ct_sdtv1_sdws_smooth_t10/c17_ct_sdtv1_sdws_smooth_t10.m3u8', '0', '2016-07-31 22:04:59', '0'), ('7', '深圳卫视', '', '', 'http://106.120.175.80:55336/tslive/c8_ct_sztv1_szws_smooth_t10/c8_ct_sztv1_szws_smooth_t10.m3u8', '0', '2016-07-31 22:04:59', '0'), ('8', '吉林卫视', '', '', 'http://106.120.175.80:55336/tslive/c15_ct_jilin1_jlws_smooth_t10/c15_ct_jilin1_jlws_smooth_t10.m3u8', '0', '2016-07-31 22:04:59', '0'), ('9', '陕西卫视', '', '', 'http://106.120.175.80:55336/tslive/c25_ct_shxitv1_sxws_smooth_t10/c25_ct_shxitv1_sxws_smooth_t10.m3u8', '0', '2016-07-31 22:04:59', '0'), ('10', '广西卫视', '', '', 'http://106.120.175.80:55336/tslive/c12_ct_guanxi1_gxws_smooth_t10/c12_ct_guanxi1_gxws_smooth_t10.m3u8', '0', '2016-07-31 22:04:59', '0'), ('11', '厦门卫视', '', '', 'http://106.120.175.80:55336/tslive/c26_ct_xmtv5_xmws_smooth_t10/c26_ct_xmtv5_xmws_smooth_t10.m3u8', '0', '2016-07-31 22:04:59', '0'), ('12', '江西卫视', '', '', 'http://106.120.175.80:55336/tslive/c26_ct_jxtv1_jxws_smooth_t10/c26_ct_jxtv1_jxws_smooth_t10.m3u8', '0', '2016-07-31 22:04:59', '0'), ('13', '中国教育-1', '', '', 'http://106.120.175.80:55336/tslive/c2_ct_cetv1_zgjy1_smooth_t10/c2_ct_cetv1_zgjy1_smooth_t10.m3u8', '0', '2016-07-31 22:04:59', '0'), ('14', '法律服务', '', '', 'http://106.120.175.80:55336/tslive/c19_ct_cctvpayfee17_falfw_smooth_t10/c19_ct_cctvpayfee17_falfw_smooth_t10.m3u8', '0', '2016-07-31 22:04:59', '0'), ('15', '山西卫视', '', '', 'http://106.120.175.80:55336/tslive/c24_ct_sxtv1_shxws_smooth_t10/c24_ct_sxtv1_shxws_smooth_t10.m3u8', '0', '2016-07-31 22:04:59', '0'), ('16', '北京卫视', '', '', 'http://106.120.175.80:55336/tslive/c15_ct_btv1_bjws_smooth_t10/c15_ct_btv1_bjws_smooth_t10.m3u8', '0', '2016-07-31 22:04:59', '0'), ('17', '天津卫视', '', '', 'http://106.120.175.80:55336/tslive/c23_ct_tjtv1_tjws_smooth_t10/c23_ct_tjtv1_tjws_smooth_t10.m3u8', '0', '2016-07-31 22:04:59', '0'), ('18', '河北卫视', '', '', 'http://106.120.175.80:55336/tslive/c8_ct_hebei1_hebws_smooth_t10/c8_ct_hebei1_hebws_smooth_t10.m3u8', '0', '2016-07-31 22:04:59', '0'), ('19', '甘肃卫视', '', '', 'http://106.120.175.80:55336/tslive/c28_ct_gstv1_gsws_smooth_t10/c28_ct_gstv1_gsws_smooth_t10.m3u8', '0', '2016-07-31 22:04:59', '0'), ('20', '宁夏卫视', '', '', 'http://106.120.175.80:55336/tslive/c4_ct_nxtv2_nxws_smooth_t10/c4_ct_nxtv2_nxws_smooth_t10.m3u8', '0', '2016-07-31 22:04:59', '0'), ('21', '贵州卫视', '', '', 'http://106.120.175.80:55336/tslive/c15_ct_guizoutv1_gzws_smooth_t10/c15_ct_guizoutv1_gzws_smooth_t10.m3u8', '0', '2016-07-31 22:04:59', '0'), ('22', '青海卫视', '', '', 'http://106.120.175.80:55336/tslive/c25_ct_qhtv1_qhws_smooth_t10/c25_ct_qhtv1_qhws_smooth_t10.m3u8', '0', '2016-07-31 22:04:59', '0'), ('23', '云南卫视', '', '', 'http://106.120.175.80:55336/tslive/c23_ct_yntv1_ynws_smooth_t10/c23_ct_yntv1_ynws_smooth_t10.m3u8', '0', '2016-07-31 22:04:59', '0'), ('24', '广东南方卫视1', '', '', 'http://106.120.175.80:55336/tslive/c13_ct_nanfang2_nfws_smooth_t10/c13_ct_nanfang2_nfws_smooth_t10.m3u8', '0', '2016-07-31 22:04:59', '0'), ('25', '内蒙古卫视', '', '', 'http://106.120.175.80:55336/tslive/c29_ct_nmgtv1_nmws_smooth_t10/c29_ct_nmgtv1_nmws_smooth_t10.m3u8', '0', '2016-07-31 22:04:59', '0'), ('26', '新疆卫视', '', '', 'http://106.120.175.80:55336/tslive/c13_ct_xjtv1_xjws_smooth_t10/c13_ct_xjtv1_xjws_smooth_t10.m3u8', '0', '2016-07-31 22:04:59', '0'), ('27', '西藏卫视', '', '', 'http://106.120.175.80:55336/tslive/c19_ct_xizangtv2_xzws_smooth_t10/c19_ct_xizangtv2_xzws_smooth_t10.m3u8', '0', '2016-07-31 22:04:59', '0'), ('28', '健康卫视', '', '', 'http://106.120.175.80:55336/tslive/c27_ct_jkwshk_jkws_smooth_t10/c27_ct_jkwshk_jkws_smooth_t10.m3u8', '0', '2016-07-31 22:04:59', '0'), ('29', '卡酷少儿', '', '', 'http://106.120.175.80:55336/tslive/c18_ct_btv10_kkdh_smooth_t10/c18_ct_btv10_kkdh_smooth_t10.m3u8', '0', '2016-07-31 22:04:59', '0'), ('30', '优漫卡通', '', '', 'http://106.120.175.80:55336/tslive/c24_ct_jstv7_ymkt_smooth_t10/c24_ct_jstv7_ymkt_smooth_t10.m3u8', '0', '2016-07-31 22:04:59', '0'), ('31', '北京新闻', '', '', 'http://106.120.175.80:55336/tslive/c22_ct_btv9_bjxw_smooth_t10/c22_ct_btv9_bjxw_smooth_t10.m3u8', '0', '2016-07-31 22:04:59', '0');
COMMIT;

-- ----------------------------
--  Table structure for `monitor_lump`
-- ----------------------------
DROP TABLE IF EXISTS `monitor_lump`;
CREATE TABLE `monitor_lump` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `desc` varchar(300) DEFAULT NULL,
  `iconUrl` varchar(300) DEFAULT NULL,
  `url` varchar(300) DEFAULT NULL,
  `categoryId` int(11) DEFAULT '0',
  `sort` int(11) DEFAULT NULL,
  `createTime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `state` int(11) DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Records of `monitor_lump`
-- ----------------------------
BEGIN;
INSERT INTO `monitor_lump` VALUES ('1', '社区动态', '了解社区最新动态', '/static/images/146997109241.png', 'http://www.baidu.com', '2', '0', '2016-07-31 21:18:20', '0'), ('2', '政务指南', '社区政务办理指南', '/static/images/146997109241.png', 'http://www.baidu.com', '2', '0', '2016-07-31 21:18:57', '0'), ('3', '问卷调查', '说说您对社区的满意度', '/static/images/146997109241.png', 'http://www.baidu.com', '2', '0', '2016-07-31 21:20:53', '0'), ('4', '居民反馈', '您有什么建议呢', '/static/images/146997109241.png', 'http://www.baidu.com', '2', '0', '2016-07-31 21:21:17', '0'), ('5', '缤纷活动', '各式各样的活动送给您', '/static/images/146997109241.png', 'http://www.baidu.com', '3', '0', '2016-07-31 21:21:41', '0'), ('6', '天天健康', '各种健康宝典', '/static/images/146997109241.png', 'http://www.baidu.com', '3', '0', '2016-07-31 21:22:10', '0'), ('7', '文创网展示', '正在建设中，敬请期待', '/static/images/146997109241.png', 'http://www.baidu.com', '3', '0', '2016-07-31 21:22:21', '0'), ('8', '智慧建党', '正在建设中，敬请期待', '/static/images/146997109241.png', 'http://www.baidu.com', '3', '0', '2016-07-31 21:22:35', '0'), ('9', '生活缴费', '帮您缴纳水电煤等各种费用', '/static/images/146997109241.png', 'http://www.baidu.com', '1', '0', '2016-07-31 21:23:51', '0'), ('10', '社区地图', '当前社区的地图', '/static/images/146997109241.png', 'http://www.baidu.com', '1', '0', '2016-07-31 21:24:14', '0'), ('11', '路况查看', '查看实时交通路况 ', '/static/images/146997109241.png', 'http://www.baidu.com', '1', '0', '2016-07-31 21:24:22', '0'), ('12', '家政服务', '帮您清洁打扫一步到位', '/static/images/146997109241.png', 'http://www.baidu.com', '1', '0', '2016-07-31 21:24:29', '0'), ('13', '生活用餐', '您饿了吗，快来点餐吧 ', '/static/images/146997109241.png', 'http://www.baidu.com', '1', '0', '2016-07-31 21:24:38', '0'), ('14', '便民号码', '快速查找便民号码', '/static/images/146997109241.png', 'http://www.baidu.com', '1', '0', '2016-07-31 21:24:48', '0'), ('15', '家居报修', '您的水管漏水吗', '/static/images/146997109241.png', 'http://www.baidu.com', '1', '0', '2016-07-31 21:25:00', '0'), ('16', '城市服务', '正在建设中，敬请期待 ', '/static/images/146997109241.png', 'http://www.baidu.com', '1', '0', '2016-07-31 21:25:09', '0'), ('17', '快递查询', '看看你的快递到哪里了 ', '/static/images/146997109241.png', 'http://www.baidu.com', '1', '0', '2016-07-31 21:25:18', '0');
COMMIT;

-- ----------------------------
--  Table structure for `monitor_lumpCategory`
-- ----------------------------
DROP TABLE IF EXISTS `monitor_lumpCategory`;
CREATE TABLE `monitor_lumpCategory` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `desc` varchar(300) DEFAULT NULL,
  `sort` int(11) DEFAULT NULL,
  `createTime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `state` int(11) DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Records of `monitor_lumpCategory`
-- ----------------------------
BEGIN;
INSERT INTO `monitor_lumpCategory` VALUES ('1', '便民服务', '便民服务', '0', '2016-07-31 21:10:53', '0'), ('2', '社区政务', '社区政务', '0', '2016-07-31 21:11:05', '0'), ('3', '风尚文化', '风尚文化', '0', '2016-07-31 21:11:30', '0');
COMMIT;

-- ----------------------------
--  Table structure for `monitor_user`
-- ----------------------------
DROP TABLE IF EXISTS `monitor_user`;
CREATE TABLE `monitor_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `imei` varchar(50) DEFAULT NULL,
  `userName` varchar(50) DEFAULT NULL,
  `passWord` varchar(50) DEFAULT NULL,
  `phoneNumber` varchar(50) DEFAULT NULL,
  `group` varchar(50) DEFAULT 'root',
  `createTime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `state` int(11) DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=52 DEFAULT CHARSET=utf8;

SET FOREIGN_KEY_CHECKS = 1;
