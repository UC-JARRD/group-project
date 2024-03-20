# **Brief manual to use Git commands.**


## **0. Install Git or similar software on your local machine. Do it once (first time)**

## **1. Config git local repository on your own machine. Do it once (first time)** 

${{\color{red}\large{\textsf{Do it using your GitHub credentials. Do it once (first time).}}}}\$
Additionally, please create token (classic) on GitHub user settings -> Developer Settings -> Personal access tokens -> Token (classic) 

```
git config --global user.name "romanaumov"
git config --global user.email "rna104@uclive.ac.nz"
```

## **2. Initialize the local folder. Do it once (first time)** 

Do it once (first time) to create a .git folder in your directory/repository on a local machine.
Choose the folder on your PC and go into it using `cd` command and then execute the command `init`.

```
git init
```

## **3. Create a repository from GitHub. Do it once (first time)** 

Copy the repository from GitHub to local machine. ${{\color{red}\large{\textsf{For this use Token (classic) as a Password.\ \}}}}\$

Use `clone` command if you are creating directory for first time.
```
git clone https://github.com/UC-JARRD/iFireTracker.git
```

## **4. Update a repository from GitHub. If you have already a repository locally.** 

Copy the repository from GitHub to local machine. ${{\color{red}\large{\textsf{For this use Token (classic) as a Password.\ \}}}}\$
If your local directory have already exists and you need to update local files from GitHub, use the command `pull`.

```
git pull
```

## **5. Switch to dev branch.** 

${{\color{red}\large{\textsf{Do it always (we are working with dev branch all time).}}}}\$

```
git switch dev
```

## **6. Check where you are**

```
git branch
```

## **7. Change the code locally.** 

${{\color{red}\large{\textsf{Everyone changes only their related folder, which already exists on GitHub.}}}}\$


## **8. Add changed files** 

Add files to local git repository to track them

```
git add .
```

## **9. Check what the files added to repository**

```
git status
```

## **10. Make a commit** 

${{\color{red}\large{\textsf{Do it for local Git repository and write the comments what were changed!}}}}\$

```
git commit -a -m "Comment to commit"
```

## **11. Push to GitHub** 

To push changes to the GitHub use your own login password (token (classic)).

```
git push -u origin dev
```
