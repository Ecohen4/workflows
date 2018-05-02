Version Control
=====================
Before you begin feature engineering and model building, you will need to establish
a workflow for your team. For this you will need git and github! Version control is your friend.
The last thing you want at the end of the day is version proliferation with
multiple, conflicting versions of your code floating around on Slack, email or elsewhere.
Instead, you want one centralized repository of code that is version controlled
and shared between every member of your team.

Let's suppose you want to contribute to an open-source project or any repository for which you do _not_ have direct write access. You can still contribute via pull requests from a forked version of the main repository.

Here is a recommended workflow:

## Fork and clone
* Your team lead should fork the repository of interest (the one you want to contribute to, but you don't have direct write access). This will be your team's "upstream repo".
* All other team members should fork the upstream repo. Before they can do so, the team lead will need to them as collaborators on github.com.
* Everyone clones their own forked repo to their own local machine.
* By default your remote origin (e.g. from where you push/pull) will be the address you used when you cloned the repository to your machine. For example: `https://github.com/Ecohen4/git_workflow.git`
* You can add additional remotes to keep your repository in sync. `git remote add <upstream> <upstream-remote-URL>`
* You can check all of your branches (local & remote) along with their latest commits: `git branch -avv`

## Branches
* On your local machine, create and checkout a branch to work on: `git checkout -b <feature_name>`. This will be your feature branch. No one works on the master branch, not even the upstream owner.
* Do your work.
* Every time you complete an atomic piece of work: `git add -p` `git commit -m` `git push origin <your feature branch>`
  * `git add -p` to interactively stage chunks of new/modified code. This is crucial to ensuring you commit only what you intend.
  * `git commit -m <something useful>`. Your commit messages serve as documentation and communication for your team.
  Example of a _good_ commit message: "add private method to feature engineering class to one-hot-encode categorical variables".
  Examples of a _useless_ commit message: "stuff", "commit", "bug fix".
  * `git push origin feature_1`, `git pull -r upstream master`. Be explicit about which remote branch you want when you push/pull.

## Pull requests
* Once a useful chunk of work is complete, issue a pull request to merge your branch with the upstream repo.
* The owner of the upstream repo can accept your pull request and merge it into the upstream master branch, then delete your feature branch.
* `git pull -r upstream master` for all collaborators to get the latest changes.
* Iterate frequently.

## Merging
* Avoid merge conflicts by working on separable areas of code and rebasing often `git pull -r origin master`.
* In the end, everything will be merged to the master branch in the upstream repo.  This will be your “production” code that everyone will have a copy of in the end.
* Consult the [github documentation](https://guides.github.com/introduction/flow/) if/when you get stuck.
