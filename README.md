🛒 E-Commerce Website – Django Based


Welcome to this simple yet functional e-commerce website built with Django. It includes essential features like product browsing, shopping cart, user login/signup, and profile management.



✨ What’s Inside?

🛍️ Product Catalog – Browse items by category

🛒 Shopping Cart – Add, remove, and view items

🔐 User Accounts – Register, log in, and manage your info securely

👤 Profile Page – Update your details and view order history

💳 Checkout – Simulate a basic checkout experience

⚙️ Admin Panel – Use Django’s built-in admin to manage everything

🧰 Tech Stack

Backend:

Python (3.8+)

Django

Frontend:

HTML + CSS + JavaScript

Database:

SQLite (for development – file: db.sqlite3)

⚙️ How to Run the Project Locally
✅ 1. Requirements
Make sure you have Python and pip installed:

📦 Download Python (v3.8 or above)

pip usually comes with Python

🧬 2. Clone the Project
```bash
git clone <your-repo-url>
cd e-commerce
```
📦 3. Set Up a Virtual Environment
```bash
# Windows

python -m venv venv
venv\\Scripts\\activate

# macOS/Linux

python3 -m venv venv
source venv/bin/activate
```
🔗 4. Install the Dependencies
```bash
pip install -r requirements.txt
```
🏗️ 5. Set Up the Database
```bash
python manage.py migrate
```
🌱 6. (Optional) Load Sample Data
You can add dummy products to test the app.

```bash
# Option 1: Load from an API
python manage.py load_api_products

# Option 2: Load predefined sample products
python manage.py add_sample_products
```
👑 7. Create an Admin (Superuser)
```bash
python manage.py createsuperuser
```
Enter the username, email, and password when prompted.

🚀 8. Start the Development Server
```bash
python manage.py runserver
```
Then open your browser and visit:

🖥️ Website: http://127.0.0.1:8000/

🔐 Admin Panel: http://127.0.0.1:8000/admin/

💡 Tip:
This is a great starting point for building a full-featured shopping site. You can extend it with:

Razorpay/Stripe integration

Product reviews

Search & filters

Product image uploads

