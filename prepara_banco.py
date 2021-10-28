import MySQLdb
print('Conectando...')
conn = MySQLdb.connect(user='root', passwd='@Aa84017591', host='localhost', port=3306)

# Descomente se quiser desfazer o banco...
conn.cursor().execute("DROP DATABASE `jogoteca`;")
conn.commit()

criar_tabelas = '''SET NAMES utf8;
    CREATE DATABASE `jogoteca` /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_bin */;
    USE `jogoteca`;
    CREATE TABLE `jogo` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `nome` varchar(50) COLLATE utf8_bin NOT NULL,
      `categoria` varchar(40) COLLATE utf8_bin NOT NULL,
      `console` varchar(20) NOT NULL,
      PRIMARY KEY (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
    CREATE TABLE `usuario` (
      `id` varchar(20) COLLATE utf8_bin NOT NULL,
      `nome` varchar(20) COLLATE utf8_bin NOT NULL,
      `senha` varchar(20) COLLATE utf8_bin NOT NULL,
      PRIMARY KEY (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;'''

conn.cursor().execute(criar_tabelas)

# inserindo usuarios
cursor = conn.cursor()
cursor.execute('''INSERT INTO jogoteca.usuario (id, nome, senha) VALUES ('admin', 'admin', 'admin')''')


# commitando senão nada tem efeito
conn.commit()
cursor.close()

print('Preparado!')