## Table of Contents - Testing
- [User Story Testing](#user-story-testing)
- [Code Validation](#code-validation)
- [Browser Testing](#browser-testing)
- [Lighthouse](#lighthouse)
- [Manual Testing](#manual-testing)
- [Bugs](#bugs)
- [Unsolved Bugs](#unsolved-bugs)

### User Story Testing
|User Story|Notes|Result|
|----|----|----|
|As a user I can navigate the website so that I can explore the contents of the pages|The user can navigate the website by clicking on the links in the navigation bar|✔|
|As a Site User I can click on the menu so that I can view available ordering options|A menu with description and prices of the food options is visible by clicking on the menu link|✔|
|As a Site Admin I can create, read, update, and delete reservations so that I can efficiently manage restaurant bookings|Through the admin page, the administrator has the ability to perform CRUD operations on users' reservations.|✔|
|As a Site User I can register an account so that I can create, read, update, and delete my reservation.|The user can sign up through the designated link in the navigation bar|✔|
|As a Site User I can create, read, update, and delete my reservation so that I can manage and update my booking|Users can perform CRUD operations on their reservations|✔|
|As a Site User I can access a profile area so that I can keep track of all of my reservations.|A specific section to keep track of all the user's reservation has been provided in *My Reservations*|✔|

### Code Validation
#### HTML
All HTML pages were run through the [W3C HTML Validator](https://validator.w3.org/). Results in the table below

|Page|Result|
|----|----|
|reservations_list.html|✔|
|menu.html|✔|
|index.html|✔|
|edit_reservation.html|✔|
|delete_reservation.html|✔|
|confirmation_page.html|✔|
|booking.html|✔|
|base.html|✔|


The errors received pertain to the built-in Django functionalities, as illustrated in the screenshot, and are independent of any issues with the HTML structure.

<details><summary>W3C HTML Validator General Error found in .html pages.</summary>
<img src="/static/images/readme-images/html-validator.jpg">
</details>

#### CSS
|File|Result|
|----|----|
|style.css|✔|

<details><summary>W3C CSS Validator</summary>
<img src="/static/images/readme-images/css-validator.jpg">
</details>

#### JavaScript

The project incorporates only two JavaScript scripts, one for the menu buttons and another taken from Code Institute's 'I Think Therefore I Blog' project.

<details><summary>JsHint Validator</summary>
<img src="/static/images/readme-images/js-validator.jpg">
</details>

#### Python

|File|Result|
|----|----|
|views|✔|
|urls|✔|
|models|✔|
|forms|✔|
|admin|✔|

### Browser Testing

The Website was tested on Google Chrome, Microsoft Edge, and Firefox with no issues.

### Lighthouse
I performed Lighthouse validation on all pages, evaluating accessibility and performances. The following outlines the results.

|Page|Performance|Accessibility|Best Practices|SEO|
|----|----|----|----|----|
|Home|95|100|100|100|
|Menu|99|98|100|100|
|Reservations List|95|100|100|100|
|Edit Reservation|91|100|100|100|
|Delete Reservation|97|100|100|100|
|Confirmation Page|99|100|100|100|
|Book a Table|98|100|100|100|

### Manual Testing
|Item|Action|Expected Result|Pass|
|----|----|----|----|
|Logo|Click|Redirect to Home Page|✔|
|Home link|Click|Redirect to Home Page|✔|
|Menu link|Click|Redirect to Menu Page|✔|
|Menu buttons|Click|Redirect to relative sections of the menu|✔|
|Book a Table link|Click|Redirect to reservation page|✔|
|Book Now button|Click|Add a reservation to My Reservation|✔|
|Book a Table drop down menus|Click|selection of number of guests, date, and time allowed|✔|
|Book a Table date in the past|Click|Invalid form message displayed|✔|
|Book a Table empty Full name|Blank|Invalid form message displayed|✔|
|Book a Table make two reservations with same nick name|Text|Invalid form message displayed|✔|
|Booking Confirmation page links|Click|Redirect either to Menu or to My Reservation page|✔|
|Login link|Click|Redirect to sign in form|✔|
|My Reservations link|Click|Redirect to the list of reservations|✔|
|My Reservations Edit button|Click|Redirect to the edit reservation|✔|
|My Reservations Delete button|Click|Redirect to confirmation page|✔|
|Delete reservation button|Click|Delete reservation and direct to My Reservations page|✔|
|Cancel reservation deletion button|Click|Redirect to My Reservations page|✔|
|Logout link|Click|Redirect to sign out confirmation page|✔|
|Sign Out button|Click|Sign out and redirect to home page|✔|
|Message success when log in and log out|Display|Temporary message visible under the navigation bar|✔|
|Navbar links|Hover|Color change to dark grey|✔|
|Footer social links|Hover|Color change to dark grey|✔|
|Other links|Hover|Color change to dark grey|✔|
|Invalid forms|Display|Temporary message visible under the navigation bar|✔|

### Bugs
I have documented all the bugs addressed over the development of the projects on the GitHub Projects kanban. Below there's a summary and links.

|Bug|Status|
|----|----|
|[Date of booking in the future only #8](https://github.com/Darioc18/PP4-restaurant-booking-system/issues/8)|Closed|
|[Preventing Selection of Past Time/Date for Bookings #9](https://github.com/Darioc18/PP4-restaurant-booking-system/issues/9)|Closed|
|[Date Django Widget Issue #10](https://github.com/Darioc18/PP4-restaurant-booking-system/issues/10)|Closed|
|[Time Display Issues in Reservation List #11](https://github.com/Darioc18/PP4-restaurant-booking-system/issues/11)|Closed|
|[Optimizing Form Proportions for Improved User Experience #12](https://github.com/Darioc18/PP4-restaurant-booking-system/issues/12)|Closed|

### Unsolved Bugs
No unsolved bugs reported in the project

[Back to Contents](#table-of-contents---testing)