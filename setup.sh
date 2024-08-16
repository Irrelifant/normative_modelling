#!/bin/bash
echo "Setup and install requirements..."

pip install -r requirements.txt
nbstripout --install --attributes .gitattributes --extra-keys 'kernelspec,metadata.language_info,widgets'

echo "Setup finished."
