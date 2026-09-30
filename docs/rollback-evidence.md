# Rollback Evidence / Procedure

This file documents the rollback procedure required for the internship submission.

## 1. Create a known-good release point

After the first successful local test and successful Render deployment:

```powershell
git add .
git commit -m "Release v1.0.0 - Word and Character Counter"
git tag -a v1.0.0 -m "Known-good release"
git push origin main
git push origin v1.0.0
```

Record the GitHub commit SHA and the Render deploy ID in your final submission notes.

## 2. Simulate a rollback safely

Do not delete the good release. If a later change breaks the application, identify the last known-good commit:

```powershell
git log --oneline --decorate --all
```

Create a rollback branch:

```powershell
git switch -c rollback-v1.0.0
git reset --hard v1.0.0
git push -u origin rollback-v1.0.0
```

For the Render service, deploy the known-good commit/branch using the Render dashboard. Render also keeps the last successful deploy running when a new deploy fails.

## 3. Alternative: revert a bad commit

If the bad change is already on `main` and you want to preserve history:

```powershell
git log --oneline -5
git revert <BAD_COMMIT_SHA>
git push origin main
```

## 4. Evidence to capture

Take screenshots showing:
- GitHub commit/tag containing the known-good version.
- Render Deploys page showing the successful deployment.
- The live application after deployment.
- The rollback/revert commit if a rollback is demonstrated.

**Important:** Do not claim that a rollback was performed unless you actually perform it and capture the evidence.
