## Исходный текст запросов

``` sql
CREATE TABLE IF NOT EXISTS `pr-cbs`.`calendar` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `date` DATETIME NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE)
ENGINE = InnoDB
```

``` sql
CREATE TABLE IF NOT EXISTS `pr-cbs`.`event` (
  `event` VARCHAR(45) NOT NULL,
  `picture` BLOB NULL,
  `date_id` INT NOT NULL,
  INDEX `date_id_idx` (`date_id` ASC) VISIBLE,
  PRIMARY KEY (`date_id`),
  CONSTRAINT `date_id`
  FOREIGN KEY (`date_id`)
  REFERENCES `pr-cbs`.`calendar` (`id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION)
ENGINE = InnoDB
```

``` sql
CREATE TABLE IF NOT EXISTS `pr-cbs`.`category` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `category_name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE)
```

``` sql
CREATE TABLE IF NOT EXISTS `pr-cbs`.`places` (
  `cat_id` INT NOT NULL,
  `place` VARCHAR(45) NOT NULL,
  `adress` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`cat_id`),
  CONSTRAINT `cat_id`
  FOREIGN KEY (`cat_id`)
  REFERENCES `pr-cbs`.`category` (`id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION)
```

``` sql
CREATE TABLE IF NOT EXISTS `pr-cbs`.`people` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `picture` BLOB NULL,
  `description` TEXT(500) NOT NULL,
  `birth_date` DATETIME NOT NULL,
  `death_date` DATETIME NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE)
```