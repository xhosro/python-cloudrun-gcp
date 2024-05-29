## Automate a python app with Cloud run & cloud build on GCP

# steps:
- create a api key with openweathermap api
- create a python app to fetch weather data
- test app locally 
- create a dockerfile
- test container image
- push container image to artifacts registry
  - after testing locally our application, I push the codes to github and I cloned it to Cloud shell in GCP and push it to    container registery

  docker build -t gcr.io/terraform-422613/weather-app:v01 .

  docker image ls

  dokcer run -p 8080:8080 image
  docker push gcr.io/terraform-422613/weather-app:v01
  gcloud auth configure-docker


- deploy container to cloud run
- Automate CI/CD process using build trigger




