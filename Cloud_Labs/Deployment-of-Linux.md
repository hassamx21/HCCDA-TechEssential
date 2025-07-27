
# Deploying a Linux Server on Huawei Cloud

This step-by-step guide will help to deploy a **Linux ECS (Elastic Cloud Server)** on **Huawei Cloud**.

---

## What Need
- A Huawei Cloud account
- Access to the **Lab Desktop** (if in a lab environment)

---

## Step 1: Create a Linux ECS

1. Log in to Huawei Cloud Console.
2. From the **Service List**, select **Elastic Cloud Server**.
3. Click **Buy ECS** (top-right corner).

### Set the Configuration:
- **Billing Mode**: Pay-per-use
- **Region**: AP-Singapore
- **Availability Zone**: AZ1 or Random
- **Architecture**: x86
- **Flavor**: s6.large.2 (2 vCPUs | 4 GB RAM)
- **Image**: CentOS 7.6 64-bit
- **System Disk**: High I/O, 40 GB

---

## Step 2: Network and Access

- **VPC**: Use default or create new
- **Security Group**: Default (or create one that allows SSH)
- **EIP (Elastic IP)**: Auto assign
  - **Type**: Dynamic BGP
  - **Bandwidth**: 10–100 Mbps

---

## Step 3: Instance Settings

- **ECS Name**: `ecs-linux`
- **Login Mode**: Password
- **Password**: e.g., `Huawei@1234` *(keep it secure and remember it)*

---

## Step 4: Launch the ECS

1. Click **Submit**.
2. On the ECS list, check that the **status = Running**.

---

## Step 5: Log in to Linux ECS

### Option 1: Remote Login (No external tool needed)
- Go to **Elastic Cloud Server**
- Click **Remote Login** on your `ecs-linux`

### Option 2: SSH (if EIP is assigned)
Use a terminal:
```bash
ssh root@<ECS_Public_IP>
```
Password: Enter the one you set earlier (e.g., `Huawei@1234`)

---

## Step 6: Optional - Basic Linux Setup

Here are some useful commands:

### Update the system:
```bash
yum update -y
```

### Install basic tools:
```bash
yum install -y vim wget curl net-tools
```

### Check IP address:
```bash
ip a
```

---

## Done!

Linux ECS is now live on Huawei Cloud! start deploying apps, configuring servers, or learning Linux.
