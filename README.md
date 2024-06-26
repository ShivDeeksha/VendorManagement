# Vendor Management System

This is a vendor management system project.

## Installation

1. Clone the repository:
git clone https://github.com/ShivDeeksha/VendorManagement


2. Navigate to the project directory:
cd VendorManagement


3. Create a virtual environment:
python -m venv venv


4. Activate the virtual environment:
- On Windows:
  ```
  venv\Scripts\activate
  ```
- On Unix or MacOS:
  ```
  source venv/bin/activate
  ```

5. Navigate to the project directory:
cd vendorMgmt

6. Install the required dependencies:
pip install -r requirements.txt


## Usage

1. Run the Django development server:
python manage.py runserver


2. Open another terminal and obtain an access token:

```powershell
$headers = @{
    "Content-Type" = "application/json"
}

$body = @{
    username = "admin"
    password = "a123"
}

$response = Invoke-WebRequest -Uri "http://localhost:8000/api/token/" -Method Post -Headers $headers -Body ($body | ConvertTo-Json)
$response.Content
```
Or you can use curl:
```
curl -X POST -H "Content-Type: application/json" -d '{"username": "admin", "password": "a123"}' http://localhost:8000/api/token/
```
3. Copy the access token.
4. Open Postman and create a new request.
5. Go to the Headers tab and add a new header with the key Authorization and the value Bearer <access_token>. Replace <access_token> with the token you copied earlier.
6. Send the request.
### Eg: Vendor List/Create Endpoint:
- **URL:** `http://localhost:8000/api/vendors/`
- **Method:** GET (to retrieve) or POST (to create)
- **Headers:** 
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE0OTEzOTU0LCJpYXQiOjE3MTQ5MTM2NTQsImp0aSI6ImI3OTkwMmRhNzNlNzRjYzhiNjFiYjAyY2U2NWRlMDk4IiwidXNlcl9pZCI6MX0.WzCLvPJRf4WtJyIjP3P00U62Zscsv5A7HOaCTJiEpAY
(replace with your own access token)
7. Test the endpoints by sending requests using Postman.
![vendors List](images/Vendor_list.png)

8. To refresh the token 
   1. Set the request type to POST.
   2. Enter the URL for the token endpoint, which is typically `http://localhost:8000/api/token/refresh/`.
   3. Go to the Body tab and select x-www-form-urlencoded.
   4. Add the following key-value pairs:
      - **username:** admin
      - **password:** a123
      - **request:**  refresh token
   5. Send the request.
## Endpoints

### 1. Create a Vendor:
   - **URL:** `/api/vendors/`
   - **Method:** `POST`
   - **Payload:** JSON object containing vendor details.
   - **Authentication:** Required (Bearer token).

### 2. Retrieve, Update, or Delete a Vendor:
   - **URL:** `/api/vendors/<vendor_id>/`
   - **Method:** `GET`, `PUT`, `PATCH`, `DELETE`
   - **Authentication:** Required (Bearer token).

### 3. Create a Purchase Order:
   - **URL:** `/api/purchase_orders/`
   - **Method:** `POST`
   - **Payload:** JSON object containing purchase order details.
   - **Authentication:** Required (Bearer token).

### 4. Retrieve, Update, or Delete a Purchase Order:
   - **URL:** `/api/purchase_orders/<purchase_order_id>/`
   - **Method:** `GET`, `PUT`, `PATCH`, `DELETE`
   - **Authentication:** Required (Bearer token).

### 5. Retrieve a Vendor's Performance Metrics:
   - **URL:** `/api/vendors/<vendor_id>/performance/`
   - **Method:** `GET`
   - **Authentication:** Required (Bearer token).
   ![Vendor Performance](images/performance.png)


### Generating Sample Data

To facilitate testing and development, we provide a script named `generate_sample_data.py` that allows you to generate fake sample data for the Vendor Management system. This script utilizes the Faker library to create realistic-looking data across various models such as Vendors and Purchase Orders.

#### Usage

1. Navigate to the `vendorMgmt\vendors` directory where the script is located.
2. Ensure that your virtual environment is activated (`venv\Scripts\activate` for Windows or `source venv/bin/activate` for Unix-based systems).
3. Run the script using the command:
```
python generate_sample_data.py
```
4. Once the script completes execution, you will find the generated sample data populated in your database.

Please note that this script is primarily intended for testing and development purposes. It creates fake data to simulate real-world scenarios and should not be used in production environments.
