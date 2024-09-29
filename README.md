# Enigma Machine - Flask Application

This project presents a Python-simulated version of the legendary Enigma machine used during World War II. Users can encrypt messages and decrypt encrypted messages through the web interface.

## Features of the project
- **Message Encryption**: Users can encrypt their text messages with the Enigma algorithm.
- **Rotor and Plugboard Settings**: Users can achieve different encryption results by adjusting the starting positions of the three rotors.
- **User Friendly Interface**: A simple and intuitive web interface allows users to easily encrypt their messages.
- **Advanced Customization**: Provides a variety of encryption options with different rotor and tagging settings.

## Usage

### Establishing Project Requirements

To start the project, you first need to install the necessary dependencies. Type the following command in the terminal or command client:

```bash
pip install -r requirements.txt
```

### Running the Project
After installing the requirements, use the following command to start the application:

```bash
python app.py
```

### User Interface
- **Message Entry**: On the home page there is a text box where you can type the message you want to encrypt.
- **Rotor Positions**: There are fields to set the starting positions of the three rotors. You can set the positions as a value between 0 and 25.
- **Encryption Button**: After entering all the information, you can encrypt your message by clicking the “Encrypt” button.
- **Result Page**: After the encryption process is complete, your encrypted message and your original message will be displayed on the result page.

### Project Interface

Verify the deployment by navigating to your server address in
your preferred browser.

```sh
127.0.0.1:5000
```

## RECOMMENDATION - Using WSGI in Production:

Flask provides a built-in server for the development environment, but in a production environment it is necessary to use a more secure and performant solution. You can achieve this by running your Flask application with a WSGI server.

**Recommended WSGI Server: Gunicorn**

Gunicorn is a lightweight and easy WSGI server that is widely used for running Python applications in a production environment.

### Setups:

- **1st Step: Install Gunicorn**: 

```bash
pip install gunicorn
```
- **2nd Step: Launch your Flask Application:**: 

```bash
gunicorn -w 4 myapp:app
```

> [!IMPORTANT]  
> -w 4 specifies that the application will be run with 4 worker processes. You can increase it according to the workload. 

> [!NOTE]  
> In myapp:app, myapp is the name of the Python file and app is the Flask application variable.

> [!TIP]
> For larger deployments, it is generally recommended to use Gunicorn in combination with a reverse proxy server (e.g. NGINX). This provides additional advantages in terms of load balancing and security.

**Developed by 👨‍💻 Ahmet Mithat Demirkol**
