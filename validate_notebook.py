"""Execute the notebook from scratch and verify the supplied dataset and plot."""
from pathlib import Path
import sys
import nbformat
from nbclient import NotebookClient
from jupyter_client import KernelManager

root = Path(__file__).resolve().parent
nb = nbformat.read(root / "notebook.ipynb", as_version=4)
nbformat.validate(nb)
for cell in nb.cells:
    if cell.cell_type == "code":
        cell.outputs = []
        cell.execution_count = None
nb.cells.append(nbformat.v4.new_code_cell("""
assert len(netflix_df) == 7787
assert len(netflix_movies) == 5377
assert len(short_movies) == 420
assert netflix_df['show_id'].is_unique
assert netflix_movies['duration'].gt(0).all()
assert netflix_movies['country'].isna().sum() == 230
assert sum(len(c.get_offsets()) for c in ax.collections) == len(netflix_movies)
assert set(t.get_text() for t in ax.get_legend().get_texts()) == set(palette)
assert Path('movie_duration.png').is_file()
print('PASS: dataset, movie filtering, plot points, legend and chart export')
"""))
km = KernelManager(kernel_name="python3")
km.kernel_spec.argv = [sys.executable, "-m", "ipykernel_launcher", "-f", "{connection_file}"]
client = NotebookClient(nb, km=km, timeout=180,
    resources={"metadata": {"path": str(root)}})
try:
    client.execute()
finally:
    if km.has_kernel:
        km.shutdown_kernel(now=True)
nb.cells.pop()
nbformat.write(nb, root / "notebook.ipynb")
print("PASS: notebook executed from cleared outputs; data and chart checks passed.")
