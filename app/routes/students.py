from flask import Blueprint, render_template, redirect, url_for
from app.forms.students import StudentForm

students_bp = Blueprint('students', __name__, url_prefix="/students")


@students_bp.route('/', methods=['GET'])
def index():
    return render_template('pages/students/index.html')


@students_bp.route('/create', methods=['GET'])
def create():
    form = StudentForm()
    return render_template('pages/students/create.html', form=form)


@students_bp.route('/store', methods=['POST'])
def store():
    form = StudentForm()

    if form.validate_on_submit():
        return redirect(url_for('students.index'))

    return render_template('frames/students/form.html', form=form)
