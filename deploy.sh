PROJECT_DIR=$(cd "$(dirname "$BASH_SOURCE")"; cd -P "$(dirname "$(readlink "$BASH_SOURCE" || echo .)")"; pwd)

source $PROJECT_DIR/../env/bin/activate
python $PROJECT_DIR/main.py
