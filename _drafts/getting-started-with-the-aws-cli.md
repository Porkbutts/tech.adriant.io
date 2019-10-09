---
layout: post
title: Getting started with the AWS Command-Line Interface
categories: aws
tags: tutorial
---

In this tutorial you'll install the AWS command line interface and learn how to set up an IAM user with programmatic access to AWS resources. This tutorial assumes you have basic command-line knowledge on either Mac or a unix-like operating system.

 <!--more-->

## Installing the AWS CLI (Command-Line Interface)

Make sure you have `python` and `pip` installed. `pip` is a tool for installing python packages. You can check that you have them installed using these commands.

```bash
$ python --version
Python 2.7.16

$ pip --version
pip 19.1.1 from /usr/local/lib/python2.7/site-packages/pip (python 2.7)
```

Next install the `awscli` package. Note that your output may look different from mine.

```bash
$ pip install --user awscli
DEPRECATION: Python 2.7 will reach the end of its life on January 1st, 2020. Please upgrade your Python as Python 2.7 won't be maintained after that date. A future version of pip will drop support for Python 2.7.
Requirement already satisfied: awscli in /usr/local/lib/python2.7/site-packages (1.16.72)
Requirement already satisfied: docutils>=0.10 in /usr/local/lib/python2.7/site-packages (from awscli) (0.14)
Requirement already satisfied: botocore==1.12.62 in /usr/local/lib/python2.7/site-packages (from awscli) (1.12.62)
Requirement already satisfied: PyYAML<=3.13,>=3.10 in /usr/local/lib/python2.7/site-packages (from awscli) (3.13)
Requirement already satisfied: s3transfer<0.2.0,>=0.1.12 in /usr/local/lib/python2.7/site-packages (from awscli) (0.1.13)
Requirement already satisfied: rsa<=3.5.0,>=3.1.2 in /usr/local/lib/python2.7/site-packages (from awscli) (3.4.2)
Requirement already satisfied: colorama<=0.3.9,>=0.2.5 in /usr/local/lib/python2.7/site-packages (from awscli) (0.3.9)
Requirement already satisfied: urllib3<1.25,>=1.20; python_version == "2.7" in /usr/local/lib/python2.7/site-packages (from botocore==1.12.62->awscli) (1.24.1)
Requirement already satisfied: jmespath<1.0.0,>=0.7.1 in /usr/local/lib/python2.7/site-packages (from botocore==1.12.62->awscli) (0.9.3)
Requirement already satisfied: python-dateutil<3.0.0,>=2.1; python_version >= "2.7" in /usr/local/lib/python2.7/site-packages (from botocore==1.12.62->awscli) (2.7.5)
Requirement already satisfied: futures<4.0.0,>=2.2.0; python_version == "2.6" or python_version == "2.7" in /usr/local/lib/python2.7/site-packages (from s3transfer<0.2.0,>=0.1.12->awscli) (3.2.0)
Requirement already satisfied: pyasn1>=0.1.3 in /usr/local/lib/python2.7/site-packages (from rsa<=3.5.0,>=3.1.2->awscli) (0.4.4)
Requirement already satisfied: six>=1.5 in /usr/local/lib/python2.7/site-packages (from python-dateutil<3.0.0,>=2.1; python_version >= "2.7"->botocore==1.12.62->awscli) (1.10.0)
```

Verify that the `awscli` tool was successfully installed.

```bash
$ aws --version
aws-cli/1.16.72 Python/2.7.16 Darwin/17.7.0 botocore/1.12.62
```

In order to make use of the `awscli` tool, you will need programmatic access keys that allow the `awscli` to *talk* to the Amazon Web Services API. API stands for **Application Program Interface** and Web APIs in particular have become a standard practice for enabling programmatic interaction with web services.

## What is an IAM User?
In this next section, you're going to create an **IAM User** from the AWS Console. IAM stands for **Identity and Access Management** and it is used extensively in AWS to allow or deny permission to resources and services.

When you first create an AWS account, you can only login as the **AWS Account Root User**. This user has the permission to do anything and everything in your account. If you create access keys for the root user and the keys are compromised, there is no limit to what a malicious actor can do in your account. You could wake up one morning to [find out that tens of thousands of dollars in charges](https://www.reddit.com/r/aws/comments/8rj9ep/my_aws_account_was_hacked/) were incurred to your account.

Therefore, it's generally recommended to create another user or set of users with limited access, while keeping the root account credentials securely locked away at all times.

### Create the IAM User
