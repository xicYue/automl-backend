# MLADS: Machine Learning Automatic Deployment System
This an example show how to deploy a module into MLADS

## Install command line tools
```shell
$ npm install @serverless-devs/s -g
```

## Deploy
```shell
$ s delpoy
```
The command line tools will read s.yaml, then build docker image and push it to repository to finish deployment.

## Invoke
```shell
$ s invoke -e "{\"key\": \"val\"}"
```
Use command above can test if deployment has been finished correctly.

## New Project
If you want create and deploy your own module into MLADS, you can start your project as follows
```shell
$ s
```
Then select your configuration
```shell
? Hello, serverlesser. Which template do you like? (Use arrow keys or type to search)
❯ Quick start 
  Custom runtime example 
  Container example 
  Custom domain example 
```

## Invoke with LLM
Here is an example shows invocation with LLM
https://matdata.cloud/MLADS/frontend