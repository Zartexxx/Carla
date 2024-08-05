import os
import subprocess

# Chemin absolu vers le répertoire stylegan2-ada-pytorch
project_path = "C:/MAMP/htdocs/stylegan2-ada-pytorch"

# Vérifiez si le répertoire existe
if not os.path.exists(project_path):
    raise FileNotFoundError(f"Le répertoire spécifié n'existe pas : {project_path}")

# Changez le répertoire de travail
os.chdir(project_path)
print("Répertoire de travail actuel :", os.getcwd())

# Chemin vers le modèle pré-entraîné
network_path = "pretrained_network.pkl"

# Si le modèle n'existe pas, téléchargez-le
if not os.path.exists(network_path):
    print(f"Le modèle pré-entraîné {network_path} n'existe pas. Téléchargement en cours...")
    download_command = "curl -O https://nvlabs-fi-cdn.nvidia.com/stylegan2-ada/pretrained/ffhq.pkl"
    subprocess.run(download_command, shell=True, check=True)
    os.rename("ffhq.pkl", network_path)
    print(f"Modèle pré-entraîné téléchargé et renommé en {network_path}")

# Vérifiez à nouveau que le modèle existe après le téléchargement
if not os.path.exists(network_path):
    raise FileNotFoundError(f"Le modèle pré-entraîné {network_path} n'existe pas.")

outdir = "out"
os.makedirs(outdir, exist_ok=True)

# Commande pour générer des images
command = f"python generate.py --network={network_path} --outdir={outdir} --trunc=0.7 --seeds=100-105"

# Exécution de la commande
try:
    subprocess.run(command, shell=True, check=True)
    print("Images générées avec succès.")
except subprocess.CalledProcessError as e:
    print(f"Erreur lors de la génération des images : {e}")
