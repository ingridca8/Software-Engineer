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
