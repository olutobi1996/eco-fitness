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

**Eco-Fitness** Eco-Fitness is a web-based application built with Django, designed to promote a healthy lifestyle while supporting environmental sustainability through the sale of eco-friendly fitness products. This interactive platform offers users a full e-commerce experience—including shopping cart functionality, a secure checkout process, product reviews, account management, and subscription-based pricing plans tailored to individual needs. Beyond commerce, Eco-Fitness fosters community engagement by offering forums for discussion and educational content focused on sustainable fitness practices. Operating under a Business-to-Consumer (B2C) model, the application directly serves individual customers seeking eco-conscious workout gear, personalized fitness and meal plans, and sustainable lifestyle solutions. The platform aims to build a loyal customer base by encouraging repeat purchases through valuable content and community interaction, while promoting sustainability as a core brand value. Marketing efforts include a strong presence on social media, targeted email campaigns, incentives like discounts and subscriptions, and the strategic use of customer testimonials and user-generated content to boost authenticity and trust.

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
The ERD (Entity Relationship Diagram) outlines the core backend structure of the application, detailing how database models interconnect and what data they store. At its center is the Django User model, managing authentication essentials such as login credentials, email, and passwords, which links directly to a custom AccountProfile model that holds additional user details like default addresses, phone numbers, and shipping information. On the product side, products are organized into categories such as supplements, fitness plans, and activewear, with users able to leave reviews; some products are grouped into special bundles offered at discounted prices. The order system creates orders upon checkout, each containing multiple order line items that record details like the product ordered, size, quantity, delivery costs, Stripe payment IDs, and timestamps. A subscription system connects users to Stripe subscriptions for premium plans or exclusive content. Beyond e-commerce, the system includes a blog and community area for admin-posted content, a contact message model to store user inquiries, a newsletter model tracking subscriber emails, and an About Us model managing the site’s mission and vision content. This modular, scalable design ensures each feature—shop, profile, blog, and more—has a clear, independent structure that can evolve seamlessly over time.

Here is my ERD:
![Image](https://github.com/user-attachments/assets/417196db-d5e5-4669-bc38-d052d4d3289d)

## Facebook
![Image](https://github.com/user-attachments/assets/b028d540-b3b9-4d76-93ec-1716601c72b8)
Follow these steps to set up your Facebook page and start building a community for your eco-friendly fitness website.

To establish your business presence on Facebook, start by logging into the Facebook account you want to associate with your business. Navigate to the Pages section from the Facebook menu and click Create New Page. Enter your page name, ideally matching your website or brand name, and select an appropriate category such as "Fitness" or "Eco-Friendly Products." Next, craft a concise and compelling bio that clearly communicates your eco-friendly fitness mission—highlighting your commitment to sustainability and health. For example: “GreenFit Eco Fitness offers eco-friendly fitness products and content to help you stay healthy while caring for the planet.” Upload a profile picture, typically your logo, and a cover photo that visually represents your brand’s fitness and sustainability values. Add your website URL along with contact details like email and phone number. Once everything looks good, hit Publish to make your page live. Finally, invite friends, family, and followers to like and follow your page to build your initial community.

## SEO and Keyword Implementation
SEO and Keyword Implementation
To improve the search engine optimization (SEO) of this project, several techniques were used to help search engines understand and rank the content better. Here's a breakdown of how keywords were implemented throughout the project:

To enhance search engine optimization (SEO) for the project, several strategic techniques were employed to improve content discoverability and ranking. In the site’s base template (base.html), essential meta tags were added inside the <head> section: a meta title like “Eco Fitness - Sustainable Fitness & Gear” defines the page title shown in search results, a meta description briefly summarizes the site’s mission to attract clicks, and meta keywords include targeted phrases such as “eco fitness,” “sustainable workout plans,” and “fitness gear.” Open Graph tags ensure social media platforms display the page properly when shared.

Keywords are carefully embedded throughout the site in key areas: headings (<h1>, <h2>) contain important terms to clarify main topics, body text naturally incorporates relevant phrases, and internal links use keyword-rich anchor text for clear navigation and SEO benefit. The use of <strong> tags emphasizes critical keywords both to users and search engines, highlighting terms like “eco-friendly fitness community” and “sustainable fitness gear.”

External links to authoritative sources (e.g., partner sites) boost credibility, while internal links facilitate smooth navigation between pages like the shop and community sections. The site is fully responsive and mobile-optimized, ensuring all SEO content is accessible across devices. Best practices include balancing keyword usage to maintain natural-sounding content, regularly updating meta tags and keywords to stay current, and ensuring all SEO elements align with the site’s core message. These combined efforts increase the project’s visibility in search engine results and attract a targeted audience.

## Project Setup

Accounts
The Accounts app manages all user-related data and interactions. It allows users to create and maintain personalized profiles, edit personal details (such as name, email, address, and contact preferences), and securely access their account. It also provides access to past order history and enables a customized experience based on individual user activity and preferences.

Cart
The Cart app handles the shopping experience before checkout. Users can add products, update quantities, view pricing totals, and remove items. It serves as a dynamic and responsive space for managing purchases in real-time, helping users plan their orders efficiently before committing to checkout.

Bag
The Bag app functions similarly to the Cart but emphasizes product detail and customization. It stores specific item variants, such as selected sizes, colors, or bundle options. This offers users a more tailored shopping experience, especially for items that involve personal preferences or configurations.

Login
The Login app provides secure user authentication. By entering their credentials, users gain access to protected areas like their account dashboard, previous orders, community sections, and subscription services. It ensures safety and convenience across user sessions.

Logout
This app ends the user session securely, ensuring that private information and activity remain confidential. It plays a key role in data protection and is essential for maintaining secure access, especially on shared devices.

Sign Up
New users can register via the Sign Up app by providing necessary details such as email and password. Once registered, users unlock full site functionality including ordering, reviewing, joining the community, and subscribing to fitness plans or eco-offers.

About Us
This section shares the brand’s mission, values, and the story behind Eco-Fitness. It highlights the company’s dedication to sustainable wellness and positions the brand as a meaningful alternative to mainstream fitness retailers, focused on community, transparency, and environmental impact.

Products
The Products app showcases the full catalog of eco-friendly fitness goods. Users can browse categories such as biodegradable workout equipment, sustainable activewear, or plant-based supplements. Each product includes detailed descriptions, photos, eco-certifications, and variant options. Filters help users find exactly what they’re looking for.

Pricing Plans
Here, users can explore and subscribe to flexible plans such as monthly, quarterly, or annual memberships. Plans may unlock exclusive benefits like personalized training guides, member-only products, discount bundles, or early access to new releases—driving long-term value.

Reviews
The Reviews app allows users to leave feedback on products and read real experiences from others. It supports star ratings and written reviews, helping potential buyers make informed decisions. Authentic reviews also boost SEO and credibility.

Community
More than just a store, Eco-Fitness is a movement. The Community app connects like-minded users through discussion boards, challenges, wellness journeys, and progress sharing. It encourages ongoing engagement and builds emotional loyalty through shared goals.

Contact
The Contact app enables direct communication with the Eco-Fitness support team. Users can submit questions, requests, or feedback through forms or contact info (email, phone). It's designed to be responsive, empathetic, and transparent.

Shop
The Shop app provides a seamless and visually engaging ecommerce experience. Users can explore categories, view curated collections, add items to their cart or bag, and move smoothly to checkout. The interface emphasizes both aesthetics and usability, reinforcing the brand’s premium and eco-conscious image.

## Marketing Strategy
Who We’re Here For
Eco-Fitness is purpose-built for a new generation of conscious consumers—those who live at the intersection of personal health and planetary wellbeing. Our two core user groups are:

Fitness Enthusiasts: People committed to improving their physical health through gym training, home workouts, running, or personalized fitness plans. These users value quality gear, effective routines, and motivation from like-minded communities.

Environmentally Conscious Consumers: Individuals passionate about reducing their environmental footprint. They prioritize sustainable living, eco-responsible products, and ethical companies that align with their lifestyle.

Eco-Fitness unites these groups, offering a space for users who refuse to choose between their health and the planet’s. Whether someone is searching for compostable yoga mats, vegan protein supplements, or climate-conscious meal plans, our brand provides a curated destination for fitness without compromise. It’s not just about what they buy—but how and why they buy it.

How We Attract, Engage & Retain Customers
Eco-Fitness leverages a comprehensive, multi-channel marketing and growth strategy rooted in trust, education, community-building, and digital precision.

Offers, Subscriptions & Loyalty
Introductory Offers: New users receive a 10% welcome discount for signing up to our newsletter.

Subscription Plans: Flexible membership tiers provide access to exclusive content, product bundles, monthly training programs, and curated eco-living guides.

Loyalty Incentives: Reward returning customers with points, referral bonuses, and early access to limited-run sustainable products.

SEO-Optimized Content Strategy
All product titles, meta descriptions, and landing pages are written with keyword research in mind—focusing on phrases like "eco-friendly gym gear," "plant-based supplements," and "sustainable fitness routines."

On-page content and blogs follow long-tail SEO best practices, increasing organic visibility.

Social Media Engagement (Instagram, TikTok, Pinterest)
We showcase real customers using products in eco-home gyms and workouts.

Bite-sized video content includes sustainability tips, quick eco-meal preps, and fitness routines.

Partnering with green influencers and fitness creators extends reach and authenticity.

Pinterest is used for moodboards and wellness inspiration, appealing to the design-conscious and eco-minimalist user base.

Content Marketing (Blog & Reviews)
Our blog highlights topics like “How to Green Your Workout” or “Top 5 Vegan Post-Workout Snacks.”

Testimonials and real transformation stories create social proof.

Product reviews improve SEO and enhance buyer confidence at critical purchase stages.

Email Campaigns
Automated flows for abandoned cart recovery, product launches, seasonal deals, and educational content.

Segmented lists allow personalized messages for first-time buyers, loyal customers, or users exploring subscriptions.

Weekly newsletters mix inspiration, exclusive offers, and sustainability education.

Paid Advertising (Google + Meta Ads)
Search ads target users seeking eco-fitness solutions.

Shopping ads highlight product bundles and top-rated gear.

Meta Ads (Instagram/Facebook) retarget visitors with carousel ads, testimonials, and time-sensitive offers.

Landing pages are optimized for each ad group, increasing conversion rates and return on ad spend.

Brand Philosophy & Community Vision
Eco-Fitness is more than a shop—it’s a movement for those who believe wellness shouldn’t cost the Earth. Our approach balances ethical commerce with digital innovation. We educate and empower our audience through transparent storytelling, planet-first products, and a supportive ecosystem of like-minded individuals. Every feature, from our community space to our biodegradable packaging, reinforces our mission: to help people thrive while helping the planet heal.

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

configure Stripe webhook URL to point to hosted app's webhook endpoint.

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

Using Stripe, configure, webhook URL in Stripe dashboard to point to your Heroku app’s /webhook/ endpoint (e.g., https://your-app-name.herokuapp.com/webhook/).

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
