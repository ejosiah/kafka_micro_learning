# Kafka micro learning

## Description
This repository contains the supporting code for the kafka session of the micro learning series

## Requirements
- python
- docker

## Running the code
### Host setup
The kafka brokers reference each other by their hostnames so we need to add these hostnames into you hosts file so they can be resolved to your 
machines localhost (127.0.0.1)

edit your host file, you can find it at `/etc/hosts` in linux and maxOs and `C:\Windows\System32\drivers\etc\hosts` in windows. Add the following entries:
```
127.0.0.1       kafka-broker-1
127.0.0.1       kafka-broker-2
127.0.0.1       kafka-broker-3
```
### Running kafka borkers
- `docker-compose up -d` to install and start the containers
- `docker-compose down` to stop and remove the containers 


#### Running producer / consumer
The kafka producer / consumer code is written in python so you need to make sure you have python installed. prefereably run the code in a vitual environment so as not to populate your global python environment

```
# Create a virtual environment 
python -m venv myenv

# Activate the virtual environment

# Windows
myenv\Scripts\activate
# macOS and Linux
source myenv/bin/activate

# install dependencies
pip install -r requirements.txt

# run sales producer
python sales_producer.py

# run sales consumer 
python main.py
```

if you get this error `Command 'python' not found, did you mean:` then either you dont have python installed or your python command is `python3`,
