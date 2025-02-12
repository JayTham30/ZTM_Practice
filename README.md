# 2/12/25

# How to push code to Git Hub through Command Prompt.
1) cd ZTM_Practice
2) git add.
3) git commit -m "Your Commit Message"
4) git push

# To add, edit, or delete code:
1) Create a new branch.
2) Create a matching pull request.
3) Merge the pull request into the main branch
4) It's bad practice to push changes directly to the main branch!

# To update Local Repo
1) cd "into local repo"
2) git branch -r
3) git branch --set-upstream-to=origin/Main main
4) git pull
    # If Git says the branch doesn’t exist, rename it to match the remote:
        git branch -m main Main
        git fetch origin
        git branch --set-upstream-to=origin/Main Main
        git pull



# This is my second time around with ZTM Python Course. I will be using this through out my journey.

