# **Brief manual to use Git commands.**


## **0. Install Git or similar software on your local machine.**

## **1. Config git local repository on your own machine** 

${{\color{red}\large{\textsf{Do it using your GitHub credentials.}}}}\$
Additionally, please create token (classic) on GitHub user settings -> Developer Settings -> Personal access tokens -> Token (classic) 

```
git config --global user.name "romanaumov"
git config --global user.email "rna104@uclive.ac.nz"
```

## **2. Initialize the local folder.** 

Do it once (first time) to create a .git folder in your directory/repository on a local machine.

```
git init
```

## **3. Create a new branch** 

Do it to relate with the GitHub branches (main branch by default which use to commit working code and dev branch for development and testing)

```
git branch dev
```

## **4. Switch to dev branch.** 

${{\color{red}\large{\textsf{Do it always (we are working with dev branch all time).}}}}\$

```
git switch dev
```

## **5. Check where you are**

```
git branch
```

## **6. Create/Update dev branch from GitHub** 

Copy the repository from GitHub to local machine. ${{\color{red}\large{\textsf{For this use Token (classic) as a Password.\ \}}}}\$

Use `clone` command if you are creating directory for first time.
```
git clone https://github.com/UC-JARRD/iFireTracker.git
```

If your local directory have already exists and you need to update local files from GitHub, use the command `pull`.
```
git pull
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

