# Module 1 — Git & GitHub

**Student:** Cruz, Jan Andrei O.
**Date:** September 25, 2026

---

## What is Git? What is GitHub? (explain like you're teaching a friend who's never used either)

Git is a version control system that helps developers keep track of changes they make to their files and projects. You can think of Git like a save history for a project. Git is the tool that runs on your computer and tracks changes to your project.

GitHub is an online platform where Git repositories can be stored and shared. GitHub also provides features such as collaboration, pull requests, and code review.



---

## Key vocabulary (in your own words)

- repository: The repository is where you will store all of your files/projects.
- commit: Commit is when you are finish editing your changes you will use commit to save your changes to your repository and you can also add a message on your commited changes.
- branch: This is a separate version of the project where you can work on new features or changes without immediately affecting the main branch.
- push / pull: Push is to send my commit changes to the repository, and the pull is to download the latest changes in the GitHub
- pull request: This is where you will request to combine the changes from one branch to another. 
- merge conflict: This happens when Git finds different changes made to the same part of a file and cannot automatically decide which version to keep.

---

## Walking through what I did

I started by creating a Git repository for my project and making sure my files were tracked by Git. I then created a separate branch so I could make changes without directly changing the main branch. First I checked the current status of my project and created a new branch. After making changes to my project files, I checked the changes and added the files to the staging area. I then created a commit with a message explaining what I changed, After committing my changes, I pushed the new branch to GitHub. Once the branch was uploaded to GitHub, I created a pull request to request that my changes be merged into the main branch  After reviewing the changes, the branch could be merged.


```
git status 
git branch 
git checkout -b feature-update
git status 
git add .
git commit -m "Update project files"
git push -u origin feature-update

```

---

## A mistake I made (or one I want to avoid)

One mistake I want to avoid is accidentally making changes directly on the main branch instead of creating a separate branch. This can make the main version of the project contain unfinished or incorrect changes. Another thing I learned is that a commit is not the same as a push. A commit saves the changes in my local Git history, while a push sends those commits to GitHub.


---

## How this connects to something else

[Optional: how does version control relate to anything else you've learned or used before?]
