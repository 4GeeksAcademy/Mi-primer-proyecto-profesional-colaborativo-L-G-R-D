"""Retira únicamente el paquete inicial duplicado, sin crear respaldos."""
import argparse
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]
ALLOWED = ('pquete-maison', 'paquete-maison')


def clean(apply=False):
    found = False
    for name in ALLOWED:
        candidate = ROOT / name
        if not candidate.exists():
            continue
        found = True
        resolved = candidate.resolve()
        # Únicamente carpetas expresamente nombradas, directamente dentro del proyecto.
        if candidate.is_symlink() or resolved.parent != ROOT or resolved.name not in ALLOWED:
            raise ValueError('Se rechaza una ruta fuera del proyecto o un enlace simbólico.')
        if not resolved.is_dir():
            raise ValueError('El destino no es una carpeta: ' + str(resolved))
        entries = list(resolved.rglob('*'))
        if any(p.is_symlink() or p.name == '.git' for p in entries):
            raise ValueError('La carpeta contiene enlaces o un repositorio; conservar y revisar manualmente.')
        print('Paquete inicial duplicado: ' + str(resolved))
        if not apply:
            print('Vista previa. Para retirarlo sin respaldo: python tools/clean_workspace.py --apply')
            continue
        # Revalidar inmediatamente antes de eliminar: no se usan rutas de otro shell.
        if resolved.parent != ROOT or candidate.resolve() != resolved:
            raise ValueError('El destino cambió; se cancela la limpieza.')
        shutil.rmtree(resolved)
        print('Retirado sin crear respaldo: ' + str(resolved))
    if not found:
        print('No hay paquetes iniciales duplicados que limpiar.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--apply', action='store_true', help='Retirar definitivamente la carpeta duplicada, sin respaldo.')
    clean(parser.parse_args().apply)
