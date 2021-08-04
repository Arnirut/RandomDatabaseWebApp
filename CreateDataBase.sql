-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema proj1
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema proj1
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `proj1` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `proj1` ;

-- -----------------------------------------------------
-- Table `proj1`.`ins`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `proj1`.`ins` (
  `INS_code` VARCHAR(5) NOT NULL,
  `Insurance_Name` VARCHAR(30) NULL DEFAULT NULL,
  `Address` VARCHAR(30) NULL DEFAULT NULL,
  `City` VARCHAR(30) NULL DEFAULT NULL,
  `State` VARCHAR(2) NULL DEFAULT NULL,
  `Zipcode` VARCHAR(5) NULL DEFAULT NULL,
  PRIMARY KEY (`INS_code`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `proj1`.`mds`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `proj1`.`mds` (
  `Code` VARCHAR(5) NOT NULL,
  `Name` VARCHAR(30) NULL DEFAULT NULL,
  `Address` VARCHAR(30) NULL DEFAULT NULL,
  `City` VARCHAR(15) NULL DEFAULT NULL,
  `State` VARCHAR(2) NULL DEFAULT NULL,
  `Zipcode` VARCHAR(5) NULL DEFAULT NULL)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `proj1`.`medical`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `proj1`.`medical` (
  `Mp_Code` VARCHAR(5) NOT NULL,
  `Description` VARCHAR(30) NULL DEFAULT NULL,
  `Price` DECIMAL(10,2) NULL DEFAULT NULL)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `proj1`.`patients`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `proj1`.`patients` (
  `Code` VARCHAR(5) NOT NULL,
  `Name` VARCHAR(30) NULL DEFAULT NULL,
  `Ins_Company_Code` VARCHAR(5) NULL DEFAULT NULL,
  `Address_line_1` VARCHAR(30) NULL DEFAULT NULL,
  `Address_line_2` VARCHAR(30) NULL DEFAULT NULL,
  `City` VARCHAR(15) NULL DEFAULT NULL,
  `State` VARCHAR(2) NULL DEFAULT NULL,
  `Zip` VARCHAR(5) NULL DEFAULT NULL,
  PRIMARY KEY (`Code`),
  INDEX `Ins_Company_Code` (`Ins_Company_Code` ASC) VISIBLE,
  INDEX `Patients_Code` (`Code` ASC) VISIBLE,
  CONSTRAINT `patients_ibfk_1`
    FOREIGN KEY (`Ins_Company_Code`)
    REFERENCES `proj1`.`ins` (`INS_code`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `proj1`.`treatments`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `proj1`.`treatments` (
  `ID` INT NOT NULL AUTO_INCREMENT,
  `Patient_code` VARCHAR(5) NULL DEFAULT NULL,
  `Md_code` VARCHAR(5) NULL DEFAULT NULL,
  `Mp_code` VARCHAR(5) NULL DEFAULT NULL,
  `Date_of_treatment` DATE NULL DEFAULT NULL,
  PRIMARY KEY (`ID`),
  INDEX `Patient_Code_idx` (`Patient_code` ASC) VISIBLE,
  CONSTRAINT `Patient_Code`
    FOREIGN KEY (`Patient_code`)
    REFERENCES `proj1`.`patients` (`Code`))
ENGINE = InnoDB
AUTO_INCREMENT = 21
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
