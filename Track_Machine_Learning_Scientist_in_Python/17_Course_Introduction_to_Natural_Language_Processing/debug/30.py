from polyglot.downloader import downloader

# Try downloading all necessary data
downloader.download("embeddings2.en")
downloader.download("ner2")
downloader.download("pos2")
downloader.download("lang2")
