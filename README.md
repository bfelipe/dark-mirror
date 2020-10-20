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

## Exposing our function

We already have our function deployed, but still we need to expose it to be able to call from an dns url. You still can test your function following the same steps described at "Testing serverless function", but let's make it something easy to access and handle for our users.
First lets create a trigger for our functions. Righ now kubeless has tree types of triggers(http, cronjob and pubsub), once you create a trigger, kubeless will handle to create an ingress for your function, so no need to write an yaml file for that.

    kubeless trigger <trigger-type> create <trigger-name> -n <namespace> --function-name <function-name> --hostname <dns> --path <ex. hello>

Now you can check if your function was exposed by typing:

    kubectl get ing -n <namespace>

For get more information about your function you can use:

    kubectl describe ing <ingress-name> -n <namespace>

Here ingress-name usually take the same name as the trigger you named your function.

or
    kubectl logs -n kubeless -l kubeless=controller -c http-trigger-controller
    curl --header "Content-Type:application/json" 172.17.0.2/dark-mirror

If everything is up and running fine, you now can call your function using:

    curl --header "Content-Type:application/json" dns/path

**IMPORTANT:** If you provide a domain.name when you created your function you should also register it in your /etc/hosts file. Otherwise you will not be able to call your function.
You can get the ip for your dns using the same command to get ingress information.

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

- Add the new york times get news function
- Add the guardian get news function
- Add the new york times get news function
- Add accuWeather function
- Add spotify random playlist function
- Add approach to handle unit tests