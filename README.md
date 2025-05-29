# Eco-Fitness - E-commerce Website

**Eco-Fitness** is a Django-based e-commerce website designed to offer eco-friendly fitness products while promoting sustainability. It allows users to browse, purchase, and review products, subscribe to eco-conscious pricing plans, and engage in community discussions. This project serves as an example of a full-stack, cloud-hosted, commercial-grade e-commerce application.

The platform integrates secure payment systems, advanced UX design, SEO optimization, role-based authentication, and several marketing features to ensure a seamless and engaging experience for users.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Business Model](#business-model)
- [Learning Outcomes](#learning-outcomes)
  - [LO1: Integrating E-commerce Payment System](#lo1-integrating-e-commerce-payment-system)
  - [LO2: Advanced UX Design](#lo2-advanced-ux-design)
  - [LO3: Search Engine Optimization (SEO)](#lo3-search-engine-optimization-seo)
  - [LO4: Authentication and Authorization](#lo4-authentication-and-authorization)
  - [LO5: Marketing Techniques](#lo5-marketing-techniques)
  - [LO6: E-commerce Fundamentals](#lo6-e-commerce-fundamentals)
- [Technologies Used](#technologies-used)
- [Project Setup](#project-setup)
  - [Requirements](#requirements)
  - [Installation](#installation)
  - [Running the Application](#running-the-application)
  - [Deployment Procedure](#deployment-procedure)
- [App Breakdown](#app-breakdown)
  - [About Us](#about-us)
  - [Pricing Plans](#pricing-plans)
  - [Reviews](#reviews)
  - [Shop](#shop)
  - [Community](#community)
  - [Contact](#contact)
  - [Products](#products)
  - [Account](#account)
  - [Login](#login)
  - [Logout](#logout)
  - [Cart](#cart)
  - [Bag](#bag)
- [Testing](#testing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

---

## Project Overview

**Eco-Fitness** is a web-based application built using Django, designed to promote eco-friendly fitness products. It incorporates an interactive frontend with e-commerce capabilities, providing users with a shopping cart, checkout process, product reviews, and account management. The website also enables users to subscribe to different pricing plans based on their needs, engage in community discussions, and access educational content on eco-friendly fitness practices.

E-commerce Business Model
This project follows a Business-to-Consumer (B2C) model.
The application, Eco Fitness, is designed to sell sustainable fitness products, eco-friendly workout gear, and personalized fitness plans directly to individual customers who are looking to achieve their fitness goals while supporting environmentally conscious initiatives.

Purpose of the Application:
To promote a healthy lifestyle combined with environmental sustainability.

To create a community of eco-conscious fitness enthusiasts.

To provide consumers with eco-friendly alternatives for their fitness needs.

Core Business Intents:
Offer premium, sustainable fitness products and personalized meal/workout plans.

Build a loyal customer base by encouraging repeat purchases through community engagement and valuable content.

Promote sustainability by aligning the brand with eco-conscious values.

Marketing Strategies:
Engage customers through a vibrant online community where users share their fitness journeys.

Promote products and services through targeted email campaigns and social media marketing.

Highlight customer testimonials and user-generated content to build brand trust and authenticity.

Offer incentives like subscription-based plans and discounts for loyal customers.

---

## Business Model

**Eco-Fitness** follows a direct-to-consumer e-commerce business model, which integrates several key components:

1. **Product Sales**: The core revenue stream comes from selling eco-friendly fitness products, ranging from gym equipment to accessories.
2. **Subscription Plans**: Users can subscribe to different pricing plans, which offer perks such as discounted products, access to exclusive community content, and free shipping.
3. **Community Engagement**: By fostering an online community, Eco-Fitness enhances customer loyalty and creates a sense of belonging among users. The platform encourages interaction through fitness challenges, shared goals, and discussions on eco-friendly living.
4. **Reviews & Recommendations**: Users can leave reviews for products they purchase, which enhances the credibility and trustworthiness of the platform, and encourages more purchases.
5. **Sustainability Focus**: The business model revolves around sustainability, focusing on products that are eco-friendly, promoting ethical business practices, and educating users on the benefits of fitness products that are kind to the planet.

---

## Learning Outcomes

### LO1: Integrate an E-commerce Payment System

- **1.1** Integrated **Stripe** for payment processing, allowing users to securely purchase products and subscribe to pricing plans.
- **1.2** Implemented a feedback system to notify users of the status of their purchases, including success and error messages.
- **1.3** Built a full-stack Django web application with interactive front-end and relational database to store product details, user data, orders, etc.
- **1.4** Developed forms with validation, allowing users to create and edit data, such as personal details, shipping addresses, and payment information.
- **1.5** Organized the project structure according to Django conventions to ensure scalability and maintainability.
- **1.6** Followed best practices for clean code, ensuring readability and maintainability.
- **1.7** Structured URL patterns consistently across all apps, providing clear paths for navigation.
- **1.8** Designed a main navigation menu and structured layout for ease of use and accessibility.
- **1.9** Integrated custom logic in Python for handling product inventory, cart functionality, and checkout processes.
- **1.10** Used compound statements, loops, and conditional statements to handle product quantity updates and cart management.
- **1.11** Created a relational database schema with clear relationships between entities such as Users, Products, Orders, and Reviews.
- **1.12** Developed three custom Django models: Product, Order, and Review.
- **1.13** Implemented CRUD functionality for all models, allowing the creation, updating, retrieval, and deletion of records.
- **1.14** Deployed the application to **Heroku**, ensuring the production version matches the development environment.
- **1.15** Removed any commented-out code and ensured all internal links were functional in the deployed version.
- **1.16** Secured the deployment environment, ensuring no passwords or secret keys are committed to the git repository, and enabling proper environment variables.
- **1.17** Utilized Git for version control with detailed commit messages and a consistent workflow. Commits are made regularly to ensure all changes are properly tracked. Each commit includes documentation updates reflecting changes made.
- **1.18** Structured the project README using consistent markdown formatting, providing clear documentation of the setup, installation, and features.
- **1.19** Documented the full deployment procedure, including database setup, testing, and application deployment steps.

### LO2: Advanced UX Design

- **2.1** Created a clean and responsive front-end design following UX principles, ensuring accessibility and ease of navigation.
- **2.2** Mapped user stories to project goals, ensuring the platform meets the needs of fitness enthusiasts and environmentally-conscious consumers.
- **2.3** Implemented both manual and automated tests to evaluate the functionality and responsiveness of the application across different devices.
- **2.4** Demonstrated a clear rationale for the development of the project in the README, addressing user needs and explaining the product's value.
- **2.5** Documented the UX design process, including wireframes and mockups created during the design phase.
- **2.6** Managed the project’s planning and implementation using **Trello** to track progress and prioritize tasks.
- **2.7** Documented all user stories and mapped them to the project in **Trello**, ensuring transparent development progress.

### LO3: Search Engine Optimization (SEO)

- **3.1** Ensured that all pages are reachable via internal links to improve crawlability.
- **3.2** Included meta description tags in the HTML for all pages to provide search engines with context.
- **3.3** Set a descriptive site title for the application, ensuring it's relevant for search engines.
- **3.4** Used the `nofollow` attribute for external paid links and `sponsored` for compensated links to avoid link manipulation.
- **3.5** Added a sitemap.xml file to assist search engine bots in crawling the site.
- **3.6** Included a robots.txt file to guide search engine bots on what content to crawl and index.
- **3.7** Designed a custom 404 error page with a friendly redirect for non-existent pages.
- **3.8** Ensured all content is purposeful, avoiding placeholder text and providing relevant information for SEO optimization.

### LO4: Authentication and Authorization

- **4.1** Implemented a user authentication system, allowing users to register, log in, and manage their accounts securely.
- **4.2** Restricted login and registration pages to anonymous users only.
- **4.3** Ensured that non-admin users cannot directly access or manipulate backend data.
- **4.4** Implemented role-based authentication, allowing different user permissions for regular users, admins, and staff.
- **4.5** Displayed the current login state in the user interface.
- **4.6** Prevented non-authenticated users from accessing restricted content before logging in.

### LO5: Marketing Techniques

- **5.1** Created a **Facebook Business Page** dedicated to **Eco-Fitness**, promoting brand awareness and customer engagement.
- **5.2** Added a **newsletter signup form** to the website, allowing users to receive updates on promotions, new products, and fitness tips.

### LO6: E-commerce Fundamentals

- **6.1** Implemented an **eco-friendly fitness product store**, focusing on sustainability and ethical business practices. 

---

## Technologies Used

- **Django**: Backend framework used to build the web application.
- **Stripe**: Payment processing integration for secure online transactions.
- **PostgreSQL**: Database system for storing user and product data.
- **HTML/CSS/JavaScript**: Front-end technologies for building the user interface.
- **Bootstrap**: CSS framework used for creating responsive and stylish web pages.
- **Git**: Version control to track changes and collaborate on the project.
- **Heroku**: Cloud platform used for deploying the application.

---
## WireFrame
![Image](https://github.com/user-attachments/assets/ca82dc1d-1403-4982-8ad0-af37c8d2534b)

![Image](https://github.com/user-attachments/assets/10f8a88a-ff42-477c-b66b-b648bd787fb7)

## MockUp

![Image](https://github.com/user-attachments/assets/bca3095e-34e1-4571-a885-6f92d786f3ae)

## ERD Diagram 
🗺️ ERD (Entity Relationship Diagram) Breakdown
This ERD maps out the core structure of the backend — basically, how all the models in the database are connected and what data is being stored behind the scenes.

At the heart of it, we’ve got the Django User model (which handles all the built-in auth stuff like login, email, password, etc.), and that links directly to a custom AccountProfile model — where we store all the extra bits like the user’s default address, phone number, and shipping details.

Then we’ve got the products side:

Products belong to categories (like supplements, fitness plans, or activewear).

Users can leave reviews on products.

Some products are bundled together in special bundles with a discounted price.

On the checkout/order side:

Orders are created when a user checks out.

Each order can have multiple order line items (which tracks what was ordered, the size if relevant, and quantity).

We also store things like delivery costs, Stripe payment ID, and timestamps for when the order was placed.

There’s also the subscription system, which ties each user to a Stripe subscription (handy for premium plans or members-only content).

Outside of ecommerce, we’ve got:

A blog/community area where admins can post content.

A contact message model that stores user messages from the contact form.

A newsletter model that tracks subscribed emails.

An About Us model that holds the page content for our mission/vision.

It’s all designed to be modular and scalable, so each feature (shop, profile, blog, etc.) has its own clear structure and can grow independently.

Here is my ERD:
![Image](https://github.com/user-attachments/assets/417196db-d5e5-4669-bc38-d052d4d3289d)

## Facebook
![Image](https://github.com/user-attachments/assets/b028d540-b3b9-4d76-93ec-1716601c72b8)
Follow these steps to set up your Facebook page and start building a community for your eco-friendly fitness website.

1. Log In to Facebook
First, log into the Facebook account you want to use for your business.

2. Create Your Page
Go to Pages from the Facebook menu.

Click Create New Page.

Add your Page Name (like your website name) and pick a Category (e.g., "Fitness" or "Eco-Friendly Products").

3. Add Bio & Description
Write a short, clear description of your eco-friendly fitness brand. Mention your focus on sustainability and health.

Example:

GreenFit Eco Fitness offers eco-friendly fitness products and content to help you stay healthy while caring for the planet.

4. Upload Photos
Profile Picture: Upload your logo or a brand image.

Cover Photo: Pick an image that reflects your brand’s eco-friendly and fitness vibe.

5. Add Website & Contact Info
Link to your website and fill in any contact details (email, phone, etc.).

6. Publish Your Page
Once you're happy with everything, click Publish to make your page live.

7. Invite People to Like the Page
Invite your friends, family, and followers to like and follow your page.

Entities:
Accounts - Represents the users of the website. Each account can have one or more orders.

Attributes: AccountID (PK), Name, Email, Password, Address, PaymentDetails.

Reviews - Represents the product reviews given by users.

Attributes: ReviewID (PK), AccountID (FK), ProductID (FK), Rating, Comment, Date.

Products - Represents the fitness products available on the website.

Attributes: ProductID (PK), Name, Description, Price, StockQuantity, Category.

Sign Up - Represents the process where a user creates an account.

Attributes: AccountID (PK), Name, Email, Password.

Login - Represents user authentication to access the website.

Attributes: LoginID (PK), AccountID (FK), Timestamp.

Community Contact - Represents the contact information from users who want to reach out to the community or support.

Attributes: ContactID (PK), AccountID (FK), Message, Date.

Pricing Plans - Represents the different subscription plans or pricing models for users.

Attributes: PlanID (PK), Name, Price, Duration.

Shop - Represents the store section where products are listed.

Attributes: ShopID (PK), AccountID (FK), ProductID (FK), Quantity, Price.

Cart Bag - Represents the shopping cart with items before the user checks out.

Attributes: CartID (PK), AccountID (FK), ProductID (FK), Quantity, TotalPrice.

Relationships:
Account ↔ Reviews: One account can give many reviews, but each review belongs to one account (One-to-Many).

Account ↔ Community Contact: One account can send multiple community messages (One-to-Many).

Account ↔ Cart Bag: One account can have many items in the cart (One-to-Many).

Account ↔ Pricing Plans: An account can be subscribed to one pricing plan, but many users can share a pricing plan (Many-to-One).

Account ↔ Login: One account can have multiple login attempts (One-to-Many).

Product ↔ Reviews: A product can have many reviews, and each review refers to one product (One-to-Many).

Product ↔ Shop: A product can be part of many different shops (Many-to-Many, possibly through an intermediate entity like ProductShop).

Product ↔ Cart Bag: A product can appear in many cart bags, and each cart bag has a product (One-to-Many).

Entity Relationship Overview:
Accounts can create Reviews, make Community Contacts, add products to their Cart Bag, and be associated with Pricing Plans.

Products can have many Reviews and be added to Cart Bags and Shops.

Pricing Plans are linked to Accounts.

Shops sell Products to Accounts, and Cart Bags represent what users are purchasing.

## SEO and Keyword Implementation
SEO and Keyword Implementation
To improve the search engine optimization (SEO) of this project, several techniques were used to help search engines understand and rank the content better. Here's a breakdown of how keywords were implemented throughout the project:

1. Meta Tags in <head>
Meta tags are essential for search engines and social media platforms to understand the content of the page. These tags were added to the <head> section in the base template (base.html):

Meta Title: This sets the title of the page that appears on search engines.

html
Copy
Edit
<title>{% block title %}Eco Fitness - Sustainable Fitness & Gear{% endblock %}</title>
Meta Description: A brief description that shows up in search results.

html
Copy
Edit
<meta name="description" content="Join our eco-friendly fitness community, shop sustainable merchandise, and achieve your health goals.">
Meta Keywords: These are relevant keywords separated by commas to help search engines find the page.

html
Copy
Edit
<meta name="keywords" content="eco fitness, sustainable workout plans, fitness gear, diet plans, workout reviews, green fitness products">
Open Graph Tags: These help social media platforms display the page correctly when shared.

html
Copy
Edit
<meta property="og:title" content="Eco Fitness - Sustainable Fitness & Gear">
<meta property="og:description" content="Join our eco-friendly fitness community and shop sustainable fitness gear.">
2. Using Keywords Throughout the Project
Keywords were sprinkled throughout the project to make the content easier for search engines to understand. Here’s where we added them:

Headings: Keywords were included in headings (<h1>, <h2>, etc.) because they help search engines understand the page's main topics.

html
Copy
Edit
<h1 class="display-3 fw-bold"><strong>Transform Your Fitness, Sustainably</strong></h1>
<h2 class="text-center mb-4"><strong>Featured Merchandise</strong></h2>
Content: Keywords were also included in the body text to make sure the page is relevant to what users are searching for.

html
Copy
Edit
<p class="lead">Join our <strong>eco-friendly fitness community</strong>, shop sustainable <strong>merchandise</strong>, and achieve your <strong>health goals</strong>.</p>
Links: Internal links also use relevant keywords, making it clear what users can expect when they click.

html
Copy
Edit
<a href="{% url 'products:all_products' %}" class="btn btn-success"><strong>Shop Now</strong></a>
3. Using <strong> Tags for Emphasis
The <strong> tag was used throughout the site to emphasize important keywords. This tells both users and search engines that these terms are crucial for understanding the content.

html
Copy
Edit
<h5 class="card-title"><strong>Eco-Friendly Shop</strong></h5>
<p class="card-text">Sustainable <strong>fitness gear</strong> and <strong>apparel</strong>.</p>
4. External Links
External links to relevant and authoritative sources were added to build credibility and improve SEO. These links help both users and search engines understand more about the content of the site. For example:

html
Copy
Edit
<a href="https://www.sustainablefitness.com" target="_blank" class="btn btn-outline-success">Visit Our Partners</a>
5. Internal Links
Internal links connect different pages within the site and help both users and search engines navigate the content more easily. For example:

html
Copy
Edit
<a href="{% url 'community' %}" class="btn btn-success"><strong>Join the Community</strong></a>
6. Optimizing for Mobile
Since mobile optimization is important for SEO, the site is fully responsive, meaning that all content, including keywords, is easily accessible on any device.

Best Practices for SEO:
Use relevant keywords across the site, especially in headings and body text.

Don’t overuse keywords—make sure the content still sounds natural.

Make sure your meta tags are descriptive and relevant to the page content.

Keep updating your content and keywords to stay relevant in search results.

By following these steps, the project will have a better chance of ranking higher in search engine results and attracting more traffic.

## Project Setup

1. Accounts
Purpose: The Accounts app manages user profiles and accounts on the site.

Functionality: Users can view and edit their account details (name, email, shipping address, etc.), manage past orders, and update preferences. It stores user data securely and enables personalized experiences on the website.

2. Cart
Purpose: The Cart app manages items users add while shopping but have not yet proceeded to checkout.

Functionality: It allows users to add and view products, adjust quantities, and remove items from the cart. Users can see an estimated total price and continue shopping or proceed to checkout.

3. Bag
Purpose: The Bag app works similarly to the cart but often contains more detailed information like product sizes or personalized selections.

Functionality: Users can view the specific items they've selected, including product variations like size or color. The bag holds the items until the user checks out.

4. Login
Purpose: The Login app allows users to authenticate themselves and gain access to their account.

Functionality: Users can log in using their registered email and password. Once logged in, they can view personal details, check previous orders, and interact with other parts of the website.

5. Logout
Purpose: The Logout app ensures that users can safely sign out from their account.

Functionality: It ends the user's session, ensuring they are logged out from their account. This improves security and prevents unauthorized access to personal information.

6. Sign Up
Purpose: The Sign Up app lets new users register for an account.

Functionality: Users provide their personal information (email, password, etc.) to create an account. Once registered, they can log in, place orders, track purchases, and access special features.

7. About Us
Purpose: The About Us app provides information about the company’s values, mission, and team.

Functionality: Users can learn more about the brand's dedication to eco-friendly fitness, the sustainability efforts of the company, and what sets Eco-Fitness apart from other fitness retailers.

8. Products
Purpose: The Products app displays and manages the product catalog.

Functionality: Users can browse all available products (e.g., eco-friendly fitness gear, apparel, supplements). It provides details for each product, including descriptions, sizes, prices, and photos. Users can also filter products by category or attributes.

9. Pricing Plans
Purpose: The Pricing Plans app displays different subscription options available to customers.

Functionality: Users can view and choose from various subscription plans, such as monthly or yearly memberships, which might provide exclusive content, discounts, or services like personalized fitness plans.

10. Reviews
Purpose: The Reviews app allows users to leave reviews and read feedback from others on products.

Functionality: After purchasing products, users can submit ratings and written reviews. The app helps customers make informed decisions by displaying product ratings and reviews from previous buyers.

11. Community
Purpose: The Community app connects users and promotes engagement around fitness and sustainability.

Functionality: Users can participate in fitness challenges, join discussions, share their fitness progress, and connect with like-minded individuals. This creates a social environment around Eco-Fitness, fostering a sense of community.

12. Contact
Purpose: The Contact app enables users to get in touch with the Eco-Fitness support team.

Functionality: Users can submit inquiries, ask questions about products or services, and request assistance. This app typically includes contact forms, phone numbers, and email addresses for customer support.

13. Shop
Purpose: The Shop app is the primary interface for users to browse and purchase products.

Functionality: It provides a user-friendly shopping experience where customers can explore different categories of products, select items to add to the cart or bag, view detailed product descriptions, and proceed to checkout.

### Future Goals & improvments
While the current focus is on providing quality products and content that promote fitness, we have exciting plans for future growth. Here's how we plan to evolve Eco-Fitness:

1. Social Media Content Marketing
We aim to expand our reach by creating engaging social media content, especially in the form of short videos. The content will focus on:

Nutritious food tips: Short clips showcasing healthy, eco-friendly recipes and meal ideas that complement a fitness lifestyle.

Fitness exercises for specific body parts: Video tutorials explaining how to target specific muscle groups and improve body strength.

Eco-friendly lifestyle tips: Integrating sustainability with fitness, showing ways people can live greener lives while staying fit.

By using platforms like Instagram, TikTok, and YouTube, we plan to share content that not only attracts new customers but builds a community around healthy and sustainable living.

2. Email Marketing
In the future, we plan to implement email marketing campaigns to stay connected with our audience. These campaigns will offer:

Discounts: Offering exclusive deals to subscribers on fitness products, eco-friendly workout gear, or membership discounts.

New product announcements: Informing customers about the latest eco-friendly fitness products, accessories, and apparel.

Fitness tips & updates: Sending helpful fitness and wellness content directly to subscribers, keeping them engaged with useful information.

The goal is to build a loyal customer base and foster long-term relationships with our audience through regular communication.

3. Paid Advertising
As the business grows, we plan to incorporate paid ads into our strategy to scale up. This will include:

Google Ads and social media ads (e.g., Facebook, Instagram) to target individuals interested in fitness, eco-friendly products, and healthy living.

Retargeting ads to re-engage visitors who didn’t convert the first time they visited the site.

### Testing 
Code Quality & Testing
While I have not written extensive tests across all applications in my eco-friendly e-commerce website, I have ensured consistent code quality by running static analysis tools. I used flake8 to check for linting errors by executing the following command:

bash
Copy
Edit
python3 -m flake8 --exclude .venv,.vscode,migrations
This command excludes common directories like virtual environments, editor settings, and database migrations. After running the checks, no significant issues were found — ensuring that the codebase maintains a clean and readable standard without major syntax or style problems.

### Custom 404 Page 
To enhance the user experience on our eco-friendly fitness website, a custom 404 error page has been implemented. This page is displayed when a user attempts to access a URL that doesn't exist.

How it Works:
If a user navigates to a non-existent page (e.g., /test), the server will render a custom 404 error page.

The custom 404 page is designed to be consistent with the website's branding, with a message guiding the user back to the homepage or relevant sections like the shop.

Implementation:
View: A handler404 function was added in the home/views.py file to handle the 404 error.

URL Configuration: In the eco_fitness/urls.py file, we set the global 404 error handler.

Template: The 404 error page is designed in home/templates/errors/404.html and integrates seamlessly with the rest of the site’s design.

### Requirements

- Python 3.8+
- Django 3.2+
- PostgreSQL (for production)
- Stripe API credentials for payment processing
- Heroku account for deployment

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/olutobi1996/eco-fitness.git
   cd eco-fitness
