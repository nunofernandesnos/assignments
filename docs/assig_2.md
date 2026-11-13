3. project structure:

1.1
refactor modules under src/: we have 3 products that use gen AI. they have similar workflows (genai). they point all to the same tasks.py under different prompts. we should have 3 modules with separate prompts. registered in mlflow.

1.2 maintain ci/cd (tests cov, quality, smoke...)

1-Can prepare a one-line description of the purpose of the library just by looking at its folder structure?
 biblioteca Python ML.
2-Without looking at the code, can you identify the main components of the library? What are they?
módulos de dados, pré-processamento, modelos, métricas e seleção de modelos.
3-Where is the main script of the package located? What script would you open to start using the library?
sklearn/ veria os exemplos.
