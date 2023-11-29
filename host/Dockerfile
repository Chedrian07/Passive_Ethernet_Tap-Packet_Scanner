
FROM ubuntu:22.04

RUN apt-get update && apt-get install -y python3 python3-pip file zip unzip 


WORKDIR /app

# Install Flask
RUN pip3 install Flask

COPY server.py /app/
COPY index.html /app/templates/

EXPOSE 5000
EXPOSE 7777

# Run the server script
CMD ["python3", "server.py"]


#docker build -t host .
#docker run -d -p 5000:5000 -p 7777:7777 host 