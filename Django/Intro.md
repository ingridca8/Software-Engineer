## Servers

We talked about how the front-end consists of the information sent to a client so that a user can see and interact with a website, but where does the information come from? The answer is a web server.

The word “server” can mean a lot of things in computing, but we’re going to focus on web servers specifically. A web server is a process running on a computer that listens for incoming requests for information over the internet and sends back responses. Each time a user navigates to a website on their browser, the browser makes a request to the web server of that website. Every website has at least one web server. A large company like Facebook has thousands of powerful computers running web servers in facilities located all around the world which are listening for requests, but we could also run a simple web server from our own computer!

The specific format of a request (and the resulting response) is called the protocol. You might be familiar with the protocol used to access websites: HTTP. When a visitor navigates to a website on their browser, similarly to how one places an order for takeout, they make an HTTP request for the resources that make up that site.

For the simplest websites, a client makes a single request. The web server receives that request and sends the client a response containing everything needed to view the website. This is called a static website. This doesn’t mean the website is not interactive. As with the individual static assets, a website is static because once those files are received, they don’t change or move. A static website might be a good choice for a simple personal website with a short bio and family photos. A user navigating Twitter, however, wants access to new content as it’s created, which a static website couldn’t provide.

A static website is like ordering takeout, but modern web applications are like dining in person at a sit-down restaurant. A restaurant patron might order drinks, different courses, make substitutions, or ask questions of the waiter. To accomplish this level of complexity, an equally complex back-end is required.

## What is the Back-end?

When a user navigates to google.com, their request specifies the URL but not the filename for today’s Google Doodle. The web application’s back-end will need to hold the logic for deciding which assets to send. Moreover, modern web applications often cater to the specific user rather than sending the same files to every visitor of a webpage. This is known as dynamic content.

When we eat at a restaurant, we’ll order to our tastes, make substitutions, etc; the result is a dining experience unique to us. Aside from that, there’s a lot happening behind the scenes to make a restaurant work: ingredients are ordered from suppliers, new menus are designed, and employees’ schedules are created. Similarly, to make a web application that runs smoothly, the back-end is doing a lot more than simply sending assets to browsers.

The collection of programming logic required to deliver dynamic content to a client, manage security, process payments, and myriad other tasks is sometimes known as the “application” or application server. The application server can be responsible for anything from sending an email confirmation after a purchase to running the complicated algorithms a search engine uses to give us meaningful results.

## What is an API?

When a user navigates to a specific item for sale on an e-commerce site, the price listed for that item is stored in a database, and when they purchase it, the database will need to be updated with the correct inventory for that item type. In fact, much of what the back-end entails is reading, updating, or deleting information stored in a database.

In order to have consistent ways of interacting with data, a back-end will often include a web API. API stands for Application Programming Interface and can mean a lot of different things, but a web API is a collection of predefined ways of, or rules for, interacting with a web application’s data, often through an HTTP request-response cycle. Unlike the HTTP requests a client makes when a user navigates to a website’s URL, this type of request indicates how it would like to interact with a web application’s data (create new data, read existing data, update existing data, or delete existing data), and it receives some data back as a response.

Let’s walk through the example of making an online purchase again, but this time, we’ll imagine how the application’s web API might be used. When a user presses the button to submit an order, that will trigger a request to send them to a different view of the website, an order confirmation page, but an additional request will be triggered from the front-end, unseen by the user, to the web API so that the database can be updated with the information from the order.

Some web APIs are open to the public. Instagram, for example, has an API that other developers can use to access some of the data Instagram stores. Others are only used by the web application internally— Codecademy, for example, has a web API that employees use to accomplish internal tasks.

## Authorization and Authentication

Two other concepts we’ll want our server-side logic to handle are authentication and authorization.

Authentication is the process of validating the identity of a user. One technique for authentication is to use logins with usernames and passwords. These credentials need to be securely stored in the back-end on a database and checked upon each visit. Web applications can also use external resources for authentication. You’ve likely logged into a website or application using your Facebook, Google, or Github credentials; that’s also an authentication process.

Authorization controls which users have access to which resources and actions. Certain application views, like the page to edit a social media personal profile, are only accessible to that user. Other activities, like deleting a post, are often similarly restricted.

When building a robust web application back-end, we need to incorporate both authentication (Who is this user? Are they who they claim to be?) and authorization (Who is allowed to do and see what?) into our server-side logic to make sure we’re creating secure, personalized, and dynamic content.


## What is a Web Framework?

Let’s first establish what it means when we say Django is a web framework.

Web frameworks are a type of software development tool that makes it easier and faster to develop web applications. They are a type of code library that provides code and patterns for database access, as well as templating systems for content. They promote code reuse, so we don’t have to write as much code to get a project running. Some features most web frameworks include are:

    URL routing
    Input form management and validation
    Templating engines for HTML and CSS
    Database configuration
    Web security
    Session repository and retrieval

Out of the box, Django comes with an admin panel, a user authentication system, a database, and something called object-relational mapper (ORM) that helps a web application interact with a database. These are some of the “batteries” included in Django to help build projects faster without having to worry about which tools to use.

Later we’ll see how we can bootstrap a fully featured web application in only a handful of commands.

## How Django Works

Before we create our first Django web app, let’s take a little look into how Django works underneath the hood. The Django project describes itself as an MTV framework, using Models, Templates and Views. Let’s break down these components:

    The model portion deals with data and databases, it can retrieve, store, and change data in a database.
    The template determines how the data looks on a web page.
    The view describes the data to be presented, and passes this information to the template.

With the basics of the components explained let’s understand how they work together when we visit a Django website. When a request comes to a web server, it’s passed to Django to figure out what is requested. A client requests a URL, let’s use codecademy.com as an example, Django will take the web address and pass it to its urlresolver. Django will try to match the URL to a list of patterns, and if there is a match, then pass the request to the associated view function.

Imagine a mail carrier delivering a letter. They walk down the street checking each house number until they find the exact one on the letter. Once they find the house, they deliver the letter. That’s how the urlresolver works!

When we land on the right page, Django uses data from the model and feeds it into the view function to determine what data is shown. That data is given to the template and presented to us via the web page.

This is a bit of a simplified version of what Django is doing underneath the hood, but a key takeaway is that Django follows this MTV pattern.
