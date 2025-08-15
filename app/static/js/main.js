document.addEventListener('DOMContentLoaded', function () {
    const tabela = document.querySelector('#tabela-funcionarios tbody');
    const modal = document.getElementById('modal');
    const closeModal = document.getElementById('close-modal');
    const btnNovo = document.getElementById('btnNovo');
    const form = document.getElementById('form-funcionario');
    const btnSalvar = document.getElementById('btnSalvar');
    let editId = null;

    function carregarFuncionarios() {
        fetch('/api/funcionarios')
            .then(res => res.json())
            .then(funcionarios => {
                tabela.innerHTML = '';
                funcionarios.forEach(f => {
                    const tr = document.createElement('tr');
                    tr.innerHTML = `
                        <td>${f[0]}</td>
                        <td>${f[1]}</td>
                        <td>${f[2]}</td>
                        <td>${f[3]}</td>
                        <td>
                            <button onclick="editarFuncionario(${f[0]}, '${f[2]}', ${f[3]})">Editar</button>
                            <button onclick="deletarFuncionario(${f[0]})">Deletar</button>
                        </td>
                    `;
                    tabela.appendChild(tr);
                });
            });
    }

    window.editarFuncionario = function(id, cargo, salario) {
        editId = id;
        document.getElementById('funcionario-id').value = id;
        document.getElementById('cargo').value = cargo;
        document.getElementById('salario').value = salario;
        modal.style.display = 'flex';
    };

    window.deletarFuncionario = function(id) {
        if (confirm('Deseja realmente excluir este funcionário?')) {
            fetch(`/deletar/${id}`, { method: 'DELETE' })
                .then(() => carregarFuncionarios());
        }
    };

    btnNovo.onclick = function () {
        editId = null;
        form.reset();
        modal.style.display = 'flex';
    };

    closeModal.onclick = function () {
        modal.style.display = 'none';
    };

    form.onsubmit = function (e) {
        e.preventDefault();
        const nome = document.getElementById('nome').value;
        const cargo = document.getElementById('cargo').value;
        const salario = document.getElementById('salario').value;
        if (editId) {
            fetch(`/atualizar/${editId}`, {
                method: 'PUT',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ cargo, salario })
            }).then(() => {
                modal.style.display = 'none';
                carregarFuncionarios();
            });
        } else {
            fetch('/inserir', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ nome, cargo, salario })
            }).then(() => {
                modal.style.display = 'none';
                carregarFuncionarios();
            });
        }
    };

    carregarFuncionarios();
});