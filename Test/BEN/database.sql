-- phpMyAdmin SQL Dump
-- version 4.6.4
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Nov 17, 2016 at 09:49 AM
-- Server version: 5.6.28
-- PHP Version: 7.0.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

--
-- Database: `BibleRaspberyPI`
--

-- --------------------------------------------------------

--
-- Table structure for table `Book`
--

CREATE TABLE `Book` (
  `id` int(11) NOT NULL,
  `Name` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Book`
--

INSERT INTO `Book` (`id`, `Name`) VALUES
(1, 'Genesis'),
(2, 'Exodus'),
(3, 'Leviticus'),
(4, 'Numbers'),
(5, 'Deuteronomy'),
(6, 'Joshua');

-- --------------------------------------------------------

--
-- Table structure for table `content`
--

CREATE TABLE `content` (
  `id` int(11) NOT NULL,
  `Testament` int(11) NOT NULL,
  `Book` int(11) NOT NULL,
  `Chapter` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `content`
--

INSERT INTO `content` (`id`, `Testament`, `Book`, `Chapter`) VALUES
(1, 1, 1, 1),
(2, 1, 2, 2);

-- --------------------------------------------------------

--
-- Table structure for table `file`
--

CREATE TABLE `file` (
  `id` int(11) NOT NULL,
  `contentID` int(11) NOT NULL,
  `folder` varchar(50) NOT NULL,
  `fileName` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `file`
--

INSERT INTO `file` (`id`, `contentID`, `folder`, `fileName`) VALUES
(1, 1, 'Genesis', 'Genesis1.mp3'),
(2, 2, 'Genesis', 'Genesis2.mp3');

-- --------------------------------------------------------

--
-- Table structure for table `Testament`
--

CREATE TABLE `Testament` (
  `id` int(11) NOT NULL,
  `Name` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Testament`
--

INSERT INTO `Testament` (`id`, `Name`) VALUES
(1, 'New Testament'),
(2, 'Old Testament');

-- --------------------------------------------------------

--
-- Table structure for table `verse`
--

CREATE TABLE `verse` (
  `id` int(11) NOT NULL,
  `contentID` int(11) NOT NULL,
  `number` int(11) NOT NULL,
  `startSec` int(11) NOT NULL,
  `endSec` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `verse`
--

INSERT INTO `verse` (`id`, `contentID`, `number`, `startSec`, `endSec`) VALUES
(1, 1, 1, 1, 4),
(2, 1, 2, 5, 7);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Book`
--
ALTER TABLE `Book`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `content`
--
ALTER TABLE `content`
  ADD PRIMARY KEY (`id`),
  ADD KEY `Testament` (`Testament`),
  ADD KEY `Book` (`Book`);

--
-- Indexes for table `file`
--
ALTER TABLE `file`
  ADD PRIMARY KEY (`id`),
  ADD KEY `contentID` (`contentID`);

--
-- Indexes for table `Testament`
--
ALTER TABLE `Testament`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `verse`
--
ALTER TABLE `verse`
  ADD PRIMARY KEY (`id`),
  ADD KEY `contentID` (`contentID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `Book`
--
ALTER TABLE `Book`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
--
-- AUTO_INCREMENT for table `content`
--
ALTER TABLE `content`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT for table `file`
--
ALTER TABLE `file`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT for table `Testament`
--
ALTER TABLE `Testament`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT for table `verse`
--
ALTER TABLE `verse`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- Constraints for dumped tables
--

--
-- Constraints for table `content`
--
ALTER TABLE `content`
  ADD CONSTRAINT `content_ibfk_1` FOREIGN KEY (`Testament`) REFERENCES `Testament` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `content_ibfk_2` FOREIGN KEY (`Book`) REFERENCES `Book` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `file`
--
ALTER TABLE `file`
  ADD CONSTRAINT `file_ibfk_1` FOREIGN KEY (`contentID`) REFERENCES `content` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `verse`
--
ALTER TABLE `verse`
  ADD CONSTRAINT `verse_ibfk_1` FOREIGN KEY (`contentID`) REFERENCES `content` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;
