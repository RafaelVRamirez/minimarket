-- MySQL Script generated by MySQL Workbench
-- Wed Jan  8 09:47:58 2025
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`Proveedor`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Proveedor` (
  `idProveedor` INT NOT NULL AUTO_INCREMENT,
  `nombreProveedor` VARCHAR(120) NOT NULL,
  `rucProveedor` VARCHAR(11) NOT NULL,
  `direccionProveedor` VARCHAR(150) NOT NULL,
  `emailProveedor` VARCHAR(150) NULL,
  `telefonoProveedor` VARCHAR(15) NOT NULL,
  `estadoProveedor` INT NOT NULL,
  PRIMARY KEY (`idProveedor`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Vendedor_Proveedor`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Vendedor_Proveedor` (
  `idVendedor_Proveedor` INT NOT NULL AUTO_INCREMENT,
  `idProveedor` INT NOT NULL,
  `nombre` VARCHAR(100) NOT NULL,
  `telefono` VARCHAR(15) NOT NULL,
  `estado` CHAR(1) NOT NULL,
  PRIMARY KEY (`idVendedor_Proveedor`),
  INDEX `fk_Vendedor_Proveedor_Proveedor_idx` (`idProveedor` ASC) VISIBLE,
  CONSTRAINT `fk_Vendedor_Proveedor_Proveedor`
    FOREIGN KEY (`idProveedor`)
    REFERENCES `mydb`.`Proveedor` (`idProveedor`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Categoria`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Categoria` (
  `idCategoria` INT NOT NULL AUTO_INCREMENT,
  `nombreCategoria` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idCategoria`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`SubCategoria`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`SubCategoria` (
  `idSubCategoria` INT NOT NULL AUTO_INCREMENT,
  `nombreSubCategoriacol` VARCHAR(200) NOT NULL,
  `idCategoria` INT NOT NULL,
  PRIMARY KEY (`idSubCategoria`),
  INDEX `fk_SubCategoria_Categoria1_idx` (`idCategoria` ASC) VISIBLE,
  CONSTRAINT `fk_SubCategoria_Categoria1`
    FOREIGN KEY (`idCategoria`)
    REFERENCES `mydb`.`Categoria` (`idCategoria`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Producto`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Producto` (
  `idProducto` INT NOT NULL AUTO_INCREMENT,
  `codigo` VARCHAR(45) NOT NULL,
  `codigoBarras` VARCHAR(45) NULL,
  `marca` VARCHAR(60) NULL,
  `nombreProducto` VARCHAR(45) NOT NULL,
  `descripcionProducto` TEXT(600) NULL,
  `idCategoria` INT NOT NULL,
  `idSubCategoria` INT NOT NULL,
  `tipo` VARCHAR(150) NOT NULL,
  `tipoPresentacion` VARCHAR(45) NOT NULL,
  `peso_de_medida` VARCHAR(10) NOT NULL,
  `stockActual` INT NOT NULL,
  `stockMinimo` INT NOT NULL,
  `precioCosto` DECIMAL(10,2) NOT NULL,
  `precioVenta` DECIMAL(10,2) NOT NULL,
  `fechaVencimiento` DATE NULL,
  `estado` CHAR(1) NOT NULL,
  PRIMARY KEY (`idProducto`),
  INDEX `fk_Producto_SubCategoria1_idx` (`idSubCategoria` ASC) VISIBLE,
  INDEX `fk_Producto_Categoria1_idx` (`idCategoria` ASC) VISIBLE,
  CONSTRAINT `fk_Producto_SubCategoria1`
    FOREIGN KEY (`idSubCategoria`)
    REFERENCES `mydb`.`SubCategoria` (`idSubCategoria`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Producto_Categoria1`
    FOREIGN KEY (`idCategoria`)
    REFERENCES `mydb`.`Categoria` (`idCategoria`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Octogono`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Octogono` (
  `idOctogono` INT NOT NULL AUTO_INCREMENT,
  `nombreOctogono` VARCHAR(45) NOT NULL,
  `imagenOctogono` BLOB NOT NULL,
  `estado` CHAR(1) NOT NULL,
  PRIMARY KEY (`idOctogono`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Octogono_Producto`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Octogono_Producto` (
  `idOctogono` INT NOT NULL,
  `idProducto` INT NOT NULL,
  PRIMARY KEY (`idOctogono`, `idProducto`),
  INDEX `fk_Octogono_has_Producto_Producto1_idx` (`idProducto` ASC) VISIBLE,
  INDEX `fk_Octogono_has_Producto_Octogono1_idx` (`idOctogono` ASC) VISIBLE,
  CONSTRAINT `fk_Octogono_has_Producto_Octogono1`
    FOREIGN KEY (`idOctogono`)
    REFERENCES `mydb`.`Octogono` (`idOctogono`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Octogono_has_Producto_Producto1`
    FOREIGN KEY (`idProducto`)
    REFERENCES `mydb`.`Producto` (`idProducto`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`ImagenProducto`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`ImagenProducto` (
  `idImagenProducto` INT NOT NULL AUTO_INCREMENT,
  `imagenProducto` BLOB NOT NULL,
  `idProducto` INT NOT NULL,
  PRIMARY KEY (`idImagenProducto`),
  INDEX `fk_ImagenProducto_Producto1_idx` (`idProducto` ASC) VISIBLE,
  CONSTRAINT `fk_ImagenProducto_Producto1`
    FOREIGN KEY (`idProducto`)
    REFERENCES `mydb`.`Producto` (`idProducto`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`DocumentoCompra`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`DocumentoCompra` (
  `idDocumentoCompra` INT NOT NULL AUTO_INCREMENT,
  `idProveedor` INT NOT NULL,
  `tipoDocumento` VARCHAR(45) NOT NULL,
  `numeroDocumento` VARCHAR(45) NOT NULL,
  `total` DECIMAL(10,2) NOT NULL,
  `igv` DECIMAL(10,2) NOT NULL,
  `percepcion` DECIMAL(10,2) NULL,
  `fecha` DATE NOT NULL,
  `formaPago` VARCHAR(20) NOT NULL,"(efectivo, transferencia, yape, plim, crédito)"
  `CondicionPago` VARCHAR(10) NOT NULL,"(contado, crédito)"
  `estadoPago` VARCHAR(12) NOT NULL,"('Pagado', 'Pendiente', 'Parcial') "
  PRIMARY KEY (`idDocumentoCompra`),
  INDEX `fk_DocumentoCompra_Proveedor1_idx` (`idProveedor` ASC) VISIBLE,
  CONSTRAINT `fk_DocumentoCompra_Proveedor1`
    FOREIGN KEY (`idProveedor`)
    REFERENCES `mydb`.`Proveedor` (`idProveedor`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`DetalledeCompra  - 
-- purchase detail   ` 
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`DetalledeCompra` (
  `idDetalledeCompra` INT NOT NULL AUTO_INCREMENT,
  `idProducto` INT NOT NULL,
  `idDocumentoCompra` INT NOT NULL,
  `cantidad` INT NOT NULL,
  `precioUnitario` DECIMAL(10,2) NOT NULL,
  `subTotal` DECIMAL(10,2) NOT NULL,
  PRIMARY KEY (`idDetalledeCompra`, `idProducto`, `idDocumentoCompra`),
  INDEX `fk_Producto_DocumentoCompra_Producto1_idx` (`idProducto` ASC) VISIBLE,
  INDEX `fk_Producto_DocumentoCompra_DocumentoCompra1_idx` (`idDocumentoCompra` ASC) VISIBLE,
  CONSTRAINT `fk_Producto_DocumentoCompra_Producto1`
    FOREIGN KEY (`idProducto`)
    REFERENCES `mydb`.`Producto` (`idProducto`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Producto_DocumentoCompra_DocumentoCompra1`
    FOREIGN KEY (`idDocumentoCompra`)
    REFERENCES `mydb`.`DocumentoCompra` (`idDocumentoCompra`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`AmortizacionCredito`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`AmortizacionCredito` (
  `idAmortizacionCredito` INT NOT NULL AUTO_INCREMENT,
  `idDocumentoCompra` INT NOT NULL,
  `fechaPago` DATE NOT NULL,
  `montoPagado` DECIMAL(10,2) NOT NULL,
  `saldoRestante` DECIMAL(10,2) NOT NULL,
  PRIMARY KEY (`idAmortizacionCredito`),
  INDEX `fk_AmortizacionCredito_DocumentoCompra1_idx` (`idDocumentoCompra` ASC) VISIBLE,
  CONSTRAINT `fk_AmortizacionCredito_DocumentoCompra1`
    FOREIGN KEY (`idDocumentoCompra`)
    REFERENCES `mydb`.`DocumentoCompra` (`idDocumentoCompra`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Cliente`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Cliente` (
  `idCliente` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(100) NOT NULL,
  `TipoDocumento` VARCHAR(45) NOT NULL,
  `NumeroDocumento` VARCHAR(12) NOT NULL,
  `Celular` VARCHAR(11) NOT NULL,
  `FechaNacimiento` DATE NULL,
  `MontoCredito` DECIMAL(4,2) NULL,
  `Direccion` VARCHAR(100) NOT NULL,
  `FechaRegistro` DATE NOT NULL,
  `Correo` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idCliente`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Pedido`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Pedido` (
  `idPedido` INT NOT NULL AUTO_INCREMENT,
  `dCliente` INT NOT NULL,
  `fechaPedido` DATE NOT NULL,
  `tipoDePago` VARCHAR(45) NOT NULL,
   PRIMARY KEY (`idPedido`),
  INDEX `fk_Pedido_Cliente1_idx` (`dCliente` ASC) VISIBLE,
  CONSTRAINT `fk_Pedido_Cliente1`
    FOREIGN KEY (`dCliente`)
    REFERENCES `mydb`.`Cliente` (`idCliente`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`DetallePedido`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`DetallePedido` (
  `idDetallePedido` INT NOT NULL AUTO_INCREMENT,
  `idPedido` INT NOT NULL,
  `idProducto` INT NOT NULL,
  `cantidad` DECIMAL(2,2) NOT NULL,
  `precioUnitario` DECIMAL(10,2) NOT NULL,
  `subTotal` DECIMAL(10,2) NOT NULL,
  INDEX `fk_DetallePedido_Pedido1_idx` (`idPedido` ASC) VISIBLE,
  INDEX `fk_DetallePedido_Producto1_idx` (`idProducto` ASC) VISIBLE,
  CONSTRAINT `fk_DetallePedido_Pedido1`
    FOREIGN KEY (`idPedido`)
    REFERENCES `mydb`.`Pedido` (`idPedido`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_DetallePedido_Producto1`
    FOREIGN KEY (`idProducto`)
    REFERENCES `mydb`.`Producto` (`idProducto`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`AmortizacionCliente`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`AmortizacionCliente` (
  `idAmortizacionCliente` INT NOT NULL AUTO_INCREMENT,
  `idPedido` INT NOT NULL,
  `fechaPago` DATE NOT NULL,
  `montoPagado` DECIMAL(10,2) NOT NULL,
  `saldoRestante` DECIMAL(10,2) NOT NULL,
  PRIMARY KEY (`idAmortizacionCliente`),
  INDEX `fk_AmortizacionCliente_Pedido1_idx` (`idPedido` ASC) VISIBLE,
  CONSTRAINT `fk_AmortizacionCliente_Pedido1`
    FOREIGN KEY (`idPedido`)
    REFERENCES `mydb`.`Pedido` (`idPedido`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
