https://hub.docker.com/r/mediagis/nominatim/
https://github.com/mediagis/nominatim-docker

```bash
ln -s /var/lib/postgresql/11/main/ /data/postgresdata
docker-compose run nominatim bash /app/init.sh /data/china.osm.pbf postgresdata 4
chown -R postgres:postgres /var/lib/postgresql/11/main
docker-compose run nominatim bash /app/start.sh
```

http://download.geofabrik.de/asia.html
