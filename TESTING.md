## Table of Contents - Testing

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