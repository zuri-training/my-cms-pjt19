# How to Contribute to this Project

Clone the project

```bash
git clone https://github.com/zuri-training/my-cms-pjt19.git
```

Go to the project directory

```bash
cd my-cms-pjt19
```

---

## For the backend developers
<details><summary>Run Locally</summary>

Create a virtual environment and install needed dependencies in it

```bash
py -m venv venv 
```

Activate the virtual environment

```bash
 venv/bin/activate
```
</details>

*If you'll just be working on the front-end, the *running locally* section is optional. All your `HTML`, `CSS`, and `JavaScript` files should go into the [`templates`](https://github.com/zuri-training/my-cms-pjt19/tree/main/mycms/mycms/templates) directory.*

---

Create a branch to make your changes to.

```bash
git branch <your-github-username_feature>
```

Switch into your branch

```bash
git checkout <your-github-username_feature>
```
  
Set Upstream branch

```bash
git push --set-upstream origin <your-github-username_feature>
```

Commit and push your changes to your branch.

```bash
  git add . || git add --all || git add -A
  git commit -m <commit-message>
  git push
```

> You can also just *fork* the repository and make your changes to that fork.

**Create a pull request** on the [GitHub Repository](https://github.com/zuri-training/team-15_my-cms). [Learn How](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request).

**Request a review for your pull request** from [@philip ifeanyi](https://www.github.com/philip-ifeanyi)

Your changes will be merged into the `main` branch when they are approved by the reviewers.

<!-- ## Major packages used at the moment (list will be updated as we progress)
