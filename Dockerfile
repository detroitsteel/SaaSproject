# Using lightweight alpine image
FROM python:3.8

# Defining working directory and adding source code
ENV PROJECT_DIR /usr/src/app
WORKDIR ${PROJECT_DIR}
COPY Pipfile Pipfile.lock bootstrap.sh ./
COPY requirements.txt .
COPY chartdata ./chartdata
COPY . .

# Installing packages
RUN pip3 install -r requirements.txt pipenv



# Install API dependencies
RUN pipenv install --deploy --ignore-pipfile

# Start app
SHELL ["/bin/activate", "-c"]
EXPOSE 5000
ENTRYPOINT ["./bootstrap.sh"]
#CMD ["pipenv", "run", "python", "api.py"]
