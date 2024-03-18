
![TailorFlow Logo](/media/default/Logo.png)
# TailorFlow

TailorFlow is a web application designed for tailors to efficiently manage their orders, products, customer details, measurements, transactions, and track business metrics through an intuitive dashboard.


## Features

- Authentication system.
- Password reset functionality.
- Create and edit orders, customer details, customer measurements etc..
- Simple and clean Dashboard for tracking key metrics such as customer acquisition, sales, payment types, etc., with filtering options.
- Search bar, filters and pagination on required pages for enhanced usability.
- Categorization of order items into "Stitched," "Urgent," "Delivered" and "Not-Stitched" for easy monitoring and management.
- Downloadable PDF invoices for orders.
- Clean and intuitive user interface.
- Tailor-specific data segregation: each tailor has their own set of customers, products, transactions, etc.


## Installation

1.Clone the repository.

```bash
git clone https://github.com/TharakaramuduN/TailorFlow1.git
```
2.Change directory to TailorFlow:

```bash
cd TailorFlow1
```

3.Install the required dependencies:

```bash
pip install -r requirements.txt
```
4.Create a .env file in the project root directory and add the following SMTP email configuration (replace 'user@gmail.com' and 'password' with your actual Gmail credentials):

```bash
EMAIL_HOST_USER='user@gmail.com'
EMAIL_HOST_PASSWORD='password'
```

5.If your Gmail account does not meet SMTP requirements and raised an error, comment out the email-related code in settings.py and remove the send email functionality in the registration view.

6.Start the development server:

```bash
python manage.py runserver
```

7.Access the application by navigating to http://localhost:8000 in your web browser. If you're a new user, sign up to create your credentials and access the full functionality of TailorFlow.


## Screenshots

- Home
  
![Home](/media/default/app_screenshots/home.png)

- Orders
  
![Orders](/media/default/app_screenshots/orders.png)

- Order Details
  
![Order Details](/media/default/app_screenshots/order_details.png)

- Customers
  
![Customers](/media/default/app_screenshots/customers.png)

- Customer Details

![Customer Details](/media/default/app_screenshots/customer_details.png)

- Transactions
  
![Transactions](/media/default/app_screenshots/transactions.png)

- Products

![Products](/media/default/app_screenshots/products.png)

- Dashboard
  
![Dashboard](/media/default/app_screenshots/dashboard.png)

- Profile
  
![Profile](/media/default/app_screenshots/profile.png)


## Contact
For support or inquiries, feel free to reach out or open an issue on GitHub.
* Email: tharakaramudu.nagaladinne@gmail.com

