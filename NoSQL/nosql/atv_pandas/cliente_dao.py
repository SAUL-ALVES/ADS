import pandas as pd
from models import Cliente
from typing import List, Optional
import os


class ClienteDAO:
    def __init__(self, arquivo_csv: str = "csv/german_credit_data.csv"):
        self.arquivo_csv = arquivo_csv
        # Verifica se o diretório existe, se não, cria
        os.makedirs(os.path.dirname(self.arquivo_csv), exist_ok=True)
        self.df = self._carregar_dataframe()

    def _carregar_dataframe(self) -> pd.DataFrame:
        """Carrega o DataFrame a partir do arquivo CSV com tratamento robusto"""
        colunas_esperadas = [
            "ID",
            "Age",
            "Sex",
            "Job",
            "Housing",
            "Saving accounts",
            "Checking account",
            "Credit amount",
            "Duration",
            "Purpose",
            "Label",
        ]

        try:
            df = pd.read_csv(self.arquivo_csv)

            # Verifica e adiciona colunas faltantes
            for col in colunas_esperadas:
                if col not in df.columns:
                    df[col] = pd.NA if col != "Job" else 0  # Valor padrão para Job

            # Garante a ordem das colunas
            return df[colunas_esperadas]

        except (FileNotFoundError, pd.errors.EmptyDataError):
            # Cria um novo DataFrame com todas as colunas necessárias
            return pd.DataFrame(columns=colunas_esperadas)

    def _salvar_dataframe(self):
        """Salva o DataFrame no arquivo CSV garantindo a existência do diretório"""
        os.makedirs(os.path.dirname(self.arquivo_csv), exist_ok=True)
        self.df.to_csv(self.arquivo_csv, index=False)

    def _mapear_para_cliente(self, row: pd.Series) -> Cliente:
        """Mapeia uma linha do DataFrame para um objeto Cliente com tratamento seguro"""
        return Cliente(
            id=int(row["ID"]),
            idade=int(row["Age"]),
            sexo=str(row["Sex"]),
            credito=float(row["Credit amount"]),
            moradia=str(row["Housing"]),
            conta_poupanca=str(row.get("Saving accounts", "")),
            conta_corrente=str(row.get("Checking account", "")),
            duracao=int(row["Duration"]),
            proposito=str(row["Purpose"]),
            aprovacao=int(row.get("Label", 0)),
        )

    def _mapear_para_dataframe(self, cliente: Cliente) -> dict:
        """Mapeia um objeto Cliente para um dicionário com tratamento completo"""
        return {
            "ID": cliente.id,
            "Age": cliente.idade,
            "Sex": cliente.sexo,
            "Job": 0,  # Valor padrão para Job
            "Housing": cliente.moradia,
            "Saving accounts": cliente.conta_poupanca,
            "Checking account": cliente.conta_corrente,
            "Credit amount": cliente.credito,
            "Duration": cliente.duracao,
            "Purpose": cliente.proposito,
            "Label": cliente.aprovacao,
        }

    def criar(self, cliente: Cliente) -> Cliente:
        """Adiciona um novo cliente com validação"""
        if cliente.id == 0:
            cliente.id = self.df["ID"].max() + 1 if not self.df.empty else 1

        if cliente.id in self.df["ID"].values:
            raise ValueError(f"ID {cliente.id} já existe")

        novo_registro = self._mapear_para_dataframe(cliente)
        self.df = pd.concat([self.df, pd.DataFrame([novo_registro])], ignore_index=True)
        self._salvar_dataframe()
        return cliente

    def buscar_por_id(self, id: int) -> Optional[Cliente]:
        """Busca um cliente pelo ID com tratamento seguro"""
        resultado = self.df[self.df["ID"] == id]
        return (
            self._mapear_para_cliente(resultado.iloc[0])
            if not resultado.empty
            else None
        )

    def listar_todos(self) -> List[Cliente]:
        """Retorna todos os clientes com verificação de DataFrame vazio"""
        return (
            []
            if self.df.empty
            else [self._mapear_para_cliente(row) for _, row in self.df.iterrows()]
        )

    def atualizar(self, cliente: Cliente) -> bool:
        """Atualiza um cliente existente com verificação"""
        mask = self.df["ID"] == cliente.id
        if not any(mask):
            return False

        self.df.loc[mask] = self._mapear_para_dataframe(cliente)
        self._salvar_dataframe()
        return True

    def remover(self, id: int) -> bool:
        """Remove um cliente com verificação de existência"""
        tamanho_inicial = len(self.df)
        self.df = self.df[self.df["ID"] != id]
        if len(self.df) < tamanho_inicial:
            self._salvar_dataframe()
            return True
        return False

    def filtrar_por_aprovacao(self, aprovacao: int) -> List[Cliente]:
        """Filtra clientes com tratamento para valores inválidos"""
        if aprovacao not in [-1, 1]:
            raise ValueError("Aprovação deve ser 1 (aprovado) ou -1 (reprovado)")

        resultado = self.df[self.df["Label"] == aprovacao]
        return [self._mapear_para_cliente(row) for _, row in resultado.iterrows()]

    def estatisticas_credito(self) -> dict:
        """Retorna estatísticas com tratamento para DataFrame vazio"""
        if self.df.empty:
            return {
                "media_credito": 0,
                "max_credito": 0,
                "min_credito": 0,
                "total_credito": 0,
                "clientes_aprovados": 0,
                "clientes_reprovados": 0,
            }

        return {
            "media_credito": round(self.df["Credit amount"].mean(), 2),
            "max_credito": self.df["Credit amount"].max(),
            "min_credito": self.df["Credit amount"].min(),
            "total_credito": self.df["Credit amount"].sum(),
            "clientes_aprovados": len(self.df[self.df["Label"] == 1]),
            "clientes_reprovados": len(self.df[self.df["Label"] == -1]),
        }
