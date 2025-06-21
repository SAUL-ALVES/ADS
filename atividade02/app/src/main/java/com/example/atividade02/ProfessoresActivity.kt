package com.example.atividade02

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.Image
import androidx.compose.foundation.layout.*
import androidx.compose.material3.Button
import androidx.compose.material3.OutlinedTextField
import androidx.compose.material3.Text
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.text.input.TextFieldValue
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp

class ProfessoresActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            ProfessoresScreen()
        }
    }
}

@Composable
fun ProfessoresScreen() {
    var nome by remember { mutableStateOf(TextFieldValue("")) }
    var imagemId by remember { mutableStateOf<Int?>(null) }
    var mensagem by remember { mutableStateOf("") }

    Column(
        modifier = Modifier
            .fillMaxSize()
            .padding(24.dp),
        horizontalAlignment = Alignment.CenterHorizontally,
        verticalArrangement = Arrangement.Center
    ) {
        OutlinedTextField(
            value = nome,
            onValueChange = { nome = it },
            label = { Text("Digite o nome do professor") },
            modifier = Modifier.fillMaxWidth()
        )

        Spacer(modifier = Modifier.height(16.dp))

        Button(onClick = {
            when (nome.text.trim().lowercase()) {
                "saulo" -> {
                    imagemId = R.drawable.saulo
                    mensagem = "Professor Saulo"
                }
                "reginaldo" -> {
                    imagemId = R.drawable.reginaldo
                    mensagem = "Professor Reginaldo"
                }
                "júlio", "julio" -> {
                    imagemId = R.drawable.julio
                    mensagem = "Professor Júlio"
                }
                "lucas" -> {
                    imagemId = R.drawable.lucas
                    mensagem = "Professor Lucas"
                }
                "jussara" -> {
                    imagemId = R.drawable.jussara
                    mensagem = "Professora Jussara"
                }
                "anelise" -> {
                    imagemId = R.drawable.anelise
                    mensagem = "Professora Anelise"
                }
                "phyllipe" -> {
                    imagemId = R.drawable.phyllipe
                    mensagem = "Professor Phyllipe"
                }
                else -> {
                    imagemId = null
                    mensagem = "Digite um nome de professor(a) válido"
                }
            }
        }) {
            Text("Buscar")
        }

        Spacer(modifier = Modifier.height(16.dp))

        imagemId?.let {
            Image(
                painter = painterResource(id = it),
                contentDescription = "Imagem do Professor",
                modifier = Modifier.size(200.dp)
            )
        }

        Text(text = mensagem, fontSize = 18.sp)
    }
}
