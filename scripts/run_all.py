import subprocess, sys

scripts = [
    "scripts/generar_datos.py",
    "scripts/analizar_gastos.py",
    "scripts/visualizar.py"
]

print("Iniciando Budget Analyzer\n")
for script in scripts:
    print(f"{script}")
    r = subprocess.run([sys.executable, script], capture_output=True, text=True)
    print(r.stdout)
    if r.returncode != 0:
        print(f"Error: {r.stderr}")
        break
print("Análisis completado.")
