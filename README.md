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

## Marketing Strategy
Target Audience
Eco-Fitness is aimed at two core user groups, brought together by a shared mindset:

Fitness Enthusiasts – individuals who are actively trying to live healthier lifestyles, whether through gym workouts, home exercise routines, or structured fitness/diet plans.

Environmentally Conscious Consumers – users who are mindful about sustainability, the climate crisis, and the impact their purchases have on the planet.

Our brand sits right at the intersection of these audiences, appealing to those who want to stay fit without compromising their values. Whether it's someone looking for biodegradable workout gear, eco-friendly supplements, or a diet plan that aligns with plant-based living — Eco-Fitness offers a curated space for all.

How We Attract Users

We’ve planned a multi-channel strategy to drive traffic, build brand recognition, and create a loyal customer base:

SEO-Driven Product Naming & Content
Through research, we’ve identified high-performing keywords combining both the eco and fitness niches (e.g. eco-friendly workout clothes, plant-based supplements, sustainable gym gear, etc.). All product names, meta descriptions, and on-page content have been written with SEO in mind to organically improve visibility across search engines.

Social Media (Instagram, TikTok & Pinterest)
We’ll leverage visual-heavy platforms like Instagram and TikTok to showcase:

Real customers using our products

Short videos around fitness tips and sustainable living

Collaborations with fitness influencers and eco-activists

Pinterest will also be used to share moodboards and lifestyle inspiration (eco-home gyms, sustainable wellness routines, etc.) to drive clicks from a health- and design-savvy audience.

Content Marketing (Wellness Blog & Product Reviews)
We’ll feature a blog/community space that regularly publishes content such as:

“5 Eco-Friendly Swaps for Your Gym Routine”

“The Benefits of Vegan Supplements Backed by Science”

Customer reviews, transformations, and testimonials

Reviews on product pages not only build trust but also improve long-tail SEO.

Email Campaigns & Subscriber Discounts
We’ll build a newsletter list from the homepage and checkout process, offering a 10% discount on first orders in exchange for a signup. Email marketing will be used to:

Send out new product drops

Share sustainable fitness tips

Re-engage abandoned carts

Promote bundles or seasonal offers

Paid Ads (Google & Meta Ads)
We’ll run targeted campaigns using Google Ads (shopping + search) and Meta Ads (Facebook/Instagram) based on users interested in:

Fitness

Vegan/eco lifestyles

Mindfulness/wellbeing

Each ad campaign will drive to a specific landing page optimised for conversions.

Overall Strategy
The idea is to create a brand, not just a shop — one that users connect with emotionally and ethically. By combining data-driven digital marketing with real user reviews and content that helps educate or inspire, Eco-Fitness will build trust, community, and long-term loyalty from customers who believe in what we stand for: Wellness for people and the planet.

## 🎨 Fonts and Typography

A strong typographic system has been implemented to support a clean and accessible user experience while aligning with the brand’s eco-conscious identity.

### Font Families Used:

- **Poppins** – Used for logos, navigation bars, section headers, and CTAs. It has a modern, geometric look that helps headlines stand out and communicates confidence and clarity.
- **Lato** – Used for body text across all pages. Chosen for its readability, subtle roundness, and friendly appeal, perfect for mobile and accessibility.
- **Playfair Display** – Used selectively for quotes and testimonials. This elegant serif font adds visual contrast and a premium, editorial feel to certain content blocks.

### Typography Roles:

- **Hero Headers** use bold Poppins at larger sizes (3rem+), giving users immediate attention on promotions and CTAs.
- **Section Headings** are set in Poppins, sized down to maintain hierarchy.
- **Paragraph Text** and UI feedback (e.g., toasts) are in Lato, ensuring excellent legibility.
- **Quote or Highlight Text** uses Playfair Display in italic for stylistic contrast.

These font choices were also optimized for performance using Google Fonts, ensuring fast loading and accessibility across devices.


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
Testing and Code Quality Assurance
In developing the Eco-Fitness platform—a comprehensive eco-friendly e-commerce website featuring user accounts, product management, shopping bag, checkout, subscription services, community engagement, and contact functionalities—I have prioritized building a clean, robust, and maintainable codebase.

While comprehensive automated test coverage across all applications has not yet been fully implemented, a rigorous manual testing process has been carried out. This process systematically verified core user flows, including:

Account registration, login, and profile management

Browsing products and adding them to the shopping bag

Completing the checkout process with subscription options

Interacting within the community section

Submitting inquiries via the contact form

Each feature was carefully tested for expected behavior and responsiveness across various devices and browsers, ensuring a seamless and consistent user experience.

To complement manual testing, I enforced high standards of code quality through static analysis. Specifically, I used flake8 to run linting checks with the following command:

bash
Copy
Edit
python3 -m flake8 --exclude .venv,.vscode,migrations
This command excludes virtual environments, editor settings, and migration files to focus on the core application code. The results confirmed strong adherence to PEP8 style guidelines, with no critical syntax or style violations detected. This approach ensures the codebase remains clean, readable, and scalable, which is crucial for ongoing maintenance and feature expansion.

Going forward, I plan to extend automated test coverage particularly around critical workflows such as checkout and subscription management. This will increase confidence in the system’s reliability and stability during deployment and future updates.

Overall, these focused efforts in testing and quality assurance establish a solid foundation for Eco-Fitness to evolve into a polished and fully functional eco-friendly e-commerce platform.

| Feature           | Test Case                            | Expected Result                                       | Outcome |
| ----------------- | ------------------------------------ | ----------------------------------------------------- | ------- |
| User Accounts     | Register a new user                  | Account created and confirmation email sent           | ✅       |
|                   | Login with valid credentials         | User logged in successfully                           | ✅       |
|                   | Edit user profile                    | Profile updates saved                                 | ✅       |
| Product Browsing  | Navigate product catalog             | Products load and display correctly                   | ✅       |
|                   | Filter products by category          | Filtered results displayed correctly                  | ✅       |
| Shopping Bag      | Add product to bag                   | Product added, total updates                          | ✅       |
|                   | Remove product from bag              | Product removed, total updates                        | ✅       |
| Checkout          | Complete purchase with valid payment | Order processed, confirmation email sent              | ✅       |
|                   | Checkout with subscription option    | Subscription activates and payment processed          | ✅       |
| Community Section | Post a new comment or discussion     | Comment posted and visible to others                  | ✅       |
| Contact Form      | Submit contact inquiry               | Inquiry sent successfully, confirmation message shown | ✅       |
| Responsiveness    | Access site on mobile and desktop    | Layout adjusts correctly, navigation works            | ✅       |
| Navigation        | Click all navbar links               | Pages load without errors                             | ✅       |

## Code Style and Linting

This project uses `flake8` for linting and `black` for auto-formatting to ensure consistent code style.

### Tools Used:
- `black` formats code automatically with a default line length of **88 characters**.
- `flake8` is used to catch potential issues and enforce coding standards, including a stricter line length limit of **79 characters** (`E501`).

### Manual Fixes:
All PEP8 issues have been reviewed and manually fixed, including long lines, spacing, and unused imports. After making corrections, I ran:
bash
pip install -r requirements.txt
black .
flake8 .

(Any Fixes left will be due to cached issues everythings been fixed manually or auto generated)
### Deployment Instructions
This section outlines the detailed steps to deploy the Eco-Fitness platform, ensuring a smooth setup on your preferred hosting environment.

1. GitHub Repository Setup
Create a GitHub repository and push your local project code to it.

Ensure .gitignore excludes sensitive files like .env and local settings.

2. Prepare Environment Variables
Create a .env file or configure environment variables for:

SECRET_KEY (Django secret key)

DEBUG (set to False in production)

Database credentials (DATABASE_URL or individual settings)

Stripe API keys (STRIPE_PUBLIC_KEY, STRIPE_SECRET_KEY)

Email server credentials (SMTP host, port, user, password)

Any other service keys (e.g., AWS S3, third-party APIs)

3. Configure Static Files Handling
Use whitenoise to serve static files in production.

Run:

bash
Copy
Edit
python manage.py collectstatic
to gather all static files.

4. Hosting Setup (Heroku / Render / Other)
Create an app on your hosting platform.

Connect your GitHub repo or deploy via CLI.

Add necessary environment variables to the platform’s config.

Set up the database service (PostgreSQL recommended).

If using Stripe, configure your Stripe webhook URL to point to your hosted app's webhook endpoint.

5. Database Migrations
Run migrations on the production server:

bash
Copy
Edit
python manage.py migrate
6. Email Configuration
Configure your email backend to send registration confirmations, password resets, and contact form emails.

Test email sending in production environment.

7. Final Testing
After deployment, test all critical flows:

User signup/login

Product browsing and shopping bag

Checkout and payment processing

Subscription management

Community interactions

Contact form submissions

### Deployment Instructions Heroku 
This section outlines detailed steps to deploy the Eco-Fitness platform, focusing on Heroku as the hosting environment, while also including general best practices for environment variables and configuration.

1. GitHub Repository Setup
Create a GitHub repository and push your local project code.

Ensure your .gitignore excludes sensitive files such as .env, local settings, and any secret keys to prevent accidental exposure.

2. Prepare Environment Variables
Locally, use a .env file for development with variables such as:

env
Copy
Edit
SECRET_KEY=your-django-secret-key
DEBUG=False
DATABASE_URL=your-database-url
STRIPE_PUBLIC_KEY=your-stripe-public-key
STRIPE_SECRET_KEY=your-stripe-secret-key
EMAIL_HOST=smtp.your-email-provider.com
EMAIL_PORT=587
EMAIL_HOST_USER=your-email@example.com
EMAIL_HOST_PASSWORD=your-email-password
On Heroku, do not push .env files. Instead, set config vars via the Heroku Dashboard or CLI:

bash
Copy
Edit
heroku config:set SECRET_KEY='your-django-secret-key'
heroku config:set DEBUG=False
heroku config:set STRIPE_PUBLIC_KEY='your-stripe-public-key'
heroku config:set STRIPE_SECRET_KEY='your-stripe-secret-key'
heroku config:set EMAIL_HOST='smtp.your-email-provider.com'
heroku config:set EMAIL_PORT=587
heroku config:set EMAIL_HOST_USER='your-email@example.com'
heroku config:set EMAIL_HOST_PASSWORD='your-email-password'
For the database, Heroku typically provides a DATABASE_URL which Django can use directly with dj-database-url.

3. Configure Static Files Handling
Use whitenoise to serve static files in production.

Run the following to collect static files before deployment or during your build process:

bash
Copy
Edit
python manage.py collectstatic --noinput
Make sure STATIC_ROOT is correctly set in your Django settings.

4. Hosting Setup on Heroku
Create a new Heroku app via the dashboard or CLI:

bash
Copy
Edit
heroku create your-app-name
Connect your GitHub repository for automatic deploys or deploy manually via CLI:

bash
Copy
Edit
git push heroku main
Add a Heroku Postgres add-on for your database:

bash
Copy
Edit
heroku addons:create heroku-postgresql:hobby-dev
Add any required buildpacks (Python is usually auto-detected).

Set environment variables (config vars) as described above.

If using Stripe, configure your webhook URL in Stripe dashboard to point to your Heroku app’s /webhook/ endpoint (e.g., https://your-app-name.herokuapp.com/webhook/).

5. Database Migrations
Run database migrations on Heroku:

bash
Copy
Edit
heroku run python manage.py migrate
You can also create a superuser if needed:

bash
Copy
Edit
heroku run python manage.py createsuperuser
6. Email Configuration
Ensure your email backend is configured to use environment variables for credentials.

Test email functionality in production by triggering password resets or contact form submissions.

On Heroku, email sending depends on your SMTP provider—make sure ports and authentication details are correctly configured in your config vars.

7. Final Testing and Maintenance
After deployment, test all critical user flows on the live site:

User signup/login/profile updates

Product browsing and shopping bag functionality

Checkout process including payment and subscriptions

Community features such as posting comments

Contact form submissions

Monitor logs for errors with:

bash
Copy
Edit
heroku logs --tail
To scale or update your app, use Heroku dashboard or CLI commands like heroku ps:scale web=1.

Regularly update dependencies and apply security patches.

### Testing Checkout with Stripe
To test the checkout functionality on the deployed site, follow these steps:

Add any product to your bag.

Proceed to checkout and fill in the required shipping details.

Use the following Stripe test card details:

Card number: 4242 4242 4242 4242

Expiry date: Any future date (e.g. 12/34)

CVC: Any 3 digits (e.g. 123)

ZIP/Postcode: Any 5-digit number (e.g. 12345)

Submit the payment — you should be redirected to a success page with an order confirmation.

 Note: Checkout may not function correctly in local development environments such as Gitpod due to Stripe webhook and API configuration.
However, all checkout functionality has been fully tested and is working as expected on the deployed Heroku site.


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
