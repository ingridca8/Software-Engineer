## Make a Request

Making a request with Requests is very simple.

Begin by importing the Requests module:

    import requests

Now, let’s try to get a webpage. For this example, let’s get GitHub’s public timeline:

    r = requests.get('https://api.github.com/events')

Now, we have a Response object called r. We can get all the information we need from this object.

Requests’ simple API means that all forms of HTTP request are as obvious. For example, this is how you make an HTTP POST request:

    r = requests.post('https://httpbin.org/post', data={'key': 'value'})

Nice, right? What about the other HTTP request types: PUT, DELETE, HEAD and OPTIONS? These are all just as simple:

    r = requests.put('https://httpbin.org/put', data={'key': 'value'})

    r = requests.delete('https://httpbin.org/delete')

    r = requests.head('https://httpbin.org/get')

    r = requests.options('https://httpbin.org/get')


## Passing Parameters In URLs

You often want to send some sort of data in the URL’s query string. If you were constructing the URL by hand, this data would be given as key/value pairs in the URL after a question mark, e.g. httpbin.org/get?key=val. Requests allows you to provide these arguments as a dictionary of strings, using the params keyword argument. As an example, if you wanted to pass key1=value1 and key2=value2 to httpbin.org/get, you would use the following code:

    payload = {'key1': 'value1', 'key2': 'value2'}

    r = requests.get('https://httpbin.org/get', params=payload)

You can see that the URL has been correctly encoded by printing the URL:

    print(r.url)
    $ https://httpbin.org/get?key2=value2&key1=value1

This sintax will work as well for key, tpkens or pws.

Note that any dictionary key whose value is None will not be added to the URL’s query string.

You can also pass a list of items as a value:

    payload = {'key1': 'value1', 'key2': ['value2', 'value3']}

    r = requests.get('https://httpbin.org/get', params=payload)

    print(r.url)
    $ https://httpbin.org/get?key1=value1&key2=value2&key2=value3

# Sources
[Quickstart](https://requests.readthedocs.io/en/latest/user/quickstart/)

[Requests: HTTP for Humans](https://docs.python-requests.org/en/latest/index.html)
