def get_files_and_file_counts(directory, extensions=None):
    """
    Récupère tous les fichiers dans un répertoire et ses sous-répertoires, avec les extensions spécifiées si fournies.
    Compte le nombre de dossiers uniques, et compte le nombre de fichiers par extension.
    
    Paramètres:
    directory (str): Le répertoire dans lequel chercher les fichiers.
    extensions (list, optional): Liste des extensions de fichiers à récupérer (ex: ['.pdf', '.docx']). 
                                Si non fourni, tous les fichiers seront récupérés.
    
    Retourne:
    pd.DataFrame: Un DataFrame contenant le chemin complet de chaque fichier trouvé.
    int: Le nombre de dossiers uniques.
    pd.DataFrame: Un DataFrame avec le compte de fichiers par extension, ordonné par ordre décroissant du nombre de fichiers.
    """
    if extensions:
        file_paths = [os.path.join(root, file) for root, dirs, files in os.walk(directory) for file in files if any(file.endswith(ext) for ext in extensions)]
    else:
        file_paths = [os.path.join(root, file) for root, dirs, files in os.walk(directory) for file in files]
    
    folders = set()
    file_extensions = defaultdict(int)
    
    for file_path in file_paths:
        folders.update(os.path.dirname(file_path).split(os.path.sep))
        _, extension = os.path.splitext(file_path)
        file_extensions[extension.lstrip('.').lower()] += 1
    
    num_folders = len(folders)
    
    file_counts_df = (
        pd.DataFrame.from_dict(file_extensions, orient='index')
        .reset_index()
        .rename(columns={'index': 'Extension', 0: 'Compte'})
        .sort_values('Compte', ascending=False)
        .reset_index(drop=True)
    )
    
    return pd.DataFrame({'Chemin du fichier': file_paths}), num_folders, file_counts_df
