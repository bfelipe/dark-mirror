## Dark Mirror

Dark mirror is a set of lambda functions which fetch data from different sources as 
news feeds and apis, weather and randomically generate playlists from your spotify 
account to you can listen diffent kind of music everyday.

# Made with

- Python 3+
- Kubernetes
- Serverless
- Kubeless

# News feed

There are tree major feed news we are going to use here:

    - BBC
    - The New York Times
    - The Guardian

# Weather

For wheather, we are going to fetch the data from AccuWeather which seems to be
pretty reliable and very detailed source.

# Spotify

The idea of this service is to access your account and generate a short playlist
with a music spotify suggest you but maybe you never saw it in your service client.

## Setup and deploy

There are a few steps you must to execute to maintain this project and also deploy all
services available here.

First things first you must have access to kubernetes or running kubernetes locally.
If you want, I also have a project that helps you to set uo k8 locally. You can find the 
project scripts here: https://gitlab.com/bfelipe/k8-local

Also you must have installed serveless framework, which relly on nodejs to handle serverless
development and deployment easy.

So. Once you have everything up and running you want to go into the service folder you want to
deploy and install the dependencies serverless requires to work with your lambda functions. To
do that you just need to execute:

    npm install

You going to see a folder called node_modules inside the service folder.
Now you just need to execute the command bellow to deploy your service into kubernetes:

    serverless deploy

You don't need to worry about packing the dependencies each lambda function needs because we are
using kubeless. This guy will take care of everything about download the project dependencies.

The function must be available once serverless finished the deploy process.
To check if it is created properlly, you can execute:

    kubectl get functions

If you have more than once function it will be listed here. If not you are going to see something like:

    NAME            AGE
    <function-name>   00s

Now you must check if your function is actually running into a pod.
To do that you must execute:

    kubectl get pods

The function you just deployed should be listed there with a generated code.

## Testing serverless functions

There are two ways to test your function once you actually finish the deploy.

The first way, you can simply invoke it using serverless framework by typing into your console

    serverless invoke --function <function-name> --log

If your function is set to return a response you are going to get it after the call.

The second way is by calling your function using kubeless cli.

    kubeless function call <function-name>

In bothe case if your function is expencting to get an input data, everything you need to do is
to add '--data' with the actual data you want to send to the lambda function.

## To Do

- Write docs about how to expose lambda function to external calls with ingress
- Add the new york times get news function
- Add the guardian get news function
- Add the new york times get news function
- Add accuWeather function
- Add spotify random playlist function
- Add script for declarative ci/cd using gilab
- Add approach to handle unit tests