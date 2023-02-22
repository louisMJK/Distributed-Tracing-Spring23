# Docker
docker build . -t rolldice
docker run -d -p 8001:5000 rolldice
curl localhost:8001


# microk8s 
sudo docker build . -t localhost:32000/rolldice-registry
sudo docker push localhost:32000/rolldice-registry

microk8s kubectl apply -f rolldice-deployment.yaml

microk8s kubectl get deployments
microk8s kubectl get pods
microk8s kubectl get pods -o wide

curl 