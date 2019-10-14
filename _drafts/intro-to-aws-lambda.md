---
layout: post
title: Introduction to AWS Lambda Functions
categories: aws
tags: lambda
---

AWS Lambda is Amazon's *function as a service* product. In other words, it's a service that lets you package and run code without having to provision or manage servers.

The basic premise is that you write some code in one of Lambda's supported languages, you package and upload this code to Lambda, and now you have a *Lambda function* that can be run on demand. The Lambda function can then be triggered from other AWS services such as SNS, SQS, API Gateway, and Cloudwatch events.

Another benefit of Lambda is its ability to scale horizontally. When an event comes in, Lambda creates an instance of your lambda function. If more events come in while the instance is still in the middle of executing, then Lambda spawns more instances of your function.

 <!--more-->

## Todo
