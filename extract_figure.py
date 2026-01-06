import os
import re
import tarfile
import subprocess
import shutil
import requests
import fitz  # PyMuPDF

def download_source(paper_id, save_path):
    """Downloads the ArXiv source archive."""
    url = f"https://arxiv.org/e-print/{paper_id}"
    try:
        # Use requests for cross-platform compatibility
        response = requests.get(url, stream=True, timeout=30)
        response.raise_for_status()
        
        with open(save_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        return True
    except Exception as e:
        print(f"Error downloading source for {paper_id}: {e}")
        return False

def find_main_tex(directory):
    """Finds the main .tex file in a directory."""
    tex_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".tex"):
                tex_files.append(os.path.join(root, file))
    
    for tex_file in tex_files:
        try:
            with open(tex_file, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                if "\\documentclass" in content and "\\begin{document}" in content:
                    return tex_file
        except:
            continue
    return tex_files[0] if tex_files else None

def extract_first_figure(paper_id, output_dir):
    """Extracts the first figure from the ArXiv source."""
    source_tar = f"{paper_id}_source.tar.gz"
    extract_path = f"{paper_id}_source_extracted"
    
    if not download_source(paper_id, source_tar):
        return None
    
    try:
        os.makedirs(extract_path, exist_ok=True)
        with tarfile.open(source_tar, "r:gz") as tar:
            tar.extractall(path=extract_path)
        
        main_tex = find_main_tex(extract_path)
        if not main_tex:
            return None
        
        with open(main_tex, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
        
        figure_file = None
        # Look for the first figure that is not commented out
        # We prefer figures in the 'figure' or 'figure*' environment
        in_figure_env = False
        for line in lines:
            stripped = line.strip()
            if stripped.startswith("%"):
                continue
            
            if "\\begin{figure}" in stripped or "\\begin{figure*}" in stripped:
                in_figure_env = True
            
            if in_figure_env:
                match = re.search(r"\\includegraphics(?:\[.*?\])?\{(.*?)\}", stripped)
                if match:
                    figure_file = match.group(1)
                    break
            
            if "\\end{figure}" in stripped or "\\end{figure*}" in stripped:
                in_figure_env = False
        
        # Fallback to any includegraphics if no figure environment found
        if not figure_file:
            for line in lines:
                stripped = line.strip()
                if stripped.startswith("%"):
                    continue
                match = re.search(r"\\includegraphics(?:\[.*?\])?\{(.*?)\}", stripped)
                if match:
                    figure_file = match.group(1)
                    break
        
        if figure_file:
            # Search for the file in the extracted directory
            # It might not have an extension in the .tex file
            found_path = None
            for root, _, files in os.walk(extract_path):
                for file in files:
                    if file.startswith(figure_file) or file == figure_file:
                        found_path = os.path.join(root, file)
                        break
                if found_path:
                    break
            
            if found_path:
                ext = os.path.splitext(found_path)[1]
                dest_path = os.path.join(output_dir, f"{paper_id}_overview{ext}")
                shutil.copy(found_path, dest_path)
                
                # If it's a PDF, try to convert to PNG for better compatibility
                if ext.lower() == ".pdf":
                    try:
                        png_path = os.path.join(output_dir, f"{paper_id}_overview.png")
                        # Use PyMuPDF for cross-platform PDF to PNG conversion
                        doc = fitz.open(dest_path)
                        if len(doc) > 0:
                            page = doc[0]  # Get first page
                            mat = fitz.Matrix(2.0, 2.0)  # 2x zoom for better quality
                            pix = page.get_pixmap(matrix=mat)
                            pix.save(png_path)
                            doc.close()
                            return f"{paper_id}_overview.png"
                        doc.close()
                    except Exception as e:
                        print(f"PDF to PNG conversion failed: {e}")
                        return f"{paper_id}_overview{ext}"
                
                return f"{paper_id}_overview{ext}"
                
    except Exception as e:
        print(f"Error extracting figure for {paper_id}: {e}")
    finally:
        # Cleanup
        if os.path.exists(source_tar):
            os.remove(source_tar)
        if os.path.exists(extract_path):
            shutil.rmtree(extract_path)
            
    return None

if __name__ == "__main__":
    paper_id = "2512.24615"
    output_dir = "test_figures"
    os.makedirs(output_dir, exist_ok=True)
    fig = extract_first_figure(paper_id, output_dir)
    print(f"Extracted figure: {fig}")
