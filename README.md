# Konfiguracja
Wejdź se do foldera w konsoli anakundy a następnie rób to
conda create -n pyoccenv python=3.8
conda activate pyoccenv
conda install -c conda-forge pythonocc-core
pip install tornado
python -c "install OCC; print(OCC.VERSION)"

Jak zadziała i wyświetli się wersja zamiast błędu to odpalaj
python main.py