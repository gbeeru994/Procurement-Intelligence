# Procurement Intelligence Platform

## API Specification

Base URL:

/api/v1

All endpoints return JSON responses.

Authentication uses JWT tokens.



## 1. Authentication APIs

POST /auth/register

Registers a new user.

Request body:

name
email
password



POST /auth/login

Authenticates user.

Request body:

email
password

Response:

access_token
user_profile



GET /auth/profile

Returns authenticated user profile.



POST /auth/logout

Invalidates session token.



## 2. Vendor APIs

POST /vendors

Create a vendor.

Fields:

name
city
area
category
brands
product_condition
email
phone
website
gst_number



GET /vendors

Returns list of vendors.

Supported filters:

city
category
verification_status
product_condition

Example:

/vendors?city=mumbai&category=networking



GET /vendors/{id}

Returns vendor details.



PUT /vendors/{id}

Updates vendor information.



DELETE /vendors/{id}

Removes vendor.



POST /vendors/{id}/verify

Marks vendor as verified.



POST /vendors/{id}/flag

Flags vendor as suspicious.



## 3. Orders APIs

POST /orders

Creates procurement order.

Fields:

product_name
brand
category
quantity
target_price
condition
location
deadline



GET /orders

Returns all orders.



GET /orders/{id}

Returns order details.



PUT /orders/{id}

Updates order.



DELETE /orders/{id}

Cancels order.



## 4. RFQ APIs

POST /orders/{id}/send-rfq

Triggers RFQ broadcast.

System selects vendors using filters.



GET /orders/{id}/quotes

Returns vendor quotes.



## 5. Quote APIs

POST /quotes

Vendor submits quote.

Fields:

vendor_id
order_id
quoted_price
quantity_available
delivery_time



PUT /quotes/{id}

Update quote.



GET /quotes

Returns all quotes.



## 6. Lead APIs

POST /leads

Create new lead.

Fields:

company_name
contact_person
email
phone
interest_category
source



GET /leads

Returns leads.



PUT /leads/{id}

Update lead status.



## 7. Price Intelligence APIs

GET /prices/history

Returns historical price data.



GET /prices/average

Returns average price of product.



GET /prices/opportunities

Returns detected market opportunities.



## 8. Analytics APIs

GET /analytics/vendors

Vendor performance metrics.



GET /analytics/deals

Deal success analytics.



GET /analytics/prices

Price trend analytics.



GET /analytics/leads

Lead conversion metrics.



## 9. Notification APIs

GET /notifications

Returns user notifications.



POST /notifications/mark-read

Marks notification as read.


