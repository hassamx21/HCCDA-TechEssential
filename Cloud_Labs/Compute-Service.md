
# Huawei Cloud Compute Service Lab (Simplified Guide)

In this we learn about how to create and manage Windows and Linux ECS (Elastic Cloud Servers) on Huawei Cloud in a simple and clear way.

---

## Step 1: Create Windows and Linux ECS

### 1.1 Create a Virtual Private Cloud (VPC)

1. Log in to Huawei Cloud (AP-Singapore region).
2. Go to **Virtual Private Cloud** from the service list.
3. Click **Create VPC** and set:
   - **Name**: vpc-WP
   - **IPv4 CIDR Block**: 192.168.0.0/16
   - **Subnet Name**: subnet-WP
   - **Subnet CIDR Block**: 192.168.0.0/24

---

### 1.2 Create a Windows ECS

1. Go to **Compute > Elastic Cloud Server**.
2. Click **Buy ECS**.
3. Set:
   - **Billing**: Pay-per-use
   - **OS**: Windows Server 2012 R2
   - **Specs**: 2 vCPU, 4 GB RAM
   - **Disk**: 40 GB
   - **Login Mode**: Password (e.g., Huawei@1234)

---

### 1.3 Create a Linux ECS

Use the same steps as Windows ECS, but change:
- **OS**: CentOS 7.6
- **Login Mode**: Password
- **EIP**: Auto assign

---

## Step 2: Log in to ECS

### Windows ECS Login

1. Click **Remote Login** on the ECS page.
2. Click **Send CtrlAltDel** and enter your password.

### Linux ECS Login

1. Click **Remote Login**.
2. Login with:
   ```
   Username: root
   Password: Huawei@123
   ```

---

## Step 3: Modify ECS Specs

1. Stop the ECS.
2. Click **More > Modify Specifications**.
3. Change RAM (e.g., from 4 GB to 8 GB).
4. Start the ECS again.

---

## Step 4: Create a System Disk Image (Windows)

### 4.1 Prepare Windows ECS

1. Enable **DHCP**.
2. Allow **remote connections**.
3. Allow **Remote Desktop** in the Firewall.
4. Check if **Cloudbase-Init** is installed.

### 4.2 Create Windows Image

1. Go to **Image Management Service**.
2. Click **Create Image**:
   - Type: System disk image
   - Source: Your ECS
   - Name: image-windows2012

---

## Step 5: Create a System Disk Image (Linux)

### 5.1 Prepare Linux ECS

1. Ensure **DHCP** is configured.
2. Check/install:
   - **CloudResetPwdAgent**
   - **Cloud-Init**
3. Delete network rule files:
   ```
   ls -l /etc/udev/rules.d
   ```

### 5.2 Create Linux Image

1. Go to **Image Management Service**.
2. Click **Create Image**:
   - Type: System disk image
   - Source: ecs-linux
   - Name: image-centos7.6

---

## Step 6: Share Private Image

1. Get your **Project ID** from "My Credentials".
2. Go to **Private Images**, click **More > Share**.
3. Add Project ID and click OK.

---

## Step 7: Add Tenants to Shared Image

1. Go to **Private Images** and click image name.
2. Under **Shared with Tenants**, click **Add Tenant**.
3. Enter the Project ID and confirm.

---

**You’ve now successfully created and managed ECS instances and images on Huawei Cloud!**
