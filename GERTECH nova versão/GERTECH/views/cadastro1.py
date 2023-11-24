from flask import Blueprint, render_template, request, redirect
import pymysql


bp = Blueprint('cadastro', __name__)

# Configurações do banco de dados
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'admin',
    'database': 'gertech_db',
}

# Rota principal
@bp.route('/')
def cadastro():
    return render_template('cadastro.html')

# Rota para lidar com o envio do formulário de funcionário
@bp.route('/cadastrar_funcionario', methods=['POST'])
def cadastrar_funcionario():
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()

    try:
        name = request.form['employeeName']
        position = request.form['employeePosition']
        email = request.form['employeeEmail']
        password = request.form['employeePassword']

        # Insere os dados no banco de dados
        cursor.execute("INSERT INTO employees (name, position, email, password) VALUES (%s, %s, %s, %s)",
                       (name, position, email, password))

        connection.commit()

        return redirect('/login')

    except Exception as e:
        return str(e)

    finally:
        cursor.close()
        connection.close()

# Rota para lidar com o envio do formulário de administrador
@bp.route('/cadastrar_admin', methods=['POST'])
def cadastrar_admin():
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()

    try:
        name = request.form['adminName']
        email = request.form['adminEmail']
        password = request.form['adminPassword']

        # Insere os dados no banco de dados
        cursor.execute("INSERT INTO admins (name, email, password) VALUES (%s, %s, %s)",
                       (name, email, password))

        connection.commit()

        return redirect('/login')

    except Exception as e:
        return str(e)

    finally:
        cursor.close()
        connection.close()

# Rota para lidar com o envio do formulário de empresa
@bp.route('/cadastrar_empresa', methods=['POST'])
def cadastrar_empresa():
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()

    try:
        # Extrai os dados do formulário
        name = request.form['companyName']
        social_name = request.form['companySocialName']
        cnpj = request.form['companyCnpj']
        sector = request.form['companySector']
        address = request.form['companyAddress']
        email = request.form['companyEmail']
        password = request.form['companyPassword']
        website = request.form['companyWebsite']
        logo_url = request.form['companyLogoUrl']
        description = request.form['companyDescription']

        # Insere os dados no banco de dados
        cursor.execute("INSERT INTO companies (name, social_name, cnpj, sector, address, email, password, website, logo_url, description) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                       (name, social_name, cnpj, sector, address, email, password, website, logo_url, description))

        connection.commit()

        return redirect('/login')
    except Exception as e:
        return str(e)

    finally:
        cursor.close()
        connection.close()

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['senha']

        connection = pymysql.connect(**db_config)
        cursor = connection.cursor()

        try:
            # Verifica se as credenciais pertencem a um funcionário
            cursor.execute("SELECT * FROM employees WHERE email = %s AND password = %s", (email, password))
            employee = cursor.fetchone()

            # Verifica se as credenciais pertencem a um administrador
            if not employee:
                cursor.execute("SELECT * FROM admins WHERE email = %s AND password = %s", (email, password))
                admin = cursor.fetchone()

            # Verifica se as credenciais pertencem a uma empresa
            if not (employee or admin):
                cursor.execute("SELECT * FROM companies WHERE email = %s AND password = %s", (email, password))
                company = cursor.fetchone()

            if employee:
                # Se as credenciais pertencerem a um funcionário, redireciona para a página do funcionário
                return redirect('/pagina_do_funcionario')
            elif admin:
                # Se as credenciais pertencerem a um administrador, redireciona para a página do administrador
                return redirect('pagina_do_administrador.html')
            elif company:
                # Se as credenciais pertencerem a uma empresa, redireciona para a página da empresa
                return redirect('/pagina_da_empresa')
            else:
                # Se as credenciais estiverem incorretas, exibe uma mensagem de erro
                return render_template('cadastro.html')

        except Exception as e:
            return str(e)

        finally:
            cursor.close()
            connection.close()
    return render_template('login.html')