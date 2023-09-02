# Brick by Brick
Welcome to Brick by Brick! This project is a replica of the popular LEGO website for my final project of my UCD Full-Stack Devlopment course. This project was developed using Django, a powerful web framework for Python, and styled with Tailwind CSS, a utility-first CSS framework. The primary aim of this project is to showcase various features commonly found on e-commerce platforms, with a focus on providing users with an immersive shopping experience in a LEGO-themed environment.

# Disclaimer
Please note that this project is purely for educational and demonstrative purposes. No actual products are sold through this website, and no financial transactions are being conducted. The project does not involve any real-world e-commerce operations or the handling of sensitive user information. The products displayed on this website are not for sale and are used for illustrative purposes. No products are sold here. This project is not affiliated with or endorsed by the LEGO Group or any other entity. All LEGO related trademarks, copyrights, and other intellectual property rights are the property of the LEGO Group. Any references to LEGO products, themes, or characters are used purely for educational and non-commercial purposes. All rights to the LEGO Group and its intellectual property are acknowledged and respected. This project serves as a personal project to showcase the skills I have learned from my full-stack course.

# **User Experience & Design**

# User Stories
* As a first time user, I want to navigate between content on brick by brick.
* As a first time user, I want to explore various brick by brick products available on the website by browsing through different themes.
* As a first time user, I want to create a new account on brick by brick so I can place orders & save my shipping and billing details for future purchases.
* As a first time user, I want to log in to my account using my credentials to access my profile and order history.
* As a a first time user, I want to add products to my shopping cart and proceed through a secure checkout process.
* As a a first time user, I want to view my previous orders and the total amount spent in my profile section.
* As a first time user, I want to sign up for marketing emails to receive updates about new LEGO products and promotions.
* As a first time user, I want to view the website on different devices (iPhone 10, Surface Pro 7+, 32-inch monitor) to ensure responsive design.
* As a first time user, I want to have the ability to modify item quantity in my cart.
* As an admin user, I want to easily add new brick by brick products to the catalog, specifying details such as name, description, price, and theme.
* As an admin user, I want the ability to delete products that are no longer available or relevant from the website.
* As an admin user, I want to add new brick by brick themes to associate products with.


## Structure
The home screen of brick by brick presents users with intuitive navigation options. Prominent button are available in the navigation bar enabling users to perform different actions. Users can choose to create an account, log in to an existing account, or explore the brick by brick shop. Users can also view their cart & see how many items are in their cart.
> As a first time user, I want to navigate between content on brick by brick.

Users who already have an account can use the 'login' navigation option. This will direct them to the login page where they can enter their credentials and access their account. If a user does not have an account they can choose signup within the login dialog & create an account
> As a first time user, I want to create a new account on brick by brick so I can place orders & save my shipping and billing details for future purchases.
> As a  first time user, I want to log in to my account using my credentials to access my profile and order history.

Users can browse various products with filter options & add items to their carts
> As a first time user, I want to explore various brick by brick products available on the website by browsing through different themes.
> As a a first time user, I want to add products to my shopping cart and proceed through a secure checkout process.

Users have the ability to increase the quantity of items in their carts & remove/delete items from their carts.
> As a first time user, I want to have the ability to modify item quantity in my cart.

Users can checkout using Paypal payment system.
> * As a a first time user, I want to add products to my shopping cart and proceed through a secure checkout process.

Admin users have permissions to add new products to the brick by brick catalogue, products can also be deleted. New themes can be added to help filter products.
> As an admin user, I want to easily add new brick by brick products to the catalog, specifying details such as name, description, price, and theme.
> As an admin user, I want the ability to delete products that are no longer available or relevant from the website.
> As an admin user, I want to add new brick by brick themes to associate products with.

# Design
The design of the brick by brick takes its inspiration from the official [Lego Website](https://www.lego.com/en-ie). Using a minimalistic design approach, the design combines simplicity with functionality. The design aims to mirror the LEGO brand's identity. With a cohesive color scheme and user-friendly layout, the website ensures seamless navigation, inviting users to explore products.

## Colour Scheme
The website uses a primary colour palette. The primary colours used throughout the website are yellow (#ffcf00), orange (#FD8024), deep purple (#201D48F) & blue. The site uses the same primary colours throughout to keep design consistent and clean.

## Wireframes
I decided to take a different approach to wireframes for this project as my aim was to follow a design that already exists & was designed by professionals. I took screenshots of each page I wanted to include & using the draw functionality on my computer, I marked the sections I wanted to include in my project & used these as a reference. I found this approach really helpful as I could reference images over a simple diagram. These were created before dev started so production site design may vary slightly to wireframes. (please excuse the awful drawing &writing....)
# add wireframe images

## Database Model
![image](https://github.com/emmaC11/brick-by-brick/assets/83119583/0a7d847d-a215-4a6a-918e-558ce1b568eb)
![image](https://github.com/emmaC11/brick-by-brick/assets/83119583/c7fee2fb-419f-4d18-b274-11e6edf65be2)
![image](https://github.com/emmaC11/brick-by-brick/assets/83119583/8bb3cc6b-8265-428a-8c32-4f21ee63a4d0)
![image](https://github.com/emmaC11/brick-by-brick/assets/83119583/68255629-f175-453a-bef3-877af23bc19e)
![image](https://github.com/emmaC11/brick-by-brick/assets/83119583/d185188a-2198-40b1-a130-26f4708f9296)
![image](https://github.com/emmaC11/brick-by-brick/assets/83119583/84aad907-8ede-4d27-acac-ba36ba741073)

# **Features**
## Home Screen
* The home screen features a top navigation bar with varying options depending on the user's login status.
* When a user is not logged in, the navigation displays - "SHOP" & "Login."
* When a user is logged in, the navigation displays - "SHOP" & minifigure icon which can be clicked to access the user profile page
* The red cartoon logo is a also a clickable link to the homepage.
* Users can access their carts also via the bag icon, & the number beside the icon reflects the number of products in the cart.
* The hero section of the home screen showcases slogan with a background image that includes lego minifigures, encouraging users to explore the site.
* The message includes a large title, a short slogan, and a call-to-action button to direct users to the shopping page.
* The call-to-action button is styled with a white background and black text, with a hover effect to underline the text.
* The overall design maintains a consistent LEGO theme with LEGO-related images and colors.
![image](https://github.com/emmaC11/Dev-Connect/assets/83119583/ad65016d-f6c4-418a-a251-b00c114bae3f)

## Product List Page
* The product list page displays a grid of LEGO sets available for purchase.
* Users have the option to filter LEGO sets by theme using a filter form.
* The filter form allows users to select a specific LEGO theme to narrow down their search.
* Users can apply the selected filter by clicking the "Apply Filter" button.
* A "Clear Filter" button is provided to reset the filter and display all LEGO sets.
* Below the filter section, there is a theme description box that provides information about the selected LEGO theme.
* The theme description box includes the theme's name and a brief description of the theme.
* If no specific theme is selected, a default welcome message is displayed, introducing the LEGO Shop mock site and providing a disclaimer.
* Each LEGO set is presented as a card within a responsive grid layout.
LEGO set cards feature an image of the LEGO set, its name, price, and recommended age.
* A "View Legoset" button is provided for each LEGO set, allowing users to view more details and potentially add the set to their cart.
* The page layout maintains a clean and organized design, making it easy for users to browse and explore the available LEGO sets.
![image](https://github.com/emmaC11/Dev-Connect/assets/83119583/30de207b-93e1-4029-a39c-a09580ff966e)

## Selected Product
* The selected product page displays detailed information about a specific LEGO set.
* The primary product image is displayed prominently at the top of the page.
* The product title is prominently displayed beneath the product details.
* A rating system is implemented using star icons to indicate the product's rating.
* The product price is displayed, showing the cost of the LEGO set (e.g., "€{{ legoset.get_legoset_price }}").
* Links are provided to access additional information related to the product
Availability information is provided, indicating that the product is "Available now."
* Important product details are presented below the image:
 - The recommended age group for the LEGO set (e.g., "Ages: {{ legoset.ages }}+").
 - The number of LEGO pieces included in the set (e.g., "{{ legoset.piece_count }} pieces").
 - The number of minifigures included in the set (e.g., "{{ legoset.minifigures }} minifigures").
 - The item number of the LEGO set (e.g., "Item Number: {{ legoset.item_number }}").
* Users can add the LEGO set to their shopping cart using the add to bag button, which adds the item to the cart
![image](https://github.com/emmaC11/Dev-Connect/assets/83119583/93bbe16f-717e-4718-88d8-6be81ed18f15)


## Cart Page
* The cart page allows users to review and manage the items they've added to their shopping cart.
* The page header displays "My Bag" to indicate that it's the user's shopping bag.
* Each product in the shopping cart is presented as a separate card, organized in a responsive grid layout.
* For each product, the following information is displayed:
 - An image of the LEGO set.
 - The name of the LEGO set.
 - The quantity of the LEGO set, with buttons to increase or decrease the quantity.
 - The total price for the LEGO set.
- An option to remove the LEGO set from the cart.
* Users can increase or decrease the quantity of each item using the "+" and "-" buttons.
* A subtotal for all items in the cart is displayed, along with the total price.
* Shipping costs of €5 are added to the total.
* A "Checkout Securely" button is provided to direct users to the checkout page.
* If the cart is empty, a message is displayed indicating that there are no items in the bag and a link to start shopping is provided.
T* he design and layout of the cart page are clean and user-friendly, making it easy for users to manage their shopping cart and proceed to checkout.
![image](https://github.com/emmaC11/Dev-Connect/assets/83119583/fd496efb-afca-4664-b929-abb247803e10)


## Checkout Page
* The checkout page is where users can review and complete their order for the selected LEGO sets.
* If the user is not logged in, a message is displayed indicating that they are nearly finished with their order but need to either log in or sign up to proceed.
* If the user is logged in, a form for entering billing details is presented.
* The billing details form includes fields for the user's name, address, and payment information.
* Users can submit the form to proceed with the payment process.
* A "Proceed to Payment" button is available at the bottom of the billing details form.
* An order summary section is displayed on the right side of the page.
* The order summary includes details such as the subtotal of the order, the standard delivery cost (€5), and the total order cost.
* The order summary provides a clear breakdown of the costs associated with the order.
* Users can review their order details, including the items they're purchasing and the total cost.
* The design of the checkout page is user-friendly and provides a seamless experience for users to complete their LEGO set purchase.
![image](https://github.com/emmaC11/Dev-Connect/assets/83119583/5e859d04-8e76-4110-b2bd-1ede73bf267e)


## Payment Page
* The payment page is the final step in the checkout process, where users can select a payment method and complete their order.
* Users are presented with the option to select a payment method for their order.
* The order's total cost is displayed prominently on the page (e.g., "Order total: €{{ order.get_order_total }}").
* Users are informed about the total amount they will be charged for their purchase.
* The primary payment method presented on the page is PayPal.
* The PayPal payment button is rendered on the page using the PayPal JavaScript SDK.
* Users can click the PayPal button to proceed with the payment process.
* The JavaScript code handles the creation of the PayPal order and the capture of payment details.
U* pon successful payment, the payment details are sent to the server for confirmation.
* If the payment is successful and confirmed, users are redirected to the order complete page.
![image](https://github.com/emmaC11/Dev-Connect/assets/83119583/e2887061-69c5-4027-9781-86a56ee4abf2)


## Order Complete Page
* The Order Complete page serves as confirmation that the user's order has been successfully processed.
* The user has the option to navigate to their profile to view their order history
![image](https://github.com/emmaC11/Dev-Connect/assets/83119583/1ac8572d-de3c-465b-a42b-ea9c6dc975c5)

## User Profile
* The User Profile page provides access to the user's account information and order history.
* It displays the user's username prominently at the top of the page.
* Users have the option to log out through a "Logout" button.
* A horizontal line (hr) separates the user information from the order history.
* The order history section lists the user's past orders, if any.
* Each order is displayed on a table with the relevant information.
If the user has not placed any orders, a message is displayed indicating that there are no orders in their history.
![image](https://github.com/emmaC11/Dev-Connect/assets/83119583/dcea8957-ffe7-4915-9196-a852b851d1e7)

## Admin Panel
The admin super user can add & delete products to the catalogue within on the catalogue. They can also add different themes that can be used to filter products. Order staus can be viewed, users billing & shipping addresses.

# **Testing**
## Validator Testing
* To verify that the HTML code was written to the best standard, I conducted validator testing with the W3C Markup Validator. I fixed the errors and warnings and currently there are no errors or warnings in the HTML code.
![image](https://github.com/emmaC11/Dev-Connect/assets/83119583/bd567c82-4ff4-4199-89b7-2055c0374a8f)

* CSS styling was validated using the W3C CSS Validation Service to ensure the code was written to the expected standard. No errors were found when passing the code through the W3C CSS validator.
![image](https://github.com/emmaC11/Dev-Connect/assets/83119583/10c56d43-9114-46f7-8340-49031808409b)

I have used the PEP8 Linter to validate my code. It is activated within my code editor (Visual Studio Code). I had lots of 'lines too long' & 'whitespace' errors. I split lines where applicable, but I had to use #noqa (meaning line(s) is ignored by linters & validators) in settings.py as these lines could not be split without causing errors. I installed a [VS Extension](https://marketplace.visualstudio.com/items?itemName=shardulm94.trailing-spaces#:~:text=At%20any%20time%2C%20you%20can,type%20%22Trailing%20Spaces%3A%20Highlight%22) that highlights whitespace within the code. Throughout development I have been making tweaks to my code to ensure there are no errors. There are now no errros in my code. View the PEP8 documentation [here](https://peps.python.org/pep-0008/)



## add manual tests

## Event Listener Testing
Event listener testing focuses on verifying the functionality and responsiveness of event listeners within a web application.
* All button clicks trigger an event on the site.

## Responsive Testing
* The website was tested on several devices and screen sizes to ensure it was responsvie regardless of the screen size. It has been tested on desktop, Ipad Mini, Ipad Air, Iphone 5, Samsung Galaxy S8+, Iphone X, Iphone SE. Mobile devices have been tested in portrait and landscape mode. The site has been tested in Chrome, Edge, FireFox & Brave browsers.

## Lighthouse Testing
* The Lighthouse tool in Chrome DevTools is used to test a websites performance & accessibility. It is an open-source automated tool used to improve the quality of webpages.
When I tested my website, an audit report was returned indicating that my website has high performance and is accessible. However my accessibility rating is low, due to the white text on my hero image. This is something that will be addressed in next sprint.
![image](https://github.com/emmaC11/Dev-Connect/assets/83119583/315c81fb-aec0-4cd1-aa79-6b2ecf953e27)

## User Testing
The site has been tested regularly during development. After the site was completed I reached out to some fellow students & asks them to test the site & provide feedback.

## Bugs Identified During Development & Testing
* Site would not run locally as I did not have gitpod server in allowed_hosts.
* Heroku deployment was failing as I did add the disable_collectstatic config var
* Missing endblock tags in html template, fixed by adding {%endblock%} tag at end of HTML code.
* Content from base.html was not displaying in index.html as I did not add block content tags to base.html
* Images were not loading as I was not using load static template tag, I used images locally as a temporary fix until I identified the issue.
* Several times I forgot to close loops & if statements, best practise was going line by line to ensure the conditional or loop was closed when required,
* Some of my commit messages have spelling errors, however this is due to an issue with the bash terminal. I type the commit message correctly however it is changed after I confirm the commit.
![image](https://github.com/emmaC11/Dev-Connect/assets/83119583/a41f9e86-5a3b-4d27-94a5-99dfcc3cd5be)
* Some of my commit messages are way to vague, several commits have comments as I only realise after I complete a git push that several files & lines have been edited. I noticed that as I reached my project deadline my commit messages were becoming shorter & shorter.
* Tailwind css file constantly adding changes automatically, that is why these changes are mentioned in commits.
* Brick-by-brick project name not available in heroku, used brick-by-brickk
* When adding tailwind originally, I followed setup without django, did steps again with django doc and worked as expected, would have been easier if I set up when first starting project.
* Stored tailwind files in lego_main app while tailwind needs to be in separate theme app
* Content not displaying as I was missing block content tags after navigation bar
* Forgot to add .asView at end of views in urls.py causing the path to not work as expected.
* Reverting commits caused me to be behind in main branch.
* Template not rendering as product defined as legoSet in view not legoset, which was in template,
Legoorderitems not items in related name
![image](https://github.com/emmaC11/Dev-Connect/assets/83119583/ff36849e-2985-4d3c-90ec-1c426165bb24)
* PAYPAL scripts not rendering as I did not load script tags in base.html

# Business Model
The primary purpose of brick by brick is to provide an online platform for users to browse, select, and purchase LEGO products. The business model is primarily B2C (Business to Consumer), targeting individual consumers who are LEGO enthusiasts and shoppers interested in LEGO sets and products.

* Product Sales: The core intent of the application is to facilitate the sale of LEGO products. Users can browse a wide range of LEGO sets, choose the ones they desire, and make purchases online.

* User Engagement: To keep users engaged, the application offers features like user accounts & profile view to track their order history.

* Payment Processing: The application integrates with PayPal to securely process online payments for the products users wish to purchase.

* Product Management: The admin functionality allows for the addition of new LEGO products, management of product availability, and pricing updates.

## Marketing Strategies
* Search Engine Optimization (SEO): Optimizing the website for search engines with relevant keywords, meta tags, and high-quality content to improve organic search rankings and visibility. The site uses a variety of long tail and short tail keywords

* Mock Facebook page
![image](https://github.com/emmaC11/Dev-Connect/assets/83119583/f76f8d0d-7d91-4894-84e4-ba669f74b72b)














