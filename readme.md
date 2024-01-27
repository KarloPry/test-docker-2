# test-docker-2
Este es un repositorio de prueba para docker
donde conectamos dos contenedores, uno que servirá
como servidor de base de datos y otro que servirá
de CLI para la base de datos.
# Instrucciones
## 1. Clonar el repositorio
```bash
git clone https://github.com/KarloPry/test-docker-2.git
```
## 2. Crear la imagen de la BD
```bash
docker run --name sql-py --network=my-bridge-network -e MYSQL_ROOT_PASSWORD=my-secret-pw -e MYSQL_DATABASE="testdb" -d mysql:latest
```
## 3. Crear la imagen del CLI
```bash
docker build -t cli-py .
```
## 4. Correr el servidor de la BD
```bash
docker run --name sql-py --network=my-bridge-network -e MYSQL_ROOT_PASSWORD=my-secret-pw -e MYSQL_DATABASE="testdb" -d mysql:latest
```
Cuando creamos el contenedor de la BD, definimos una primer base de datos llamada
testbd, esta no tiene ninguna tabla. Para crear una tabla, debemos conectarnos
## 5. Correr el CLI
```bash
docker run --name cli-py --network=my-bridge-network -it cli-py
```
Una vez dentro del CLI, podemos crear una tabla con el siguiente comando
```sql
CREATE TABLE test_table (id int not null auto_increment, name varchar(255), primary key (id));
```
Para ver las tablas que tenemos en la BD, podemos usar el siguiente comando
```sql
SHOW TABLES;
```
Para ver la estructura de una tabla, podemos usar el siguiente comando
```sql
DESCRIBE test_table;
```
Para insertar un registro en la tabla, podemos usar el siguiente comando
```sql
INSERT INTO test_table (name) VALUES ('Karlo');
```
Para ver los registros de la tabla, podemos usar el siguiente comando
```sql
SELECT * FROM test_table;
```
Para borrar un registro de la tabla, podemos usar el siguiente comando
```sql
DELETE FROM test_table WHERE id=1;
```
Para borrar la tabla, podemos usar el siguiente comando
```sql
DROP TABLE test_table;
```
## 6. Salir del CLI
Una vez hayamos terminado de manipular la BD a través del CLI,
podemos salir del CLI con el siguiente comando
```bash
exit
```
