import kagglehub # type: ignore

path = kagglehub.dataset_download("sebastienverpile/consumercomplaintsdata", output_dir='./data/raw')

print("Dataset downloaded to:", path)