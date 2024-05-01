.PHONY: up start stop restart down help 

COMPOSE = compose-dev.yml
CONTAINER = django_app

help:
	@echo "Usage:"
	@echo "  make up       	  Executa: docker-compose up -d"
	@echo "  make down        Executa: docker-compose down"
	@echo "  make start       Inicia um contêiner parado"
	@echo "  make stop        Para o contêiner"
	@echo "  make restart     Reinicia o contêiner (equivalente a stop e start)"
	@echo "  make help        Exibe as opções disponíveis de ajuda"
	
up: 
	docker-compose -f $(COMPOSE) up -d
down:
	docker-compose -f $(COMPOSE) down
start:
	docker-compose -f $(COMPOSE) start
stop:
	docker-compose -f $(COMPOSE) stop
restart:
	docker-compose -f $(COMPOSE) restart	
exec:
	docker exec -it $(CONTAINER) bash