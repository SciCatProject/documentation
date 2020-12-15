# Setup SciCat with Docker Compose

The [scicatlive](https://github.com/SciCatProject/scicatlive#readme) repo defines a quick and convenient method for getting started. It sets up the Mongo DB , catamel and catanie, all using docker containers, starts the containers and connects them , all with a single command. This is also a convenient method to contribute to the development of this project easily.

## Extending Docker Compose to include RabbitMQ

When using RabbitMQ with scicat it needs to be configured initially, before the rest of the scicat services are run. It can be also run in docker compose, but it must be set up with users before catamel is started, otherwise catamel cannot connect. It is easier to configure rabbitmq as a separate service before starting scicat through docker compose. A basic docker compose for rabbitmq looks like:
```
version: "3.8"
services:
  local-rabbitmq:
    hostname: local-rabbitmq
    image: 'bitnami/rabbitmq:latest'
    labels:
      kompose.service.type: nodeport
    ports:
      - '4369:4369'
      - '5672:5672'
      - '25672:25672'
      - '15672:15672'
    volumes:
      - 'rabbitmq_data:/bitnami'
volumes:
    rabbitmq_data:
      driver: local

```

In this set up the users and user management portal need to be configured manually which can be done via CLI. The following commands can be executed in the docker container to set up initial users and the management portal.

```
# To add the management plugin
rabbitmq-plugins enable rabbitmq_management

#to add a user
rabbitmqctl add_user <username> <password>
rabbitmqctl set_user_tags <username> administrator
rabbitmqctl set_permissions -p / <username> '.*' '.*' '.*'
```
An user with the administrator tag needs to be activated in order to be able to log into the rabbitmq management portal hosted at localhost:15672.