# Soupa Restaurant
This website is designed for a fictional restaurant located in Ireland.
It has been created as part of the Project Portfolio 4 for Code Institute's Full Stack Software Development Diploma.
The development utilized a Full-Stack Toolkit, with VS Code as a IDE, and GitHub for repository management and emulation of an Agile development environment through GitHub Projects.
When completed, the website was deployed using Heroku.

![Mockup image](/static/images/readme-images/mockup.png)

## Live site

[Soupa Restaurant](https://pp4-restaurant-booking-system-d75be81c2fba.herokuapp.com/) _(Ctrl + click to open in a new tab)_

## Table of Contents





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

#### Existing User
- As an existing user, I can easily navigate the website to either check alternative menu options or to log in into my account. [#1](https://github.com/Darioc18/PP4-restaurant-booking-system/issues/1)
-  As an existing user, I want to quickly access and check the menu to explore any new additions or seasonal offerings at the restaurant. [#2](https://github.com/Darioc18/PP4-restaurant-booking-system/issues/2) 
- As an existing user I can create, read, update, and delete my reservation so that I can manage and update my booking [#5](https://github.com/Darioc18/PP4-restaurant-booking-system/issues/5)
- As an existing user I can access a profile area so that I can keep track of all of my reservations. [#6](https://github.com/Darioc18/PP4-restaurant-booking-system/issues/6)
- As an existing user, I rely on the website's map functionality to confirm the restaurant's location and plan my return visits efficiently. [#7](https://github.com/Darioc18/PP4-restaurant-booking-system/issues/7)
- As an existing user, I appreciate the continued responsiveness of the website, allowing me to consistently access and interact with its features on different devices with ease. [#13](https://github.com/Darioc18/PP4-restaurant-booking-system/issues/13)
- As an existing user I can reset my password so that I can quickly and securely regain access to my account. [#14](https://github.com/Darioc18/PP4-restaurant-booking-system/issues/14)

#### Website Owner/Developer
- As a Site Admin I can create, read, update, and delete reservations (CRUD functionality) so that I can efficiently manage restaurant bookings [#3](https://github.com/Darioc18/PP4-restaurant-booking-system/issues/3)

#### Benefit of User Stories and Agile Development
Creating user stories during the development process offers several key benefits for the users, the developers and the customer. 
- **Benefit for the users:** Creating user stories during the development process, especially within the context of agile development, significantly benefits users by ensuring a continuous and iterative focus on their needs. The agile approach allows for frequent feedback loops and adjustments, meaning that as users see early iterations of the product, their insights can be incorporated quickly. This responsiveness to user feedback leads to a final product that is not only aligned with user expectations but can also adapt to changing requirements throughout the development cycle. 
- **Benefit for the developers:** In an agile development environment, user stories play a crucial role in providing developers with a clear and prioritized roadmap. By breaking down features into user stories, developers can work on small, manageable tasks in short development cycles, known as sprints. This incremental approach allows for more flexibility and adaptability to changing requirements. Developers can focus on delivering tangible value in each iteration, leading to a more efficient and responsive development process.
- **Benefit for the customer:** Agile development, driven by user stories, offers customers the advantage of flexibility and continuous improvement. Customers can actively participate in the development process, prioritizing features based on changing business needs. The iterative nature of agile development ensures that customers see a functional product early and often, providing them with a tangible representation of progress. This close collaboration and responsiveness to customer feedback contribute to a final product that not only meets their expectations but also aligns closely with evolving business objectives.

[Back to Contents](#table-of-contents)

### Agile Methodology
GitHub Projects was used to manage the development process following an agile methodology. The project board, accessible through this [link](https://github.com/users/Darioc18/projects/2), served as a practical tool for organizing tasks and tracking progress. This approach allowed the team to respond promptly to changes and collaborate effectively.

The **MOSCOW** method was employed for task prioritization, categorizing them into Must-haves, Should-haves, Could-haves, and Won't-haves. This systematic prioritization ensured a focused and flexible development process, adapting to changing requirements while delivering incremental value.

[Back to Contents](#table-of-contents)

### Database Scheme
The data model for the restaurant project adheres to Object-Oriented Programming principles and utilizes Django's Class-Based Views. The **user authentication system** is powered by Django AllAuth.
Facilitating table bookings involves the incorporation of a **custom reservation model**. This model captures essential details like full name, nickname, booking date and time, number of guests, and any additional notes from guests. Importantly, the reservation model establishes a connection with the User model, ensuring that each reservation is associated with a specific user.

![Database Scheme](/static/images/readme-images/data-model.png)

[Back to Contents](#table-of-contents)



