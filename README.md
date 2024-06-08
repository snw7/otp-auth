## Documentation
This is a lightweight API that allows communication between iOS devices and a remote server. The API endpoint is containerized with docker. It relies on OTP authentication. Each token is valid for 30s.

## Setup
### Server
1. copy this repo to your remote server and install docker
2. (optional) install "letsencrypt" SSL certificates for a secure connection
3. create a new .env file (based on `.env.example`) and fill the values accordingly
4. generate a random salt: `openssl rand -hex 32` & save it to your `.env`
5. update the `EXPOSE` value in your `Dockerfile`
6. build the docker container with `docker build -t otp-auth .`
7. run the docker container `docker run -d -p <your-port>:<your-port> -v /etc/letsencrypt/:/etc/letsencrypt/ otp-auth` (volume mount is only required for SSL setup)

### Client
1. install the `Scriptable` app from the App Store
2. for each of the `*.js` files in the `client/` folder: create a new script in the `Scriptable` app
3. replace the default SALT in the `run.js` file with the previously generated value 
4. open the `otp-auth-client.shortcut` file with the `Shortcuts` app and install the workflow
5. select the `gen-otp-token.js` script in the first action of the workflow
6. enter the domain of your server and the port the service is running on in action 4
7. execute the shortcut -> you should receive a success message from your server

## License
This project is written by snw7 and licensed under the MIT License.

This project uses https://github.com/emn178/js-sha3 &copy; Chen, Yi-Cyuan 2015-2018.
