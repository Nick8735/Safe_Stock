# Safe Stock

[View here for Safe Stock Inventory Management](https://safe-stock-77310870f391.herokuapp.com/login)



![Responsive Image](static/images/responsive.png)




# Project Goals
Safe Stock is crafted for the straightforward management of stock in small businesses, eliminating complexity from the process. It empowers users with the flexibility to oversee both incoming and outgoing stock effortlessly. Users can seamlessly review stock levels and rectify any discrepancies promptly, ensuring accurate and well-maintained stock levels.

Additionally, users have the convenience of monitoring stock levels and user engagement through an intuitive dashboard. In instances where understanding the reason behind stock changes becomes crucial, the system provides a last transaction user stamp. This feature allows users to review and identify the individual responsible for the latest transaction for each item.

Safe Stock employs MongoDB as its non-relational database for efficient data storage and retrieval.

## C.R.U.D

1. C - Create - Receipt Stock
2. R - Read - Stock Overveiw & Low Stock report
3. U - Update - Stock Overveiw - Edit
4. D - Delete - Issue Stock 


# User Experience (UX)

##  <b>User Stories</b>

### First Time Visitor Goals

1.  As a first time visitor, I want to view what data is being stored.
2.  As a first time visitor I want to bring stock to account and have a variety of different data ranging across multple different identifiers to support with traceability and stock control. 
3.  As a first time visitor, I want to issue stock from account to keep stock accurate with stock movement out of the business and data base.
4. As a first-time visitor,  I want to navigate the website easily and have clear access to all pages of the site.

### Returning Visitor Goals

1. As a returning visitor, I want to check stock levels.
2. As a returning visitor, I want to check stock accuracy and know if there are discrepancies within the stock.
3. As a returning visitor, I want to look at stock that needs to be reordered.
 

### Frequent Visitors Goals

1. As a frequent user, I want to see a dashboard that shows stock levels and users.
2. As a frequent user, I want to investigate stock discrepancies by reviewing the stock levels and seeing who was last to adjust any of the stock.
3. As a frequent user, I want to search for a specific item by searching for the name when reviewing stock levels.

## Testing User Stories

* Diane - Chef

First Time Visitor

1. First time visitor was able to navigate to the stock overveiw screen.
2. User was able to receipt stock to account without any errors.
3. User was able to issue stock from account without any errors.

Returning Visitor

1. User found it simple to check the stock on the overveiw report.
2. User was able to navigate to stock check and input stock details into check accuracy.
3. User was able to navigate to low stock report and was able to explain what they would use this report would be used for.

Frequent Visitor

1. The user was able to navigate to the dashboard and was able to outline the importance of both graphs. 
2. The User to see what user completed the last transaction.
3. The user was able to search for a specific stock item.

# Design

### Colour Scheme

<img src="static/images/palette.png" alt="home-page" style="width:550px;"/>

1. I chose the color palette as I believe the shades of blue and grey give a professional feel. 

### Imagery

1. All images were selected from [Shutterstock](https://www.shutterstock.com). I looked for perfossional setting images with the hero image linking to learning.

# Project design plan
<br>

## Login 

1. Login page stayed to similar design, this is simplistic and clear for user to complete goal..

<img src="static/images/wf_login.png" alt="page-2" style="width:450px;"/><img src="static/images/login.png" alt="page-2" style="width:450px;"/>

<img src="static/images/register.png" alt="page-2" style="width:450px;"/>

2. Home screen remained similar to original design however. the live version has more transactions than originally planned due to ensuring that C.R.U.D could be clearly shown throughout the system. 

<img src="static/images/wf_home.png" alt="page-2" style="width:450px;"/> <img src="static/images/home.png" alt="page-2" style="width:450px;"/>

3. The stock report also stayed to the planned design just with extra columns to allow more data to be presented to the user.

<img src="static/images/wf_stock_report.png" alt="page-4" style="width:450px;"/> <img src="static/images/stock_overveiw.png" alt="page-4" style="width:450px;"/>

4. Receipt stock design stayed similar to design. I would change the colour of the form to a lighter colour for this part of the design.

<img src="static/images/wf_receipt.png" alt="page-5" style="width:450px;"/> <img src="static/images/receipt.png" alt="page-5" style="width:450px;"/> 

5. Issue stock stayed stayed similar to initial design, again I would change the form colours and more the text more clearer if done again.

<img src="static/images/wf_issue.png" alt="page-6" style="width:450px;"/> <img src="static/images/issue.png" alt="page-6" style="width:450px;"/>

6. Move stock was not used in the final production.

<img src="static/images/wf_move.png" alt="page-6" style="width:450px;"/>

7. Dashboard added during production.

<img src="static/images/dashboard.png" alt="page-6" style="width:450px;"/>

8. Low stock report added during production.

<img src="static/images/low_stock_report.png" alt="page-6" style="width:450px;"/>

9. Stock Count added during production.

<img src="static/images/check_stock.png" alt="page-6" style="width:450px;"/>

## Areas that changed during development

* I increased the amount of transactions to ensure that the system would support the user with more tasks.
* I removed the move stock feature as this was not going to have the controls I wanted being that my aim was to have a dynamic schema and not fixed.
* I added low stock page, this would be used to remind the user to re-order stock when the levels hit a certain threshold. Future development of this would be to allow the user to set the threshold.
* I added a dashboard to track KPI's for the system. Future development would be a selection of data the user could request to capture the desired KPI in a multitude of graphs including histograms with trend lines.
* I added a stock count process, this is to enable the user to do a blind stock count and will give the user access to update the system to the correct findings.

# Features

* Nav-Bar - Professional and centered for user focus.

![Nav-Bar](static/images/navbar1.png)

* Nav-Bar dropdown used with mobile.

![Nav-Bar_dropdown](static/images/navbar2.png)

* Login Page.

![Mission](static/images/login.png)

 * Register for user to create an account.

![Relate](static/images/register.png)

* Access page for site, links to all transaction pages.

![Demo's](static/images/home1.png)

* Stock overview page which shows the stock list taken from MONGO DB.

![Procedure](static/images/stock_overveiw_1.png)

 * Edit stock, edit documents and change stock levels.

 ![Test](static/images/edit_stock.png)

* Receipt stock, adds a document to Mongo DB which can then be viewed on the stock overview page. 

![End](static/images/receipt.png)

* Issue Stock, deletes a line off Mongo DB which can be viewed in the stock overview. 

![Cert](static/images/issue.png)

* Dashboard view KPI's. 

![Contact](static/images/dashboard.png)

* Low Stock report, filters for all stock levels 5 and below, this is used for the user to re-order stock. 

![Contact_submit](static/images/check_stock.png)

* Stock count page, used for when the user is checking stock. Transaction will tell the user if the details are correct, if not the user will be sent to the stock overview page to change the stock. 

## Future Updates

1. Stock overview will have a search bar so the users can view selective data.
2. Issue transaction will be simplified and will be drop downs to stock user error causing problems with issuance.
3. Master data for locations and stock details will mean easier searching and stock could be moved locations.
4. Cycle counting to ensure all lodactions are checked once a month.
5. Change password for login page.
6. More graphs for dashboard.
7. mutiple reports including Transaction history, Purchase order history etc...
8. Purchase order planned delivery dates which can be used in conjunction with on time in full report.
9. electronic registers, this would be used for bespoke business requirments such as safety checks of racking and out of scope system work.

# Technologies Used

## Languages Used

* HTML5
* CSS3
* JS
* python
* Heroku
* Mongo DB
* Flask

## Frameworks, Libraries & Programs Used

1. Bootstrap 4.4.1
* Bootstrap was used to support only with the Nav Bar and Footer.
2. Git
* Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub. 
3. GitHub
* Github was used to store project coding after being pushed.
4. Balsamic
*  Balsamic was used to support with design and planning.
5. Shutterstock 
* Shutterstock was used to format images.
6. Stack Overflow
* Supported with debugging across the different functions.
7. Slack
* Supported with mutiple issues with deploying and dockerfile queries.
8. Mongo DB
* Database for the software.
9. Heroku
* Cloud server for deployment.
10. Gitpod
* Gitpod used to code.


# Testing

### HTML

The W3C Markup Validator was used to validate every page of HTML code.

* 0 errors with only one warning which has no impact on the user or integrity on the site.


![HTML validation no errors](asset/css/script/images/html-warning.png)


### CSS

* The following shows CSS errors found at W3C Validator: 

Errors were for oversights in my code. 

![CSS validation errors](asset/css/script/images/css-validation.png)

* Errors rectified and validation complete.

![CSS validation no errors](asset/css/script/images/css-no_errors.png)


### JS 

* The following validation was done with JS Hint.

* The following errors found were for missing semicolon that was an oversight that has now been corrected.

![JS validation errors](asset/css/script/images/js-errors.png)
<br>
<br>
<br>

* Errors corrected

![JS validation errors](asset/css/script/images/js-validation_no-error.png)

### Lighthouse testing

* Lighthouse shows areas could be improved regarding some images positioning and file sizes which could affect the durability of the website if in the red.
* Main objective for myself was to have an accessibility score of over 90% as seen by the foillowing images the site has a score of 98%.

![Lighthouse 1](asset/css/script/images/lighthouse-1.png)

![Lighthouse 2](asset/css/script/images/lighthouse-2.png)

## User Stories Testing

## Test 1

|Action                                         |                       Expected Result                        | Actual Result |
|:-----------------------------------------------|:------------------------------------------------------------:|--------------:|
| I want to Access the register page and register a new user and password. |Flash message will appear to confirm creation  |   As expected |


https://github.com/Nick8735/Safe_Stock/assets/110351696/fbb632d4-76c3-491d-9bb9-5b233fabe863


<br>

## Test 2

|Action                                         |                       Expected Result                        | Actual Result |
|:-----------------------------------------------|:------------------------------------------------------------:|--------------:|
| I have registered I want to return to login. | Press already register button to go back to login. |   As expected |

[![Test 2](asset/css/asset/doc/user-storie_testing/test-2.gif)](https://github.com/Nick8735/Safe_Stock/assets/110351696/39aef6b2-6c0f-42c4-93e8-adfada9148e2)

<br>

## Test 3

|Action                                         |                       Expected Result                        | Actual Result |
|:-----------------------------------------------|:------------------------------------------------------------:|--------------:|
| I want to login with my new account. | login via login box. |   As expected |


https://github.com/Nick8735/Safe_Stock/assets/110351696/3d789c58-3994-4132-a08b-8b507035e5fc




<br>

## Test 4

|Action                                         |                       Expected Result                        | Actual Result |
|:-----------------------------------------------|:------------------------------------------------------------:|--------------:|
| If I put in the incorrect details do I still login. | User receives flash message stating incorrect details and does not progress. |   As expected |



https://github.com/Nick8735/Safe_Stock/assets/110351696/ca64d5b6-bb9d-4726-bbba-ca171633244c



<br>

## Test 5

|Action                                         |                       Expected Result                        | Actual Result |
|:-----------------------------------------------|:------------------------------------------------------------:|--------------:|
| I want to go to the home page. | user will be at the home page after login|   As expected |


https://github.com/Nick8735/Safe_Stock/assets/110351696/cc26a0e1-b3bc-48c9-a674-7b4b05ab1c97



<br>

## Test 6

|Action                                         |                       Expected Result                        | Actual Result |
|:-----------------------------------------------|:------------------------------------------------------------:|--------------:|
| Does the Navbar buttons work. | Each NavBar button will take the user to each specific transaction.|   As expected |



https://github.com/Nick8735/Safe_Stock/assets/110351696/5476bfc8-98fd-488c-96e3-c9e415477b43



<br>

## Test 7

|Action                                         |                       Expected Result                        | Actual Result |
|:-----------------------------------------------|:------------------------------------------------------------:|--------------:|
| Where to find stock the stock list taken from Mongo DB and shown on site. | User will click on stock overview and see full stock list taken from Mongo DB|   As expected |


https://github.com/Nick8735/Safe_Stock/assets/110351696/c66771d6-6435-47a8-b77d-e24b89ad7b76


<br>

## Test 8

|Action                                         |                       Expected Result                        | Actual Result |
|:-----------------------------------------------|:------------------------------------------------------------:|--------------:|
| Does the receipt button work. | User will click on Receipt and a form will show |   As expected |



https://github.com/Nick8735/Safe_Stock/assets/110351696/39e5e775-494b-4458-98b6-f0e9f0b17582



<br>

## Test 9

|Action                                         |                       Expected Result                        | Actual Result |
|:-----------------------------------------------|:------------------------------------------------------------:|--------------:|
| How do I create stock and view stock holdings. | User will complete receipt form and notification will appear to tell user stock is created. User will go to stock overview to check new row.|   As expected |



https://github.com/Nick8735/Safe_Stock/assets/110351696/739a9ef8-a146-420c-96fb-ab4f140b2c63



<br>

## Test 10

|Action                                         |                       Expected Result                        | Actual Result |
|:-----------------------------------------------|:------------------------------------------------------------:|--------------:|
| Has this row been created in Mongo DB and matches what is on the site in stock overview. | User will check stock overview then check the document in Mongo DB|   As expected |



https://github.com/Nick8735/Safe_Stock/assets/110351696/bcf8a21d-0896-4402-8f52-49c9312331ce



<br>

## Test 11

|Action                                         |                       Expected Result                        | Actual Result |
|:-----------------------------------------------|:------------------------------------------------------------:|--------------:|
| I want to Issue stock from account. | User will go to Issue transaction and complete form and get confirmation of issuance|   As expected |


https://github.com/Nick8735/Safe_Stock/assets/110351696/70878c6e-5747-4906-b1f9-40e89575218f



<br>

## Test 12

|Action                                         |                       Expected Result                        | Actual Result |
|:-----------------------------------------------|:------------------------------------------------------------:|--------------:|
| Has the Row been deleted in Mongo DB. | User will check stock overview to see that row is deleted then will check Mongo DB for the document|   As expected |



https://github.com/Nick8735/Safe_Stock/assets/110351696/9424f7eb-ad48-45ec-8b2c-8c4771e06e06


<br>

## Test 13

|Action                                         |                       Expected Result                        | Actual Result |
|:-----------------------------------------------|:------------------------------------------------------------:|--------------:|
| I want to see a graph on stock holding, qty. | User will navigate to the Dashboard transaction on the home page and verify one coloumn against the stock overview to see if it is correct. |   As expected |



https://github.com/Nick8735/Safe_Stock/assets/110351696/1ed0af9a-d928-4d21-9a8e-356c7dc2038b


<br>

## Test 14

|Action                                         |                       Expected Result                        | Actual Result |
|:-----------------------------------------------|:------------------------------------------------------------:|--------------:|
| I want to edit my stock holding. | User will go to stock overview and press edit, user will adjust Qty and submit, user will get a message to stock holdings have been changed. |   As expected |



https://github.com/Nick8735/Safe_Stock/assets/110351696/131ed80e-b2ef-4d92-80e4-eeeb742f74a2


<br>

## Test 15

|Action                                         |                       Expected Result                        | Actual Result |
|:-----------------------------------------------|:------------------------------------------------------------:|--------------:|
| Has the document in Mongo DB been adjusted from the edit in stock overview. | User will check stock overview then go to Mongo DB and check the document for the change. |   As expected |



https://github.com/Nick8735/Safe_Stock/assets/110351696/5f1ca2bf-3eb0-4b7b-a95c-65bfd769ad40


<br>

## Test 16

|Action                                         |                       Expected Result                        | Actual Result |
|:-----------------------------------------------|:------------------------------------------------------------:|--------------:|
| I want my stock holdings that have a qty 5 or below to show on the low stock report. | user will check low stock report then go to stock overview and make a qty over 5 down to a number less than 5, once done user will check the low stock report to see if row has appeared. |   As expected |



https://github.com/Nick8735/Safe_Stock/assets/110351696/147a2e7c-e410-4c0b-9b2d-9c21aa0e1b9b



<br>

## Test 17

|Action                                         |                       Expected Result                        | Actual Result |
|:-----------------------------------------------|:------------------------------------------------------------:|--------------:|
| I want to check that if I get a stock increase over 5 on an item it will be removed from the low stock report. | User will check the low stock report for a row and will then go to the stock overview and increase the qty, user will then check this against the low stock report to see that row has disappeared |   As expected |



https://github.com/Nick8735/Safe_Stock/assets/110351696/df7d4586-69a5-45f9-92bf-e23f035a8fae




<br>

## Test 18

|Action                                         |                       Expected Result                        | Actual Result |
|:-----------------------------------------------|:------------------------------------------------------------:|--------------:|
| When checking physical stock I want input my findings and get a message to tell me my stock is correct. | user will access the stock count menu and fill in the form with current stock details and press the button |   As expected |



https://github.com/Nick8735/Safe_Stock/assets/110351696/a2e358ec-16e3-4b28-add1-a9021cf665ca



## Test 19

|Action                                         |                       Expected Result                        | Actual Result |
|:-----------------------------------------------|:------------------------------------------------------------:|--------------:|
| I want to be told if my stock has a discrepancie during a stock count. | User will go to stock count and input incorrect details on the form user will get a message to say stock is incorrect. |   As expected |



https://github.com/Nick8735/Safe_Stock/assets/110351696/73543ec9-4570-4849-91f2-d57edf82b421



## Test 20

|Action                                         |                       Expected Result                        | Actual Result |
|:-----------------------------------------------|:------------------------------------------------------------:|--------------:|
| I want to logout. | user will press the logout button in Navbar |   As expected |



https://github.com/Nick8735/Safe_Stock/assets/110351696/baba31f6-3a03-4cc9-9355-7f4a4bbe90a3


## User Feedback

* Website was accessed by multiple family and friends who gave the following feedback for bugs and suggestions.

1. Andrew - The website is very simple and easy to use, as a shift manager I need to be confident that the systems we use for training will result in skilled workers. The way the system is presented pushes the user to leanr when unsure. My only criticism was a question that could of been easily misconstured for something else which you re-worded.

2. Wendy - I believe this kind of training system is a must for businesses with large amounts of employees. Updates down the line I would like to see some statistics of who has completed the tests and who has struggled. This would help me understand which of my employees need more support. Great job! 

# Deployment

## GitHub Pages

The project was deployed to GitHub Pages using the following steps...

1. Log in to GitHub and locate the GitHub Repository
2. At the top of the Repository (not top of page), locate the "Settings" Button on the menu. Alternatively Click Here for a GIF demonstrating the process starting from Step 2.
3. Scroll down the Settings page until you locate the "GitHub Pages" Section.
4. Under "Source", click the dropdown called "None" and select "Master Branch".
5. The page will automatically refresh.
6. Scroll back down through the page to locate the now published site link in the "GitHub Pages" section.



## Forking the GitHub Repository

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log in to GitHub and locate the GitHub Repository
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

## Making a Local Clone

1. Log in to GitHub and locate the GitHub Repository
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type git clone, and then paste the URL you cpoied in step 3

$ git clone https://github.com/Nick8735/Training


Press Enter. Your local clone will be created.


$ git clone https://github.com/Nick8735/Training


* Cloning into `CI-Clone`...
* remote: Counting objects: 10, done.
* remote: Compressing objects: 100% (8/8), done.
* remove: Total 10 (delta 1), reused 10 (delta 1)
* Unpacking objects: 100% (10/10), done.

# Credits

* [W3Schools](https://www.w3schools.com/) for support with bugs and coding errors.

* [Bootstrap5.3](https://getbootstrap.com/) Used to support with navigation bar.

* [Shutterstock](https://www.shutterstock.com/) for all images.

* [Balsamiq](https://balsamiq.com/) For Wireframes.

## Content

All content was written by the developer.

## Acknowledgemts 
* My College Tutor for continuous support and understanding throughout.
* My Mentor for great feedback and support.
* My partner who looked after the kids while I tapped away.
