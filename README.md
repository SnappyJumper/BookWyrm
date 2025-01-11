# BookWyrm


![BookWyrm mockup image](assets/readme_files/mockup_img.png)


BookWyrm is a website created for avid readers to post and share information about their favourite books and authors. All under the protection of dragons.

The main objective of the site is to create a space where users can share the stories and authors they love with a wider community. This is achieved through the publishing of reviews and author bios.

Visit the deployed site [here](https://bookwyrm-f93c738e909e.herokuapp.com/)


## Table of Contents

1. [User Experience (UX)](#user-experience-ux)
    1. [Strategy](#strategy)
        1. [Project Goals](#project-goals)
        2. [User Goals](#user-goals)
        3. [Strategy Table](#strategy-table)
    2. [Scope](#scope)
        1. [User Stories](#user-stories)
    3. [Structure](#structure)
    4. [Skeleton](#skeleton)
    5. [Surface](#surface)
2. [Features](#features)
    1. [General](#general)
    2. [Home Page](#home-page)
    3. [Reviews Page](#reviews-page)
    4. [Authors Page](#authors-page)
    5. [Book Review Page](#book-review-page)
    6. [Author Bio Page](#author-bio-page)
    7. [Add Review Page](#add-review-page)
    8. [Edit Review Page](#edit-review-page)
    9. [Delete Review Prompt](#delete-review-prompt)
    10. [Add Author Page](#add-author-page)
    11. [Edit Author Page](#edit-author-page)
    12. [Delete Author Prompt](#delete-author-prompt)
    13. [Authentication Pages](#authentication-pages)
    14. [404 Page](#404-page)
3. [Technologies Used](#technologies-used)
    1. [Languages Used](#languages-used)
    2. [Libraries and Frameworks](#libraries-and-frameworks)
    3. [Packages / Dependencies Installed](#packages-dependencies-installed)
    4. [Database Management](#database-management)
    5. [Tools and Programs](#tools-and-programs)
4.  [Testing](#testing)
    1. [Go to TESTING.md](https://github.com/SnappyJumper/BookWyrm/blob/main/TESTING.md#bookwyrm-testing)
5. [Deployment](#deployment)
6. [Finished Product](finished-product)
7. [Credits](#credits)
8. [Known Bugs](#known-bugs)
9. [Acknowledgements](#acknowledgements)


***


## User Experience (UX)

### Strategy

### Project Goals

* The website contains rich colors to go with the theme of dragons, whilst also not drawing away from the content too much.

* It has a responsive design so its accessable across a range of screen sizes.

* Structure is easy to navigate and understand.

* Site Users can login or register to fully interact with the site contents.

* Site Users can leave reviews about the authors posted on the site.

* Site Users can add bios about their favourite authors and post them to the site.


### User Goals

* As a Site Admin, I want to be able to manage the content of the site.

* As a Site User, I want to be able to interact with the content on the site.

* As a Site User, I want the information provided by the site to be simple to understand and easy to navigate.

* As a Site User, I want to be able to create and manage my content.


#### Strategy Table

Issue | Importance | Viability / Feasibility
--- | --- | ---
Responsive design | 5 | 5
User registration | 5 | 5
Create, edit and delete Authors | 5 | 4
Create, edit and delete Reviews | 5 | 4
Saving reviews and authors as drafts | 5 | 4
Adding profile pictures for users | 3 | 2
Commenting on other users content | 3 | 2
Social Media registration | 3 | 2
Ability to search for reviews | 3 | 2
Have a community rating system for book entries | 2 | 2
**Total** | **39** | **32**


### Scope

When reviewing the strategy table it is clear that not all features can be implemented in the first release of the project. In this case the project will be released in phases. The first phase will consist of features identified to build the minimul viable product.

**First Phase**

* Responsive design

* Account registration

* Create, edit and delete Authors

* Create, edit and delete Reviews

* Save un-published content as a draft 

**Second Phase**

* Commenting on other users content

* Adding profile pictures for users

* Social Media registration

* Ability to search for reviews

**Future Phases**

*  Have a community rating system for book entries


### User Stories

GitHub projects was used as my project management tool to track user stories. Using the Kanban board helped me to better visualise the scope of the project and get tasks completed in an organised manner.

![User Stories Kanban img](assets/readme_files/user_story_kanban.png)


### Structure

The website has a Hierarchial Tree Structure so that navigation through the site is effortless. Here is a sketch of the structure made using [miro](https://miro.com/).

![BookWyrm website map](assets/readme_files/site_structure.png)

* The header, footer and nav bar remain consistent across all pages.

* Links and forms provide feedback to the Site User.

* Once the User us logged in or registered they are given greater access to the site.

* A custom 404 page has also been implemented.


#### Database Model

The databade model was designed using [drawsql](https://drawsql.app/). The type of database being used is a relational PostgreSQL database supplied by [Code Institute](https://dbs.ci-dbs.net/)

![BookWyrm database model](assets/readme_files/database_model.png)

The database model was designed before the project with a larger scope in mind. For this MVP release I will discuss the models that have been implemented. The others will be added at a later phase.

**Book Model**

* Title: Unique book title provided by the review's author.

* Slug: Stores a unique slug to identify the review by.

* Author: Stores the Author of the book being reviewed as a Author Foreign Key.

* Genre: Stores the genre of the book.

* Book_published: Stores the date the book was published set by the review's author.

* Review: Review details provided by the review's author.

* Rating: A rating out of 5 for the book provided by the review's author

* Status: Review author provides the status so the review is either published or a draft.

* Review_author: Stores the author of the review as a User Foreign Key.

* Created_on: Date and time set when review is created

**Author Model**

* Name: Unique author name provided by the bio's author.

* Slug_author: Stores a unique slug to identify the author by.

* Date_of_birth: Stores the date the author was born supplied by the author of the bio.

* Nationality: Stores author's nationality supplied by bio's author.

* Genre: Stores the authors writting genre supplied by the bio's author.

* Favourite_book: Stores the author's favoutite book supplied by the bio's author.

* Bio: Author bio details suppplied by the bio's author.

* Status: Bio's author proved the status to determine wether to publish bio or save as a draft.

Posted_by: Stores the author of the bio as a User Foreign Key.

### Skeleton

#### Wireframes

[Balsamiq](https://balsamiq.com/) was used to help build the appearance of the site and display the placement of different elements in the pages. As the development of the project progressed some of the ideas in the wireframes were altered or abandoned so the wireframes differ from the final product.

Page | Desktop | Mobile
--- | --- | ---
Index | ![Desktop Index](assets/wireframes/wireframe_home_desktop.png) | ![Mobile Index](assets/wireframes/wireframe_home_mobile.png)
login | ![Desktop Login](assets/wireframes/wireframes_login_desktop.png) | ![Mobile Login](assets/wireframes/wireframe_login_mobile.png)
Reviews | ![Desktop Reviews](assets/wireframes/wireframe_reviews_desktop.png) | ![Mobile Reviews](assets/wireframes/wireframe_reviews_mobile.png)
Authors | ![Desktop Authors](assets/wireframes/wireframe_authors_desktop.png) | ![Mobile Authors](assets/wireframes/wireframe_authors_mobile.png)
Review | ![Desktop Review](assets/wireframes/wireframe_review_desktop.png) | ![Mobile Review 1](assets/wireframes/wireframe_review_mobile_1.png) ![Mobile Review 2](assets/wireframes/wireframe_review_mobile_2.png)
Author | ![Desktop Author](assets/wireframes/wireframe_author_bio_desktop.png) | ![Mobile Author](assets/wireframes/wireframe_author_bio_mobile.png)
Add / Edit Author | ![Desktop Add/Edit Author](assets/wireframes/wireframe_add_author_desktop.png) | ![Mobile Add/Edit Author](assets/wireframes/wireframe_add_author_mobile.png)
Add / Edit Review | ![Desktop Add/Edit Review](assets/wireframes/wireframe_add_review_desktop.png) | ![Mobile Add / Edit Review](assets/wireframes/wireframe_add_review_mobile.png)
Add / Edit Comment | ![Desktop Add / Edit Comment](assets/wireframes/wireframe_leave_comment_desktop.png) | ![Mobile Add / Edit Comment](assets/wireframes/wireframe_leave_comment_mobile.png)


### Surface

#### Color Scheme

![Color scheme image](assets/readme_files/color_scheme.png)

The colors used in the website are a dark red (#8B0000) for the main background and white smoke (#F5F5F5) for the header background and body text. Gold (FFD700) was used for subtitles and Davy's Grey (#4A4A4F) for the brand and alert text. Dark moss green (#4B5320) was used for the content boxes whereas golden gate bridge (#E84610), tangelo(#FF4500), brandeis blue (0D6EFD) , teal (188181) and verdigris (23BBBB) were used to style numerous buttons and links thoughout the site.

These colors were chosen because of their warmth and richness. They also match golds, greens and reds of dragons which suit the sites theme.

#### Typograpy

The main font used in the site is Roboto, with a sans-serif fall back in case of import errors. The font used on the brand and titles throughout the website is Kaushan Script with a serif fall back incase if import errors.

The Kaushan Script was chosen because it suited the theme of the site and Roboto is a script that reads well for content.

[Back to top ⇧](#bookwyrm)


## Features

### General

* The website was designed with mobile first in mind.

* The design is responsive across all devices.

* Navigation Bar:
    * Desktop:
    ![Nav Bar Desktop](assets/readme_files/nav_bar_desktop.png)

    * Mobile:
    ![Nav Bar Mobile](assets/readme_files/nav_bar_mobile.png)

    * Contains the site brand.

    * Contains the links to other areas of the site with the current page highlighted.

    * Collapses into a burger bar button when viewed on smaller devices.

* Footer
    * ![Footer](assets/readme_files/footer.png)

    * Footer displays the site creators username and some links to socials.


### Home Page

* Featured Reviews and Authors List

    * Desktop:
    ![Home Desktop](assets/readme_files/home_page_desktop.png)

    * Mobile:
    ![Home Mobile 1](assets/readme_files/home_page_mobile_1.png)
    ![Home Mobile 2](assets/readme_files/home_page_mobile_2.png)

    * Displays a list of 4 featured reviews and 3 featured authors and some relevant info to engage the User.

    * Provides a button below each to take the User to the author or review.

    * For un-registered Users buttons display to encourage you to login or sign up in both the welcome field and at the bottom of the page.

    * For registered Users buttons replace the login or sign up prompts encouraging you to explore reviews and authors in the welcome field and at the bottom of the page to add a review.

### Reviews Page

* Reviews List:

    * Desktop:
    ![Reviews List Desktop](assets/readme_files/reviews_page_desktop.png)

    * Mobile:
    ![Reviews List Mobile](assets/readme_files/reviews_page_mobile.png)

    * Displays a paginated, responsive list of all the reviews and some relative info to engage the User.

    * Provides the user with a link in the title to the detailed review.

    * For logged in Users there is a section for their saved drafts so they can view them before final editing and publishing.

    * User is encouraged to add more reviews when logged in via a button at the bottom of the page.

### Authors Page

* Authors List:

    * Desktop:
    ![Authors Page Desktop](assets/readme_files/authors_page_desktop.png)

    * Mobile:
    ![Authors Page Mobile](assets/readme_files/authors_page_mobile.png)

    * Displays a paginated, responsive list of all the authors and some relative info to engage the User.

    * Provides the user with a link in the name to the detailed bio.

    * For logged in Users there is a section for their saved drafts so they can view them before final editing and publishing.

    * User is encouraged to add more authors when logged in via a button at the bottom of the page.

### Book Review Page

* Book Instance:

    * Desktop:
    ![Book Review Page Desktop](assets/readme_files/book_review_page_desktop.png)

    * Mobile:
    ![Book Review Page Mobile](assets/readme_files/book_review_page_mobile.png)

    * Displays a responsive instance of the Book Model for the User to view.

    * Logged in Users who created the instance can edit or delete it via two buttons in the masthead.

    * The Review itself is delivered in a rich text format.

### Author Bio Page

* Author Instance:

    * Desktop:
    ![Author Bio Page Desktop](assets/readme_files/author_bio_page_desktop.png)

    * Mobile:
    ![Author Bio Page Mobile](assets/readme_files/author_bio_page_mobile.png)

    * Displays a responsive instance of the Author Model for the User to view.

    * Logged in Users who created the instance canedit or delete it via two buttons in the masthead.

    * The review itself is delivered in a rich text format.

### Add Review Page

* Add Review Form:

    * Desktop:
    ![Add Review Page Desktop](assets/readme_files/add_new_review_desktop.png)

    * Mobile:
    ![Add Review Page Mobile](assets/readme_files/add_new_review_mobile.png)

    * Renders a responsive form for the logged in User to add their own review to the site.

### Edit Review Page

* Edit Review Form:

    Desktop:
    ![]


