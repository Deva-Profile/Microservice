
# 🌱 SeedApp Microservices – Agri Management System

This is a Django-based microservices project for managing agricultural operations. Each service is isolated and can be deployed independently. Docker is used for containerization.

---

## 🧩 Microservices

- `user_service/` – Handles user registration, login, and management
- `product_service/` – Manages agriculture-related products
- `order_service/` *(optional)* – Could handle ordering logic (if added later)
- `.env` files are used for secure environment variables
- `docker-compose.yml` – Runs all services together

---

## 🚀 Getting Started

### ✅ Prerequisites

- Python 3.9+
- Docker & Docker Compose
- Git

---

### 🐳 Run the Project using Docker

1. Clone the repository:

```bash
git clone git@github.com:Deva-Profile/Microservice.git
docker-compose up --build

