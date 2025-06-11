# PowerFitConnect

**Fitness Management and Community Platform for Gyms in Quito**

PowerFitConnect is an innovative digital platform specifically designed to connect gyms, athletes, and trainers in Quito, Ecuador. The platform facilitates interaction between different stakeholders in the local sports sector through an integrated fitness ecosystem.

## 🎯 Objectives

- **Connectivity:** Direct connection between sports facilities and users
- **Competition:** Robust local tournament system for various disciplines
- **Communication:** Specialized thematic chat groups for fitness topics
- **Optimization:** Efficient use of AWS services and open source tools

## 🏗️ Architecture

The project follows an evolutionary architecture approach:

1. **Phase 1:** Modular Monolithic Architecture
2. **Phase 2:** Hybrid Architecture (Critical modules as microservices)
3. **Phase 3:** Complete Microservices Architecture

## 🛠️ Tech Stack

### Frontend
- **React** - Core framework
- **Tailwind CSS** - Styling and responsive design
- **Axios** - HTTP client for API communication
- **Vite** - Build tool and development server

### Backend (Evolutionary)
- **Python/Flask** - Initial monolithic backend
- **Node.js** - Authentication microservices
- **Java** - Sports discipline services
- **Go** - Tournament system
- **C#** - Chat and community features

### Databases
- **PostgreSQL** - Authentication and tournaments
- **MySQL** - Gym management
- **MongoDB Atlas** - Sports disciplines and chat

### Infrastructure
- **AWS EC2** - Compute instances
- **AWS RDS** - Managed relational databases
- **AWS S3** - Object storage
- **AWS ALB** - Load balancing
- **AWS SQS** - Message queuing

### DevOps
- **Docker** - Containerization
- **Terraform** - Infrastructure as Code
- **GitHub Actions** - CI/CD pipeline

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- Node.js 18+
- Docker & Docker Compose
- AWS CLI configured
- Terraform

### Development Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/powerfitconnect.git
   cd powerfitconnect
   ```

2. **Start with Docker Compose**
   ```bash
   docker-compose up --build
   ```

3. **Access the application**
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:5000

### Manual Setup

#### Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

#### Frontend
```bash
cd frontend
npm install
npm run dev
```

## 📁 Project Structure

```
powerfitconnect/
├── frontend/          # React application
├── backend/           # Flask modular monolith
├── terraform/         # Infrastructure as Code
├── .github/           # GitHub Actions workflows
├── docker-compose.yml # Development environment
└── docs/             # Project documentation
```

## 🌍 Geographic Scope

- **Phase 1:** Quito, Ecuador (Pilot)
- **Phase 2:** Pichincha Province
- **Phase 3:** National expansion

## 🏃‍♂️ Features

### Core Features
- [x] User registration and authentication
- [x] Gym search with geolocation
- [x] Tournament management system
- [x] Real-time chat and community groups

### Planned Features
- [ ] Wearable device integration (Fitbit, Garmin)
- [ ] Premium subscription models
- [ ] Advanced performance analytics
- [ ] Mobile application

## 🧪 Testing

```bash
# Backend tests
cd backend
python -m pytest tests/

# Frontend tests
cd frontend
npm test
```

## 🚀 Deployment

### Development
```bash
docker-compose up --build
```

### Production
```bash
# Deploy infrastructure
cd terraform
terraform init
terraform plan
terraform apply

# Deploy application
docker-compose -f docker-compose.prod.yml up --build
```

## 📊 Development Timeline

- **Weeks 1-2:** Modular monolith foundation
- **Weeks 3-4:** CI/CD pipeline setup
- **Weeks 5-6:** Authentication microservice migration
- **Weeks 7-8:** Chat system with WebSocket
- **Weeks 9-10:** Tournament system implementation
- **Weeks 11-12:** Frontend decoupling and final architecture

## 🤝 Contributing

This project is developed as part of an academic project at Central University of Ecuador. 

### Development Guidelines
- Follow modular architecture principles
- Write tests for all new features
- Update documentation for architectural changes
- Use conventional commit messages

## 📄 License

This project is developed for academic purposes as part of the Distributed Programming course at Central University of Ecuador.

## 👨‍💻 Author

**Cristian Bladimir Alemán Revelo**  
Information Systems Engineering Student  
Central University of Ecuador  
SI8-003 - Ninth Semester  

## 📞 Contact

For questions about this project, please contact through the university's official channels.

---

**PowerFitConnect** - Revolutionizing Quito's fitness community through innovative technology.