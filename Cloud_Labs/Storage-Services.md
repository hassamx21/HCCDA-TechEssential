
# Huawei Cloud - Storage Services (Easy Guide)

This guide helps to understand and use **Huawei Cloud storage services**. We learn to use EVS (Elastic Volume Service), OBS (Object Storage Service), and SFS (Scalable File Service).

---

## EVS (Elastic Volume Service)

EVS provides extra disk space for your cloud servers.

### What to Do
- Buy and attach EVS disks
- Initialize disks on Windows and Linux
- Use snapshots to back up data

---

### EVS with Windows

#### 1. Buy a Windows ECS
- Go to Huawei Cloud > Elastic Cloud Server > Buy ECS
- Use:
  - Region: AP-Singapore
  - Image: Windows Server 2012 R2
  - Specs: 2 vCPUs, 4GB RAM
  - Disk: 40 GB

#### 2. Buy an EVS Disk
- Go to: **Storage > Elastic Volume Service**
- Click **Buy Disk**:
  - Type: High I/O
  - Size: 20 GB
  - Name: `volume-vivi`

#### 3. Attach the Disk
- Find the disk in EVS list
- Click **Attach**
- Select the ECS and mount point

#### 4. Initialize the Disk
- Use **Remote Login** to open the ECS
- Go to: `Server Manager > Tools > Computer Management > Disk Management`
- Bring the disk online, initialize, format, and assign a drive letter

#### 5. Test Disk Transfer
- Create a file (e.g., `test.txt`) on the disk
- Detach the disk
- Attach it to another ECS
- Check if the file exists

---

### EVS with Linux

#### 1. Buy a Linux ECS (CentOS 7.6)

#### 2. Attach EVS Disk (e.g., `volume-linuxadd`)

#### 3. Partition and Format the Disk
```bash
fdisk /dev/vdb
mkfs -t ext4 /dev/vdb1
mkdir /mnt/sdc
mount /dev/vdb1 /mnt/sdc
```

#### 4. Optional: Auto Mount on Boot
```bash
blkid /dev/vdb1
vi /etc/fstab
# Add this line:
UUID=xxxxxx /mnt/sdc ext4 defaults 0 2
mount -a
```

#### 5. Use Snapshots
- Create a test file in `/mnt/sdc`
- Go to EVS > More > Create Snapshot
- Create new disk from snapshot and mount it to check the file

---

## OBS (Object Storage Service)

OBS stores files (images, docs, videos) securely and lets you access them anywhere.

### What to Do
- Create a bucket
- Upload, download, and delete files

#### 1. Create a Bucket
- Go to: **Storage > OBS > Create Bucket**
- Set:
  - Region: AP-Singapore
  - Storage Class: Standard
  - Policy: Private
  - Name: `test-vivi`

#### 2. Upload Files
- Click on the bucket > Upload Object
- Select and upload a file

#### 3. Download or Delete
- Select the file > Click Download or Delete

---

## SFS (Scalable File Service)

SFS is shared file storage that works with both Linux and Windows ECS.

### What to Do
- Create and mount SFS file system
- Share data between Linux and Windows ECS

---

### Mounting on Linux

1. Install NFS client:
```bash
yum install nfs-utils bind-utils
```

2. Mount the file system:
```bash
mkdir /localfolder
mount -t nfs -o vers=3,timeo=600,nolock your_sfs_address:/share-id /localfolder
```

3. Add to auto-mount:
```bash
vi /etc/fstab
# Add:
your_sfs_address:/share-id /localfolder nfs vers=3,timeo=600,nolock 0 0
```

4. Reboot and verify:
```bash
reboot
mount -l
```

---

### Mounting on Windows

1. Login and open **Server Manager**
2. Add Role: **Client for NFS**
3. Use Command Prompt to mount:
```cmd
mount -o nolock -o casesensitive=yes IP:/share-id X:
```
4. Open "This PC" and check the new drive

---

### Test File Sharing

- Create a file in Linux on SFS
- Access it from Windows — if you see it, the setup works!

---

# Done!

Now know how to:
- Use EVS for disk storage
- Manage files with OBS
- Share data using SFS between Windows and Linux
