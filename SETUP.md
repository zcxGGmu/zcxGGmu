# zcxGGmu GitHub profile setup

This folder contains a ready-to-use profile README inspired by:

- Platane: minimal profile with the contribution snake visual.
- Kautuk Kundan: terminal-style, systems/agentic engineering identity.

## Install

1. Create a public GitHub repository named exactly `zcxGGmu`.
2. Copy `README.md` into that repository.
3. Copy `build_readme.py` and `.github/workflows/{build.yml,snake.yml}` into that repository.
4. Commit and push.
5. Open the repository's `Actions` tab and run `Generate contribution snake` once.

After the workflow completes, the snake SVGs will be published to the `output` branch and the image in the README will start rendering.

`Build README` refreshes the PR radar from GitHub and the latest blog posts from `https://zcxggmu.github.io/index.xml` every 12 hours.

## Important

GitHub profile READMEs only render on your user page when the repository name exactly matches your username: `zcxGGmu/zcxGGmu`.

If you keep the README in a differently named repository, GitHub will show it as a normal repository README, not as your profile homepage.
