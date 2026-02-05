-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Table `Curso`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Curso` (
  `id_curso` INT NOT NULL,
  `nome` VARCHAR(45) NULL,
  `carga_horaria` INT NULL,
  PRIMARY KEY (`id_curso`))
ENGINE = InnoDB;

CREATE UNIQUE INDEX `id_curso_UNIQUE` ON `Curso` (`id_curso` ASC) VISIBLE;


-- -----------------------------------------------------
-- Table `Aluno`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Aluno` (
  `id_aluno` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(100) NULL,
  `cpf` VARCHAR(11) NULL,
  `data_nascimento` VARCHAR(10) NULL,
  `Curso_id_curso` INT NOT NULL,
  PRIMARY KEY (`id_aluno`),
  CONSTRAINT `fk_Aluno_Curso1`
    FOREIGN KEY (`Curso_id_curso`)
    REFERENCES `Curso` (`id_curso`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE UNIQUE INDEX `id_aluno_UNIQUE` ON `Aluno` (`id_aluno` ASC) VISIBLE;

CREATE UNIQUE INDEX `cpf_UNIQUE` ON `Aluno` (`cpf` ASC) VISIBLE;

CREATE INDEX `fk_Aluno_Curso1_idx` ON `Aluno` (`Curso_id_curso` ASC) VISIBLE;


-- -----------------------------------------------------
-- Table `Professor`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Professor` (
  `id_professor` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(100) NULL,
  `formacao` VARCHAR(45) NULL,
  PRIMARY KEY (`id_professor`))
ENGINE = InnoDB;

CREATE UNIQUE INDEX `id_professor_UNIQUE` ON `Professor` (`id_professor` ASC) VISIBLE;


-- -----------------------------------------------------
-- Table `Contrato`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Contrato` (
  `id_contrato` INT NOT NULL AUTO_INCREMENT,
  `vinculo` VARCHAR(45) NULL,
  `carga_horaria_semanal` VARCHAR(45) NULL,
  `Professor_id_professor` INT NOT NULL,
  PRIMARY KEY (`id_contrato`),
  CONSTRAINT `fk_Contrato_Professor1`
    FOREIGN KEY (`Professor_id_professor`)
    REFERENCES `Professor` (`id_professor`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE UNIQUE INDEX `id_contrato_UNIQUE` ON `Contrato` (`id_contrato` ASC) VISIBLE;

CREATE INDEX `fk_Contrato_Professor1_idx` ON `Contrato` (`Professor_id_professor` ASC) VISIBLE;


-- -----------------------------------------------------
-- Table `Prontuario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Prontuario` (
  `id_prontuario` INT NOT NULL AUTO_INCREMENT,
  `data_matricula` VARCHAR(10) NULL,
  `situacao_matricula` VARCHAR(45) NULL,
  `Aluno_id_aluno` INT NOT NULL,
  PRIMARY KEY (`id_prontuario`),
  CONSTRAINT `fk_Prontuario_Aluno`
    FOREIGN KEY (`Aluno_id_aluno`)
    REFERENCES `Aluno` (`id_aluno`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE UNIQUE INDEX `id_prontuario_UNIQUE` ON `Prontuario` (`id_prontuario` ASC) VISIBLE;

CREATE INDEX `fk_Prontuario_Aluno_idx` ON `Prontuario` (`Aluno_id_aluno` ASC) VISIBLE;


-- -----------------------------------------------------
-- Table `Professor_Curso`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Professor_Curso` (
  `Professor_id_professor` INT NOT NULL,
  `Curso_id_curso` INT NOT NULL,
  PRIMARY KEY (`Professor_id_professor`, `Curso_id_curso`),
  CONSTRAINT `fk_Professor_has_Curso_Professor1`
    FOREIGN KEY (`Professor_id_professor`)
    REFERENCES `Professor` (`id_professor`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Professor_has_Curso_Curso1`
    FOREIGN KEY (`Curso_id_curso`)
    REFERENCES `Curso` (`id_curso`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_Professor_has_Curso_Curso1_idx` ON `Professor_Curso` (`Curso_id_curso` ASC) VISIBLE;

CREATE INDEX `fk_Professor_has_Curso_Professor1_idx` ON `Professor_Curso` (`Professor_id_professor` ASC) VISIBLE;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
