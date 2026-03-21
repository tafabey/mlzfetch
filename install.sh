mkdir -p ~/.local/share/mlzfetch/
cp -r logos/ ~/.local/share/mlzfetch/
python3 -m venv .venv
source .venv/bin/activate
pip install .
cp .venv/bin/mlzfetch ~/.local/bin/
deactivate
