# Exemplo de Xcom entre dokerOperators no Apache Airflow
Este repositório tem o objetivo de criar uma imagem que será executada dentro do Apache Airflow com `dockerOperator`, para exemplo de transferência de dados entre containers.

## Requisitos
- [Docker](https://www.docker.com/) instalado da máquina

## Criando imagem
Basta executar o código na raiz do projeto:

```bash
docker build -t xcom-docker-operator:latest .
```

Agora você poderá usar a imagem que criou para executar um container no `Apache Airflow` usando a tag: `xcom-docker-operator:latest`
