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

When you first create an AWS account, you can only login as the **AWS Account Root User**. This user has the permission to do anything and everything in your account. If you create access keys for the root user and the keys are compromised, there is no limit to what a malicious actor can do in your account, and you could wake up one morning to an AWS bill for tens of thousands of dollars.

It's generally recommended to create another user or set of users with limited access, while keeping the root account credentials securely locked away. However, since IAM is beyond the scope of this tutorial, we'll be creating a user with very permissive access for the sake of convenience. Please note this is only a slight improvement from using the root account directly and is not very secure nor recommended for a production setup.

### Create the IAM User
Log in to the AWS console and search for the IAM service.
![AWS Console searchbar IAM][searchbar-iam]


Click on the *Users* link.

![IAM dashboard users link][users-link]

Click on the *Add user* button.

![IAM dashboard add user button][add-users-btn]

Fill in the username and make sure to check *Programmatic access*. Click *Next: Permissions*.

![Add user page one][create-usr-1]

Click on *Attach existing policies directly* and search for **PowerUserAccess**. Select the policy and click *Next: Tags*.

![Select PowerUserAccess policy][poweruser-policy]

Skip the tags section and click *Next: Review*. The summary should look something like this.

![Create user summary][review-create]

The next page shows that IAM User creation was successful. The *Access Key ID* will be displayed, but you will have to click *Show* to display the *Secret access key*. You will need to take note of both of these keys for CLI access.

![Display access and secret key][access-key-secret-key]

**Note that for security reasons, you will not be able to look up the secret access key after this point**. If you end up losing access to your secret access key, you will have to create a new set of access keys, but not necessarily a new user.

## Update the CLI to use access keys
Run the `aws configure` command which will prompt you for the access and secret key. You can leave the region and output as their defaults. This command will create two files `~/.aws/credentials` and `~/.aws/config` and update their contents with the information you specified. You can always update these files directly rather than using the `aws configure` command.

The `awscli` tool should now be configured to use the `default` profile which uses your access keys.

## Summary
You created an **IAM User** with programmatic access and attached the **PowerUserAccess** policy to the new user. This gives the user programmatic access to do most things in AWS, with the exception being creation of *other* IAM resources.

You noted the *Access Key ID* and *Secret access key* for the new user and updated your AWS credentials file with these keys.


[searchbar-iam]: {{ site.images }}aws-console-search-iam.png
[users-link]: {{ site.images }}iam-dashboard-select-users.png
[add-users-btn]: {{ site.images }}iam-dashboard-add-user-button.png
[create-usr-1]: {{ site.images }}iam-create-user-page-one.png
[poweruser-policy]: {{ site.images }}attach-power-user-iam-policy.png
[review-create]: {{ site.images }}iam-user-create-review.png
[access-key-secret-key]: {{ site.images }}access-key-secret-key.png
