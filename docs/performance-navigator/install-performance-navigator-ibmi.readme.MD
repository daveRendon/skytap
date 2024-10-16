# Installing Performance Navigator on IBMi

## Prerequisites
- IBM account  
- A Windows VM with Java installed  

## Steps

### Step 1: Install Performance Navigator
1. Download the Windows Performance Navigator Client / GUI from [here](https://s3.amazonaws.com/hsdownloads.helpsystems.com/software/robot/performance-nav/PerfNav.exe).
2. Run the `.exe` file.

![alt](/assets/images/performance-navigator/perfnav-01.jpg)

3. Execute the `.exe` file to install the client. This will place an icon on your desktop.  
4. Start Performance Navigator:  
   Click on the Performance Navigator icon on your desktop. The first time you start it, you will be prompted to install the IBM i host code.

![alt](/assets/images/performance-navigator/perfnav-02.jpg)



---

### Step 2: Install IBM i Host Code

1. Download the `setupPERFNAV.exe` Windows IBM i Host Code install program.
 - Click the download buttom when prompted to download the `setupPERFNAV.exe`

![alt](/assets/images/performance-navigator/perfnav-03.jpg)

 

2. Run the `setupPERFNAV.exe` program.  

![alt](/assets/images/performance-navigator/perfnav-04.jpg)

![alt](/assets/images/performance-navigator/perfnav-05.jpg)
![alt](/assets/images/performance-navigator/perfnav-06.jpg)
![alt](/assets/images/performance-navigator/perfnav-07.jpg)



3. Next, configure the IBM i partition.

---

### Step 3: Connect Windows GUI to IBM i Partitions

1. Enter the partition IP address, ID, and password.  
![alt](/assets/images/performance-navigator/perfnav-08.jpg)

![alt](/assets/images/performance-navigator/perfnav-09.jpg)

2. Select the **Immediate install** option.  
![alt](/assets/images/performance-navigator/perfnav-010.jpg)
![alt](/assets/images/performance-navigator/perfnav-011.jpg)
![alt](/assets/images/performance-navigator/perfnav-012.jpg)

3. Click the **Restart** button to install other partitions if needed.  
![alt](/assets/images/performance-navigator/perfnav-013.jpg)


#### Configure the Job Scheduler
- A few jobs will be added to the default job scheduler or to Robot Scheduler if installed.  

#### Install ODBC Driver
- **IBM ACS ODBC Driver**: Performance Navigator uses this driver to connect to IBM i partitions.  
- Click **Yes** to install the ODBC driver.  

![alt](/assets/images/performance-navigator/perfnav-014.jpg)

- Follow the URL to download the IBM i Access Client Solutions and agree to the terms and conditions.

![alt](/assets/images/performance-navigator/perfnav-015.jpg)
![alt](/assets/images/performance-navigator/perfnav-016.jpg)

![alt](/assets/images/performance-navigator/perfnav-017.jpg)

Then, a process will be executed to attempt the connection to the LPAR as shown below:

![alt](/assets/images/performance-navigator/perfnav-018.jpg)

![alt](/assets/images/performance-navigator/perfnav-019.jpg)


---

### Run PERFNAVDR Job
1. Run the `PERFNAVDR` job once during the first installation.  
   - By default, it runs 30 minutes after midnight, but it can be run anytime.  
2. Go to the IBM i system and run Performance Navigator. 
   - Start Performance Navigator:
   - Start the Performance Navigator application.

   - Reply **NO** to the host code installation prompt.
   - Go to **File > New IBM i**, enter the IP address, and click **NEW** for each partition.

   ![alt](/assets/images/performance-navigator/perfnav-020.jpg)

![alt](/assets/images/performance-navigator/perfnav-021.jpg)


---

### Step 4: Sending Data for Capacity Planning Analysis
1. Go to **File > SOS Data** in Performance Navigator.  
2. Select all systems by highlighting the first system name and Shift-clicking the last system name.  
3. Click **3. Save To Disk** to create a small file for each partition.  
4. Click **View SOS Directory** to see the saved files.  
5. Email the SOS files for analysis.

