provider "aws" {
  region = "us-east-1"
}

variable "services" {
  default = ["auth", "gyms", "memberships", "sports", "tournaments"]
}

# Genera una clave privada para las instancias EC2
resource "tls_private_key" "ec2_key" {
  algorithm = "RSA"
  rsa_bits  = 4096
}

# Sube la clave pública a AWS para acceso SSH
resource "aws_key_pair" "deployer" {
  key_name   = "powerfitconnect-key"
  public_key = tls_private_key.ec2_key.public_key_openssh
}

# Grupo de seguridad para permitir SSH, HTTP y API (puerto 5000)
resource "aws_security_group" "service_sg" {
  name        = "service_sg"
  description = "Permite SSH, HTTP y API para microservicios"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 5000
    to_port     = 5000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# Instancia EC2 para cada microservicio
resource "aws_instance" "service" {
  count                       = length(var.services)
  ami                         = "ami-0c7217cdde317cfec" # Ubuntu 22.04 LTS
  instance_type               = "t2.micro"
  associate_public_ip_address = true
  vpc_security_group_ids      = [aws_security_group.service_sg.id]
  key_name                    = aws_key_pair.deployer.key_name

  user_data = <<-EOF
    #!/bin/bash
    apt-get update
    apt-get install -y docker.io git
    systemctl start docker
    systemctl enable docker
  EOF

  tags = {
    Name = "powerfitconnect-${var.services[count.index]}"
  }
}

# Base de datos RDS PostgreSQL
resource "aws_db_instance" "powerfitconnect_db" {
  allocated_storage      = 20
  engine                 = "postgres"
  engine_version         = "14.17"
  instance_class         = "db.t3.micro"
  db_name                = "powerfitdb"
  username               = "powerfituser"
  password               = "admin1234"
  parameter_group_name   = "default.postgres14"
  skip_final_snapshot    = true
  publicly_accessible    = true
  vpc_security_group_ids = [aws_security_group.service_sg.id]
}

# Output de la clave privada para acceso SSH
output "private_key_pem" {
  value     = tls_private_key.ec2_key.private_key_pem
  sensitive = true
}