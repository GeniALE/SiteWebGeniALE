# ORCHESTER

We are using [orchester](https://github.com/popojargo/orchester) to easily
manage the access of our member through different third party apps.

To use that service, we need to create some token in order for our api to 
query the APIs.

# Credentials

The credentials must be placed into the `/credentials` folder at the root.
Our integration will be looking that that beautiful directory!

# Renewing

Usually, to renew the tokens, you first need to have a `.orchester.json` file already
created with the require values.

Then, you can use the [**orchest**](https://github.com/popojargo/orchester#cli) command to generate the tokens. 

## Renew cycle

Some token expire at some times (I know right). 

Here's the list:
- Trello: Every month
