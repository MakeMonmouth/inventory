# Inventory

An inventory platform for Wye Make.

SnipeIT is overly complicated, Homebox doesn't have the features we need, so we're writing our own.

## Goals

This system has been written to adhere to the following goals:

### 1. API-Driven

If you're not a developer, this probably means nothing to you, but it enables us to talk to the system from just about anything else including our website, our membership system, Discord, and even Smart Assistants such as Amazon Alexa and Google Home.

It means the system remains flexible and can be updated without worrying about how people access it.

### 2. Tailored to our needs

As a makerspace, we have a number of requirements that other systems either don't have or make overly complex.

Whilst we will release the code "early and often", we will not release a version 1.0 until the following features are in place:

   - [ ] The ability to add and remove items
   - [ ] The ability to add items to a specific location
   - [ ] The ability to "nest" locations (i.e. "The hammer is in toolbox 01 which is stored in cupboard 9 in room 5 of the space")
   - [ ] The ability to "loan" equipment to members
   - [ ] The ability to track stock of consumables and who is using them

### 3. Open Source

The platform will use Open Source software.  

The backend will be written using the [Django](https://www.djangoproject.com/) framework and [Treebeard](https://django-treebeard.readthedocs.io/en/latest/tutorial.html) to deal with nested locations, the API is provided by the [Django Rest Framework (DRF)](https://www.django-rest-framework.org/).

The platform is backed by the PostgreSQL database, and application performance is measured using the [Open Telemetry](https://opentelemetry.io) framework.

The project itself is released under the [MIT Licence](https://choosealicense.com/licenses/mit/) and we hope that this will encourage anyone who uses the platform to donate their improvements back to the original code base.


