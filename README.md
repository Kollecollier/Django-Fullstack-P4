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

  As any other website, you fill out your username and password and then get redirected to the home page as a logged in user.

    ![This is an image](https://res.cloudinary.com/kolle1993/image/upload/v1669644058/Metalblog/sign_in_oirxou.png) <br />

  - Pressing the "sign up here!" link will redirect you to the "Register" page. 

  - There is also a "Remember me" option provided that will save your credentials.













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