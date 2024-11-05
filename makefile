run:
	uvicorn bet_maker.main:app --host 0.0.0.0 --port 8000 --reload

run_line:
	uvicorn line_provider.app:app --host 0.0.0.0 --port 8080 --reload


run_db:
	docker run --name postgres-bsw \
	-e POSTGRES_USER=postgres \
	-e POSTGRES_PASSWORD=postgres_password \
	-e POSTGRES_DB=postgres_bsw \
	-p 5432:5432 \
	-d postgres:16-alpine \
	-c 'max_connections=100'


run_mq:
	docker run -d \
    --name rabbitmq \
    -e RABBITMQ_DEFAULT_USER=guest \
    -e RABBITMQ_DEFAULT_PASS=guest \
    -p 5672:5672 \
    -p 15672:15672 \
    rabbitmq:3-management
