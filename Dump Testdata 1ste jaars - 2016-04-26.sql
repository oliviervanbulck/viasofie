-- MySQL dump 10.13  Distrib 5.6.24, for Win64 (x86_64)
--
-- Host: octamir.eu    Database: viasofie
-- ------------------------------------------------------
-- Server version	5.5.49-0ubuntu0.14.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
INSERT INTO `auth_group` VALUES (2,'Makelaar'),(1,'Verkoper');
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add dossier',7,'add_dossier'),(20,'Can change dossier',7,'change_dossier'),(21,'Can delete dossier',7,'delete_dossier'),(22,'Can add stavaza lijn',8,'add_stavazalijn'),(23,'Can change stavaza lijn',8,'change_stavazalijn'),(24,'Can delete stavaza lijn',8,'delete_stavazalijn'),(25,'Can add stavaza',9,'add_stavaza'),(26,'Can change stavaza',9,'change_stavaza'),(27,'Can delete stavaza',9,'delete_stavaza'),(28,'Can add dossier doc lijn',10,'add_dossierdoclijn'),(29,'Can change dossier doc lijn',10,'change_dossierdoclijn'),(30,'Can delete dossier doc lijn',10,'delete_dossierdoclijn'),(31,'Can add dossier doc status',11,'add_dossierdocstatus'),(32,'Can change dossier doc status',11,'change_dossierdocstatus'),(33,'Can delete dossier doc status',11,'delete_dossierdocstatus'),(34,'Can add dossier doc beschrijving',12,'add_dossierdocbeschrijving'),(35,'Can change dossier doc beschrijving',12,'change_dossierdocbeschrijving'),(36,'Can delete dossier doc beschrijving',12,'delete_dossierdocbeschrijving'),(43,'Can add land',15,'add_land'),(44,'Can change land',15,'change_land'),(45,'Can delete land',15,'delete_land'),(46,'Can add adres',16,'add_adres'),(47,'Can change adres',16,'change_adres'),(48,'Can delete adres',16,'delete_adres'),(49,'Can add gebruiker',17,'add_gebruiker'),(50,'Can change gebruiker',17,'change_gebruiker'),(51,'Can delete gebruiker',17,'delete_gebruiker'),(52,'Can add type',18,'add_type'),(53,'Can change type',18,'change_type'),(54,'Can delete type',18,'delete_type'),(55,'Can add kenmerk',19,'add_kenmerk'),(56,'Can change kenmerk',19,'change_kenmerk'),(57,'Can delete kenmerk',19,'delete_kenmerk'),(58,'Can add pand',20,'add_pand'),(59,'Can change pand',20,'change_pand'),(60,'Can delete pand',20,'delete_pand'),(61,'Can add pand immo link',21,'add_pandimmolink'),(62,'Can change pand immo link',21,'change_pandimmolink'),(63,'Can delete pand immo link',21,'delete_pandimmolink'),(64,'Can add foto',22,'add_foto'),(65,'Can change foto',22,'change_foto'),(66,'Can delete foto',22,'delete_foto'),(67,'Can add pand kenmerk per pand',23,'add_pandkenmerkperpand'),(68,'Can change pand kenmerk per pand',23,'change_pandkenmerkperpand'),(69,'Can delete pand kenmerk per pand',23,'delete_pandkenmerkperpand'),(70,'Can add label',24,'add_label'),(71,'Can change label',24,'change_label'),(72,'Can delete label',24,'delete_label'),(73,'Can add taalcode',25,'add_taalcode'),(74,'Can change taalcode',25,'change_taalcode'),(75,'Can delete taalcode',25,'delete_taalcode'),(76,'Can add taalcode per label',26,'add_taalcodeperlabel'),(77,'Can change taalcode per label',26,'change_taalcodeperlabel'),(78,'Can delete taalcode per label',26,'delete_taalcodeperlabel');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$24000$FOnqyWAK0Nhd$YTRH31tngKFaMjGZJcCcMgzPSQRuu7ezEUr0myyi2yQ=','2016-04-26 08:37:58',1,'olivier.vanbulck','Olivier','Van Bulck','olivier@vanbulck.com',1,1,'2016-04-21 10:06:07'),(2,'pbkdf2_sha256$24000$AQD2TiV0YewR$rKrMwrzd4MiW36h0gDTtyYzxALAfbi7ZT19B4EhLkvc=',NULL,1,'glenn.michiels','Glenn','Michiels','glennprogrammeur@gmail.com',1,1,'2016-04-21 10:08:46'),(3,'pbkdf2_sha256$24000$26OqmEHq50ZT$sJMhEBSkj0Ijx8V1SqjfSsbyeQP3F3SK2wEl3q+8sHw=','2016-04-25 13:34:16',1,'tim.cocx','Tim','Cocx','timcocx788@gmail.com',1,1,'2016-04-21 10:09:50'),(4,'pbkdf2_sha256$24000$QaSKI9kYFwXH$dsN3vTvq3SSeAvnFe+KffjiHgFn+F/RXLJGCqoA0PdM=','2016-04-25 13:01:53',1,'tom.bruyninx','Tom','Bruyninx','tom.bruyninx@gmail.com',1,1,'2016-04-21 10:10:19'),(5,'pbkdf2_sha256$24000$RzYtbWl1u6U6$qgZK5y2Ze8QrdUdvBBlNLzuI/7xqpXvnEEy1pd2OcBk=','2016-04-25 08:06:11',0,'test','Test','Account','test.account@mail.com',0,1,'2016-04-22 10:35:15'),(6,'pbkdf2_sha256$24000$h5X2odSgV6zL$Eg/IBXv+v2nW/RZyCoMmZU/ZWD7AVyKL0jSImrkgj74=','2016-04-25 13:29:04',1,'michael.vanderborght','Michaël','Vanderborght','michael.vanderborght.mv@gmail.com',1,1,'2016-04-25 11:03:24'),(7,'pbkdf2_sha256$24000$Ub8U2vzewsBA$A8DKFXQpU/eFcdCIVe5+hke9kzqjRUGWZ28bGmzKHV4=','2016-04-25 14:37:15',1,'Pompernikkels','','','',1,1,'2016-04-25 11:07:08'),(8,'pbkdf2_sha256$24000$UgjIvSbgxe30$AwNyEQFbfvgvNA4pNJsVyJzOvmU6KJUiJ1kUip5Bu1o=','2016-04-25 17:33:00',1,'Hashtags','','','',1,1,'2016-04-25 11:07:27'),(9,'pbkdf2_sha256$24000$baScDuEFfqJV$Dkg4f/UaNN+UajpKymviH02xxg4q1ZlPnGwIV6PlaeM=',NULL,0,'bart.peeters','Bart','Peeters','bart.peeters@hotmail.com',0,1,'2016-04-25 14:37:21'),(10,'pbkdf2_sha256$24000$6FPYZUPlkmzY$o6YrSwICLyijUmipTyX75S0SBIvoYSx2scYrtdOM97c=',NULL,0,'kelly.casal','Kelly','Casal','kelly.casal@finalproject.be',0,1,'2016-04-25 14:41:37'),(11,'pbkdf2_sha256$24000$4Kd4LGuFVAd6$fwWs5BuRd2JZjvVYZ5jse+6yTYH9MOfmLc9+ZRIqwVQ=',NULL,0,'koe.trein','Olga','Coutrin','olga.coutrin@ap.be',0,1,'2016-04-25 14:44:08'),(12,'pbkdf2_sha256$24000$cIL0KJxuW9T8$FRahyskZLn/+iyolG7IfZCqNXtpdhxOh7N9N2jppqs0=',NULL,0,'ossebolle.o','Ossebolle','O','Ossebolle-O@gmail.com',0,1,'2016-04-25 14:45:00'),(13,'pbkdf2_sha256$24000$3dlQNj3NzpjE$/Y7TQlEO0lVm4wnkNupepZF9eJvY8zxl1eh/KAW8+8E=',NULL,0,'michael.jackson','Michael','Jackson','michaeljackson@rip.com',0,1,'2016-04-25 14:45:37'),(14,'pbkdf2_sha256$24000$kmW0pii7B7Po$156O7bHrvWsrzj88P+l7QGCLy+ew+Xylgh/oc+30+eo=',NULL,0,'bouncing.marijn','Marijn','De Pooter','marijn.depooter@ap.be',0,1,'2016-04-25 14:47:33'),(15,'pbkdf2_sha256$24000$4lVtjZgU9brY$VQk+CI9n0OSlrwmt4P4K3kSjdCjesdyWHxsni4mnBTI=',NULL,0,'bartje.debever','Bart','De Bever','bart.debever@nva.be',0,1,'2016-04-25 14:48:52'),(17,'pbkdf2_sha256$24000$ZSWcqfuXU0WX$rv+ReppjofLwdB4g5T7mJKVZcbr2yVaPYptpHATKovw=',NULL,0,'Daeynerys.Targaryen','Daeynerys','Targaryen','Daeynerys.Targaryen@hotmail.com',0,1,'2016-04-25 14:50:58'),(18,'pbkdf2_sha256$24000$NSpLugoLdY3h$P/MVPs2IP+LZvpT+tqgGmf4Iq9mKA7ExOQQw6eCGciE=',NULL,0,'Spongebob.Squarepants','Spongebob','Squarepants','Spongebob.squarepants@zoho.com',0,1,'2016-04-25 14:56:56'),(19,'pbkdf2_sha256$24000$QR9uaGEPp3F2$G1osPNZEBqsS9l89LCw+dkkbO+VEsDyMB3uGTqopMZ8=',NULL,0,'christel.declerck','Christel','De Clerck','christel.declerck@outlook.com',0,1,'2016-04-25 15:00:25'),(20,'pbkdf2_sha256$24000$IbDR9U0V6lvF$LUpkKkxLCD61Hqk9K7Jzw4jTl+6WbpUOJEHj63Q0kqU=',NULL,0,'Boratboy','Borat','Sagdiev','Borat.sagdiev@yahoo.com',0,1,'2016-04-25 16:57:58'),(21,'pbkdf2_sha256$24000$UEiLFSRQbDA0$tPZT+UtzdhfTshL06FraSGNGG4xheFLG3uVH0x08H7M=',NULL,0,'Azamatboy','Azamat','Bagatov','Bagatov.azamat@yahoo.com',0,1,'2016-04-25 16:59:22'),(22,'pbkdf2_sha256$24000$zhM4Mf7uYyfe$gVcnBXcFPfLOEi0x6l8ePfWHP5pK2+6xzRc8ckUZ0+E=',NULL,0,'Pablo','Pablo','Escobar','Drugs4leven@yahoo.be',0,1,'2016-04-25 17:00:57'),(23,'pbkdf2_sha256$24000$wl6ki7aalazx$9xSp8frRiPN7BOu9EBoCPLntoJihYwy9ntuawiQLVB8=',NULL,0,'HerbMaster','Bobientje','Peters','Herbmaster2000@hotmail.com',0,1,'2016-04-25 17:02:11'),(24,'pbkdf2_sha256$24000$2lbokcuR8o4Y$b1CbW2CB3zTBDZMjGXS1f/EC4ODcUXfA8G1Gh29plSg=',NULL,0,'Zezima','Zezima','Zezma','Zezima.rs@hotmail.com',0,1,'2016-04-25 17:04:23'),(25,'pbkdf2_sha256$24000$saea0fYNFiKq$4C9+55dzbdyWnoGOATVld+4EukqK39o/X0G2GOnmiDo=',NULL,0,'KAKEROT','Goku','Son','Goku_Son@namek.com',0,1,'2016-04-25 17:15:16'),(26,'pbkdf2_sha256$24000$eocWRyBHZyZA$DlCf9ga3zjLMsF62EjXj2VyMVsaPs2UpOtp2XxZ5yK4=',NULL,0,'IncompetenteKoe','Musatafa','El Beoi','Musti599@yahoo.nl',0,1,'2016-04-25 17:29:33'),(27,'pbkdf2_sha256$24000$1V6EHHjo98FH$+v0ByGj4+6MYRBuJcg5HnxoD6igjrkw696WqmJTkHJA=',NULL,0,'APLover','Apu','Abdesalaat','Apuman@yahoo.com',0,1,'2016-04-25 17:32:46'),(28,'pbkdf2_sha256$24000$WXxZ7vFIuomu$YY4AinOXzn1rQhvHknUlrpXHwl6wVINbaJ6Cn1/yOIU=',NULL,0,'VEGETA','Vegeta','Breigh','VEGI_BREI@Vegeta.com',0,1,'2016-04-25 17:39:44');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
INSERT INTO `auth_user_groups` VALUES (2,1,2),(1,2,2),(3,3,2),(4,4,2),(5,6,2),(6,9,1),(7,10,1),(8,11,1),(10,12,1),(9,13,1),(11,14,1),(12,15,1),(13,17,1),(14,18,1),(15,19,1),(16,20,1),(17,22,1),(19,25,1),(18,26,2),(20,27,1),(21,28,1);
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2016-04-21 10:12:14','2','glenn.michiels',2,'Changed first_name and last_name.',4,1),(2,'2016-04-21 10:12:27','1','olivier.vanbulck',2,'Changed first_name and last_name.',4,1),(3,'2016-04-21 10:12:46','3','tim.cocx',2,'Changed first_name and last_name.',4,1),(4,'2016-04-21 10:13:35','4','tom.bruyninx',2,'Changed first_name and last_name.',4,1),(5,'2016-04-22 10:34:12','1','Land object',1,'Added.',15,1),(6,'2016-04-22 10:34:54','1','Adres object',1,'Added.',16,1),(7,'2016-04-22 10:35:15','5','test',1,'Added. Added gebruiker \"Gebruiker object\".',4,1),(8,'2016-04-22 10:35:48','5','test',2,'Changed first_name, last_name and email.',4,1),(9,'2016-04-22 11:47:50','2','glenn.michiels',2,'Added gebruiker \"Glenn Michiels (glennprogrammeur@gmail.com)\".',4,3),(10,'2016-04-22 11:48:11','1','olivier.vanbulck',2,'Added gebruiker \"Olivier Van Bulck (olivier@vanbulck.com)\".',4,3),(11,'2016-04-22 11:48:28','4','tom.bruyninx',2,'Added gebruiker \"Tom Bruyninx (tom.bruyninx@gmail.com)\".',4,3),(12,'2016-04-22 11:48:38','3','tim.cocx',2,'Added gebruiker \"Tim Cocx (timcocx788@gmail.com)\".',4,3),(13,'2016-04-22 11:49:43','1','NL',1,'Added.',25,3),(14,'2016-04-22 11:49:48','2','FR',1,'Added.',25,3),(15,'2016-04-22 11:49:52','3','EN',1,'Added.',25,3),(16,'2016-04-22 11:50:51','2','Nederland - NL',1,'Added.',15,3),(17,'2016-04-22 12:21:10','3','Italiëlei 14, 2000 Antwerpen',1,'Added.',16,3),(18,'2016-04-22 12:27:45','1','Verkoper',1,'Added.',3,3),(19,'2016-04-22 12:27:51','2','Makelaar',1,'Added.',3,3),(20,'2016-04-22 12:30:02','1','olivier.vanbulck',2,'Changed user_permissions.',4,3),(21,'2016-04-22 12:30:41','1','olivier.vanbulck',2,'Changed user_permissions.',4,3),(22,'2016-04-22 12:38:10','2','glenn.michiels',2,'Changed groups.',4,3),(23,'2016-04-22 12:38:22','1','olivier.vanbulck',2,'Changed groups.',4,3),(24,'2016-04-22 12:38:36','3','tim.cocx',2,'Changed groups.',4,3),(25,'2016-04-22 12:38:48','4','tom.bruyninx',2,'Changed groups.',4,3),(26,'2016-04-25 08:08:30','1','Huis',1,'Added.',18,1),(27,'2016-04-25 08:09:54','1','Huis - Teststraat 45, 1000 Brussel',1,'Added.',20,1),(28,'2016-04-25 08:44:15','1','Foto object',1,'Added.',22,1),(29,'2016-04-25 09:56:46','2','Foto object',1,'Added.',22,1),(30,'2016-04-25 11:03:00','2','glenn.michiels',2,'No fields changed.',4,1),(31,'2016-04-25 11:03:24','6','michael.vanderborght',1,'Added. Added gebruiker \"  ()\".',4,1),(32,'2016-04-25 11:04:10','6','michael.vanderborght',2,'Changed first_name, last_name, email, is_staff, is_superuser and groups.',4,1),(33,'2016-04-25 11:07:08','7','Pompernikkels',1,'Added. Added gebruiker \"  ()\".',4,3),(34,'2016-04-25 11:07:27','8','Hashtags',1,'Added. Added gebruiker \"  ()\".',4,3),(35,'2016-04-25 11:08:24','8','Hashtags',2,'Changed is_superuser.',4,3),(36,'2016-04-25 11:08:32','7','Pompernikkels',2,'Changed is_superuser.',4,3),(37,'2016-04-25 11:16:28','7','Pompernikkels',2,'Changed is_staff.',4,3),(38,'2016-04-25 11:16:47','8','Hashtags',2,'Changed is_staff.',4,3),(39,'2016-04-25 13:15:48','7','Pompernikkels',2,'Changed password.',4,3),(40,'2016-04-25 13:18:04','8','Hashtags',2,'Changed password.',4,3),(41,'2016-04-25 14:37:18','4','Meistraat 3, 2000 Antwerpen',1,'Added.',16,7),(42,'2016-04-25 14:37:21','9','BartPeeters',1,'Added. Added gebruiker \"  ()\".',4,7),(43,'2016-04-25 14:37:53','3','DE - Duitsland',1,'Added.',15,7),(44,'2016-04-25 14:37:59','9','BartPeeters',2,'Changed first_name, last_name, email and groups.',4,7),(45,'2016-04-25 14:38:00','4','FR - Frankrijk',1,'Added.',15,7),(46,'2016-04-25 14:38:20','9','bart.peeters',2,'Changed username.',4,7),(47,'2016-04-25 14:38:21','5','GB - Verenigd Koningkrijk',1,'Added.',15,7),(48,'2016-04-25 14:39:13','5','Elf-Novemberstraat 69, 2910 Essen',1,'Added.',16,7),(49,'2016-04-25 14:39:43','6','LU - Luxemburg',1,'Added.',15,7),(50,'2016-04-25 14:40:47','7','DK - Denemarken',1,'Added.',15,7),(51,'2016-04-25 14:41:08','6','Gegevensstraat 1, 2000 Analyse',1,'Added.',16,7),(52,'2016-04-25 14:41:30','7','Tjoeplaan 420, 2900 Schoten',1,'Added.',16,7),(53,'2016-04-25 14:41:37','10','kelly.casal',1,'Added. Added gebruiker \"  ()\".',4,7),(54,'2016-04-25 14:42:01','10','kelly.casal',2,'Changed first_name, last_name, email and groups.',4,7),(55,'2016-04-25 14:43:14','8','Liesje\'s Bordeel 14, 3800 Sint-Truiden',1,'Added.',16,7),(56,'2016-04-25 14:43:42','9','Hypothesestraat 13, 75008 Pompernikkel',1,'Added.',16,7),(57,'2016-04-25 14:44:05','9','Hypothesestraat 13, 3928 Pompernikkel',2,'Changed postcode and land.',16,7),(58,'2016-04-25 14:44:08','11','koe.trein',1,'Added. Added gebruiker \"  ()\".',4,7),(59,'2016-04-25 14:44:26','10','Aardbeienlaan 12, 9120 Melsele',1,'Added.',16,7),(60,'2016-04-25 14:44:46','11','koe.trein',2,'Changed first_name, last_name, email and groups.',4,7),(61,'2016-04-25 14:45:00','12','ossebolle.o',1,'Added. Added gebruiker \"  ()\".',4,7),(62,'2016-04-25 14:45:37','13','michael.jackson',1,'Added. Added gebruiker \"  ()\".',4,7),(63,'2016-04-25 14:46:01','13','michael.jackson',2,'Changed first_name, last_name, email and groups.',4,7),(64,'2016-04-25 14:46:21','13','michael.jackson',2,'Changed email.',4,7),(65,'2016-04-25 14:47:07','11','Memestreet 5/7, 420 Doge',1,'Added.',16,7),(66,'2016-04-25 14:47:16','12','ossebolle.o',2,'Changed first_name, last_name, email and groups.',4,7),(67,'2016-04-25 14:47:33','14','bouncing.marijn',1,'Added. Added gebruiker \"  ()\".',4,7),(68,'2016-04-25 14:47:46','14','bouncing.marijn',2,'Changed first_name, last_name, email and groups.',4,7),(69,'2016-04-25 14:48:08','13','michael.jackson',2,'Changed email.',4,7),(70,'2016-04-25 14:48:52','15','bartje.debever',1,'Added. Added gebruiker \"  ()\".',4,7),(71,'2016-04-25 14:49:09','15','bartje.debever',2,'Changed first_name, last_name, email and groups.',4,7),(72,'2016-04-25 14:49:11','16','mia.khalifa',1,'Added. Added gebruiker \"  ()\".',4,7),(73,'2016-04-25 14:49:36','16','mia.khalifa',2,'Changed first_name, last_name and email.',4,7),(74,'2016-04-25 14:49:42','8','Liesje\'s Club 14, 3800 Sint-Truiden',2,'Changed straat.',16,7),(75,'2016-04-25 14:50:51','12','Targaryenstraat 12, 2070 Zwijndrecht',1,'Added.',16,7),(76,'2016-04-25 14:50:59','17','Daeynerys.Targaryen',1,'Added. Added gebruiker \"  ()\".',4,7),(77,'2016-04-25 14:51:12','13','Dertienstraat 13, 1313 Dertienwerpen',1,'Added.',16,7),(78,'2016-04-25 14:51:40','17','Daeynerys.Targaryen',2,'Changed first_name, last_name, email and groups.',4,7),(79,'2016-04-25 14:52:14','16','mia.khalifa',3,'',4,7),(80,'2016-04-25 14:56:26','8','GR - Griekenland',1,'Added.',15,7),(81,'2016-04-25 14:56:34','14','Schelpstraat 120 38, 1970 Bikinibroek',1,'Added.',16,7),(82,'2016-04-25 14:56:56','18','Spongebob.Squarepants',1,'Added. Added gebruiker \"  ()\".',4,7),(83,'2016-04-25 14:57:03','9','IT - Italië',1,'Added.',15,7),(84,'2016-04-25 14:57:51','18','Spongebob.Squarepants',2,'Changed first_name, last_name, email and groups.',4,7),(85,'2016-04-25 14:58:20','10','IE - Ierland',1,'Added.',15,7),(86,'2016-04-25 14:59:35','3','Huis - Schelpstraat 120 38, 1970 Bikinibroek',1,'Added.',20,7),(87,'2016-04-25 15:00:20','3','Foto object',1,'Added.',22,7),(88,'2016-04-25 15:00:21','15','Klapperstraat 12, 9100 Sint-Niklaas',1,'Added.',16,7),(89,'2016-04-25 15:00:25','19','christel.declerck',1,'Added. Added gebruiker \"  ()\".',4,7),(90,'2016-04-25 15:00:53','2','Appartement',1,'Added.',18,7),(91,'2016-04-25 15:00:59','19','christel.declerck',2,'Changed first_name, last_name, email and groups.',4,7),(92,'2016-04-25 15:01:03','3','Rijhuis',1,'Added.',18,7),(93,'2016-04-25 15:01:26','4','Halfopen bebouwing',1,'Added.',18,7),(94,'2016-04-25 15:01:37','3','Gesloten bebouwing',2,'Changed type.',18,7),(95,'2016-04-25 15:01:43','5','Loft',1,'Added.',18,7),(96,'2016-04-25 15:02:00','6','Caravan',1,'Added.',18,7),(97,'2016-04-25 15:02:20','7','Villa',1,'Added.',18,7),(98,'2016-04-25 15:02:32','8','Duplex appartement',1,'Added.',18,7),(99,'2016-04-25 15:02:41','9','Villa',1,'Added.',18,7),(100,'2016-04-25 15:02:50','9','Villa',3,'',18,7),(101,'2016-04-25 15:03:06','10','Kot',1,'Added.',18,7),(102,'2016-04-25 15:03:46','1','Immovlan - Huis - Schelpstraat 120 38, 1970 Bikinibroek',1,'Added.',21,7),(103,'2016-04-25 15:03:52','11','Landhuis',1,'Added.',18,7),(104,'2016-04-25 15:04:10','1','Aantal verdiepingen',1,'Added.',19,7),(105,'2016-04-25 15:04:57','8','Liesje\'s Club 14, 3800 Sint-Truiden',3,'',16,7),(106,'2016-04-25 15:08:13','2','Aantal badkamers',1,'Added.',19,7),(107,'2016-04-25 15:08:36','3','Verdieping',1,'Added.',19,7),(108,'2016-04-25 15:08:53','4','Aantal kamers',1,'Added.',19,7),(109,'2016-04-25 15:09:02','5','Aantal keukens',1,'Added.',19,7),(110,'2016-04-25 15:09:28','6','Aantal parkeerplaatsen',1,'Added.',19,7),(111,'2016-04-25 15:09:50','7','Oppervlakte tuin',1,'Added.',19,7),(112,'2016-04-25 15:10:21','1','Aantal kamers - 3 - Huis - Schelpstraat 120 38, 1970 Bikinibroek',1,'Added.',23,7),(113,'2016-04-25 15:10:40','2','Aantal verdiepingen - 2 - Huis - Schelpstraat 120 38, 1970 Bikinibroek',1,'Added.',23,7),(114,'2016-04-25 15:13:03','1','Coutrin\'s Aankoop',1,'Added.',12,7),(115,'2016-04-25 15:13:49','1','Dossier: Huis - Teststraat 45, 1000 Brussel',1,'Added.',7,7),(116,'2016-04-25 15:14:04','1','Coutrin\'s Aankoop',3,'',12,7),(117,'2016-04-25 15:15:12','2','Dit is de dossierbeschrijving van het testdossier',1,'Added.',12,7),(118,'2016-04-25 15:15:27','1','<class \'django.db.models.fields.IntegerField\'>',1,'Added.',11,7),(119,'2016-04-25 15:19:05','2','<class \'django.db.models.fields.IntegerField\'>',1,'Added.',11,7),(120,'2016-04-25 15:21:57','1','Dit pand is te koop',1,'Added.',9,7),(121,'2016-04-25 15:22:02','2','Dit pand is verkocht',1,'Added.',9,7),(122,'2016-04-25 15:22:20','3','Dit pand is verhuurd',1,'Added.',9,7),(123,'2016-04-25 15:22:28','4','Dit pand is te huur',1,'Added.',9,7),(124,'2016-04-25 15:23:22','1','Huis - Teststraat 45, 1000 BrusselDit pand is te koop',1,'Added.',8,7),(125,'2016-04-25 15:25:07','5','Er wordt nog onderhandeld over dit pand',1,'Added.',9,7),(126,'2016-04-25 15:27:19','3','<class \'django.db.models.fields.IntegerField\'>',1,'Added.',11,7),(127,'2016-04-25 15:27:21','4','<class \'django.db.models.fields.IntegerField\'>',1,'Added.',11,7),(128,'2016-04-25 15:27:22','5','<class \'django.db.models.fields.IntegerField\'>',1,'Added.',11,7),(129,'2016-04-25 15:27:22','6','<class \'django.db.models.fields.IntegerField\'>',1,'Added.',11,7),(130,'2016-04-25 15:27:24','7','<class \'django.db.models.fields.IntegerField\'>',1,'Added.',11,7),(131,'2016-04-25 15:27:25','8','<class \'django.db.models.fields.IntegerField\'>',1,'Added.',11,7),(132,'2016-04-25 15:27:31','9','<class \'django.db.models.fields.IntegerField\'>',1,'Added.',11,7),(133,'2016-04-25 15:27:32','10','<class \'django.db.models.fields.IntegerField\'>',1,'Added.',11,7),(134,'2016-04-25 16:22:28','11','S - Zweden',1,'Added.',15,8),(135,'2016-04-25 16:23:02','12','N - Noorwegen',1,'Added.',15,8),(136,'2016-04-25 16:23:36','13','PL - Polen',1,'Added.',15,8),(137,'2016-04-25 16:24:42','14','ES - Spanje',1,'Added.',15,8),(138,'2016-04-25 16:24:59','11','SE - Zweden',2,'Changed landcode.',15,8),(139,'2016-04-25 16:25:15','12','NO - Noorwegen',2,'Changed landcode.',15,8),(140,'2016-04-25 16:25:52','15','CZ - Tsjechië',1,'Added.',15,8),(141,'2016-04-25 16:26:35','16','CH - Zwitserland',1,'Added.',15,8),(142,'2016-04-25 16:27:08','17','AT - Oostenrijk',1,'Added.',15,8),(143,'2016-04-25 16:27:42','18','PT - Portugal',1,'Added.',15,8),(144,'2016-04-25 16:29:35','19','MA - Marokko',1,'Added.',15,8),(145,'2016-04-25 16:30:35','20','HR - Kroatië',1,'Added.',15,8),(146,'2016-04-25 16:34:14','16','Panamarenkolaan 23, 3050 Kruibeke',1,'Added.',16,8),(147,'2016-04-25 16:35:34','17','Sagdievstraat 123, 5010 boratyurt',1,'Added.',16,8),(148,'2016-04-25 16:36:54','18','boeddhistenstraat 56, 2090 Isos',1,'Added.',16,8),(149,'2016-04-25 16:37:51','19','Renemagrittelaan 44, 5080 Vladslo',1,'Added.',16,8),(150,'2016-04-25 16:39:35','20','Ulitsa dictatorskaja 666, 1945 Stalinskaja',1,'Added.',16,8),(151,'2016-04-25 16:40:43','21','Lenin Pidaraz 56, 3069 Stalinskaja',1,'Added.',16,8),(152,'2016-04-25 16:41:59','22','Zonderhaatstraat 101, 9010 Antwerpen',1,'Added.',16,8),(153,'2016-04-25 16:42:41','23','Zoisnatuurlaan 99, 6030 Brabant',1,'Added.',16,8),(154,'2016-04-25 16:43:15','24','Nietmeerdoenstraat 80, 5040 Helemaalmooi',1,'Added.',16,8),(155,'2016-04-25 16:43:56','25','Honderdeurolaan 100, 1010 Brabant',1,'Added.',16,8),(156,'2016-04-25 16:48:44','26','Johnsnowisdoodstraat 1, 2020 Westeros',1,'Added.',16,8),(157,'2016-04-25 16:57:58','20','Boratboy',1,'Added. Added gebruiker \"  ()\".',4,8),(158,'2016-04-25 16:58:40','20','Boratboy',2,'Changed first_name, last_name, email and groups.',4,8),(159,'2016-04-25 16:59:22','21','Azamatboy',1,'Added. Added gebruiker \"  ()\".',4,8),(160,'2016-04-25 16:59:59','21','Azamatboy',2,'Changed first_name, last_name and email.',4,8),(161,'2016-04-25 17:00:57','22','Pablo',1,'Added. Added gebruiker \"  ()\".',4,8),(162,'2016-04-25 17:01:21','22','Pablo',2,'Changed first_name, last_name, email and groups.',4,8),(163,'2016-04-25 17:02:11','23','HerbMaster',1,'Added. Added gebruiker \"  ()\".',4,8),(164,'2016-04-25 17:02:47','23','HerbMaster',2,'Changed first_name, last_name and email.',4,8),(165,'2016-04-25 17:04:23','24','Zezima',1,'Added. Added gebruiker \"  ()\".',4,8),(166,'2016-04-25 17:04:56','24','Zezima',2,'Changed first_name, last_name and email.',4,8),(167,'2016-04-25 17:06:57','6','Dit pand is onbeschikbaar',1,'Added.',9,8),(168,'2016-04-25 17:09:03','7','Dit pand is momenteel in onderhoud',1,'Added.',9,8),(169,'2016-04-25 17:09:25','6','Dit pand is momenteel onbeschikbaar',2,'Changed status.',9,8),(170,'2016-04-25 17:14:22','8','Dit pand is momenteel ongeschikt voor gebuik',1,'Added.',9,8),(171,'2016-04-25 17:15:02','27','Namek 9000, 9000 Maima region',1,'Added.',16,8),(172,'2016-04-25 17:15:07','8','Garage',1,'Added.',19,8),(173,'2016-04-25 17:15:16','25','KAKEROT',1,'Added. Added gebruiker \"  ()\".',4,8),(174,'2016-04-25 17:15:17','9','Berging',1,'Added.',19,8),(175,'2016-04-25 17:16:29','10','Zolder',1,'Added.',19,8),(176,'2016-04-25 17:16:33','11','Zwembad',1,'Added.',19,8),(177,'2016-04-25 17:17:05','12','Oppervlakte terras',1,'Added.',19,8),(178,'2016-04-25 17:29:34','26','IncompetenteKoe',1,'Added. Added gebruiker \"  ()\".',4,8),(179,'2016-04-25 17:30:44','26','IncompetenteKoe',2,'Changed first_name, last_name, email and groups.',4,8),(180,'2016-04-25 17:31:37','25','KAKEROT',2,'Changed first_name, last_name, email and groups.',4,8),(181,'2016-04-25 17:32:46','27','APLover',1,'Added. Added gebruiker \"  ()\".',4,8),(182,'2016-04-25 17:34:08','27','APLover',2,'Changed first_name, last_name, email and groups.',4,8),(183,'2016-04-25 17:35:19','19','MA - Marokko',3,'',15,8),(184,'2016-04-25 17:36:59','21','RS - Servië',1,'Added.',15,8),(185,'2016-04-25 17:39:05','28','Vegeta 8999, 8999 Vegeta',1,'Added.',16,8),(186,'2016-04-25 17:39:44','28','VEGETA',1,'Added. Added gebruiker \"  ()\".',4,8),(187,'2016-04-25 17:39:56','12','Vrijstaande woning',1,'Added.',18,8),(188,'2016-04-25 17:40:11','13','Rijtjeswoning of tussenwoning',1,'Added.',18,8),(189,'2016-04-25 17:40:18','28','VEGETA',2,'Changed first_name, last_name, email and groups.',4,8),(190,'2016-04-25 17:40:23','14','Drive-in-woning',1,'Added.',18,8),(191,'2016-04-25 17:40:31','15','Schakelwoning',1,'Added.',18,8),(192,'2016-04-25 17:40:46','16','Bungalow',1,'Added.',18,8),(193,'2016-04-25 17:41:01','17','Grachtenpand / herenhuis',1,'Added.',18,8),(194,'2016-04-25 17:41:12','18','Penthouse',1,'Added.',18,8),(195,'2016-04-25 17:41:27','19','Maisonettes',1,'Added.',18,8),(196,'2016-04-25 17:41:34','20','Etagewoning',1,'Added.',18,8),(197,'2016-04-25 17:42:06','21','Boomhut',1,'Added.',18,8),(198,'2016-04-25 17:44:32','4','Villa - Sagdievstraat 123, 5010 boratyurt',1,'Added.',20,8),(199,'2016-04-25 17:46:12','3','Aantal badkamers - 2 - Villa - Sagdievstraat 123, 5010 boratyurt',1,'Added.',23,8),(200,'2016-04-25 17:46:30','4','Aantal verdiepingen - 3 - Villa - Sagdievstraat 123, 5010 boratyurt',1,'Added.',23,8),(201,'2016-04-25 17:46:44','5','Garage - 2 - Villa - Sagdievstraat 123, 5010 boratyurt',1,'Added.',23,8),(202,'2016-04-25 17:47:02','6','Zwembad - 1 - Villa - Sagdievstraat 123, 5010 boratyurt',1,'Added.',23,8),(203,'2016-04-25 17:47:31','7','Aantal kamers - 14 - Villa - Sagdievstraat 123, 5010 boratyurt',1,'Added.',23,8),(204,'2016-04-25 17:47:46','8','Zolder - 1 - Villa - Sagdievstraat 123, 5010 boratyurt',1,'Added.',23,8),(205,'2016-04-25 17:48:01','9','Aantal keukens - 2 - Villa - Sagdievstraat 123, 5010 boratyurt',1,'Added.',23,8),(206,'2016-04-25 17:49:07','5','Villa - Zoisnatuurlaan 99, 6030 Brabant',1,'Added.',20,8),(207,'2016-04-25 17:51:29','6','Villa - Tjoeplaan 420, 2900 Schoten',1,'Added.',20,8),(208,'2016-04-25 17:51:58','10','Aantal kamers - 10 - Villa - Tjoeplaan 420, 2900 Schoten',1,'Added.',23,8),(209,'2016-04-25 17:52:08','11','Aantal keukens - 2 - Villa - Tjoeplaan 420, 2900 Schoten',1,'Added.',23,8),(210,'2016-04-25 17:52:25','12','Aantal badkamers - 2 - Villa - Tjoeplaan 420, 2900 Schoten',1,'Added.',23,8),(211,'2016-04-25 17:52:54','7','Boomhut - boeddhistenstraat 56, 2090 Isos',1,'Added.',20,8),(212,'2016-04-25 17:54:21','4','Villa - Sagdievstraat 123, 5010 boratyurt',2,'Changed algemene_beschrijving.',20,8),(213,'2016-04-25 17:54:39','5','Villa - Zoisnatuurlaan 99, 6030 Brabant',2,'No fields changed.',20,8),(214,'2016-04-25 17:57:31','8','Penthouse - Nietmeerdoenstraat 80, 5040 Helemaalmooi',1,'Added.',20,8),(215,'2016-04-25 17:58:26','8','Penthouse - Nietmeerdoenstraat 80, 5040 Helemaalmooi',2,'No fields changed.',20,8),(216,'2016-04-25 17:58:31','8','Penthouse - Nietmeerdoenstraat 80, 5040 Helemaalmooi',2,'No fields changed.',20,8),(217,'2016-04-25 18:01:38','9','Huis - Renemagrittelaan 44, 5080 Vladslo',1,'Added.',20,8),(218,'2016-04-25 18:09:09','10','Duplex appartement - Klapperstraat 12, 9100 Sint-Niklaas',1,'Added.',20,8),(219,'2016-04-25 18:10:18','10','Duplex appartement - Klapperstraat 12, 9100 Sint-Niklaas',2,'No fields changed.',20,8),(220,'2016-04-25 18:12:57','11','Bungalow - Dertienstraat 13, 1313 Dertienwerpen',1,'Added.',20,8),(221,'2016-04-25 18:14:11','11','Bungalow - Dertienstraat 13, 1313 Dertienwerpen',2,'No fields changed.',20,8),(222,'2016-04-25 18:15:20','3','Foto object',2,'No fields changed.',22,8),(223,'2016-04-25 18:35:57','28','VEGETA',2,'No fields changed.',4,8),(224,'2016-04-25 18:46:02','4','Foto object',1,'Added.',22,8),(225,'2016-04-25 18:48:36','5','Foto object',1,'Added.',22,8),(226,'2016-04-25 18:52:11','6','Foto object',1,'Added.',22,8),(227,'2016-04-25 18:54:34','7','Foto object',1,'Added.',22,8),(228,'2016-04-25 18:57:02','8','Foto object',1,'Added.',22,8),(229,'2016-04-25 19:00:42','9','Foto object',1,'Added.',22,8),(230,'2016-04-25 19:05:12','10','Foto object',1,'Added.',22,8),(231,'2016-04-25 19:06:08','4','Foto object',2,'No fields changed.',22,8),(232,'2016-04-25 19:08:51','11','Foto object',1,'Added.',22,8),(233,'2016-04-25 19:11:17','2','Dossier: Boomhut - boeddhistenstraat 56, 2090 Isos',1,'Added.',7,8),(234,'2016-04-25 19:11:28','3','Dossier: Huis - Teststraat 45, 1000 Brussel',1,'Added.',7,8),(235,'2016-04-25 19:11:36','4','Dossier: Huis - Schelpstraat 120 38, 1970 Bikinibroek',1,'Added.',7,8),(236,'2016-04-25 19:11:56','5','Dossier: Duplex appartement - Klapperstraat 12, 9100 Sint-Niklaas',1,'Added.',7,8),(237,'2016-04-25 19:12:12','6','Dossier: Bungalow - Dertienstraat 13, 1313 Dertienwerpen',1,'Added.',7,8),(238,'2016-04-25 19:12:32','7','Dossier: Villa - Tjoeplaan 420, 2900 Schoten',1,'Added.',7,8),(239,'2016-04-25 19:12:40','8','Dossier: Villa - Sagdievstraat 123, 5010 boratyurt',1,'Added.',7,8),(240,'2016-04-25 19:13:09','9','Dossier: Villa - Zoisnatuurlaan 99, 6030 Brabant',1,'Added.',7,8),(241,'2016-04-25 19:13:35','10','Dossier: Penthouse - Nietmeerdoenstraat 80, 5040 Helemaalmooi',1,'Added.',7,8),(242,'2016-04-25 19:15:54','2','Huis - Teststraat 45, 1000 BrusselDit pand is verkocht',1,'Added.',8,8),(243,'2016-04-25 19:16:05','2','Huis - Teststraat 45, 1000 BrusselDit pand is verkocht',3,'',8,8),(244,'2016-04-25 19:16:32','3','Dossier: Huis - Teststraat 45, 1000 Brussel',3,'',7,8),(245,'2016-04-25 19:16:56','3','Huis - Schelpstraat 120 38, 1970 BikinibroekDit pand is verhuurd',1,'Added.',8,8),(246,'2016-04-25 19:17:05','4','Villa - Sagdievstraat 123, 5010 boratyurtDit pand is momenteel in onderhoud',1,'Added.',8,8),(247,'2016-04-25 19:17:12','5','Villa - Zoisnatuurlaan 99, 6030 BrabantDit pand is te huur',1,'Added.',8,8),(248,'2016-04-25 19:17:25','6','Villa - Tjoeplaan 420, 2900 SchotenDit pand is momenteel ongeschikt voor gebuik',1,'Added.',8,8),(249,'2016-04-25 19:17:56','7','Boomhut - boeddhistenstraat 56, 2090 IsosEr wordt nog onderhandeld over dit pand',1,'Added.',8,8),(250,'2016-04-25 19:19:33','8','Duplex appartement - Klapperstraat 12, 9100 Sint-NiklaasDit pand is momenteel onbeschikbaar',1,'Added.',8,8),(251,'2016-04-25 20:43:29','4','Villa - Sagdievstraat 123, 5010 boratyurt',2,'No fields changed.',20,8),(252,'2016-04-25 20:48:54','2','Verynice - Villa - Sagdievstraat 123, 5010 boratyurt',1,'Added.',21,8),(253,'2016-04-25 20:49:14','2','Verynice - Villa - Sagdievstraat 123, 5010 boratyurt',2,'No fields changed.',21,8),(254,'2016-04-25 20:50:16','3','Narcos - Villa - Zoisnatuurlaan 99, 6030 Brabant',1,'Added.',21,8),(255,'2016-04-25 20:59:00','2','Verynice - Villa - Sagdievstraat 123, 5010 boratyurt',2,'No fields changed.',21,8),(256,'2016-04-25 21:04:38','9','Pand is verkocht maar nog niet betaald',1,'Added.',9,8),(257,'2016-04-25 21:05:13','9','Pand is verkocht maar nog niet betaald',3,'',9,8),(258,'2016-04-25 21:10:46','13','Aantal verdiepingen - 0 - Bungalow - Dertienstraat 13, 1313 Dertienwerpen',1,'Added.',23,8),(259,'2016-04-25 21:12:25','9','Bungalow - Dertienstraat 13, 1313 DertienwerpenDit pand is verkocht',1,'Added.',8,8),(260,'2016-04-25 21:14:55','7','Boomhut - boeddhistenstraat 56, 2090 Isos',2,'Changed prijs.',20,8),(261,'2016-04-25 21:16:22','6','Villa - Tjoeplaan 420, 2900 Schoten',2,'Changed bouwjaar.',20,8),(262,'2016-04-26 08:42:09','6','michael.vanderborght',2,'Changed first_name.',4,3),(263,'2016-04-26 08:44:18','6','michael.vanderborght',2,'Changed first_name.',4,3);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(7,'dossiers','dossier'),(12,'dossiers','dossierdocbeschrijving'),(10,'dossiers','dossierdoclijn'),(11,'dossiers','dossierdocstatus'),(9,'dossiers','stavaza'),(8,'dossiers','stavazalijn'),(16,'gebruikers','adres'),(17,'gebruikers','gebruiker'),(15,'gebruikers','land'),(22,'panden','foto'),(19,'panden','kenmerk'),(20,'panden','pand'),(21,'panden','pandimmolink'),(23,'panden','pandkenmerkperpand'),(18,'panden','type'),(6,'sessions','session'),(24,'talen','label'),(25,'talen','taalcode'),(26,'talen','taalcodeperlabel');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2016-04-21 09:58:00'),(2,'auth','0001_initial','2016-04-21 09:58:00'),(3,'admin','0001_initial','2016-04-21 09:58:00'),(4,'admin','0002_logentry_remove_auto_add','2016-04-21 09:58:01'),(5,'contenttypes','0002_remove_content_type_name','2016-04-21 09:58:01'),(6,'auth','0002_alter_permission_name_max_length','2016-04-21 09:58:01'),(7,'auth','0003_alter_user_email_max_length','2016-04-21 09:58:01'),(8,'auth','0004_alter_user_username_opts','2016-04-21 09:58:01'),(9,'auth','0005_alter_user_last_login_null','2016-04-21 09:58:02'),(10,'auth','0006_require_contenttypes_0002','2016-04-21 09:58:02'),(11,'auth','0007_alter_validators_add_error_messages','2016-04-21 09:58:02'),(12,'gebruikers','0001_initial','2016-04-21 09:58:03'),(13,'panden','0001_initial','2016-04-21 09:58:04'),(14,'dossiers','0001_initial','2016-04-21 09:58:05'),(15,'panden','0002_pand_kenmerken','2016-04-21 09:58:05'),(16,'sessions','0001_initial','2016-04-21 09:58:05'),(17,'talen','0001_initial','2016-04-21 09:58:05'),(18,'gebruikers','0002_auto_20160421_1350','2016-04-21 11:50:52'),(19,'panden','0003_auto_20160421_1400','2016-04-21 12:00:17'),(20,'dossiers','0002_auto_20160421_1426','2016-04-21 12:26:18'),(21,'gebruikers','0003_auto_20160421_1426','2016-04-21 12:26:19'),(22,'talen','0002_auto_20160421_1426','2016-04-21 12:26:19'),(23,'dossiers','0003_auto_20160422_1334','2016-04-22 11:34:24'),(24,'gebruikers','0004_auto_20160422_1334','2016-04-22 11:34:25'),(25,'panden','0004_auto_20160422_1334','2016-04-22 11:34:25'),(26,'gebruikers','0005_auto_20160422_1347','2016-04-22 11:47:20'),(27,'panden','0005_auto_20160422_1347','2016-04-22 11:47:21');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('96lzkn32tupduzbtinb6zj2v9pcavhv3','NzE4Zjg2YjI5OGY2MjBmOWYwNGUxMjZiNGIyZDkxMjE5YjExZWQxZjp7Il9hdXRoX3VzZXJfaGFzaCI6IjA2MDVjYzE4YTc0ODhjYTgwZDdlZDNlZDQ3NWVjZDE4OWYyOGMwZDYiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiI4In0=','2016-05-09 17:33:00'),('9hu5486fcym1rk3voi6ssaha9gh8h4a7','YzBlYjBjMDVhOTQyNjViNDEzM2M1MDQyYTkzODRiYTk3MzUyMjZhYTp7Il9hdXRoX3VzZXJfaGFzaCI6ImQyN2Y1NDc3MDQxMDM5ZGZiMDgxZTFmZjkyZjkyYTExYzIwNTYzNjUiLCJfYXV0aF91c2VyX2lkIjoiMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2016-05-09 13:07:42'),('9xt0ut2icxcoei087qkdxhabrgt6zu8s','ZDJmNjEyNDZhNzAyMjYzZTI0NzE0NThkNzQ1YTVkNGNlOTY3ZDNlNDp7Il9hdXRoX3VzZXJfaGFzaCI6ImQyN2Y1NDc3MDQxMDM5ZGZiMDgxZTFmZjkyZjkyYTExYzIwNTYzNjUiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2016-05-10 08:37:58'),('b7ewhfai4yjn6eni95p4eo7ea5gzu8gt','NjIzMmRjNzBlZDY2ZDExMWIxYTU2MTI5MTUzZDM5ZjdlNjQwMTNmNzp7Il9hdXRoX3VzZXJfaGFzaCI6ImVmNzNjNDc0ZjE4MGY2Mjg3NmI4ZGY3YTBlZTViOTIxMzFhY2UyMjQiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiI3In0=','2016-05-09 14:37:15'),('erh0z1q6f1yyjgx750ow6aoccawurz17','MzNhYmE0MDFmZTg0NTFjYmVkMDgyMzI5ZGE5NmY2ZWQzYTY0NTk2NTp7Il9hdXRoX3VzZXJfaGFzaCI6IjBhNTljZWI1YWIzOTI5MTVhYzlkMzQxNjVhMTdkYjc2ZThlNWFmODQiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiI2In0=','2016-05-09 11:04:32'),('f4imhaznifa6sajjhj1ahq6lhd3zs2xk','NzE4Zjg2YjI5OGY2MjBmOWYwNGUxMjZiNGIyZDkxMjE5YjExZWQxZjp7Il9hdXRoX3VzZXJfaGFzaCI6IjA2MDVjYzE4YTc0ODhjYTgwZDdlZDNlZDQ3NWVjZDE4OWYyOGMwZDYiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiI4In0=','2016-05-09 17:08:39'),('gxvu7hgezj32419qsm75up803uegmazj','YzNkMGE4MDBkNGIzNTQ4YzQ1ZGVlNDE0YWRhYjdlN2Y0MDdiMDI1MDp7Il9hdXRoX3VzZXJfaGFzaCI6IjQ1OTg3MmU4ZWRiMDVkZGM1NTMyNDkzYzhlYTRkZWE3NjZhMzUwNmIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIzIn0=','2016-05-09 13:13:28'),('i6k8b3o5p3101zbj5kjnuatr5jacbdkc','YzNkMGE4MDBkNGIzNTQ4YzQ1ZGVlNDE0YWRhYjdlN2Y0MDdiMDI1MDp7Il9hdXRoX3VzZXJfaGFzaCI6IjQ1OTg3MmU4ZWRiMDVkZGM1NTMyNDkzYzhlYTRkZWE3NjZhMzUwNmIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIzIn0=','2016-05-09 13:34:16'),('iewmsnhxbndu2rma7m3abr4qhqsliqlo','NjIzMmRjNzBlZDY2ZDExMWIxYTU2MTI5MTUzZDM5ZjdlNjQwMTNmNzp7Il9hdXRoX3VzZXJfaGFzaCI6ImVmNzNjNDc0ZjE4MGY2Mjg3NmI4ZGY3YTBlZTViOTIxMzFhY2UyMjQiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiI3In0=','2016-05-09 14:35:00'),('ilpcgapdewbhssbmyttfx3i0imkwjtmv','NzE4Zjg2YjI5OGY2MjBmOWYwNGUxMjZiNGIyZDkxMjE5YjExZWQxZjp7Il9hdXRoX3VzZXJfaGFzaCI6IjA2MDVjYzE4YTc0ODhjYTgwZDdlZDNlZDQ3NWVjZDE4OWYyOGMwZDYiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiI4In0=','2016-05-09 16:01:16'),('l1zo1kokmw9zwhbrw1nys3zbje4msddo','NzE4Zjg2YjI5OGY2MjBmOWYwNGUxMjZiNGIyZDkxMjE5YjExZWQxZjp7Il9hdXRoX3VzZXJfaGFzaCI6IjA2MDVjYzE4YTc0ODhjYTgwZDdlZDNlZDQ3NWVjZDE4OWYyOGMwZDYiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiI4In0=','2016-05-09 16:14:17'),('noifsfvuvv7h3c0zuo5mybas3fwjpb79','NjIzMmRjNzBlZDY2ZDExMWIxYTU2MTI5MTUzZDM5ZjdlNjQwMTNmNzp7Il9hdXRoX3VzZXJfaGFzaCI6ImVmNzNjNDc0ZjE4MGY2Mjg3NmI4ZGY3YTBlZTViOTIxMzFhY2UyMjQiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiI3In0=','2016-05-09 14:35:20'),('p2f70vxannyi881x8y212o53b77yv8ha','NzE4Zjg2YjI5OGY2MjBmOWYwNGUxMjZiNGIyZDkxMjE5YjExZWQxZjp7Il9hdXRoX3VzZXJfaGFzaCI6IjA2MDVjYzE4YTc0ODhjYTgwZDdlZDNlZDQ3NWVjZDE4OWYyOGMwZDYiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiI4In0=','2016-05-09 15:51:23'),('t9pku2ywd6qt5gu3jakwu6zlq0vwnxof','NjIzMmRjNzBlZDY2ZDExMWIxYTU2MTI5MTUzZDM5ZjdlNjQwMTNmNzp7Il9hdXRoX3VzZXJfaGFzaCI6ImVmNzNjNDc0ZjE4MGY2Mjg3NmI4ZGY3YTBlZTViOTIxMzFhY2UyMjQiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiI3In0=','2016-05-09 14:35:23'),('uhv3q5jglwbw7ml7sefgciesupyipuxy','MzNhYmE0MDFmZTg0NTFjYmVkMDgyMzI5ZGE5NmY2ZWQzYTY0NTk2NTp7Il9hdXRoX3VzZXJfaGFzaCI6IjBhNTljZWI1YWIzOTI5MTVhYzlkMzQxNjVhMTdkYjc2ZThlNWFmODQiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiI2In0=','2016-05-09 13:29:04');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `dossiers_dossier`
--

LOCK TABLES `dossiers_dossier` WRITE;
/*!40000 ALTER TABLE `dossiers_dossier` DISABLE KEYS */;
INSERT INTO `dossiers_dossier` VALUES (1,1),(4,3),(8,4),(9,5),(7,6),(2,7),(10,8),(5,10),(6,11);
/*!40000 ALTER TABLE `dossiers_dossier` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `dossiers_dossierdocbeschrijving`
--

LOCK TABLES `dossiers_dossierdocbeschrijving` WRITE;
/*!40000 ALTER TABLE `dossiers_dossierdocbeschrijving` DISABLE KEYS */;
INSERT INTO `dossiers_dossierdocbeschrijving` VALUES (2,'Dit is de dossierbeschrijving van het testdossier');
/*!40000 ALTER TABLE `dossiers_dossierdocbeschrijving` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `dossiers_dossierdoclijn`
--

LOCK TABLES `dossiers_dossierdoclijn` WRITE;
/*!40000 ALTER TABLE `dossiers_dossierdoclijn` DISABLE KEYS */;
/*!40000 ALTER TABLE `dossiers_dossierdoclijn` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `dossiers_dossierdocstatus`
--

LOCK TABLES `dossiers_dossierdocstatus` WRITE;
/*!40000 ALTER TABLE `dossiers_dossierdocstatus` DISABLE KEYS */;
INSERT INTO `dossiers_dossierdocstatus` VALUES (1),(2),(3),(4),(5),(6),(7),(8),(9),(10);
/*!40000 ALTER TABLE `dossiers_dossierdocstatus` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `dossiers_stavaza`
--

LOCK TABLES `dossiers_stavaza` WRITE;
/*!40000 ALTER TABLE `dossiers_stavaza` DISABLE KEYS */;
INSERT INTO `dossiers_stavaza` VALUES (1,'Dit pand is te koop'),(2,'Dit pand is verkocht'),(3,'Dit pand is verhuurd'),(4,'Dit pand is te huur'),(5,'Er wordt nog onderhandeld over dit pand'),(6,'Dit pand is momenteel onbeschikbaar'),(7,'Dit pand is momenteel in onderhoud'),(8,'Dit pand is momenteel ongeschikt voor gebuik');
/*!40000 ALTER TABLE `dossiers_stavaza` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `dossiers_stavazalijn`
--

LOCK TABLES `dossiers_stavazalijn` WRITE;
/*!40000 ALTER TABLE `dossiers_stavazalijn` DISABLE KEYS */;
INSERT INTO `dossiers_stavazalijn` VALUES (1,1,1),(3,4,3),(4,8,7),(5,9,4),(6,7,8),(7,2,5),(8,5,6),(9,6,2);
/*!40000 ALTER TABLE `dossiers_stavazalijn` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `gebruikers_adres`
--

LOCK TABLES `gebruikers_adres` WRITE;
/*!40000 ALTER TABLE `gebruikers_adres` DISABLE KEYS */;
INSERT INTO `gebruikers_adres` VALUES (1,'Teststraat','45','1000','Brussel',1),(3,'Italiëlei','14','2000','Antwerpen',1),(4,'Meistraat','3','2000','Antwerpen',1),(5,'Elf-Novemberstraat','69','2910','Essen',1),(6,'Gegevensstraat','1','2000','Analyse',1),(7,'Tjoeplaan','420','2900','Schoten',1),(9,'Hypothesestraat','13','3928','Pompernikkel',1),(10,'Aardbeienlaan','12','9120','Melsele',1),(11,'Memestreet','5/7','420','Doge',5),(12,'Targaryenstraat','12','2070','Zwijndrecht',1),(13,'Dertienstraat','13','1313','Dertienwerpen',1),(14,'Schelpstraat 120','38','1970','Bikinibroek',2),(15,'Klapperstraat','12','9100','Sint-Niklaas',1),(16,'Panamarenkolaan','23','3050','Kruibeke',1),(17,'Sagdievstraat','123','5010','boratyurt',15),(18,'boeddhistenstraat','56','2090','Isos',7),(19,'Renemagrittelaan','44','5080','Vladslo',1),(20,'Ulitsa dictatorskaja','666','1945','Stalinskaja',13),(21,'Lenin Pidaraz','56','3069','Stalinskaja',13),(22,'Zonderhaatstraat','101','9010','Antwerpen',1),(23,'Zoisnatuurlaan','99','6030','Brabant',2),(24,'Nietmeerdoenstraat','80','5040','Helemaalmooi',2),(25,'Honderdeurolaan','100','1010','Brabant',2),(26,'Johnsnowisdoodstraat','1','2020','Westeros',6),(27,'Namek','9000','9000','Maima region',13),(28,'Vegeta','8999','8999','Vegeta',21);
/*!40000 ALTER TABLE `gebruikers_adres` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `gebruikers_gebruiker`
--

LOCK TABLES `gebruikers_gebruiker` WRITE;
/*!40000 ALTER TABLE `gebruikers_gebruiker` DISABLE KEYS */;
INSERT INTO `gebruikers_gebruiker` VALUES (1,'0484848484',1,5),(2,'0484848484',1,2),(3,'0484848484',1,1),(4,'0484848484',1,4),(5,'0484848484',1,3),(6,'0484848484',1,6),(7,'Ge hebt er geen jong',1,7),(8,'Ge hebt er geen begot :o',1,8),(9,'+32472208465',4,9),(10,'+32472923847',6,10),(11,'+32478736492',9,11),(12,'+32494781355',10,12),(13,'+3263739100',7,13),(14,'+32472938263',5,14),(15,'+3238464627',11,15),(17,'+32435654533',12,17),(18,'+32474352644',14,18),(19,'+32491529199',15,19),(20,'0486548741',17,20),(21,'0465223147',17,21),(22,'0471226987',16,22),(23,'0456987123',19,23),(24,'0489663214',18,24),(25,'0483287483',27,25),(26,'0487552123',12,26),(27,'0478512698',10,27),(28,'0455645865',28,28);
/*!40000 ALTER TABLE `gebruikers_gebruiker` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `gebruikers_land`
--

LOCK TABLES `gebruikers_land` WRITE;
/*!40000 ALTER TABLE `gebruikers_land` DISABLE KEYS */;
INSERT INTO `gebruikers_land` VALUES (1,'België','BE'),(2,'Nederland','NL'),(3,'Duitsland','DE'),(4,'Frankrijk','FR'),(5,'Verenigd Koningkrijk','GB'),(6,'Luxemburg','LU'),(7,'Denemarken','DK'),(8,'Griekenland','GR'),(9,'Italië','IT'),(10,'Ierland','IE'),(11,'Zweden','SE'),(12,'Noorwegen','NO'),(13,'Polen','PL'),(14,'Spanje','ES'),(15,'Tsjechië','CZ'),(16,'Zwitserland','CH'),(17,'Oostenrijk','AT'),(18,'Portugal','PT'),(20,'Kroatië','HR'),(21,'Servië','RS');
/*!40000 ALTER TABLE `gebruikers_land` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `panden_foto`
--

LOCK TABLES `panden_foto` WRITE;
/*!40000 ALTER TABLE `panden_foto` DISABLE KEYS */;
INSERT INTO `panden_foto` VALUES (2,1,'./maxresdefault.jpg'),(3,3,'./SpongeBobs_pineapple_house_in_Season_4-7.png'),(4,4,'./article-0-05A476E30000044D-741_468x286.jpg'),(5,5,'./PabloEscobar.jpg'),(6,7,'./boomhut-2.jpg'),(7,8,'./PentHouse.jpg'),(8,6,'./villa_vistaibizai_javea.jpg'),(9,9,'./1.jpg'),(10,11,'./Bungalow.jpg'),(11,10,'./Duplex.jpg');
/*!40000 ALTER TABLE `panden_foto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `panden_kenmerk`
--

LOCK TABLES `panden_kenmerk` WRITE;
/*!40000 ALTER TABLE `panden_kenmerk` DISABLE KEYS */;
INSERT INTO `panden_kenmerk` VALUES (1,'Aantal verdiepingen'),(2,'Aantal badkamers'),(3,'Verdieping'),(4,'Aantal kamers'),(5,'Aantal keukens'),(6,'Aantal parkeerplaatsen'),(7,'Oppervlakte tuin'),(8,'Garage'),(9,'Berging'),(10,'Zolder'),(11,'Zwembad'),(12,'Oppervlakte terras');
/*!40000 ALTER TABLE `panden_kenmerk` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `panden_pand`
--

LOCK TABLES `panden_pand` WRITE;
/*!40000 ALTER TABLE `panden_pand` DISABLE KEYS */;
INSERT INTO `panden_pand` VALUES (1,100000,'1996-01-01',125,'test',1,1,1),(3,749000,'2003-01-04',94,'Prachtige spongebob mansion, gelegen diep in de zee. Weinig onderhoud vereist.\r\n\r\nLet op: dit huis is enkel bereikbaar met een onderzeeër.',14,18,1),(4,780000,'2009-11-03',100,'Het is een rustige plaats met wat joden in de buurt maar daar moet je geen zorgen maken.\r\nEr zijn genoeg wapenwinkels in de buurt om ze overhoop te schieten.',17,20,7),(5,3000000,'2001-09-11',150,'Wil je leven als drugsbaron, dan ben je welkom op zoisnatuurlaan. Hier kun je gang gaan zonder zorgen.\r\nanders kun je kiezen tussen plata o plomo.',23,22,7),(6,250000,'2002-04-09',2610,'Zeer mooie villa aan een zeer scherpe prijs. Ideaal voor leuke praktijken.',7,13,7),(7,1000,'2008-04-13',25,'mooie huis op een boom omdat het kan. Alleen mensen die niet veel geld hebben kunnen dit wel betalen.\r\nBoomhut op een mooie eikenboom is het geld waard.',18,26,21),(8,4000000,'2002-05-18',50,'Als je een mens bent die van programmeren houdt maar die geen les kan geven aan de klas, dan is dit plek ideaal voor u om je zelf op te hangen. Er zijn namelijk bomen in de buurt die het mogelijk maken.',24,11,18),(9,20000,'2005-07-24',30,'Leuke huis voor vreemden. \r\nIdeaal voor koppels die graag vreemd gaan.',19,19,1),(10,850000,'2006-11-16',90,'Mooie duplex appartement, heeft een 2 hectare wildernis. Zeer goed om te gaan vechten.\r\nHet appartement bevat een cooking en een mining plaats. Heeft een zeer grote garage voor smithing.',15,24,8),(11,850,'2016-04-25',15,'Bungalow in goede staat, Veel is er niet maar dat maakt helemaal niet uit.',13,15,16);
/*!40000 ALTER TABLE `panden_pand` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `panden_pandimmolink`
--

LOCK TABLES `panden_pandimmolink` WRITE;
/*!40000 ALTER TABLE `panden_pandimmolink` DISABLE KEYS */;
INSERT INTO `panden_pandimmolink` VALUES (1,'Immovlan','http://immo.vlan.be/nl/bikinibroekspongebob',3),(2,'Verynice','http://veryNice.kz/be/ThisSuitIsBlacknot',4),(3,'Narcos','http://EmilioBar.be/EscobarGaviria',5);
/*!40000 ALTER TABLE `panden_pandimmolink` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `panden_pandkenmerkperpand`
--

LOCK TABLES `panden_pandkenmerkperpand` WRITE;
/*!40000 ALTER TABLE `panden_pandkenmerkperpand` DISABLE KEYS */;
INSERT INTO `panden_pandkenmerkperpand` VALUES (1,3,4,3),(2,2,1,3),(3,2,2,4),(4,3,1,4),(5,2,8,4),(6,1,11,4),(7,14,4,4),(8,1,10,4),(9,2,5,4),(10,10,4,6),(11,2,5,6),(12,2,2,6),(13,0,1,11);
/*!40000 ALTER TABLE `panden_pandkenmerkperpand` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `panden_type`
--

LOCK TABLES `panden_type` WRITE;
/*!40000 ALTER TABLE `panden_type` DISABLE KEYS */;
INSERT INTO `panden_type` VALUES (1,'Huis'),(2,'Appartement'),(3,'Gesloten bebouwing'),(4,'Halfopen bebouwing'),(5,'Loft'),(6,'Caravan'),(7,'Villa'),(8,'Duplex appartement'),(10,'Kot'),(11,'Landhuis'),(12,'Vrijstaande woning'),(13,'Rijtjeswoning of tussenwoning'),(14,'Drive-in-woning'),(15,'Schakelwoning'),(16,'Bungalow'),(17,'Grachtenpand / herenhuis'),(18,'Penthouse'),(19,'Maisonettes'),(20,'Etagewoning'),(21,'Boomhut');
/*!40000 ALTER TABLE `panden_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `talen_label`
--

LOCK TABLES `talen_label` WRITE;
/*!40000 ALTER TABLE `talen_label` DISABLE KEYS */;
/*!40000 ALTER TABLE `talen_label` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `talen_taalcode`
--

LOCK TABLES `talen_taalcode` WRITE;
/*!40000 ALTER TABLE `talen_taalcode` DISABLE KEYS */;
INSERT INTO `talen_taalcode` VALUES (1,'NL'),(2,'FR'),(3,'EN');
/*!40000 ALTER TABLE `talen_taalcode` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `talen_taalcodeperlabel`
--

LOCK TABLES `talen_taalcodeperlabel` WRITE;
/*!40000 ALTER TABLE `talen_taalcodeperlabel` DISABLE KEYS */;
/*!40000 ALTER TABLE `talen_taalcodeperlabel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'viasofie'
--

--
-- Dumping routines for database 'viasofie'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-04-26 10:51:52
