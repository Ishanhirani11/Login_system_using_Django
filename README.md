# Django Task Manager & Authentication System

A secure, full-featured Django web application that implements user authentication and a task management dashboard with CRUD operations. This project demonstrates real-world Django architecture, authentication workflows, UI design, and browser security handling.

---

## 🚀 Features

### 🔐 Authentication System

* User registration with validation
* Secure login & logout
* Password change functionality
* Profile page
* Session handling
* Back-button security (prevents viewing cached protected pages)

### ✅ Task Management (CRUD)

* Create tasks
* View task details
* Update tasks
* Delete tasks
* Mark tasks as completed / pending
* Separate sections for pending & completed tasks
* Dashboard overview

### 🎨 UI & Styling

* Responsive centered layout
* Reusable base template
* Styled forms and buttons
* Dropdown profile menu
* Clean dashboard interface

### 🛡 Security Enhancements

* Login protection using Django authentication
* No-cache handling after logout
* Forced page reload on browser back navigation
* Protected views with login requirement

---

## 🏗 Project Structure

```
loginsystem/
│
├── login/                 # Main Django app
│   ├── migrations/
│   ├── templates/login/
│   ├── static/
│   │   └── style.css
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── forms.py
│
├── templates/
│   └── base.html          # Global layout template
│
├── loginsystem/
│   ├── settings.py
│   ├── urls.py
│
├── manage.py
└── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```
git clone https://github.com/g00562/Login-System.git
cd loginsystem
```

### 2. Create virtual environment

```
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Run migrations

```
python manage.py makemigrations
python manage.py migrate
```

### 5. Start the server

```
python manage.py runserver
```

Visit:

```
http://127.0.0.1:8000
```

---

## 👤 User Workflow

1. Register a new account
2. Login with credentials
3. Access dashboard
4. Create and manage tasks
5. Mark tasks complete/pending
6. View and edit profile
7. Change password securely
8. Logout safely

---

## 🧠 Technical Highlights

### Django Concepts Used

* Function-based views
* Django authentication framework
* Model-Form integration
* Template inheritance
* Static file management
* URL routing
* Session handling

### Browser Security Handling

The application prevents cached page access after logout using:

* Cache prevention strategies
* JavaScript reload detection
* Secure logout flow

This ensures users cannot access protected content via browser back navigation.

---

## 📦 Dependencies

* Python 3.10+
* Django 4.x / 5.x

---

## 🛠 Customization Ideas

This project can be extended with:

* Task search & filtering
* Pagination
* REST API (Django REST Framework)
* Email verification
* Password reset system
* User roles & permissions
* Deployment to cloud platforms
* Database optimization
* Admin dashboard enhancements

---

## 🧪 Testing

Run the Django development server and manually test:

* Registration flow
* Login/logout security
* Task CRUD operations
* Password change
* Back button behavior

---

## 📚 Learning Outcomes

This project demonstrates:

* Building a secure Django authentication system
* Implementing CRUD operations
* Managing sessions & browser caching
* Structuring scalable Django apps
* Creating reusable UI templates
* Handling real-world security issues

---

## 🤝 Contributing

Contributions are welcome!

You can:

* Improve UI/UX
* Add new features
* Optimize performance
* Enhance security
* Write tests

---

## 📄 License

This project is open source and available under the MIT License.

---

## 🙌 Acknowledgements

Built using the Django web framework and modern web development best practices.

---

**Author:** Your Name
**Project:** Django Task Manager & Authentication System
