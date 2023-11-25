from flask import Blueprint, render_template, request, redirect, url_for
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
                return redirect(url_for('pagina_do_funcionario.abrir_pagina_do_funcionario'))
            elif admin:
                # Se as credenciais pertencerem a um administrador, redireciona para a página do administrador
                return redirect(url_for('pagina_do_administrador.abrir_pagina_do_administrador'))
            elif company:
                # Se as credenciais pertencerem a uma empresa, redireciona para a página da empresa
                return redirect(url_for('pagina_da_empresa.abrir_pagina_da_empresa'))
            else:
                # Se as credenciais estiverem incorretas, exibe uma mensagem de erro
                return render_template('cadastro.html')

        except Exception as e:
            return str(e)

        finally:
            cursor.close()
            connection.close()
    return render_template('login.html')

@bp.route('/editar_funcionario/<int:employee_id>', methods=['GET', 'POST'])
def editar_funcionario(employee_id):
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()

    try:
        if request.method == 'POST':
            # Atualize as informações do funcionário no banco de dados
            name = request.form['employeeName']
            position = request.form['employeePosition']
            email = request.form['employeeEmail']
            password = request.form['employeePassword']

            cursor.execute("UPDATE employees SET name=%s, position=%s, email=%s, password=%s WHERE id=%s",
                           (name, position, email, password, employee_id))

            connection.commit()

            return redirect('/lista_funcionarios')

        else:
            # Obtenha as informações atuais do funcionário para exibir no formulário de edição
            cursor.execute("SELECT * FROM employees WHERE id=%s", (employee_id,))
            employee = cursor.fetchone()

            return render_template('editar_funcionario.html', employee=employee)

    except Exception as e:
        return str(e)

    finally:
        cursor.close()
        connection.close()

@bp.route('/excluir_funcionario/<int:employee_id>', methods=['GET'])
def excluir_funcionario(employee_id):
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()

    try:
        # Implemente a lógica para excluir um funcionário existente
        cursor.execute("DELETE FROM employees WHERE id=%s", (employee_id,))
        connection.commit()

        return redirect('/lista_funcionarios')


    except Exception as e:
        return str(e)

    finally:
        cursor.close()
        connection.close()

@bp.route('/lista_funcionarios', methods=['GET'])
def lista_funcionarios():
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()

    try:
        # Implemente a lógica para obter a lista de funcionários do banco de dados
        cursor.execute("SELECT * FROM employees")
        employees = cursor.fetchall()

        return render_template('lista_funcionarios.html', employees=employees)

    except Exception as e:
        return str(e)

    finally:
        cursor.close()
        connection.close()
@bp.route('/adicionar_funcionario', methods=['GET', 'POST'])
def adicionar_funcionario():
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()

    try:
        if request.method == 'POST':
            # Adicione um novo funcionário ao banco de dados
            name = request.form['employeeName']
            position = request.form['employeePosition']
            email = request.form['employeeEmail']
            password = request.form['employeePassword']

            cursor.execute("INSERT INTO employees (name, position, email, password) VALUES (%s, %s, %s, %s)",
                           (name, position, email, password))

            connection.commit()

            return redirect('/lista_funcionarios')

        else:
            # Renderize a página de formulário para adicionar um novo funcionário
            return render_template('adicionar_funcionario.html')

    except Exception as e:
        return str(e)

    finally:
        cursor.close()
        connection.close()
@bp.route('/excluir_empresa/<int:company_id>', methods=['GET'])
def excluir_empresa(company_id):
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()

    try:
        cursor.execute("DELETE FROM companies WHERE id=%s", (company_id,))
        connection.commit()

        return redirect('/lista_empresas')

    except Exception as e:
        return str(e)

    finally:
        cursor.close()
        connection.close()

@bp.route('/confirmar_exclusao_empresa/<int:company_id>', methods=['GET'])
def confirmar_exclusao_empresa(company_id):
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()

    try:
        cursor.execute("SELECT * FROM companies WHERE id=%s", (company_id,))
        company = cursor.fetchone()

        return render_template('confirmar_exclusao_empresa.html', company=company)

    except Exception as e:
        return str(e)

    finally:
        cursor.close()
        connection.close()

@bp.route('/lista_empresas', methods=['GET'])
def lista_empresas():
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()

    try:
        cursor.execute("SELECT * FROM companies")
        companies = cursor.fetchall()

        return render_template('lista_empresas.html', companies=companies)

    except Exception as e:
        return str(e)

    finally:
        cursor.close()
        connection.close()

@bp.route('/adicionar_empresa', methods=['GET', 'POST'])
def adicionar_empresa():
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()

    try:
        if request.method == 'POST':
            nome_empresa = request.form['companyName']
            razao_social = request.form['companyLegalName']
            cnpj = request.form['companyCnpj']
            setor_atuacao = request.form['companySector']
            endereco_comercial = request.form['companyAddress']
            email = request.form['companyEmail']
            senha = request.form['companyPassword']
            site_empresa = request.form['companyWebsite']
            logo_empresa = request.form['companyLogo']
            descricao_empresa = request.form['companyDescription']

            cursor.execute(
                "INSERT INTO companies (nome_empresa, razao_social, cnpj, setor_atuacao, endereco_comercial, email, senha, site_empresa, logo_empresa, descricao_empresa) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (nome_empresa, razao_social, cnpj, setor_atuacao, endereco_comercial, email, senha, site_empresa, logo_empresa, descricao_empresa)
            )

            connection.commit()

            return redirect('/lista_empresas')

        else:
            return render_template('adicionar_empresa.html')

    except Exception as e:
        return str(e)

    finally:
        cursor.close()
        connection.close()
@bp.route('/comunidade')
def comunidade():
    return render_template('comunidade.html')
