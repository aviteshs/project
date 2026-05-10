provider "aws" {
  region = "us-east-1"
}

# -----------------------------
# Create SSH Key Pair
# -----------------------------
# ssh key generate firstthen run command
resource "aws_key_pair" "generated_key" { 
	key_name = "devops-key2" 
	public_key = file("~/.ssh/id_ed25519.pub") 
}
# -----------------------------
# Security Group
# -----------------------------
resource "aws_security_group" "web_sg" {
  name        = "web-security-group3"
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
  ingress {
	description = "Prometheus"

	from_port = 9090
	to_port   = 9090
	protocol  = "tcp"

	cidr_blocks = ["0.0.0.0/0"]
  } 
  
  ingress {
	description = "Grafana"

	from_port = 3000
	to_port   = 3000
	protocol  = "tcp"

	cidr_blocks = ["0.0.0.0/0"]
  }
  ingress {
	description = "Node Exporter"

	from_port = 9100
	to_port   = 9100
	protocol  = "tcp"

	cidr_blocks = ["0.0.0.0/0"]
  }
  
  ingress {
	description = "HTTP"

	from_port = 80
	to_port   = 80
	protocol  = "tcp"

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

  ami           = "ami-091138d0f0d41ff90"
  instance_type = "t3.small"

  key_name = aws_key_pair.generated_key.key_name


  vpc_security_group_ids = [
    aws_security_group.web_sg.id
  ]
  
	user_data = templatefile("setup.sh", {
	  public_key = file("~/.ssh/id_ed25519.pub")
	})

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