docker run -d -p 8086:8086 \
      -v influxdb:/var/lib/influxdb \
      -e DOCKER_INFLUXDB_INIT_MODE=setup \
      -e DOCKER_INFLUXDB_INIT_USERNAME=kjn \
      -e DOCKER_INFLUXDB_INIT_PASSWORD=parmesan007 \
      -e DOCKER_INFLUXDB_INIT_ORG=scr@pers \
      -e DOCKER_INFLUXDB_INIT_BUCKET=AMAZON \
      -e DOCKER_INFLUXDB_INIT_ADMIN_TOKEN=my-super-secret-auth-token \
      influxdb:2.0