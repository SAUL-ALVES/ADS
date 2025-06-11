package com.example.atividade02

import android.content.Intent
import android.os.Bundle
import android.view.View
import android.widget.Button
import android.widget.EditText
import android.widget.ImageView
import android.widget.TextView
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.tooling.preview.Preview
import com.example.atividade02.ui.theme.Atividade02Theme

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        setContentView(R.layout.activity_times)

        val editTextTime = findViewById<EditText>(R.id.editTextTime)
        val buttonMostrar = findViewById<Button>(R.id.buttonMostrar)
        val buttonLimpar = findViewById<Button>(R.id.buttonLimpar)
        val textViewResultado = findViewById<TextView>(R.id.textViewResultado)
        val buttonSobre = findViewById<Button>(R.id.buttonSobre)
        val buttonProfessores = findViewById<Button>(R.id.buttonProfessores)

        val imageViewTaca = findViewById<ImageView>(R.id.imageViewTaca)

        imageViewTaca.visibility = View.GONE

        val mundiaisPorTime = mapOf(
            "santos" to Pair(2, R.drawable.taca_mundial),
            "flamengo" to Pair(1, R.drawable.taca_mundial),
            "grêmio" to Pair(1, R.drawable.taca_mundial),
            "são paulo" to Pair(3, R.drawable.taca_mundial),
            "internacional" to Pair(1, R.drawable.taca_mundial),
            "corinthians" to Pair(2, R.drawable.taca_mundial)
        )
        buttonMostrar.setOnClickListener {
            val nomeDigitado = editTextTime.text.toString().trim().lowercase()

            if (mundiaisPorTime.containsKey(nomeDigitado)) {
                val (quantidade, imagem) = mundiaisPorTime[nomeDigitado]!!
                val nomeFormatado = nomeDigitado.replaceFirstChar { it.uppercase() }
                textViewResultado.text =
                    "O $nomeFormatado possui $quantidade campeonato(s) mundial(is)"
                imageViewTaca.setImageResource(imagem)
                imageViewTaca.visibility = View.VISIBLE
            } else {
                textViewResultado.text = "Time não encontrado ou sem títulos mundiais."
                imageViewTaca.visibility = View.GONE
            }
        }

        buttonLimpar.setOnClickListener {
            editTextTime.text.clear()
            textViewResultado.text = ""
            imageViewTaca.visibility = View.GONE
        }

        buttonSobre.setOnClickListener {
            val intent = Intent(this, SobreActivity::class.java)
            startActivity(intent)
        }

        buttonProfessores.setOnClickListener {
            val intent = Intent(this, ProfessoresActivity::class.java)
            startActivity(intent)
        }
    }
}

