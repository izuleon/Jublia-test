
<h3 align="center">Event Mail</h3>

<div align="center">

[![Status]]()
[![GitHub Issues]](https://github.com/izuleon/Jublia-test/issues)
[![GitHub Pull Requests]](https://github.com/izuleon/Jublia-test/pulls)
[![License]](/LICENSE)

</div>

---

<p align="center"> e-mail scheduler based on event
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Built Using](#built_using)
- [TODO](../TODO.md)
- [Contributing](../CONTRIBUTING.md)
- [Authors](#authors)
- [Acknowledgments](#acknowledgement)

## 🧐 About <a name = "about"></a>

For sending mass email to a certain group or event at a scheduled time

## 🏁 Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites


```
python ^3.12.2
pip ^24.0
```

### Installing

A step by step series of examples that tell you how to get a development env running.

Installing requirement
```
pip install -r requirement.txt
```

alembic migrations (if needed to)
```
alembic upgrade head
```

Running aplication
```
python main.py
```

## 🎈 Usage <a name="usage"></a>
Saving emails
```
{baseurl}/save_emails[POST]
```
list of all available emails scheduled
```
{baseurl}/event_mails/
```
specific emails scheduled
```
{baseurl}/event_mails/<id>
```
list of all available event_id
```
{baseurl}/recipient/
```
save recipient
```
{baseurl}/recipient/[POST]
```
list of all registered recipient in an event id
```
{baseurl}/recipient/event/<event_id>
```
specific registered recipient
```
{baseurl}/recipient/id/<id>
```

## 🔧 Running the tests <a name = "tests"></a>

Explain how to run the automated tests for this system.

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## 🚀 Deployment <a name = "deployment"></a>

Add additional notes about how to deploy this on a live system.

## ⛏️ Built Using <a name = "built_using"></a>

- [SQLAlchemy](https://docs.sqlalchemy.org/) - Database ORM
- [Alembic](https://alembic.sqlalchemy.org/) - Database migration management
- [Flask](https://flask.palletsprojects.com/) - Web Framework

## ✍️ Authors <a name = "authors"></a>

- [@izuleon](https://github.com/izuleon) - Idea & Initial work

See also the list of [contributors](https://github.com/izuleon/Jublia-test/contributors) who participated in this project.
