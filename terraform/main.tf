provider "aws" {
  region = "us-east-1"
}

# -----------------------------
# Create SSH Key Pair
# -----------------------------
resource "tls_private_key" "mykey" {
  algorithm = "RSA"
  rsa_bits  = 4096
}

resource "local_file" "private_key" {
  content  = tls_private_key.mykey.private_key_pem
  filename = "devops-key.pem"
}

resource "aws_key_pair" "generated_key" {
  key_name   = "devops-key"
  public_key = tls_private_key.mykey.public_key_openssh
}

# -----------------------------
# Security Group
# -----------------------------
resource "aws_security_group" "web_sg" {
  name        = "web-security-group"
  description = "Allow SSH and Flask"

  ingress {
    description = "SSH"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "Flask App"
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

# -----------------------------
# Ubuntu EC2
# -----------------------------
resource "aws_instance" "web_server" {

  ami           = "ami-0fc5d935ebf8bc3bc"
  instance_type = "t2.micro"

  key_name = aws_key_pair.generated_key.key_name

  vpc_security_group_ids = [
    aws_security_group.web_sg.id
  ]
  
  user_data = file("setup.sh")

  tags = {
    Name = "DevOps-WebApp"
  }
}

# -----------------------------
# Output
# -----------------------------
output "public_ip" {
  value = aws_instance.web_server.public_ip
}