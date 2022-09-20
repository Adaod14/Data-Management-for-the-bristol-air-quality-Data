-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 13, 2022 at 06:20 PM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.1.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pollution-db`
--

-- Table structure for table `schema`
--

CREATE TABLE `schema_table` (
  `schema_id` int NOT NULL,
  `Measure` varchar(90) NOT NULL,
  `unit` varchar(90) NOT NULL,
  `Description` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `sites`
--

CREATE TABLE `sites` (
  `Location` varchar(90) NOT NULL,
  `Site_id` int NOT NULL,
  `geo_point` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
--
-- --------------------------------------------------------
-- Table structure for table `readings`
--

CREATE TABLE `readings` (
  `reading_id` int NOT NULL,
  `Site_id` int NOT NULL,
  `Date_time` varchar(90) NOT NULL,
  `NO` float NOT NULL,
  `NOx` float NOT NULL,
  `NO2` float NOT NULL,
  `PM10` float NOT NULL,
  `NVPM10` float NOT NULL,
  `VPM10` float NOT NULL,
  `PM2.5` float NOT NULL,
  `NVPM2.5` float NOT NULL,
  `VPM2.5` float NOT NULL,
  `CO` float NOT NULL,
  `O3` float NOT NULL,
  `SO2` float NOT NULL,
  `Temperature` varchar(90) NOT NULL,
  `RH` varchar(90) NOT NULL,
  `Air_pressure` varchar(90) NOT NULL,
  `date_start` varchar(90) NOT NULL,
  `date_end` varchar(90) NOT NULL,
  `current` float NOT NULL,
  `instrument` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--

--
-- Indexes for dumped tables
--

--
-- Indexes for table `readings`
--
ALTER TABLE `readings`
  ADD PRIMARY KEY (`reading_id`),
  ADD KEY `reading_id` (`reading_id`);

--
-- Indexes for table `schema`
--
ALTER TABLE `schema`
  ADD PRIMARY KEY (`schema_id`);

--
-- Indexes for table `sites`
--
ALTER TABLE `sites`
  ADD PRIMARY KEY (`Site_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
