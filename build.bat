docker build --pull --rm -f "dockerfile" -t sampleflask:latest "." 
docker tag sampleflask:latest registry.digitalocean.com/smn-sockets-test/sampleflask:latest
docker push registry.digitalocean.com/smn-sockets-test/sampleflask:latest