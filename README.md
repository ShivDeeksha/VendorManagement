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

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, feel free to open an issue or create a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
