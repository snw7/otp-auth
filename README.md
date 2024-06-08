## Documentation
This is a lightweight API that allows communication between iOS devices and a remote server. The API endpoint is containerized with docker. It relies on OTP authentication. Each token is valid for 30s.

## Setup
### Server
1. copy this repo to your remote server and install docker
2. (optional) install "letsencrypt" SSL certificates for a secure connection
2. create a new .env file (based on `.env.example`) and fill the values accordingly
3. generate a random salt: `openssl rand -hex 32` & save it to your `.env`
4. update the `EXPOSE` value in your `Dockerfile`
4. build the docker container with `docker build -t otp-auth .`
6. run the docker container `docker run -d -p <your-port>:<your-port> -v /etc/letsencrypt/:/etc/letsencrypt/ otp-auth` (volume mount is only required for SSL setup)

### Client
1. install the `Scriptable` app from the App Store
2. for each of the `*.js` files in the `client/` folder: create a new script in the `Scriptable` app
3. replace the default SALT in the `run.js` file with the previously generated value 
4. open the `otp-action.shortcut` file with the `Shortcuts` app and install the workflow
5. check if the correct js script is selected in the first action
6. execute the shortcut -> you should receive a success message from your server

## License
This project is written by snw7 and licensed under the MIT License.

This project uses https://github.com/emn178/js-sha3 @copyright Chen, Yi-Cyuan 2015-2018.