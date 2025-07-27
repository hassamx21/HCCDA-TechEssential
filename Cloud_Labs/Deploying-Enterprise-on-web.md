
# Huawei Cloud Lab 1: Deploying an Enterprise Website

This guide explains how to deploy a WordPress website using the LAMP stack on Huawei Cloud. It includes setting up cloud resources, installing necessary software, and configuring load balancing and auto scaling for high availability.

---

## Step 1: Log In to Huawei Cloud

1. Open Chrome on your Lab Desktop.
2. Go to the Huawei Cloud login page.
3. Select **IAM User Login**.
4. Enter the lab-provided account and password.

---

## Step 2: Create Network Infrastructure

### 2.1 Create a VPC (Virtual Private Cloud)

- Go to: **Service List > Networking > Virtual Private Cloud**
- Click **Create VPC**
- Use these settings:
  - Region: `AP-Singapore`
  - Name: `vpc-mp`
  - Leave other settings as default

### 2.2 Create a Security Group

- Go to: **Access Control > Security Groups**
- Create a security group
- Add an **Inbound Rule**:
  - Protocol & Port: `All`
  - Source IP: `0.0.0.0/0`

---

## Step 3: Buy and Configure Cloud Resources

### 3.1 Buy an ECS (Elastic Cloud Server)

- Go to: **Compute > Elastic Cloud Server > Buy ECS**
- Settings:
  - Billing Mode: `Pay-per-use`
  - Region: `AP-Singapore`
  - Image: `CentOS 7.6 64bit`
  - Specs: `1 vCPU, 1GB RAM`
  - Disk: `40GB`
  - VPC: Use your created one
  - Security Group: Use your created one
  - EIP: `Auto assign (2 Mbps)`

### 3.2 Buy an RDS (Relational Database Service)

- Go to: **Database > Relational Database Service**
- Buy DB Instance with:
  - Engine: `MySQL 8.0`
  - Specs: `2 vCPU, 4GB RAM`
  - VPC and Security Group: use existing
  - Set your password

---

## Step 4: Set Up LAMP Stack on ECS

### 4.1 Install Apache, PHP, MySQL

1. **Remote login** to ECS
2. Run:
   ```bash
   yum install -y httpd php php-fpm php-mysql mysql
   ```
3. Edit Apache config:
   ```bash
   vim /etc/httpd/conf/httpd.conf
   ```
   Add at end:
   ```
   ServerName localhost:80
   ```
4. Download WordPress:
   ```bash
   wget -c https://koolabsfiles.obs.ap-southeast-3.myhuaweicloud.com:443/20220731/wordpress-4.9.10.tar.gz
   tar -zxvf wordpress-4.9.10.tar.gz -C /var/www/html
   chmod -R 777 /var/www/html
   ```
5. Start services:
   ```bash
   systemctl start httpd
   systemctl start php-fpm
   systemctl enable httpd
   systemctl enable php-fpm
   ```

---

## Step 5: Create WordPress Database in RDS

1. Log in to your RDS MySQL database
2. Run:
   ```sql
   create database wordpress;
   ```

---

## Step 6: Install WordPress

1. Open browser and go to:
   ```
   http://<ECS-EIP>/wordpress
   ```
2. Fill form with:
   - Database Name: `wordpress`
   - Username: `root`
   - Password: your password
   - Host: `<RDS-IP>:3306`
   - Click: `Run the installation`

---

## Step 7: Set Up Load Balancer (ELB)

### 7.1 Create ELB

- Go to: **Networking > Elastic Load Balance**
- Create Shared Load Balancer with:
  - Network Type: Public
  - EIP: New, 2 Mbps

### 7.2 Add Listener and Backend

- Add Listener (HTTP:80)
- Backend group: Add ECS instance
- Disable Health Check

---

## Step 8: Configure Auto Scaling (AS)

### 8.1 Create Image from ECS

1. **Stop ECS** from console
2. Go to: **Compute > Image Management Service**
3. Create image from your ECS
4. Start ECS again

### 8.2 Create Auto Scaling Group

1. Go to: **Compute > Auto Scaling**
2. Create AS Configuration:
   - Use your image
   - Do not assign EIP
3. Create AS Group:
   - Attach load balancer and config

### 8.3 Add AS Policies

- Add:
  - **Scale Out:** CPU >= 60% → Add 1 ECS
  - **Scale In:** CPU <= 20% → Remove 1 ECS

---

## Step 9: Access the Website

- Visit:
  ```
  http://<Load-Balancer-EIP>/wordpress
  ```
- Your website should load.

---

## Step 10: Monitor the Deployment

1. Go to: **Management & Governance > Cloud Eye**
2. Check:
   - Resource overview
   - Alarms
   - ECS performance

---

## ✅ Done!

You’ve successfully deployed a scalable and highly available WordPress website using Huawei Cloud.
