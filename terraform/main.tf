provider "aws" {
  region = "us-east-1"  # Mantiene la región us-east-1
}

resource "aws_instance" "example" {
  ami                    = "ami-0c7217cdde317cfec"  # Ubuntu 22.04 LTS en us-east-1
  instance_type          = "t2.micro"               # Mantiene t2.micro
  associate_public_ip_address = true               # Para acceder desde Internet
  
  # Grupo de seguridad para SSH
  vpc_security_group_ids = [aws_security_group.allow_ssh.id]
  
  tags = {
    Name = "powerfitconnect-app"
  }
}

# Grupo de seguridad para permitir SSH
resource "aws_security_group" "allow_ssh" {
  name        = "allow_ssh"
  description = "Allow SSH, HTTP and API traffic"  # Corregido sin acentos
  
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