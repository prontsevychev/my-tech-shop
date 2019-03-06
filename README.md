# tech-shop

My first _big_ project. Tech shop which using this [template][1].

Has the following functionality:
* main page (static, at present);
* blog page, with 1 post from db, others static;
* post page, with information from db. In addition, 
if there is a quote in the text of the post, it`s wrapped with special tags;
* contact information in header and separate contacts page with Google map and form for feedback.
For contact info used django-constance. For send emails from own domain used mailgun;
* Internationalization and localization for russian and ukrainian languages in templates.
For models using Django-modeltranslation;
* Django-environ for environment variables;
* product page with an opportunity to add it to cart;
* cart page and cart info in header;
* possibility to pay for the contents of the cart using LiqPay payment API;
* tuned ansible for quick project deploy.


[1]: https://colorlib.com/wp/template/onetech/
