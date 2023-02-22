CREATE DATABASE  IF NOT EXISTS `rz_seed_shop` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `rz_seed_shop`;
-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: localhost    Database: rz_seed_shop
-- ------------------------------------------------------
-- Server version	8.0.31

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
-- Table structure for table `admins`
--

DROP TABLE IF EXISTS `admins`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admins` (
  `id` varchar(50) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `last_name` varchar(100) DEFAULT NULL,
  `user_id` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admins`
--

LOCK TABLES `admins` WRITE;
/*!40000 ALTER TABLE `admins` DISABLE KEYS */;
INSERT INTO `admins` VALUES ('66496d8c-4cd2-4bac-a879-cc1c33ffb55c','admin1','admin1','85ca074b-8d9f-4543-ac21-c4c957df4c0c');
/*!40000 ALTER TABLE `admins` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `carts`
--

DROP TABLE IF EXISTS `carts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `carts` (
  `id` varchar(50) NOT NULL,
  `created_at` date NOT NULL,
  `status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `carts`
--

LOCK TABLES `carts` WRITE;
/*!40000 ALTER TABLE `carts` DISABLE KEYS */;
INSERT INTO `carts` VALUES ('a1a071ff-37a3-4e4a-8b24-1be284837242','2023-02-22','processed'),('5b7aa517-3c81-4cc8-8319-b2c55a2f35cb','2023-02-22','processed'),('f3e226cc-a52a-4570-8d45-f9ca5e14b1f4','2023-02-22','processed'),('f7bdeee6-8cf7-46a3-9ff4-517c842d091f','2023-02-22','pending'),('e83190b9-6889-47ef-87dd-b6b6057c79b5','2023-02-22','pending');
/*!40000 ALTER TABLE `carts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `completed_orders`
--

DROP TABLE IF EXISTS `completed_orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `completed_orders` (
  `id` varchar(50) NOT NULL,
  `order_date` date DEFAULT NULL,
  `order_value` float NOT NULL,
  `discount` tinyint(1) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  `cart_id` varchar(50) NOT NULL,
  `customer_id` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `cart_id` (`cart_id`),
  KEY `customer_id` (`customer_id`),
  CONSTRAINT `check_order_value` CHECK ((`order_value` >= 0))
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `completed_orders`
--

LOCK TABLES `completed_orders` WRITE;
/*!40000 ALTER TABLE `completed_orders` DISABLE KEYS */;
INSERT INTO `completed_orders` VALUES ('66f0b6a2-25b5-4f71-9e9e-f22f092e0fa9','2023-02-22',14400,1,'finalized','a1a071ff-37a3-4e4a-8b24-1be284837242','77bf13d2-47c9-4232-8e2d-ac747fbbea04'),('33f66161-4900-4659-90e6-e1a07e780f44','2023-02-22',54000,1,'pending','5b7aa517-3c81-4cc8-8319-b2c55a2f35cb','5bca477d-6f5a-43f4-9203-f34cd5ff9f9a'),('66c583d1-39e8-4304-8e5f-01cd9fdf8dd3','2023-02-22',7500,0,'pending','f3e226cc-a52a-4570-8d45-f9ca5e14b1f4','407d9833-34c9-4b42-ae4b-eab6be2c4eef');
/*!40000 ALTER TABLE `completed_orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `courses`
--

DROP TABLE IF EXISTS `courses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `courses` (
  `id` varchar(50) NOT NULL,
  `code` varchar(100) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `description` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `code` (`code`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `courses`
--

LOCK TABLES `courses` WRITE;
/*!40000 ALTER TABLE `courses` DISABLE KEYS */;
/*!40000 ALTER TABLE `courses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customers`
--

DROP TABLE IF EXISTS `customers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customers` (
  `id` varchar(50) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `last_name` varchar(100) DEFAULT NULL,
  `address` varchar(150) DEFAULT NULL,
  `district` varchar(100) DEFAULT NULL,
  `telephone_number` varchar(100) DEFAULT NULL,
  `key_customer` tinyint(1) DEFAULT NULL,
  `newsletter_subscription` tinyint(1) DEFAULT NULL,
  `user_id` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customers`
--

LOCK TABLES `customers` WRITE;
/*!40000 ALTER TABLE `customers` DISABLE KEYS */;
INSERT INTO `customers` VALUES ('77bf13d2-47c9-4232-8e2d-ac747fbbea04','name2','last_name2','address2','district2','string2',0,0,'39e51a04-f29f-4a2c-9caa-8ee941a7416e'),('5bca477d-6f5a-43f4-9203-f34cd5ff9f9a','name3','last_name3','address3','district3','string3',0,0,'5b10ed3a-080a-40b7-bb92-8e9f59075e5e'),('407d9833-34c9-4b42-ae4b-eab6be2c4eef','name4','last_name4','address4','district1','string4',0,0,'d6d8420d-ad6b-41f2-8db8-a863ba37d426'),('d49b396a-75db-4fc0-89f2-807da3482048','name5','last_name5','address5','district2','string5',0,0,'34f9577b-09c0-4212-9566-bfb5dbec45aa'),('17d088fb-ed13-4441-bcc5-7e5c96491de0','name6','last_name6','address6','district1','string6',0,0,'70840685-bc6b-4323-9f96-500565f72a0f');
/*!40000 ALTER TABLE `customers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product_orders`
--

DROP TABLE IF EXISTS `product_orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product_orders` (
  `id` varchar(50) NOT NULL,
  `quantity` int NOT NULL,
  `variety_id` varchar(50) NOT NULL,
  `cart_id` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `variety_id` (`variety_id`),
  KEY `cart_id` (`cart_id`),
  CONSTRAINT `check_quantity` CHECK ((`quantity` > 0))
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product_orders`
--

LOCK TABLES `product_orders` WRITE;
/*!40000 ALTER TABLE `product_orders` DISABLE KEYS */;
INSERT INTO `product_orders` VALUES ('05a9f9ae-d91f-4373-801d-adc8214c3f5d',10,'93ddfe7e-c1b8-4a6d-9c12-4b55f5c088cb','a1a071ff-37a3-4e4a-8b24-1be284837242'),('9a50ea94-0d59-4470-8697-457adcd0edce',15,'5001ed34-2402-4fc8-94d8-5e8cff9dd7c1','a1a071ff-37a3-4e4a-8b24-1be284837242'),('6a6226c0-c7e3-49e0-adb7-c08483289316',30,'bc855e8f-9f1c-408c-a99b-38b2daa5cdcf','5b7aa517-3c81-4cc8-8319-b2c55a2f35cb'),('3e727056-616c-4377-8f67-20f092166dae',15,'e1e6fd84-9711-4f9e-a01a-6d605b7646e4','5b7aa517-3c81-4cc8-8319-b2c55a2f35cb'),('5c716aa3-0005-4e9f-9025-391c807c8f5d',15,'d1752036-31fe-4716-8c9c-78b7b71e294e','5b7aa517-3c81-4cc8-8319-b2c55a2f35cb'),('5f3b4851-a97b-48a0-8f0a-14eb2ba93ab3',25,'34f85844-f6cd-4919-a0ee-884eaa7f365c','5b7aa517-3c81-4cc8-8319-b2c55a2f35cb'),('537e6008-f5c5-4df7-b235-71263eaa7ec2',50,'bc855e8f-9f1c-408c-a99b-38b2daa5cdcf','f3e226cc-a52a-4570-8d45-f9ca5e14b1f4');
/*!40000 ALTER TABLE `product_orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shipments`
--

DROP TABLE IF EXISTS `shipments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `shipments` (
  `id` varchar(50) NOT NULL,
  `status` varchar(100) NOT NULL,
  `shipment_name` varchar(100) NOT NULL,
  `shipment_last_name` varchar(100) NOT NULL,
  `shipment_address` varchar(150) NOT NULL,
  `shipment_district` varchar(100) NOT NULL,
  `shipment_telephone_number` varchar(100) NOT NULL,
  `completed_order_id` varchar(50) DEFAULT NULL,
  `customer_id` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `completed_order_id` (`completed_order_id`),
  KEY `customer_id` (`customer_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shipments`
--

LOCK TABLES `shipments` WRITE;
/*!40000 ALTER TABLE `shipments` DISABLE KEYS */;
INSERT INTO `shipments` VALUES ('c979c088-344d-4864-9fc1-5586b190ba1e','pending','name2','last_name2','address2','district2','string2','66f0b6a2-25b5-4f71-9e9e-f22f092e0fa9','77bf13d2-47c9-4232-8e2d-ac747fbbea04');
/*!40000 ALTER TABLE `shipments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` varchar(50) NOT NULL,
  `email` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `is_active` tinyint(1) DEFAULT NULL,
  `is_superuser` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES ('85ca074b-8d9f-4543-ac21-c4c957df4c0c','user@example1.com','string1',1,1),('39e51a04-f29f-4a2c-9caa-8ee941a7416e','user@example2.com','string2',1,0),('5b10ed3a-080a-40b7-bb92-8e9f59075e5e','user@example3.com','string3',1,0),('d6d8420d-ad6b-41f2-8db8-a863ba37d426','user@example4.com','string4',1,0),('34f9577b-09c0-4212-9566-bfb5dbec45aa','user@example5.com','string5',1,0),('70840685-bc6b-4323-9f96-500565f72a0f','user@example6.com','string6',1,0);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `variety_products`
--

DROP TABLE IF EXISTS `variety_products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `variety_products` (
  `id` varchar(50) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `crop` varchar(100) DEFAULT NULL,
  `price` float DEFAULT NULL,
  `package_size` varchar(100) DEFAULT NULL,
  `stock` int DEFAULT NULL,
  `added_to_inventory` date DEFAULT NULL,
  `on_discount` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name_price_uc` (`name`,`price`),
  CONSTRAINT `check_price` CHECK ((`price` >= 0)),
  CONSTRAINT `check_stock` CHECK ((`stock` >= 0))
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `variety_products`
--

LOCK TABLES `variety_products` WRITE;
/*!40000 ALTER TABLE `variety_products` DISABLE KEYS */;
INSERT INTO `variety_products` VALUES ('93ddfe7e-c1b8-4a6d-9c12-4b55f5c088cb','variety1','crop1',100,'100s',975,'2022-02-22',0),('5001ed34-2402-4fc8-94d8-5e8cff9dd7c1','variety2','crop1',1000,'1000s',990,'2022-02-22',0),('bc855e8f-9f1c-408c-a99b-38b2daa5cdcf','variety3','crop2',150,'100s',1000,'2022-12-22',0),('e1e6fd84-9711-4f9e-a01a-6d605b7646e4','variety4','crop2',1500,'1000s',1000,'2023-01-22',0),('d1752036-31fe-4716-8c9c-78b7b71e294e','variety5','crop3',200,'2500s',1000,'2023-02-22',0),('34f85844-f6cd-4919-a0ee-884eaa7f365c','variety7','crop3',3000,'1000s',1000,'2023-02-22',0);
/*!40000 ALTER TABLE `variety_products` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `variety_traits`
--

DROP TABLE IF EXISTS `variety_traits`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `variety_traits` (
  `id` varchar(50) NOT NULL,
  `open_field` tinyint(1) DEFAULT NULL,
  `indoor` tinyint(1) DEFAULT NULL,
  `fresh_market` tinyint(1) DEFAULT NULL,
  `industry` tinyint(1) DEFAULT NULL,
  `fruit_size_g` int DEFAULT NULL,
  `fruit_size_kg` float DEFAULT NULL,
  `maturity_days` int DEFAULT NULL,
  `spring_production` tinyint(1) DEFAULT NULL,
  `summer_production` tinyint(1) DEFAULT NULL,
  `autumn_production` tinyint(1) DEFAULT NULL,
  `winter_production` tinyint(1) DEFAULT NULL,
  `product_id` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `product_id` (`product_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `variety_traits`
--

LOCK TABLES `variety_traits` WRITE;
/*!40000 ALTER TABLE `variety_traits` DISABLE KEYS */;
INSERT INTO `variety_traits` VALUES ('f6a25200-83ba-4b07-9206-2dab21ba3057',1,1,1,1,100,0.1,50,1,1,1,1,'93ddfe7e-c1b8-4a6d-9c12-4b55f5c088cb'),('d9dacb1a-3184-48af-9ca0-a723fad97c6b',1,0,1,0,150,1.5,55,1,1,1,1,'5001ed34-2402-4fc8-94d8-5e8cff9dd7c1'),('850f6e89-48db-467a-804a-40188c4281a0',1,0,1,0,200,2,60,1,1,1,1,'bc855e8f-9f1c-408c-a99b-38b2daa5cdcf'),('f0aed837-4c2b-48d7-91a0-2b3d539b8a9f',1,0,1,0,200,2,60,1,1,1,1,'e1e6fd84-9711-4f9e-a01a-6d605b7646e4'),('1a9ae18a-d9d6-4ff2-97d1-ace76bf2e7ef',1,0,1,0,200,0.2,65,1,1,1,1,'d1752036-31fe-4716-8c9c-78b7b71e294e'),('76b25f77-ccb5-412d-8892-afce97b035df',1,1,1,1,2000,2,90,1,1,1,1,'34f85844-f6cd-4919-a0ee-884eaa7f365c');
/*!40000 ALTER TABLE `variety_traits` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-02-22 16:59:22
