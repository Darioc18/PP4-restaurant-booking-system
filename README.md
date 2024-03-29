# Soupa Restaurant
This website is designed for a fictional restaurant located in Ireland.
It has been created as part of the Project Portfolio 4 for Code Institute's Full Stack Software Development Diploma.
The development utilized a Full-Stack Toolkit, with VS Code as a IDE, and GitHub for repository management and emulation of an Agile development environment through GitHub Projects.
When completed, the website was deployed using Heroku.

![Mockup image](/static/images/readme-images/mockup.png)

## Live site

[Soupa Restaurant](https://pp4-restaurant-booking-system-d75be81c2fba.herokuapp.com/) _(Ctrl + click to open in a new tab)_

## GitHub Repository

[My GitHub](https://github.com/Darioc18/PP4-restaurant-booking-system)

## Table of Contents
- [User Experience](#user-experience)
- [Agile Methodology](#agile-methodology)
- [Database Scheme](#database-scheme)
- [Defensive Design](#defensive-design)
- [Design](#design)
- [Features](#features)
- [Testing](#testing)
- [Technologies Used](#technologies-used)
- [Deployment](#deployment)
- [Credits](#credits)

## User Experience

### Project Goals
The goals of the website include:

- **Online Visibility:** Increase the restaurant's online presence by creating a professional and easily discoverable website.
- **Menu Showcase:** Clearly present the restaurant's menu with detailed descriptions and prices to attract potential customers.
- **User-Friendly Experience:** Ensure a seamless and user-friendly experience for visitors, making it easy for them to navigate the website and find relevant information.
- **Online Reservations:** Implement a reservation system to allow customers to book tables conveniently through the website.
- **Contact Information:** Display accurate and up-to-date contact information, including address, phone number, and business hours, to assist potential customers.
- **Responsive Design:** Ensure the website is mobile-friendly and responsive to accommodate users accessing it from various devices.
- **Social Media Integration:** Connect the website with social media platforms to leverage social sharing and engage with customers on different channels.

[Back to Contents](#table-of-contents)

### User Stories

#### New User
- As a new user, I want to navigate the website to gain an understanding of the restaurant's type and offerings. [#1](https://github.com/Darioc18/PP4-restaurant-booking-system/issues/1)
- As a new user, I want the ability to click on the menu to view the available cuisine types. [#2](https://github.com/Darioc18/PP4-restaurant-booking-system/issues/2)
- As a new user I can register an account so that I can create, read, update, and delete my reservation. [#4](https://github.com/Darioc18/PP4-restaurant-booking-system/issues/4)
- As a new user, I want to use the website's map feature to easily locate the restaurant and get directions to ensure a smooth first-time visit. [#7](https://github.com/Darioc18/PP4-restaurant-booking-system/issues/7)
- As a new user, I expect the website to be responsive, providing a seamless and accessible experience across various devices, ensuring I can easily navigate and explore its content. [#13](https://github.com/Darioc18/PP4-restaurant-booking-system/issues/13)
- As a new user, I want to access the customer review section to gain insights into the restaurant's reputation and build trust before making a reservation. [#16](https://github.com/Darioc18/PP4-restaurant-booking-system/issues/16)

#### Existing User
- As an existing user, I can easily navigate the website to either check alternative menu options or to log in into my account. [#1](https://github.com/Darioc18/PP4-restaurant-booking-system/issues/1)
-  As an existing user, I want to quickly access and check the menu to explore any new additions or seasonal offerings at the restaurant. [#2](https://github.com/Darioc18/PP4-restaurant-booking-system/issues/2) 
- As an existing user I can create, read, update, and delete my reservation so that I can manage and update my booking [#5](https://github.com/Darioc18/PP4-restaurant-booking-system/issues/5)
- As an existing user I can access a profile area so that I can keep track of all of my reservations. [#6](https://github.com/Darioc18/PP4-restaurant-booking-system/issues/6)
- As an existing user, I rely on the website's map functionality to confirm the restaurant's location and plan my return visits efficiently. [#7](https://github.com/Darioc18/PP4-restaurant-booking-system/issues/7)
- As an existing user, I appreciate the continued responsiveness of the website, allowing me to consistently access and interact with its features on different devices with ease. [#13](https://github.com/Darioc18/PP4-restaurant-booking-system/issues/13)
- As an existing user I can reset my password so that I can quickly and securely regain access to my account. [#14](https://github.com/Darioc18/PP4-restaurant-booking-system/issues/14)
- As an existing user, I aim to explore special offers and promotions on the site to make informed decisions about booking a table during active promotion periods. [#15](https://github.com/Darioc18/PP4-restaurant-booking-system/issues/15)
- As an existing user, I aim to contribute to and revisit the customer review section regularly to stay informed about others' experiences and maintain trust in the restaurant's credibility. [#16](https://github.com/Darioc18/PP4-restaurant-booking-system/issues/16)

#### Website Owner/Developer
- As a Site Admin I can create, read, update, and delete reservations (CRUD functionality) so that I can efficiently manage restaurant bookings [#3](https://github.com/Darioc18/PP4-restaurant-booking-system/issues/3)

### Benefit of User Stories and Agile Development
Creating user stories during the development process offers several key benefits for the users, the developers and the customer. 
- **Benefit for the users:** Creating user stories during the development process, especially within the context of agile development, significantly benefits users by ensuring a continuous and iterative focus on their needs. The agile approach allows for frequent feedback loops and adjustments, meaning that as users see early iterations of the product, their insights can be incorporated quickly. This responsiveness to user feedback leads to a final product that is not only aligned with user expectations but can also adapt to changing requirements throughout the development cycle. 
- **Benefit for the developers:** In an agile development environment, user stories play a crucial role in providing developers with a clear and prioritized roadmap. By breaking down features into user stories, developers can work on small, manageable tasks in short development cycles, known as sprints. This incremental approach allows for more flexibility and adaptability to changing requirements. Developers can focus on delivering tangible value in each iteration, leading to a more efficient and responsive development process.
- **Benefit for the customer:** Agile development, driven by user stories, offers customers the advantage of flexibility and continuous improvement. Customers can actively participate in the development process, prioritizing features based on changing business needs. The iterative nature of agile development ensures that customers see a functional product early and often, providing them with a tangible representation of progress. This close collaboration and responsiveness to customer feedback contribute to a final product that not only meets their expectations but also aligns closely with evolving business objectives.

[Back to Contents](#table-of-contents)

## Agile Methodology

Agile methodology is an iterative and flexible approach to project management and software development that prioritizes adaptability, collaboration, and customer satisfaction. It emphasizes incremental progress, continuous feedback, and the ability to respond to changing requirements throughout the development process.

I've adhered to the principles of agile methodology during the website development, incorporating the following key aspects:

### GitHub Projects/Kanban Board
GitHub Projects was used to manage the development process following an agile methodology. The project board, accessible through this [link](https://github.com/users/Darioc18/projects/2), served as a practical tool for organizing tasks and tracking progress.

### MoSCoW Prioritization

The MOSCOW method was employed for task prioritization, categorizing them into Must-haves, Should-haves, Could-haves, and Won't-haves. This systematic prioritization ensured a focused and flexible development process, adapting to changing requirements while delivering incremental value.

<details><summary>MoSCoW & GitHub Kanban</summary>
<img src="/static/images/readme-images/moscow.jpg">
</details>

### User Stories

I designed a template for streamlined user story creation. The user story issue format includes tasks detailing the crucial steps for resolving the issue. This method visually tracks the progress of each project issue.

<details><summary>User Story Template</summary>
<img src="/static/images/readme-images/user-story-template.jpg">
</details>

[Back to Contents](#table-of-contents)

## Database Scheme
The data model for the restaurant project adheres to Object-Oriented Programming principles and utilizes Django's Class-Based Views. The **user authentication system** is powered by Django AllAuth.
Facilitating table bookings involves the incorporation of a **custom reservation model**. This model captures essential details like full name, nickname, booking date and time, number of guests, and any additional notes from guests. Importantly, the reservation model establishes a connection with the User model, ensuring that each reservation is associated with a specific user.

![Database Scheme](/static/images/readme-images/data-model.png)

[Back to Contents](#table-of-contents)

## Defensive Design

### Form Validation:

Comprehensive form validation mechanisms have been implemented. In the event of incorrect or empty data during form submission, the form blocks the submission and displays a user-friendly warning. This approach ensures users promptly receive feedback about the specific fields causing errors.

### Database Protection:

Prioritizing confidentiality and safeguarding against unauthorized access, my database security approach involves storing the database URL and secret key in a separate *env-py* file. This precautionary measure was established before the initial push to GitHub, preserving the confidentiality of sensitive information.

### Cross-Site Request Forgery (CSRF) Protection:

The website employs CSRF tokens on all forms across the site, adding an extra layer of defense against cross-site request forgery attacks.

[Back to Contents](#table-of-contents)

## Design

The primary design goal for this restaurant website is to create an intuitive, visually appealing, and responsive interface that prioritizes user experience. The design aims to seamlessly guide users through the website, ensuring easy navigation and quick access to essential information. A clean and visually engaging layout will enhance the presentation of the restaurant's cuisine. Additionally, the overall aesthetic will reflect the restaurant's brand identity, creating a cohesive and inviting online presence that aligns with the establishment's atmosphere and values.

### Colour Scheme

The decision behind the color palette for this website is anchored in the principles of simplicity and elegance. A deliberately limited color palette has been chosen to maintain a clean and uncluttered visual appearance, contributing to a straightforward and user-friendly design.
By employing a restrained color scheme, the focus is directed towards essential elements.
This approach to color selection aims to create a harmonious and visually pleasing design.

![Colour Scheme](/static/images/readme-images/palette.png)

### Typography

The project employs the Roboto font from Google Fonts throughout.
Roboto is a distinguished typeface renowned for its elegant and versatile design. With a modern and sophisticated aesthetic that perfectly adapts to the design intent of the website.

![Roboto Font](/static/images/readme-images/font.jpg)

## Features

### Logo

I conceptualized a restaurant name and created a logo using Photoshop. The logo represents a stylized smoking soup bowl.

![Logo](/static/images/readme-images/logo.jpg)

### Navigation Bar

- The navigation bar looks the same on every page, made with Bootstrap to work well on all screen sizes.
![Navbar](/static/images/readme-images/navbar.jpg)

- When the user is logged in the navigation options expand including *Book a Table*, *My Reservations*, and *Logout* 
![Navbar Logged In](/static/images/readme-images/navbar-logged-in.jpg)

- On smaller devices, you can open the navbar elements using a hamburger menu.
![Navbar Hamburger Menu](/static/images/readme-images/navbar-hamburger.jpg)

### Footer

The footer includes essential information such as the address and contacts, opening days and hours, and social links, including a link to [my GitHub repository](https://github.com/Darioc18/PP4-restaurant-booking-system).

![Footer](/static/images/readme-images/footer.jpg)

### Home Page

The homepage features a simple yet elegant and minimal restaurant interior image created with Bing AI.

### Menu
The menu, styled with CSS, features buttons with added JavaScript functionality to redirect users to the main menu categories.

![Menu](/static/images/readme-images/menu.jpg)

### Register, Login, Logout

Django Allauth was used to incorporate register, login, and logout functionalities.
<details><summary>Sign Up</summary>
<img src="/static/images/readme-images/register.jpg">
</details>

<details><summary>Sign In</summary>
<img src="/static/images/readme-images/login.jpg">
</details>

<details><summary>Sign Out</summary>
<img src="/static/images/readme-images/logout.jpg">
</details>

Users are provided with success messages upon successful login and logout actions. In case of invalid inputs, error messages are displayed to notify users of the incorrect submission.

<details><summary>Success Message</summary>
<img src="/static/images/readme-images/success-message.jpg">
</details>

### Book a Table
The feature comprises a custom form enabling users to make reservations. I have used tuples in the model class to provide specific selections for the number of guests and booking times, offering a tailored and user-friendly reservation experience.

<details><summary>Number of Guests</summary>
<img src="/static/images/readme-images/num-of-guests.jpg">
</details>

<details><summary>Time of Booking</summary>
<img src="/static/images/readme-images/time.jpg">
</details>

Specifically for the booking time in Ireland, I have integrated *pytz* within Django, a time zone library. This provides reservation scheduling tailored to Ireland's local time.
```
class Reservation(models.Model):
    DUBLIN_TZ = pytz.timezone('Europe/Dublin')
```
For dates I have used a custom widget that specifically handles dates:
```
class DateInput(forms.DateInput):
    input_type = 'date'
```
<details><summary>Date of Booking</summary>
<img src="/static/images/readme-images/date.jpg">
</details>

### My Reservations
 This feature showcases cards containing details of all reservations made by the user. Users have two options:
 <details><summary>My Reservations</summary>
<img src="/static/images/readme-images/reservations.jpg">
</details>

- **Edit**: Redirects to the edit reservation page, allowing users to make modifications and save changes.
<details><summary>Edit Reservation</summary>
<img src="/static/images/readme-images/edit-reservation.jpg">
</details>

- **Delete**: Redirects to a confirmation page where users can confirm their intention to delete the reservation.
<details><summary>Delete Reservation</summary>
<img src="/static/images/readme-images/delete-reservation.jpg">
</details>

### Future Implementations

A few user stories were excluded from the current project due to time limitations. They are visible in on the dedicated [GitHub Projects](https://github.com/users/Darioc18/projects/2) kanban board for this project. The following are some of features that could be implemented in future iterations and that have been added to the *future implementations* on the kanban board:

- **Specials and Promotions:** Highlight any special offers, promotions, or events to attract and engage customers.

- **Customer Reviews and Testimonials:** Incorporate a section for customer reviews and testimonials to build trust and credibility.

- **Online Ordering:** If applicable, provide an option for online food ordering to cater to customers who prefer takeaway or delivery services.

[Back to Contents](#table-of-contents)

## Testing
Testing documentation can be found [here](TESTING.md)

## Technologies Used

### Languages

- Python
- HTML
- CSS
- JavaScript
- Bootstrap
- Django

### Python Modules
- [Django-allauth](https://pypi.org/project/django-allauth/) Integrated set of Django applications addressing authentication, registration, account management as well as 3rd party (social) account authentication.
- [Gunicorn](https://pypi.org/project/gunicorn/) is a Web Server Gateway Interface (WSGI) server implementation that is commonly used to run Python web applications.
- [Psycopg2](https://pypi.org/project/psycopg2/) is a PostgreSQL database adapter for Python. It allows Django to connect to PostgreSQL databases.

### Other Programs and Applications

- [Git](https://developer.mozilla.org/en-US/docs/Glossary/Git)
- [Github Pages](https://github.com/)
- [Visual Studio Code](https://code.visualstudio.com/)
- [Google Fonts](https://fonts.google.com/)
- [Google Dev Tools](https://developer.chrome.com/docs/devtools/open/)
- [Google Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/)
- [Code Institutes Pep8 Checker](https://pep8ci.herokuapp.com/)
- [Lucid Chart](https://www.lucidchart.com/)
- [Favicon.io](https://favicon.io/)
- [Photoshop](https://www.adobe.com/ie/products/photoshop.html)
- [W3C HTML Validator](https://validator.w3.org/)
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
- [CI Python Pep8 Checker](https://pep8ci.herokuapp.com/)
- [PostGresSQl](https://www.postgresql.org/) used to store the database locally
- [ElephantSQL](https://www.elephantsql.com/) is a PostgreSQL database hosting service
- [Heroku](https://heroku.com/) used to deploy the application
## Deployment
### Deployment process
1. Navigate to the Heroku dashboard and create a new app with a unique name.
2. Click on the Settings tab and reveal the config vars. Add a key of DISABLE_COLLECTSTATIC and a value of 1 and click Add. This step prevents Heroku from uploading static files, such as CSS and JS, during the build.
3. Install Gunicorn, a production-ready webserver for Heroku. Add gunicorn to the requirements.txt file
4. Create a file named Procfile at the root directory of the project (same directory as requirements.txt).
5. In the Procfile, declare this is a web process followed by the command to execute your Django project.
```web: gunicorn my_project.wsgi```
Where my_project is the name of my project.
6. Open the my_project/settings.py file and replace DEBUG=True with DEBUG=False.
7. In settings.py append the Heroku hostname to the ALLOWED_HOSTS list
8. On Heroku click on the Deploy tab.
9. In the Deployment method section enable GitHub integration by clicking on Connect to GitHub.
10. Search for the Github repository and click Connect.
11. After setting up the database on Elephant SQL create a file env.py and add it to gitignore
12. In the env.py file, the DATABASE_URL value was copied from ElephantSQL when we created our database instance.
13. Make up a new SECRET_KEY value. It can be any combination of letters, numbers and symbols.
14. Once you have your secret key, set it as an environment variable in your env.py file.
15. Modify your settings.py file to retrieve the new SECRET_KEY from the environment variables.
```SECRET_KEY = os.environ.get("SECRET_KEY")```
16. To ensure the security of your Django app on Heroku, set the SECRET_KEY as a config variable on Heroku as well and add the following Config Vars:
    - DARABASE_URL from the env.py
    - DEBUG = False
    - PORT = 8000
    - DISABLE_COLLECTSTATIC = 1
17. Ensure in Django settings, DEBUG is False
18. Scroll to the bottom of the deploy page and either click Enable Automatic Deploys for automatic deploys or Deploy Branch to deploy manually. Manually deployed branches will need re-deploying each time the repo is updated.
19. Click View to view the deployed site.

### Local Development

To fork the repository:

1.  Go to the [GitHub repository](https://github.com/Darioc18/memory-game);
2.  In the top-right corner of the page, click _Fork_;
3.  Optionally type the _Repository name_ and _Description_;
4.  Click the green button _Create fork_.

To clone the repository:

1. Go to the [GitHub repository](https://github.com/Darioc18/memory-game);
2. Above the list of files, click the green button _Code_;
3. Choose your preferred method for cloning: HTTPS, SSH, or Github CLI. Click the copy button to copy the URL to your clipboard.
4. Open Git Bash.
5. Change the current working directory to the location where you want the cloned directory.
6. Type git clone, and then paste the URL you copied earlier.
7. Press Enter. Your local clone will be created.

## Credits

### Code

- [Code Institute Full Template](https://github.com/Code-Institute-Org/ci-full-template)
- [Django Docs](https://docs.djangoproject.com/en/3.2/)
- [Django All Auth Documentation](https://docs.allauth.org/en/latest/installation/quickstart.html)
- [Bootstrap v5.1 Docs](https://getbootstrap.com/docs/5.1/getting-started/introduction/)
- [W3Schools](https://www.w3schools.com/)
- [Stack Overflow](https://stackoverflow.com/)

## Aknowledgments

I would like to express my gratitude to my Code Institute mentor, [Iuliia Konovalova](https://github.com/IuliiaKonovalova) for her guidance and clear advice to build this project.
