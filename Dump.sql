CREATE DATABASE  IF NOT EXISTS `math0295_db_cursos` /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci */;
USE `math0295_db_cursos`;
-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: ns984.hostgator.com.br    Database: math0295_db_cursos
-- ------------------------------------------------------
-- Server version	5.7.23-23

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
INSERT INTO `auth_group` VALUES (3,'administrativo'),(1,'aluno'),(2,'desenvolvedor'),(5,'gestão'),(4,'rh');
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=81 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
INSERT INTO `auth_group_permissions` VALUES (1,2,1),(2,2,2),(3,2,3),(4,2,4),(5,2,5),(6,2,6),(7,2,7),(8,2,8),(9,2,9),(10,2,10),(11,2,11),(12,2,12),(13,2,13),(14,2,14),(15,2,15),(16,2,16),(17,2,17),(18,2,18),(19,2,19),(20,2,20),(21,2,21),(22,2,22),(23,2,23),(24,2,24),(25,2,25),(26,2,26),(27,2,27),(28,2,28),(29,2,29),(30,2,30),(31,2,31),(32,2,32),(33,2,33),(34,2,34),(35,2,35),(36,2,36),(37,2,37),(38,2,38),(39,2,39),(40,2,40),(41,3,1),(42,3,2),(43,3,3),(44,3,4),(45,3,5),(46,3,6),(47,3,7),(48,3,8),(49,3,9),(50,3,10),(51,3,11),(52,3,12),(53,3,13),(54,3,14),(55,3,15),(56,3,16),(57,3,17),(58,3,18),(59,3,19),(60,3,20),(61,3,21),(62,3,22),(63,3,23),(64,3,24),(65,3,25),(66,3,26),(67,3,27),(68,3,28),(69,3,29),(70,3,30),(71,3,31),(72,3,32),(73,3,33),(74,3,34),(75,3,35),(76,3,36),(77,3,37),(78,3,38),(79,3,39),(80,3,40);
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add Usuário',1,'add_usuario'),(2,'Can change Usuário',1,'change_usuario'),(3,'Can delete Usuário',1,'delete_usuario'),(4,'Can view Usuário',1,'view_usuario'),(5,'Can add Token',2,'add_token'),(6,'Can change Token',2,'change_token'),(7,'Can delete Token',2,'delete_token'),(8,'Can view Token',2,'view_token'),(9,'Can add Curso',3,'add_curso'),(10,'Can change Curso',3,'change_curso'),(11,'Can delete Curso',3,'delete_curso'),(12,'Can view Curso',3,'view_curso'),(13,'Can add Solicitação',4,'add_solicitacao'),(14,'Can change Solicitação',4,'change_solicitacao'),(15,'Can delete Solicitação',4,'delete_solicitacao'),(16,'Can view Solicitação',4,'view_solicitacao'),(17,'Can add my model',5,'add_mymodel'),(18,'Can change my model',5,'change_mymodel'),(19,'Can delete my model',5,'delete_mymodel'),(20,'Can view my model',5,'view_mymodel'),(21,'Can add log entry',6,'add_logentry'),(22,'Can change log entry',6,'change_logentry'),(23,'Can delete log entry',6,'delete_logentry'),(24,'Can view log entry',6,'view_logentry'),(25,'Can add permission',7,'add_permission'),(26,'Can change permission',7,'change_permission'),(27,'Can delete permission',7,'delete_permission'),(28,'Can view permission',7,'view_permission'),(29,'Can add group',8,'add_group'),(30,'Can change group',8,'change_group'),(31,'Can delete group',8,'delete_group'),(32,'Can view group',8,'view_group'),(33,'Can add content type',9,'add_contenttype'),(34,'Can change content type',9,'change_contenttype'),(35,'Can delete content type',9,'delete_contenttype'),(36,'Can view content type',9,'view_contenttype'),(37,'Can add session',10,'add_session'),(38,'Can change session',10,'change_session'),(39,'Can delete session',10,'delete_session'),(40,'Can view session',10,'view_session');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `curso`
--

DROP TABLE IF EXISTS `curso`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `curso` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `nome` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `curso`
--

LOCK TABLES `curso` WRITE;
/*!40000 ALTER TABLE `curso` DISABLE KEYS */;
INSERT INTO `curso` VALUES (1,'teste');
/*!40000 ALTER TABLE `curso` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext COLLATE utf8_unicode_ci,
  `object_repr` varchar(200) COLLATE utf8_unicode_ci NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext COLLATE utf8_unicode_ci NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_usuario_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_usuario_id` FOREIGN KEY (`user_id`) REFERENCES `usuario` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2023-04-09 04:51:51.958884','1','matheus',2,'[{\"changed\": {\"fields\": [\"First name\", \"Last name\", \"CPF\"]}}]',1,1),(2,'2023-04-09 04:52:20.320432','1','teste',1,'[{\"added\": {}}]',3,1),(3,'2023-04-09 05:11:07.966007','1','matheus batista',3,'',4,1),(4,'2023-04-09 19:38:53.472479','1','matheus',2,'[{\"changed\": {\"fields\": [\"Imagem perfil\"]}}]',1,1),(5,'2023-04-09 23:04:41.720922','1','matheus',2,'[{\"changed\": {\"fields\": [\"Cursos\"]}}]',1,1),(6,'2023-04-09 23:37:00.622271','2','',3,'',1,1),(7,'2023-04-09 23:47:49.175219','3','angelicatorquato',3,'',1,1),(8,'2023-04-09 23:51:57.216119','4','angelicatorquato',3,'',1,1),(9,'2023-04-10 01:56:40.041826','6','angelica torquato',2,'[{\"changed\": {\"fields\": [\"Criado\"]}}]',4,1),(10,'2023-04-10 01:58:40.355606','6','angelicatorquato',3,'',1,1),(11,'2023-04-10 01:58:40.527362','5','vandecyadãodossantos',3,'',1,1),(12,'2023-04-10 01:59:17.146865','5','vandecy adão dos santos',2,'[{\"changed\": {\"fields\": [\"Criado\"]}}]',4,1),(13,'2023-04-10 01:59:37.707879','6','angelica torquato',2,'[{\"changed\": {\"fields\": [\"Criado\"]}}]',4,1),(14,'2023-04-10 02:06:51.902717','5','vandecy adão dos santos',2,'[{\"changed\": {\"fields\": [\"Criado\"]}}]',4,1),(15,'2023-04-10 02:07:19.423453','7','vandecyadãodossantos',3,'',1,1),(16,'2023-04-10 02:09:32.726098','8','vandecyadãodossantos',3,'',1,1),(17,'2023-04-10 02:15:54.967119','1','matheus',2,'[]',1,1),(18,'2023-04-10 02:16:55.757757','5','vandecy adão dos santos',2,'[{\"changed\": {\"fields\": [\"Validado\"]}}]',4,1),(19,'2023-04-10 02:20:42.973493','9','angelicatorquato',3,'',1,1),(20,'2023-04-10 02:24:12.227576','6','angelica torquato',2,'[{\"changed\": {\"fields\": [\"Validado\"]}}]',4,1),(21,'2023-04-10 02:26:36.016186','5','vandecy adão dos santos',2,'[{\"changed\": {\"fields\": [\"Validado\"]}}]',4,1),(22,'2023-04-10 02:27:03.302902','10','vandecyadãodossantos',3,'',1,1),(23,'2023-04-10 02:28:58.142248','11','vandecyadãodossantos',3,'',1,1),(24,'2023-04-10 02:29:32.280506','5','vandecy adão dos santos',2,'[{\"changed\": {\"fields\": [\"Validado\"]}}]',4,1),(25,'2023-04-10 02:31:34.162672','3','nataly lima',2,'[{\"changed\": {\"fields\": [\"Validado\"]}}]',4,1),(26,'2023-04-10 02:32:02.936156','12','natalylima',3,'',1,1),(27,'2023-04-10 02:37:37.484073','13','vandecyadãodossantos',3,'',1,1),(28,'2023-04-10 02:41:11.999710','14','alamdanielventura',3,'',1,1),(29,'2023-04-10 02:48:45.772068','15','angelicaventura',3,'',1,1),(30,'2023-04-10 02:49:57.698241','1','aluno',1,'[{\"added\": {}}]',8,1),(31,'2023-04-10 02:50:24.646437','2','desenvolvedor',1,'[{\"added\": {}}]',8,1),(32,'2023-04-10 02:50:51.114150','3','administrativo',1,'[{\"added\": {}}]',8,1),(33,'2023-04-10 02:51:15.625627','4','rh',1,'[{\"added\": {}}]',8,1),(34,'2023-04-10 02:51:38.143619','5','gestor',1,'[{\"added\": {}}]',8,1),(35,'2023-04-10 02:52:30.566314','1','matheus',2,'[{\"changed\": {\"fields\": [\"Groups\"]}}]',1,1),(36,'2023-04-10 14:12:08.696552','19','teste',1,'[{\"added\": {}}]',1,1),(37,'2023-04-10 15:01:36.033606','21','testeteste',3,'',1,1),(38,'2023-04-10 15:58:35.535068','16','angelicaventura',3,'',1,1),(39,'2023-04-10 15:58:35.687676','18','matheusbatista',3,'',1,1),(40,'2023-04-10 15:58:35.838602','23','matheusbatista1',3,'',1,1),(41,'2023-04-10 15:58:35.989379','24','matheusbatista2',3,'',1,1),(42,'2023-04-10 15:58:36.137367','17','nátalybutka',3,'',1,1),(43,'2023-04-10 15:58:36.287498','19','teste',3,'',1,1),(44,'2023-04-10 16:31:04.950444','25','natalybutka',3,'',1,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `model` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (6,'admin','logentry'),(8,'auth','group'),(7,'auth','permission'),(2,'conta','token'),(1,'conta','usuario'),(9,'contenttypes','contenttype'),(5,'cpf_field','mymodel'),(3,'home','curso'),(4,'home','solicitacao'),(10,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2023-04-09 04:49:01.410495'),(2,'contenttypes','0002_remove_content_type_name','2023-04-09 04:49:02.498271'),(3,'auth','0001_initial','2023-04-09 04:49:04.607174'),(4,'auth','0002_alter_permission_name_max_length','2023-04-09 04:49:05.128437'),(5,'auth','0003_alter_user_email_max_length','2023-04-09 04:49:05.426605'),(6,'auth','0004_alter_user_username_opts','2023-04-09 04:49:05.724766'),(7,'auth','0005_alter_user_last_login_null','2023-04-09 04:49:06.034407'),(8,'auth','0006_require_contenttypes_0002','2023-04-09 04:49:06.337372'),(9,'auth','0007_alter_validators_add_error_messages','2023-04-09 04:49:06.654807'),(10,'auth','0008_alter_user_username_max_length','2023-04-09 04:49:06.975332'),(11,'auth','0009_alter_user_last_name_max_length','2023-04-09 04:49:07.297576'),(12,'auth','0010_alter_group_name_max_length','2023-04-09 04:49:07.810073'),(13,'auth','0011_update_proxy_permissions','2023-04-09 04:49:08.576736'),(14,'auth','0012_alter_user_first_name_max_length','2023-04-09 04:49:08.888944'),(15,'conta','0001_initial','2023-04-09 04:49:11.678340'),(16,'admin','0001_initial','2023-04-09 04:49:12.812830'),(17,'admin','0002_logentry_remove_auto_add','2023-04-09 04:49:13.122917'),(18,'admin','0003_logentry_add_action_flag_choices','2023-04-09 04:49:13.437155'),(19,'conta','0002_usuario_imagem_perfil','2023-04-09 04:49:14.060299'),(20,'conta','0003_alter_usuario_imagem_perfil','2023-04-09 04:49:14.567925'),(21,'home','0001_initial','2023-04-09 04:49:15.867265'),(22,'home','0002_remove_solicitacao_curso','2023-04-09 04:49:17.598973'),(23,'home','0003_solicitacao_curso','2023-04-09 04:49:18.379587'),(24,'sessions','0001_initial','2023-04-09 04:49:19.184890'),(25,'conta','0004_usuario_cursos','2023-04-09 23:01:28.550538'),(26,'conta','0005_alter_usuario_cursos','2023-04-09 23:44:33.862960'),(27,'conta','0006_alter_usuario_cursos','2023-04-09 23:47:16.601355'),(28,'conta','0007_alter_usuario_email','2023-04-10 02:14:10.966207'),(29,'home','0004_alter_solicitacao_criado','2023-04-10 02:14:11.388674');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) COLLATE utf8_unicode_ci NOT NULL,
  `session_data` longtext COLLATE utf8_unicode_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('4tmlq9tixftfrigirjlze3szghf1lxcb','.eJxVizsOwjAQRO_iGkW7sfGHkp4zWGOvI0egICV2hbg7QUoBxRQzb95LRfRWY9_KGmdRF8Xq9Lsl5HtZviA_l4bh6NtwQ1vn3B-4Ho8_rWKru2OFJuGRg4SzEECJNUrhMSS2LrMNpDEFT3Dk_R5iScanrJ11Bka9P3huM4Q:1plqu3:St8LRj19lUHY5GyfOVjPjb8PX-D0j89tOCZMRURhRZM','2023-04-24 12:45:47.680990'),('dsk5wchm8fvu8bwst1shdi6cek8t8pr2','.eJxVizsOwjAQBe_iGkW2158sJT1nsHadtRyBghTbFeLugJQCynnz5qkSjV7TaLKndVFnZaI6_Y5M-Sbb1-TH1mk6uE1X6vuax50ux-Mvq9Tqpylog9aEwmC8tjgXyGDR-MDFsDgygV2O2i_I1jmWOFvxGAmQOACo1xuOdjPK:1pljt7:zxFqZHz7fqhyoSQODLwnBSSf4NLfKk-a3lHcMTe3H3E','2023-04-24 05:16:21.705123');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `solicitacao`
--

DROP TABLE IF EXISTS `solicitacao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `solicitacao` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `nome` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `sobrenome` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `cpf` varchar(14) COLLATE utf8_unicode_ci NOT NULL,
  `email` varchar(254) COLLATE utf8_unicode_ci NOT NULL,
  `data_solicitacao` datetime(6) NOT NULL,
  `criado` tinyint(1) NOT NULL,
  `usuario_id` bigint(20) NOT NULL,
  `curso_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `cpf` (`cpf`),
  KEY `solicitacao_usuario_id_51b4387b_fk_usuario_id` (`usuario_id`),
  KEY `solicitacao_curso_id_7004c8d1_fk_curso_id` (`curso_id`),
  CONSTRAINT `solicitacao_curso_id_7004c8d1_fk_curso_id` FOREIGN KEY (`curso_id`) REFERENCES `curso` (`id`),
  CONSTRAINT `solicitacao_usuario_id_51b4387b_fk_usuario_id` FOREIGN KEY (`usuario_id`) REFERENCES `usuario` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `solicitacao`
--

LOCK TABLES `solicitacao` WRITE;
/*!40000 ALTER TABLE `solicitacao` DISABLE KEYS */;
/*!40000 ALTER TABLE `solicitacao` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `token`
--

DROP TABLE IF EXISTS `token`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `token` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `token` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `validou` tinyint(1) NOT NULL,
  `data_criacao` datetime(6) NOT NULL,
  `usuario_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `token` (`token`),
  UNIQUE KEY `usuario_id` (`usuario_id`),
  CONSTRAINT `token_usuario_id_ce053182_fk_usuario_id` FOREIGN KEY (`usuario_id`) REFERENCES `usuario` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `token`
--

LOCK TABLES `token` WRITE;
/*!40000 ALTER TABLE `token` DISABLE KEYS */;
/*!40000 ALTER TABLE `token` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuario`
--

DROP TABLE IF EXISTS `usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuario` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) COLLATE utf8_unicode_ci NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) COLLATE utf8_unicode_ci NOT NULL,
  `first_name` varchar(150) COLLATE utf8_unicode_ci NOT NULL,
  `last_name` varchar(150) COLLATE utf8_unicode_ci NOT NULL,
  `email` varchar(254) COLLATE utf8_unicode_ci DEFAULT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `matricula` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `cpf` varchar(14) COLLATE utf8_unicode_ci NOT NULL,
  `imagem_perfil` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `matricula` (`matricula`),
  UNIQUE KEY `cpf` (`cpf`),
  UNIQUE KEY `usuario_email_de9343f9_uniq` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario`
--

LOCK TABLES `usuario` WRITE;
/*!40000 ALTER TABLE `usuario` DISABLE KEYS */;
INSERT INTO `usuario` VALUES (1,'pbkdf2_sha256$390000$cL4xZnF6UAKF07v8gSKQM9$Jz6lmH8cdSPzH/q5coQV90RnlunQlteFMWjFih6L1yM=','2023-04-10 12:45:47.532477',1,'matheus','matheus','batista','matheusarrow28@gmail.com',1,1,'2023-04-09 04:50:14.000000','0000000000','125.298.929.62','perfil_img/2023/04/09/image.jpg'),(26,'pbkdf2_sha256$390000$pzcBg8v4VrgCsEz6FJVdx3$Wl/0NtMy2vD9ks3V4xXMIx03dBfZwdycphukciQeCyM=',NULL,0,'natalybutka','nataly','butka','matheusb28-@hotmail.com',0,1,'2023-04-10 16:33:24.296335','0000000001','443.713.868-65','');
/*!40000 ALTER TABLE `usuario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuario_cursos`
--

DROP TABLE IF EXISTS `usuario_cursos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuario_cursos` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `usuario_id` bigint(20) NOT NULL,
  `curso_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `usuario_cursos_usuario_id_curso_id_1688bfcb_uniq` (`usuario_id`,`curso_id`),
  KEY `usuario_cursos_curso_id_b39ef385_fk_curso_id` (`curso_id`),
  CONSTRAINT `usuario_cursos_curso_id_b39ef385_fk_curso_id` FOREIGN KEY (`curso_id`) REFERENCES `curso` (`id`),
  CONSTRAINT `usuario_cursos_usuario_id_0b8b1d3f_fk_usuario_id` FOREIGN KEY (`usuario_id`) REFERENCES `usuario` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario_cursos`
--

LOCK TABLES `usuario_cursos` WRITE;
/*!40000 ALTER TABLE `usuario_cursos` DISABLE KEYS */;
INSERT INTO `usuario_cursos` VALUES (1,1,1),(22,26,1);
/*!40000 ALTER TABLE `usuario_cursos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuario_groups`
--

DROP TABLE IF EXISTS `usuario_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuario_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `usuario_id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `usuario_groups_usuario_id_group_id_2e3cd638_uniq` (`usuario_id`,`group_id`),
  KEY `usuario_groups_group_id_c67c8651_fk_auth_group_id` (`group_id`),
  CONSTRAINT `usuario_groups_group_id_c67c8651_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `usuario_groups_usuario_id_161fc80c_fk_usuario_id` FOREIGN KEY (`usuario_id`) REFERENCES `usuario` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario_groups`
--

LOCK TABLES `usuario_groups` WRITE;
/*!40000 ALTER TABLE `usuario_groups` DISABLE KEYS */;
INSERT INTO `usuario_groups` VALUES (1,1,2),(9,26,3);
/*!40000 ALTER TABLE `usuario_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuario_user_permissions`
--

DROP TABLE IF EXISTS `usuario_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuario_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `usuario_id` bigint(20) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `usuario_user_permissions_usuario_id_permission_id_3db58b8c_uniq` (`usuario_id`,`permission_id`),
  KEY `usuario_user_permiss_permission_id_a8893ce7_fk_auth_perm` (`permission_id`),
  CONSTRAINT `usuario_user_permiss_permission_id_a8893ce7_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `usuario_user_permissions_usuario_id_693d9c50_fk_usuario_id` FOREIGN KEY (`usuario_id`) REFERENCES `usuario` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario_user_permissions`
--

LOCK TABLES `usuario_user_permissions` WRITE;
/*!40000 ALTER TABLE `usuario_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `usuario_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-04-10 17:07:00
