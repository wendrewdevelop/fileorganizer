import pathlib
from flask import (
    Flask, 
    url_for,
    request,
    redirect,
    render_template,
    flash,
    Blueprint
)
from werkzeug.utils import secure_filename


bp_core = Blueprint('core', __name__, template_folder='templates')

@bp_core.route('/', methods=['GET', 'POST'])
def upload_file():
    default_directory = pathlib.Path(__file__).parent.absolute()
    unprocessed_files = str(default_directory) + '/unprocessed_files/'

    try:
        if request.method == 'POST':
            f = request.files['filefield']
            f.save(str(unprocessed_files) + secure_filename(f.filename))
            flash('File uploaded successfully!')
            flash('Your file is being processed.')
            return redirect(url_for('core.upload_file'))
    except Exception as error:
        flash(error)
        
    return render_template('index.html')