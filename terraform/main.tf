provider "aws" {
  region = "us-east-1"  # Mantiene la región us-east-1
}
resource "tls_private_key" "ec2_key" {
  algorithm = "RSA"
  rsa_bits  = 4096
}

resource "aws_key_pair" "deployer" {
  key_name   = "powerfitconnect-key"
  public_key = tls_private_key.ec2_key.public_key_openssh
}

resource "aws_instance" "example" {
  ami                    = "ami-0c7217cdde317cfec"  # Ubuntu 22.04 LTS en us-east-1
  instance_type          = "t2.micro"               # Mantiene t2.micro
  associate_public_ip_address = true               # Para acceder desde Internet
  
  # Grupo de seguridad para SSH
  vpc_security_group_ids = [aws_security_group.allow_ssh.id]
  key_name               = aws_key_pair.deployer.key_name
  
  tags = {
    Name = "powerfitconnect-app-v1"
  }
}

output "private_key_pem" {
    value     = tls_private_key.ec2_key.private_key_pem
    sensitive = true
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