# Metalcore Django Blog P4

## This is my first business based blog.
<br />

- ### As a musician and a music lover i have tried to implement my love for the heavier music genre into my programming work. This is a one page music blog were i can place and let people read my personal thought's  and review's of some of my favourite band's from 2022!
<br />
 
### This idea can be used for all sorts of businesses of any kind!
<br />
 Please take the time to check this read me file and get an understanding of the website.

![This is an image](https://res.cloudinary.com/kolle1993/image/upload/v1669640729/Metalblog/FireShot_Capture_109_-_Am_I_Responsive__-_ui.dev_oscpyq.png)
- # Content list:
    - 1 WireFrame and routing
    - 2 Frontend Interface
    - 3 Authentication
    - 4 Features
    - 5 Comment section
    - 6 CRUD
    - 7 Deployment steps
    - 8 Extentions
    - 9 Installed apps
    - 10 Admin panel
    - 11 

 <br />

# 1 Wireframe and routing!

- ### Routes
- ![This is an image](https://res.cloudinary.com/kolle1993/image/upload/v1669642276/Metalblog/routing_a69nn0.png)

- ### Home page structure:
- ![This is an image](https://res.cloudinary.com/kolle1993/image/upload/v1669645704/Metalblog/wirehome_c3mz1i.png)

- ### Post and content structure:
- ![This is an image](https://res.cloudinary.com/kolle1993/image/upload/v1669646965/Metalblog/poststucture_wv0910.png)

<br />

# 2 Frontend & Pages
 - #### The Home Page (Frontend)
-  The Frontend is a clean and simple easy to navigate starter page. <br />
    For this page i have used the templates provided to me as a student via the Code Institute walkthrough project, these templates and css have been changed to my liking throughout the entire frontend.
![This is and image](https://res.cloudinary.com/kolle1993/image/upload/v1669647213/Metalblog/Frontend_home_page_uvmqom.png) <br />

- #### The Post Page (Frontend)
    -  The top section of the page is identical across all post's and is in 3 sections:

- ### Top
    - The top is banner of the post with post title and post image:
    - ![This is an image](https://res.cloudinary.com/kolle1993/image/upload/v1669647550/Metalblog/post_page_header_wcmx1s.png)

- ### Middle
    - The mid section of the page is displaying the post text and an inbedded spotify player with the post artist the post is refering to, there is also a like and comment counter:
    - ![This is an image](https://res.cloudinary.com/kolle1993/image/upload/v1669647551/Metalblog/post_page_text_and_player_ean7k6.png)

    - ### Bottom
    - The bottom section of the post is the comment section of the page with comments on the left side and the comment field body on the right.
    - ![This is an image](https://res.cloudinary.com/kolle1993/image/upload/v1669647575/Metalblog/post_page_comment_section_kub9up.png)

<br />

# 3 Authentication

- ### The register page:
- When pressing the register page, you get sent over to a sign up form. <br /> Here you get to fill out our username, email(optional) and password! <br /> The request then get's sent to the backend and you are officialy a authenticated user. 

   ![This is an image](https://res.cloudinary.com/kolle1993/image/upload/v1669642763/Metalblog/Register_hathm4.png) <br />

  - The register password error:
    - When entering an invalid password that dose not meet the citeria, these errors will be show'n:
    - ![This is an image](https://res.cloudinary.com/kolle1993/image/upload/v1669643110/Metalblog/password_error_yi4x2x.png)

    - Upon success on account registration, a pop up message is displayed that let's you know that you have been registered:

        ![This is an image](https://res.cloudinary.com/kolle1993/image/upload/v1669643617/Metalblog/popup_hlz58i.png)

    - And as seen below, our new user "Adam123" has been stored as a user in the backend along with the rest!
    
    ![This is an image](https://res.cloudinary.com/kolle1993/image/upload/v1669643728/Metalblog/stored_users_dvlare.png)

- ### The login page:


    - When pressing the login page, you will get redirected to Sign in form page.
    As any other website, you fill out your username and password and then get redirected to the home page as a logged in user. <br />
    ![This is an image](https://res.cloudinary.com/kolle1993/image/upload/v1669644058/Metalblog/sign_in_oirxou.png) <br />

  - Pressing the "sign up here!" link will redirect you to the "Register" page. 

  - There is also a "Remember me" option provided that will save your credentials.

- ### The Logout page:

    - The logout page is as seen below, asking if the user if they are sure they want to logout!

    ![This is an image](https://res.cloudinary.com/kolle1993/image/upload/v1669715490/Metalblog/signout_vsiw3s.png)

- Upon successful logout, the following message is displayed:

    ![This is an image](https://res.cloudinary.com/kolle1993/image/upload/v1669715621/Metalblog/singedoutmessage_q3pz8w.png)


# 4. Features
  - ## The NavBar

 - #### This Navigation bar is clean and simple and more or less says it'self!
    - ### Right side (Logged out)
        ![This is an image](https://res.cloudinary.com/kolle1993/image/upload/v1669641055/Metalblog/nav_logged_out_jsdhsz.png) <br />

       - As seen above, when the user is not logged in or authenticated, the navigationbar give's 3 responsive buttons, "Home", "Register", "Login"


    - ### Left side (Logged in)
        ![This is an image](https://res.cloudinary.com/kolle1993/image/upload/v1669640727/Metalblog/nav1_zko876.png)


       - When You are logged in (also know as authenticated), the navigationbar will display "Home" & "Logout"
<br />

    - ### Right side
        ![This is an image](https://res.cloudinary.com/kolle1993/image/upload/v1669642324/Metalblog/rightnav_a9n8fc.png)
        - The right side of the navbar shows the same if you are logged in or not.
<br />
  - ## Spotify Player
    - On the post pages, there are diffrent media players for the diffrent artist's the post is refering to, inbedded with a javascript code into the blog post. Simply play the music by pressing play, and your music will start playing!

    ![This is an image](https://res.cloudinary.com/kolle1993/image/upload/v1669716551/Metalblog/dplayer_ujmkab.png)
<br />

- Please notice the diffrent players here, the player for a so called "singel" (a one song release), is just playable as a preview. <br>
Also worth mentioning that the "E" beside "preview" stands for "Explicit Content" and is targeted for a mature audiance.

     ![This is an image](https://res.cloudinary.com/kolle1993/image/upload/v1669716632/Metalblog/mplayer_xyytd3.png)

- ## The Comment Section
 - On every post page at the bottom of the post there is a comment section.
- On everypage without a comment the field is shown as below:


![This is an image](https://res.cloudinary.com/kolle1993/image/upload/v1670234286/Metalblog/comment_space_spuqzf.png)
   <br />

 - ## The comment section view (logged out):
- If you are logged out or not an authenticated user, the comment section will only display the comment,time,date and the user that created the comment if there is one.

 ![This is an image](https://res.cloudinary.com/kolle1993/image/upload/v1670234063/Metalblog/comment_signed_out_k5s2ot.png)

 - ## The comment section view (logged in):

 - If you are logged in user, the comment field changes to this view:

 ![This is an image](https://res.cloudinary.com/kolle1993/image/upload/v1670234580/Metalblog/logged_in_comment_ilufpk.png)

  - Now there is a comment form avalible for the logged in user, also showing who you are posting as.

  - The update button is already provided when logged a logged in user is authenticated (see comment crud funtion section.)

- ## Submitting a comment
 - When submitting a comment, the comment is sent to the backend for admin approval, As seen below, this is the process of commenting:

 ![This is an image](https://res.cloudinary.com/kolle1993/image/upload/v1670234975/Metalblog/this_is_a_comment_of2xop.png)

 ![This is an image](https://res.cloudinary.com/kolle1993/image/upload/v1670235082/Metalblog/comment_approval_er8lzo.png)

## The comment is sent to thhe backend for admin approval:
 ![This is an image](https://res.cloudinary.com/kolle1993/image/upload/v1670235196/Metalblog/comment_approval_admin_wxckkc.png)

 - Admin select's the "approved" action then presses "go":

![This is an image](https://res.cloudinary.com/kolle1993/image/upload/v1670235309/Metalblog/comment_approval_admin_action_ku7wyl.png)

- After Admin approval, the comment is greenlit and you comment is now shown on the comment section of the page:
![This is an image](https://res.cloudinary.com/kolle1993/image/upload/v1670235581/Metalblog/comment_view_approved_flmg1t.png)

 - ## Comment CRUD Function
- If you are a logged in user and you comment has been admin approved, you will se the 3 diffent options displayed on the comment field:
![This is an image](https://res.cloudinary.com/kolle1993/image/upload/v1670239302/Metalblog/crud1_gfr8wi.png)

- The Delete & and Update button is only fuctional for the logged in user that has made the comment on the page.

- Pressing delete will reflect directly on the frontend and you comment will be erased from the page.
  The image's below show the update steps:
  ### Set your new comment in the comment form and press "Update"
  ![This is an image](https://res.cloudinary.com/kolle1993/image/upload/v1670239921/Metalblog/crud4_hk26ld.png)

   ### After pressing update, you will get a preview as shown below, is you are satisfied, press update again:
  ![This is an image](https://res.cloudinary.com/kolle1993/image/upload/v1670239828/Metalblog/crud3_m7xbzf.png) 

  ### The result is a updated comment with a new time stamp: 
  ![This is an image](https://res.cloudinary.com/kolle1993/image/upload/v1670240498/Metalblog/crud5_bbc57a.png) 

  ### Now press delete:
  ![This is an image](https://res.cloudinary.com/kolle1993/image/upload/v1670241187/Metalblog/cruddelete_h6hkst.png)

  ### As seen above, you comment has been deleted and the comment field is empty, the page also signals a message at the top leting you know your comment is gone.
<br />

 - ## Deployment Steps
    <br>
 - 1 Created Workspace
 - 2 Created app on heroku
 - 3 Took all steps in gitpod to install the app to get it running
 - 4 Server used is guniorn
 - 5 Deployed to heroku at an early stage for convenience
 - 6 Added all the code to the app, git added and pushed after every new code added, migrated after every model change.
 - 7 Did command pip3 freeze for txt file after each new installed app or program.
 - 8 Before final deployment, some tests were done to the code to check for any error ect (See testing section)
 - 9 Deployed with the following config vars:

   ![This is an image](https://res.cloudinary.com/kolle1993/image/upload/v1670241884/Metalblog/vars_oemrhk.png)
 
 # Extentions Used
 - Auto Close Tag
 - Auto Open Preview Panel
 - Beautify, but has been replaced with prettier
 - Bootstrap 4 CDN
 - Django
 - ES7 React (For react components but auto installed)
 - Groovy lint, Format and Fix
 - Html Css support
 - Jupyter, keymap, notebook renderers
 - Pretty Formatter
 - Python
 - React Javascript snippet
 - React Typescript snippet (XAcademy)
 <br />

 # Used Apps
- django contrib admin (FOR BACKEND)
- django contrib auth (FOR BACKEND)
- django contrib contenttypes
- django contrib sessions
- django contrib messages 
- django contrib sites
- allauth (AUTHENTICATION)
- allauth account 
- allauth socialaccount (FOR SOCIAL ACCOUNT REGISTRATION)
- cloudinary storage (CLOUD BASED FILE STROAGE)
- django contrib staticfiles
- cloudinary (CLOUDBASED STORAGE)
- blog (APP NAME)
- django summernote (BACKEND POST)
- crispy forms (BACKEND POST FORM STYLE)
- Gunicorn (For server)
- Bootstrap 4 (For styling and CSS templates)

 # Admin Panel
  - The admin panel is the stardard django admin panel.
    - This is were you can manage all comments, make posts, and were all the data is stored.
    ## Admin Layout:
    Site administration is as shown below, the diffrent pages on the left and recent actions on the right:
    ![This is an image](https://res.cloudinary.com/kolle1993/image/upload/v1670253684/Metalblog/siteadmin_uc8sg3.png)

    ### The most important thing's in this backend is the "Users","Posts" and "Comment" pages.
    <br />
  - ## Users 
  - Here all the registered users are stored, each user has it's own data (Due to security this information will not be added here)
  ![This is an image](https://res.cloudinary.com/kolle1993/image/upload/v1670253891/Metalblog/siteusers_dbevcj.png)

- ## Posts
 - The post page is were the admin can create a new post to published or save a draft post, inside the post page you see all the post's that are draft or published:
 ![This is an image](https://res.cloudinary.com/kolle1993/image/upload/v1670261632/Metalblog/post_page_x00hax.png) 
<br />

 ### If you press "ADD POST" on the top right, you will be redirected to a post create form, were summernote has been implemented:

 ![This is an image](https://res.cloudinary.com/kolle1993/image/upload/v1670261876/Metalblog/postsave_ut2van.png)


 - At the bottom right of the page, you can save and add another, save and continue editing, and last save.
   - Select "draft" or "published" before saving the blog post to set this as a draft or a published post! 

- ## Comment's

### In the comment's section the page is identical to the post's page!
- Diffrence here is that you as an admin can approve or delete a selected commeent on the "Action" dropdown button, also at top right you can add a comment.
- This page works the same and operates the same as the post page:
 ![This is an image](https://res.cloudinary.com/kolle1993/image/upload/v1670262450/Metalblog/commentpost_vxje6o.png)

 ## That cover's the backend and the frontend for this django project.
 <br />


 # Testing
 # UserStory
 # Credits
 # Debuging
  1 cloudinary not delcared in settings 2.typo configvar, fixed
 