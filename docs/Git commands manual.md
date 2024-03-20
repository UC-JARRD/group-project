# **Brief manual to use Git commands.**


### **0. Install Git or similar software on your local machine.**

### **1. Config git local repository on your own machine** 

${{\color{red}\Large{\textsf{Do\ it\ using\ your\ GitHub\ credentials.\ \}}}}\$
Additionally, please create token (classic) on GitHub user settings -> Developer Settings -> Personal access tokens -> Token (classic) 

```
git config --global user.name "- romanaumov"
git config --global user.email "- rna104@uclive.ac.nz"
```

### **2. Initialize the local folder.** 

Do it once (first time) to create a .git folder in your directory/repository on a local machine.

```
git init
```

### **3. Create a new branch** 

Do it to relate with the GitHub branches (main branch by default which use to commit working code and dev branch for development and testing)

```
git branch dev
```

### **4. Switch to dev branch.** 

${{\color{red}\Large{\textsf{Do\ it\ always\ (we\ are\ working\ with\ dev\ branch\ all\ time)\ \}}}}\$

```
git switch dev
```

### **5. Check where you are**

```
git branch
```

### **6. Clone dev branch from GitHub** 

Copy the repository from GitHub to local machine. ${{\color{red}\Large{\textsf{For this use Token (classic) as a Password.\ \}}}}\$

```
git clone https://github.com/UC-JARRD/iFireTracker.git
```

### **7. Change the code locally.** 

<span style="color:red">Everyone changes only their related folder, which already exists on GitHub.</span>

### **8. Add changed files** 

Add files to local git repository to track them

```
git add .
```

### **9. Check what the files added to repository**

```
git status
```

### **10. Make a commit** 

<span style="color:red">Do it for local Git repository and write the comments what were changed!</span>

```
git commit -a -m "Comment to commit"
```

### **11. Push to GitHub** 

To push changes to the GitHub use your own login password (token (classic)).

```
git push -u origin dev
```

