/*
SQLyog Community v13.0.1 (64 bit)
MySQL - 5.1.32-community : Database - bug_tracking
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`bug_tracking` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `bug_tracking`;

/*Table structure for table `buglogin` */

DROP TABLE IF EXISTS `buglogin`;

CREATE TABLE `buglogin` (
  `loginid` int(10) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `usertype` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`loginid`)
) ENGINE=InnoDB AUTO_INCREMENT=46 DEFAULT CHARSET=latin1;

/*Data for the table `buglogin` */

insert  into `buglogin`(`loginid`,`username`,`password`,`usertype`) values 
(1,'admin','Admin@12','admin'),
(42,'anu','Anu@12','Developer'),
(43,'sudha','Su@12','Developer'),
(44,'raji','Raji@12','Tester'),
(45,'mohu','Mohu@12','Tester');

/*Table structure for table `developer_registration` */

DROP TABLE IF EXISTS `developer_registration`;

CREATE TABLE `developer_registration` (
  `developer_id` int(10) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(50) DEFAULT NULL,
  `last_name` varchar(50) DEFAULT NULL,
  `company_name` varchar(50) DEFAULT NULL,
  `location` varchar(50) DEFAULT NULL,
  `qualification` varchar(50) DEFAULT NULL,
  `skills` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `contact_number` bigint(10) DEFAULT NULL,
  `loginid` int(10) DEFAULT NULL,
  PRIMARY KEY (`developer_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `developer_registration` */

insert  into `developer_registration`(`developer_id`,`first_name`,`last_name`,`company_name`,`location`,`qualification`,`skills`,`email`,`contact_number`,`loginid`) values 
(7,'answara','p','qwert','qwer','msc','qwertgcx','an@gmail.com',9961105121,42),
(8,'sudha','p','fcvgb','fvgn','sdf','awsedfgvbh','su@gmail.com',9910512123,43);

/*Table structure for table `project_test_details` */

DROP TABLE IF EXISTS `project_test_details`;

CREATE TABLE `project_test_details` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `project_test_request_id` int(10) NOT NULL,
  `test_details` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

/*Data for the table `project_test_details` */

insert  into `project_test_details`(`id`,`project_test_request_id`,`test_details`) values 
(1,1,'ERRORS FIXED'),
(2,2,'its a new project'),
(3,3,'jjjj'),
(4,4,'nyc'),
(5,2,'asdfghjterty'),
(6,5,'errror free'),
(7,6,'pending templateadded'),
(8,7,'nyc'),
(9,8,'asedrftgy'),
(10,9,'asdfcgvb');

/*Table structure for table `project_test_request` */

DROP TABLE IF EXISTS `project_test_request`;

CREATE TABLE `project_test_request` (
  `project_test_request_id` int(10) NOT NULL AUTO_INCREMENT,
  `developer_id` int(10) DEFAULT NULL,
  `tester_id` int(10) DEFAULT NULL,
  `projecttype_id` varchar(10) DEFAULT NULL,
  `project_name` varchar(100) DEFAULT NULL,
  `project_description` varchar(50) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `request_status` varchar(50) DEFAULT 'pending',
  `project_test_status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`project_test_request_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

/*Data for the table `project_test_request` */

insert  into `project_test_request`(`project_test_request_id`,`developer_id`,`tester_id`,`projecttype_id`,`project_name`,`project_description`,`date`,`request_status`,`project_test_status`) values 
(9,43,44,'2','newproject','xcfgvbnm','2024-02-22','accepted','COMPLETED'),
(10,43,45,'1','thisproject','sdfghbnm','2024-02-02','accepted',NULL);

/*Table structure for table `project_type` */

DROP TABLE IF EXISTS `project_type`;

CREATE TABLE `project_type` (
  `projecttypeid` int(50) NOT NULL AUTO_INCREMENT,
  `project_type` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`projecttypeid`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `project_type` */

insert  into `project_type`(`projecttypeid`,`project_type`) values 
(1,'ANDROID'),
(2,'DESKTOP APPLICATION'),
(3,'WEB APPLICATION & ANDROID');

/*Table structure for table `tester_payment` */

DROP TABLE IF EXISTS `tester_payment`;

CREATE TABLE `tester_payment` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `testerid` int(10) DEFAULT NULL,
  `projecttypeid` int(50) DEFAULT NULL,
  `payment` int(10) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `tester_payment` */

insert  into `tester_payment`(`id`,`testerid`,`projecttypeid`,`payment`) values 
(1,44,2,50000),
(2,44,3,10000),
(3,45,1,30000);

/*Table structure for table `tester_registration` */

DROP TABLE IF EXISTS `tester_registration`;

CREATE TABLE `tester_registration` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(50) DEFAULT NULL,
  `last_name` varchar(50) DEFAULT NULL,
  `experience_level` varchar(50) DEFAULT NULL,
  `skill` varchar(50) DEFAULT NULL,
  `location` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `contact` bigint(10) DEFAULT NULL,
  `loginid` int(10) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;

/*Data for the table `tester_registration` */

insert  into `tester_registration`(`id`,`first_name`,`last_name`,`experience_level`,`skill`,`location`,`email`,`contact`,`loginid`) values 
(10,'rajin','k','Experienced','ASDFGH','CVBN','xcv',2345455,44),
(11,'mohandas','p','Intermediate','asdfcgvb','dfg','mohu@gmail.com',9946699457,45);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
