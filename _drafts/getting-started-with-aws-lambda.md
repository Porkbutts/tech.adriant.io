---
layout: post
title: Getting started with AWS Lambda Functions
categories: aws
tags: lambda tutorial
---

AWS Lambda is Amazon's *function as a service* product. It's a service that lets you package and run code without having to provision or manage servers. With Lambda, you only pay when your code is running. By contrast, you pay for managed servers like EC2 as long as they are running, even while they are not serving any requests.

To begin with AWS Lambda, you first write some code in one of the supported languages, you package and upload this code to Lambda, and now you have a *Lambda function* that can be run on demand. The Lambda function can be triggered from other AWS services such as SNS, SQS, API Gateway, and Cloudwatch events. Another benefit of Lambda is that it scales automatically based on the number of requests.

In this tutorial, I'll go over how to create and manage a Lambda function, as well as how to trigger the lambda function from different event sources. This tutorial assumes you know how to write some very basic code and are familiar with the AWS Console.

 <!--more-->

## Create a Lambda Function
Let's start by creating a simple Lambda function. Navigate to the AWS Console and search for "Lambda".

![AWS Console searchbar Lambda][searchbar-lambda]

Please make a note of the region in which you create your lambda function. AWS resources are generally tied to a specific region and Lambda is no exception.

![AWS Console navbar region][console-navbar-region]

Next select the *Create function* button.

![Lambda dashboard create function button][lambda-dash-create-fn-btn]

In this tutorial we'll be selecting *Author from Scratch*.

Other options include *Use a blueprint* which lets you browse the repository of Lambda functions to use as a starter template, and *Serverless App repository*. The *Serverless App repository* contains **CloudFormation** templates which often define, in addition to one or more Lambda functions, a group of AWS resources to create. **CloudFormation** is outside the scope of this tutorial.

Fill out the form by giving your function a name and selecting the runtime language of your choice. For the execution role, we'll create a new one with basic permissions.

![Lambda dashboard create function form][lambda-dash-create-fn-form]

An execution role is an *IAM Role* that the Lambda function assumes whenever it runs. This role has permissions tied to it so you can limit the scope of what the lambda function does. There are three options:
- *Create a new role with basic Lambda permissions*: Lambda creates a new IAM role with minimal permissions, ie. ability to send CloudWatch logs, for your Lambda. This is the one we've chosen for convenience.
- *Use an existing role*: Select a role which already exists.
- *Create a new role from AWS policy templates*: Creates an IAM role from several cookie-cutter policy templates.

Click *Create function* and wait for the lambda function to be created.

## Getting to know the UI

![Lambda UI designer section][lambda-ui-designer-section]
![Lambda UI code section][lambda-ui-code-section]

### Run it using a test event

### Attach a trigger to it like SNS

### Cloudwatch scheduled event trigger

### Update the function to return some JSON

### Hook it up to an API with lambda proxy integration

[console-navbar-region]: {{ site.images }}aws-console-navbar-region.png
[searchbar-lambda]: {{ site.images }}aws-console-search-lambda.png
[lambda-dash-create-fn-btn]: {{ site.images }}lambda-dashboard-create-function-button.png
[lambda-dash-create-fn-form]: {{ site.images }}lambda-dashboard-create-form.png

[lambda-ui-designer-section]: {{ site.images }}lambda-ui-designer-section.png
[lambda-ui-code-section]: {{ site.images }}lambda-ui-code-section.png
