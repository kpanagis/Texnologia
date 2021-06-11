-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 10, 2021 at 11:45 PM
-- Server version: 10.4.17-MariaDB
-- PHP Version: 8.0.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `texnologia_xrhstes`
--

-- --------------------------------------------------------

--
-- Table structure for table `parking spots`
--

CREATE TABLE `parking spots` (
  `Spot Id` int(11) NOT NULL,
  `Spot History` varchar(255) NOT NULL,
  `Spot Class` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `Username` varchar(255) NOT NULL,
  `User e-mail` varchar(255) NOT NULL,
  `User Password` varchar(255) NOT NULL,
  `User Phone Number` int(10) NOT NULL,
  `Users History` varchar(255) NOT NULL,
  `Users Class` varchar(255) NOT NULL
  `Users card_id` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `user vehicle`
--

CREATE TABLE `user vehicle` (
  `Username` varchar(255) NOT NULL,
  `Vehicle Model` varchar(255) NOT NULL,
  `Vehicle Plates` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `parking spots`
--
ALTER TABLE `parking spots`
  ADD PRIMARY KEY (`Spot Id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`Username`);
ALTER TABLE `users` ADD FULLTEXT KEY `Username` (`Username`);

--
-- Indexes for table `user vehicle`
--
ALTER TABLE `user vehicle`
  ADD PRIMARY KEY (`Username`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
