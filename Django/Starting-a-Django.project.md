# Starting a Django Project

Django provides us with django-admin, a command-line utility that helps us with a variety of administrative tasks. We can use it with various commands by calling it in the terminal like this:

    django-admin <command> [options]

Running django-admin help will provide a list of possible commands.

A Django project can be easily created with the startproject command. It takes a couple of options– the name of the project and optionally the directory for our project. The full command would look like this:

    django-admin startproject projectname

Django will then create a directory for the project, or the project root folder.

    my-project/
      ├── my-project/
      └── manage.py

Inside the project root folder is a Python file, manage.py, that contains a collection of useful functions used to administer the project. This file performs the same actions as django-admin but is set specifically to the project. We can do a number of things with it, such as starting a server.

Alongside the manage.py is another directory with the same name as the project. This folder is treated as a Python package because of the presence of __ init__.py, and inside this directory contains important settings and configuration files for the project.

## Configuring Django Settings

With only a one-line command, Django has started a functioning project! Behind the scenes, Django will do all the configurations for us and store them in an inner directory with the same name as the project. Important for us are settings.py and urls.py. We can safely ignore the other files, just remember to not delete them by accident!

settings.py is a Python file that contains configurations that we’ll be editing throughout the development of our project. Inside, there is a list called INSTALLED_APPS which contains the apps that make up the Django project, more on these later. After running the startproject command, our settings.py should contain:

    INSTALLED_APPS = [
      'django.contrib.admin',
      'django.contrib.auth',
      'django.contrib.contenttypes',
      'django.contrib.sessions',
      'django.contrib.messages',
      'django.contrib.staticfiles',
    ]

We can see that Django pre-installs some common apps for us, such as admin, authentication, sessions, and an app to help manage static files. When we create new applications for the project, we have to include them here so that Django will know about them!

Further down in settings.py, is a dictionary named DATABASES. It looks like:

    DATABASES = {
      'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
      }
    }

We see that Django by default will set up an SQLite database for us. In later lessons, we’ll learn how to use it to store content.

Next, in the same directory where settings.py is located, is another Python file named urls.py. Inside are the URL declarations for this Django project, or a “table of contents” for the Django project. Remember earlier when we said that Django goes down a list of patterns to match a URL? This is that list!

When we first create the project, urls.py will include this:

    urlpatterns = [
      path('admin/', admin.site.urls),
    ]

This means that the admin app already has a route.

Since the project comes pre-configured, we can start a server to test that the project works. A development server can be started by using manage.py and providing the runserver command. This command must be run in the root directory, the same directory where manage.py is located. By default, Django will start a development server with port 8000, but an alternate port can be provided as an option.

The full command will look like this:

    python3 manage.py runserver <port number>

The Django development server will hot-reload as changes are made to the project, so we don’t have to keep restarting the server as we develop. The server will keep running until we stop it with the ctrl + c.

## Migrating the Database

When we started the server, Django gave us an error message that there were unapplied migrations:

You have 15 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.

A migration is a pending database change. As we saw in settings.py, by default, Django will have some apps installed. Some of these default apps, for example, the admin interface, use the database and the migrations must be applied to the SQLite database.

Whenever we make changes to the model of the database, we must apply the changes by running python3 manage.py migrate. After applying the migration, when we run the server our errors are gone.

By applying our migration, we have access to the admin app! The admin app comes pre-installed and can be navigated to since it has its URL provided in urls.py we saw earlier. At the moment there aren’t any admin users but we can still visit localhost/admin to see the admin login page.

## Django Apps

We’ve been talking about Django projects and apps for a while, but what exactly are apps? How are apps different from a project? Well, a Django app is a submodule to a project, that contains the code for a specific feature. In the submodule, we’ll find things like: a models.py file, a migration directory, and other files and directories related to the application. Django apps should be self-sufficient and in theory, can be picked up and placed in another project without any modification. A Django project refers to the entire code base and its parts. The Django project folder holds manage.py and the other module that includes settings.py.

In a real-world example, think of a website for a veterinarian’s office as a Django project. It would consist of smaller apps, such as an appointment calendar, patient profiles, and perhaps a testimonial section. Apps are part of what makes Django projects so scalable. Since they should be entirely self-sufficient, they shouldn’t break any parts as more features are added to a project. A Django app can be created by running the startapp command in the project root directory, the directory with manage.py, and providing the name of the app as an additional option.

    python3 manage.py startapp myapp

This will create a new directory called myapp alongside the project settings folder. Running startapp will result in the following folder structure.

    mysite/
    ├── manage.py
    └── mysite/
       ├── __init__.py
       ├── settings.py
       └── urls.py
    └── myapp/

Inside our project root folder, we have our previous folder which held our project settings and a new folder for our app. Inside it are files related specifically for the app such as models.py and tests.py.

In order for Django to be aware of the app’s existence, it needs to be added to the list of INSTALLED_APPS in the project’s settings.py file.

    INSTALLED_APPS = [
      "myapp.apps.MyappConfig"
    ]

## Creating a View for an App

Earlier, we discussed the MTV pattern and the integral role that views play. They are the information brokers in a Django application that decides what data gets delivered to a template and displayed. More simply put, a view is a class or function that processes a request and sends a response back.

In our veterinarian’s office example website, a customer might go to the /profile page of the website and their request gets passed to a view function to be processed. The view function may:

   + Check to see if the customer is logged in
   + Request their profile information from a database
  +  Format the information in a template
   + Send back the profile page as an HTML file for the customer to view in their browser

The view function does quite a bit of work!

At the core, Django uses a protocol called, Hypertext Transfer Protocol, which is the foundation for data communication on the worldwide web. In Django, requests, and responses are handled as HttpRequest and HttpResponse objects from a module called django.http.

When a page is requested:

  1.  Django creates an HttpRequest object that contains information about the request
  2.  Django loads the appropriate view, passing the HttpRequest as the first argument to the view function

Each view function is responsible for returning an HttpResponse object. The HttpResponse response object can be the HTML contents of a web page, a redirect, an error, an XML document, an image, or just about anything that can display on a web page.

A simple view function would look like this:

    # In views.py
    def index(request):
      return HttpResponse("This is the response!")

Above, we have an index() view function for our home page. When users visit our home page, the view function sends back an HttpResponse with the string "This is the response!" to be displayed on a web page.

## Using a View To Send an HTML Page

We just made a view that sends raw text to the browser. But, websites aren’t just plain text! In order to create stylish web pages, we mainly use HTML, CSS, and JavaScript.

We can use Django to render an HTML page when a view function is called. Django will look in each app folder inside INSTALLED_APPS for directories named templates. The best practice for structuring this folder is to namespace them. That is to place our HTML pages inside a directory that has the same name as your app within the templates/ directory.

The resulting templates folder structure will look like this:

    myapp/
    └── templates/
        └── myapp/
          └── mytemplate.html

The reason for this nested structure is if there was a template file with the same name in a different application, Django would be unable to distinguish between them. We need to be able to point Django at the right one and namespacing them ensures against future conflicts, so that apps lower down in the INSTALLED_APPS setting do not override previous templates.

With our file structure set up, we can build out the logic in our view function in views.py like so:

    from django.template import loader
    def home():
      template = loader.get_template("app/home.html")
      return HttpResponse(template.render())

In the above code, we import loader from django.template. Inside the view function (home()) we load the template with .get_template(). Then, we use the .render() method on the template object inside the HttpResponse object to send HTML pages to clients.

## Creating a Django Template

To place content generated from Django inside the HTML file, we need to turn our static HTML file into a template.

In the context of a web framework, templates are pages created with special markup that allows for backend data and commands to modify the contents of a page. Django employs a special syntax called Django Templating Language to distinguish itself from HTML, CSS, and JavaScript. That syntax in many template languages uses curly braces, sometimes referred to as handlebars, as a placeholder for data that is passed by Django.

In HTML, we use curly braces like this:

    <h1>Hello, {{name}}</h1>

When we call the view to render the template, we can use something called a context to tell Django what to replace in the template. The relationships in the context are referred to as a name/value pair. By default, a context is an empty dictionary. Our context for name will look like this inside the view function:

    context = {"name": "Junior"}

We then pass the context as an argument in the render function. The full view.py will look like this:

    from django.http import HttpResponse
    from django.template import loader
    def home(request):
      context = {"name": "Junior"}
      template = loader.get_template("app/home.html")
      return HttpResponse(template.render(context))

This would return a webpage that says “Hello, Junior” inside an < h1> tag.

It’s quite common in Django to load templates, fill their context, and return an HttpResponse object with their rendered template. Django provides a shortcut for this pattern called the render() function! The render() function will do the work of loading the template and provide the contexts when they are passed as arguments.

Our example above can be rewritten with the shortcut function like this:

from django.shortcuts import render

    def home(request):
      context = {"name": "Junior"}
      return render(request, "app/home.html", context)

Note that we no longer need to import loader and HttpResponse when we use the render() function. The render() function takes the request object as its first argument, a template name as its second argument, and a dictionary as an optional third argument that passes the context variables to the template.

## Wiring Up a View

On the internet, every page needs its own URL because each URL displays unique information. In Django, we can use something called a URLconf, for URL configuration. This module is a set of patterns that Django will try to match the requested URL to find the correct view.

An app’s URLconf is located in a file named urls.py inside the app’s directory. At the top of the urls.py we import the path object from django.urls and we import the view functions from views.py and add routes that direct to each of our view functions.

The urls.py will look like this:

    from django.urls import path
    from . import views

    urlpatterns = [
      path('', views.home),
      path('profile/', views.profile, name="profile")  
    ]

After the import statements is a list of patterns called urlpatterns, which contain the routes to each view function. Each route is provided as a path() object that has three arguments: the URL route as a string, the name of the function of the view, and an optional name used to refer to the view.

With the above example, when we navigate to the URL without any additional route, '', the home() view function will be called. Going to the URL ending with /profile will call the profile() view function.

To make Django aware of the app’s URLconf, it must be included in the project’s URLconf, also called urls.py.

The default urls.py folder for a project looks like this:

    from django.contrib import admin
    from django.urls import path

    urlpatterns = [
      path("admin/", admin.site.urls),
    ]

We can see that Django already includes some URLs for us in urlpatterns. The admin page we visited earlier is already there: path('admin/', admin.site.urls).

To include the app’s URLconf we import the include path from django.urls and add a path()to the urlpatterns.

    from django.contrib import admin
    from django.urls import include, path

    urlpatterns = [
      path("admin/", admin.site.urls),
      path("", include("myapp.urls")),
    ]

With both URLconfs set up, we can properly view our routes for the application: myapp in a web browser.

