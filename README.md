# The Request-Response Cycle

## Learning Goals

- Build and run a Flask application on your computer.
- Manipulate and test the structure of a request object.

***

## Key Vocab

- **Web Framework**: software that is designed to support the development of
  web applications. Web frameworks provide built-in tools for generating web
  servers, turning Python objects into HTML, and more.
- **Extension**: a package or module that adds functionality to a Flask
  application that it does not have by default.
- **Request**: an attempt by one machine to contact another over the internet.
- **Client**: an application or machine that accesses services being provided
  by a server through the internet.
- **Web Server**: a combination of software and hardware that uses Hypertext
  Transfer Protocol (HTTP) and other protocols to respond to requests made
  over the internet.
- **Web Server Gateway Interface (WSGI)**: an interface between web servers
  and applications.
- **Template Engine**: software that takes in strings with tokenized
  values, replacing the tokens with their values as output in a web browser.

***

## Introduction

Web browsers cannot execute Python code. To make our views show up in the
browser, Flask needs to translate HTTP requests into Python objects and new
Python objects into HTTP responses. There are plenty of strategies to do this
by hand, but Flask makes our lives easier with Werkzeug- you'll find that Flask
generates WSGI maps for your application with little to no manual configuration
on your part.

Let's take a look under the hood at the request-response cycle in Flask
applications.

***

## Application and Request Contexts

When a Flask application gets a request from the browser, it has to pass some
specific objects to the view function that will respond to that request. One
example is the `request` object itself, which contains the HTTP request from the
browser.

You may have noticed in the past few lessons, though, that view functions do not
take `request` objects as arguments. Since every view function needs access to
a `request` object- among other things- Flask manages requests through
**contexts.**

Let's take a look at a simple view function that uses a request object:

```py
# app/flask_app.py

from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    host = request.headers.get('Host')
    return f'<h1>The host for this page is {host}</h1>'

if __name__ == '__main__':
    app.run()

```

Navigating to `127.0.0.1:5000`, you should see the following:

![Simple web page with the text "The host for this page is 127.0.0.1:5000"](
https://curriculum-content.s3.amazonaws.com/python/flask-request-response-cycle-index.png
)

This might seem a bit odd. While we did import `request`, we didn't assign it
any attributes that would tell it about the activity on our server. It almost
seems like a **global** variable- one that is set outside of our application
instances and views that provides an unchanging set of information. That
wouldn't make much sense as an implementation, though: our application will be
handling many requests, often overlapping with one another while multiple users
are visiting our website.

Flask generates a context for requests after receiving a request and before our
application runs. When `request` is called, we have access to all of that
request data without having to do any configuration or include a `request`
argument to our view.

If you're testing `request` for a specific app outside of any views, you will
have to generate this context manually. This only requires two commands:

```py
# example only- no need to write this out

from flask_app import app
from flask import request

request_context = app.test_request_context()
request_context.push()
```

As the name `test_request_context()` suggests, this only provides test data.
You won't use this in your applications, but you might see it in the tests
for Phase 4's labs.

Flask also has an **application context**. This works very much the same way as
a request context: when a request is received, Flask generates the application
context. When the application instance is accessed, the application context
becomes available to our app and views. This provides information on the
application we're working on and is accessible through the `flask.current_app`
object.

```py
# app/flask_app.py

from flask import Flask, request, current_app

app = Flask(__name__)

@app.route('/')
def index():
    host = request.headers.get('Host')
    appname = current_app.name
    return f'''<h1>The host for this page is {host}</h1>
               <h2>The name of this application is {appname}</h2>'''

if __name__ == '__main__':
    app.run()

```

***

## Lesson Section

Lorem ipsum dolor sit amet. Ut velit fugit et porro voluptas quia sequi quo
libero autem qui similique placeat eum velit autem aut repellendus quia. Et
Quis magni ut fugit obcaecati in expedita fugiat est iste rerum qui ipsam
ducimus et quaerat maxime sit eaque minus. Est molestias voluptatem et nostrum
recusandae qui incidunt Quis 33 ipsum perferendis sed similique architecto.

```py
# python code block
print("statement")
# => statement
```

```js
// javascript code block
console.log("use these for comparisons between languages.")
// => use these for comparisons between languages.
```

```console
echo "bash/zshell statement"
# => bash/zshell statement
```

<details>
  <summary>
    <em>Check for understanding text goes here! <code>Code statements go here.</code></em>
  </summary>

  <h3>Answer.</h3>
  <p>Elaboration on answer.</p>
</details>
<br/>

***

## Instructions

This is a **test-driven lab**. Run `pipenv install` to create your virtual
environment and `pipenv shell` to enter the virtual environment. Then run
`pytest -x` to run your tests. Use these instructions and `pytest`'s error
messages to complete your work in the `lib/` folder.

Instructions begin here:

- Make sure to specify any class, method, variable, module, package names
  that `pytest` will check for.
- Any other instructions go here.

Once all of your tests are passing, commit and push your work using `git` to
submit.

***

## Conclusion

Conclusion summary paragraph. Include common misconceptions and what students
will be able to do moving forward.

***

## Resources

- [Resource 1](https://www.python.org/doc/essays/blurb/)
- [Reused Resource][reused resource]

[reused resource]: https://docs.python.org/3/
