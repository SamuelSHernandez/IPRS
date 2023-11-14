# Questions to investigate:

* Who is IDEConsultant@gc.adventist.org?
* Who is IDEWebUser and why is its type 'user'? is it all IDE users or is it a special kind of group?
* Who is IDEConsultant?
* In the IPRS Directors group, each member is duplicated. Why?
All members are duplicated to include the GC and ISE active directory (This will hopefully be consolidated into a single authentication method to remove duplication)
* What is Harmon.ie? is it still used or necessary? (Last edited date, 2012)

* Why are there two users Emmi Otts2 and Emi Otts? Seems like 'Emmi Otts' is all inputed into either the first or last name
* Is it necesary to have an IDEVisitors? What is that user/role used for?
* What's the use of APServiceDev and APServiceLive user accounts?
* Every user should have its department (for role based permissions) and for documentation;
* Every user should have its title (for documentation)
* If the about me section is not used by any user, it should be removed/disabled
* Naming convention should switch from IDE->ISE
* **Does our Sharepoint use NTFS or ReFS? NTSF**
* Would it be worth considering **Access Based Enumeration (ABE)?** Reasasoning for it is that it would significantly reduce the clutter of files that do not corncern certain departments. Making it easier to navigate. Access would be tied to dedicated permission groups. Avoid the 'why can't I open this folder/file?' emails. Reasoning against would be a non-essential layer of complexity for the development team

* Is it possible to add a small line separator to help readabiity in ISE Records - Current?
* Is there an archiving policy/process in place already?
* Is there a file deletion policy/process in place already?

## File ages
* ISE > IPRS Admin > ArchiveDocs_FromFileCabinets dated 2015
* All IT training material dated 2012-2013
* ISE > Documents file has 0 items

## NTFS

[Source](https://www.tenfold-security.com/en/set-ntfs-permissions/)

### Full Control
Grants complete access, including the ability to see, read, write, execute and delete files or folders, as well as change permission settings for all subdirectories.

## Modify
The user can see, read, execute, write and delete files. Also allows for the deletion of the folder itself.

## Read & Execute
Can view folder contents and run programs or scripts.

### List folder contents
Allows the user to see files and directories contained within a folder. An important setting for navigating to deeper levels in the folder structure.

### Read
Can see folder contents and also open the files and folders in question.

### Write
Users can add new files and folders and write to existing files.

> Users who have Read and Execute access to a specific folder must also have the **List Folder Contents** permission for any higher-up folders in order to navigate to their target

## Good practices in NFTS

1.  Create consistent policies and naming conventions

2. Always use permission groups, avoid assigning permissions directly

3. Keep the root directory clear, don’t allow users to create new folders

4. Use “full control” only when absolutely necessary

5. Assign “list folder contents” through nested permission groups

6. Keep explicit permissions to the top of the directory tree, let inheritance handle the rest

7. Ensure that permission inheritance is working as intended

8. Enable access-based enumeration to hide sensitive information

9. Implement least privilege access for optimal security

Advice

> Never assign special permissions

> Never assign direct user access

> Assign permissions to **dedicated permision groups** that govern access to a specific resource.

For example `FS_Sales_Read`

> Don't reuse permission groups to alter an existing group. If more permissions are needed the same group, make a new dedicated permisssions group

> Do not set explicit NTFS permissions on deep levels in the directory tree. Stick to two or three levels for explicit permissions to keep things simple and let permission inheritance take care of the res

> Assign **Full Control** permissions only to IT


[Sharepoint file naming Restrictions](https://support.microsoft.com/en-us/office/restrictions-and-limitations-in-onedrive-and-sharepoint-64883a5d-228e-48f5-b3d2-eb39e07630fa?ui=en-us&rs=en-us&ad=us#invalidcharacters)