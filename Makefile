# Build the app (make build, make daemon_up)
build:
	docker-compose up --build

daemon_up:
	docker-compose up -d

make_migrations:
	docker exec -it scraper_api python src/manage.py makemigrations

migrate:
	docker exec -it scraper_api python src/manage.py migrate

get_loans:
	docker exec -it scraper_api python src/manage.py get_loans


# Common commands
clean_all:
	docker system prune --all

clean_all_force:
	docker system prune --all --force

docker_stop:
	docker stop $(docker ps -aq)

clean_volumes:
	docker volume prune
