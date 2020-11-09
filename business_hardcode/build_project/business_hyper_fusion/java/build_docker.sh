cat /root/.m2/dockerregistry-auth |  docker login ${DOCKER_REGISTRY_URL} --username ${DOCKER_REGISTRY_USERNAME} --password-stdin
docker build --build-arg IMAGE_PROJECT_TAG=${IMAGE_PROJECT_TAG} -t ${IMAGE_ID}  .
docker push ${IMAGE_ID}