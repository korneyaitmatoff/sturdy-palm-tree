docker rm -f $(docker rm -aq)
docker rmi -f $(docker rmi -aq)

docker build -t django-polls-app ./

docker-compose up -d

read -p "Press enter to continue"
