3. project structure:

1.1
refactor modules under src/: we have 3 products that use gen AI. they have similar workflows (genai). they point all to the same tasks.py under different prompts. we should have 3 modules with separate prompts. registered in mlflow.

1.2 maintain ci/cd (tests cov, quality, smoke...)