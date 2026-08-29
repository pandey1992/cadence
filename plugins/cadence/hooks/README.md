# Optional Git hook

Cadence does not install hooks automatically or use hooks to block normal work. The included `pre-commit` hook performs Git’s whitespace/error check on staged changes, a fast signal that is safe for any repository.

Install it explicitly from the repository root:

```bash
plugins/cadence/scripts/install-git-hook.sh
```

This copies the hook into `.git/hooks/pre-commit` only if no hook exists. If your repository already has a hook, integrate the one-line call from `pre-commit` into its existing hook; do not overwrite it.

The hook intentionally does not run a guessed test command. Test commands are repository-specific and should be run by Cadence after it has inspected the project.
