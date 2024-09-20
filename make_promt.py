import os


def collect_relevant_files(root_dir, output_file, extensions):
    with open(output_file, "w", encoding="utf-8") as outfile:
        for dirpath, dirnames, filenames in os.walk(root_dir):
            for filename in filenames:
                if filename.endswith(extensions):
                    file_path = os.path.join(dirpath, filename)
                    try:
                        with open(file_path, "r", encoding="utf-8") as infile:
                            content = infile.read()
                            outfile.write(f"\n--- Inhalt von {file_path} ---\n\n")
                            outfile.write(content)
                    except Exception as e:
                        print(f"Fehler beim Lesen der Datei {file_path}: {e}")


if __name__ == "__main__":
    # Hier das Top-Level-Verzeichnis angeben
    root_directory = "./fitness_tracker/"
    # Name der Ausgabedatei
    output_filename = "made_prompt.txt"
    # Dateiendungen der relevanten Dateien
    relevant_extensions = (
        ".py",  # Python-Dateien
        ".html",  # Template-Dateien
        ".css",  # Stylesheets
        ".js",  # JavaScript-Dateien
        ".txt",  # Textdateien
        ".md",  # Markdown-Dateien
        ".json",  # JSON-Konfigurationsdateien
        ".yaml",  # YAML-Dateien
        ".ini",  # INI-Konfigurationsdateien
    )

    collect_relevant_files(root_directory, output_filename, relevant_extensions)
    print(f"Alle relevanten Dateien wurden in '{output_filename}' gesammelt.")
