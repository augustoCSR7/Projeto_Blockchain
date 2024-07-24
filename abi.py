ABI_CONTRATO = [
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "_id",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "_nome",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_edicao",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "_pontos",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "_img_hash",
				"type": "string"
			}
		],
		"name": "adicionarAluno",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "alunosGlobal",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "id",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "nome",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "edicao",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "pontos",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "img_hash",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "alunosPorEdicao",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "id",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "nome",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "edicao",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "pontos",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "img_hash",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "_id",
				"type": "uint256"
			}
		],
		"name": "buscarAlunoPorID",
		"outputs": [
			{
				"components": [
					{
						"internalType": "uint256",
						"name": "id",
						"type": "uint256"
					},
					{
						"internalType": "string",
						"name": "nome",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "edicao",
						"type": "string"
					},
					{
						"internalType": "uint256",
						"name": "pontos",
						"type": "uint256"
					},
					{
						"internalType": "string",
						"name": "img_hash",
						"type": "string"
					}
				],
				"internalType": "struct RegistroAlunos.Aluno[]",
				"name": "",
				"type": "tuple[]"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_edicao",
				"type": "string"
			}
		],
		"name": "buscarAlunosPorEdicao",
		"outputs": [
			{
				"components": [
					{
						"internalType": "uint256",
						"name": "id",
						"type": "uint256"
					},
					{
						"internalType": "string",
						"name": "nome",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "edicao",
						"type": "string"
					},
					{
						"internalType": "uint256",
						"name": "pontos",
						"type": "uint256"
					},
					{
						"internalType": "string",
						"name": "img_hash",
						"type": "string"
					}
				],
				"internalType": "struct RegistroAlunos.Aluno[]",
				"name": "",
				"type": "tuple[]"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "buscarTodosOsAlunos",
		"outputs": [
			{
				"components": [
					{
						"internalType": "uint256",
						"name": "id",
						"type": "uint256"
					},
					{
						"internalType": "string",
						"name": "nome",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "edicao",
						"type": "string"
					},
					{
						"internalType": "uint256",
						"name": "pontos",
						"type": "uint256"
					},
					{
						"internalType": "string",
						"name": "img_hash",
						"type": "string"
					}
				],
				"internalType": "struct RegistroAlunos.Aluno[]",
				"name": "",
				"type": "tuple[]"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "edicoesPorAluno",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "todosOsRegistros",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "id",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "nome",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "edicao",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "pontos",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "img_hash",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]