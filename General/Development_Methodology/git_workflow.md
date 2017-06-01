
# Workflow

Currently, this project is being developed by following a variation of the [one flow](http://endoflineblog.com/oneflow-a-git-branching-model-and-workflow) model.

In summary, the following branches should exist and be in the following states:
1. `master` - always ready to deploy
2. `hotfix/<bug_name` - forks from master to fix a known issue (this issue should be documented in the repository and a branch can be created from within Gitlab
3. `feature/<feature_name>` - forks from master to a feature branch, explained [here](https://gitlab.psi.ch/help/workflow/workflow.md)
4.  

## Branching out and back into master

```
# Ensure master is up to date with a pull
git pull origin master
git checkout -b <branch_name>
# complete work and commit 
git checkout master 
git merge --no-ff <branch_name>
git push origin master
git branch -d <branch_name>
```

### No-FF (TL;DR - THIS SHOULD ALWAYS BE USED)

No-ff is a vital flag because it forces a merge commit to be inserted into the history of the main branch, without it, merge will try and fast forward the HEAD of the branch to the latest commit. In essence, without this flag, there will **not** be a visible merge commit in the history,

### INFO: Rebase vs. Merge

A lot of information can be found on the web but the basics of it are:
* Rebase rewrites histories  (and allows for interactive editing of commits)
* Merge will maintain history of commits (although the `squash` flag can reduce this and bring your branch tip back in line with the master.

### Git Pull

Some sites have mentioned that simply using a `git pull` (which is essentially a `git fetch` followed by a `git merge` will likely cause issues in large teams due to the changing nature of the branch meaning that you will experience merge commits. It is my personal opinion that this should not be a problem if work is never done directly on the master and the regular practice of pulling down before any major action is followed.

However, it should be noted that `git fetch origin` and `git rebase --preserve-merges origin/<branch_name>` will ensure that a history is maintained and merge conflicts are avoided where possible.


Once a feature is complete (and tested locally), it should be merged into the latest version of `master` and tested on the whole. If the tests pass, the develop can then be merged with master and any new merges to master should cause it to redeploy.

## Current status:

There is no CI set up for any of these projects, but it would need to be linked into Kubernetes.

# Useful git commands

* `git branch -r` -  List all branches
* `git fetch -p` -  Update branches from remote and remove deleted branches locally
* `git merge --no-ff <branch>` -  Merge branch into current branch
* `git branch -d <branch>` -  Remove branch once merged 

## Considerations

Issues with git flow have been documented ([see here](https://gitlab.psi.ch/help/workflow/gitlab_flow.md), [here](http://endoflineblog.com/gitflow-considered-harmful)). The idea of following the `Google` approach is an option and uses one single branch `master` instead of pulling into develop. Used correctly, this could allow for a clearer idea of continuous delivery and removes one extra layer of abstraction.
