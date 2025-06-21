package com.example.fitfan


import android.content.Intent
import android.net.Uri
import android.widget.MediaController
import android.os.Bundle
import android.widget.Button
import android.widget.EditText
import android.widget.ImageView
import android.widget.TextView
import android.widget.VideoView
import androidx.activity.ComponentActivity
import kotlin.jvm.java


class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        setContentView(R.layout.imc_activity)


        val etPeso = findViewById<EditText>(R.id.et_peso)
        val etAltura = findViewById<EditText>(R.id.et_altura)
        val btnCalcularIMC = findViewById<Button>(R.id.btn_calcular_imc)
        val tvResultadoIMC = findViewById<TextView>(R.id.tv_resultado_imc)
        val tvClassificacaoIMC = findViewById<TextView>(R.id.tv_classificacao_imc)

        val etExercicioFavorito = findViewById<EditText>(R.id.et_exercicio_favorito)
        val btnMostrarExercicio = findViewById<Button>(R.id.btn_mostrar_exercicio)
        val ivImagemExercicio = findViewById<ImageView>(R.id.iv_imagem_exercicio)
        val tvNomeExercicio = findViewById<TextView>(R.id.tv_nome_exercicio)
        val btnLimpar = findViewById<Button>(R.id.btn_limpar)

        val btnSobre = findViewById<Button>(R.id.btn_sobre)
        val btnDicasTreino = findViewById<Button>(R.id.btn_dicas_treino)

        val vvMotivacional = findViewById<VideoView>(R.id.vv_motivacional)
        val videoUri = Uri.parse("android.resource://${packageName}/raw/video")



        btnCalcularIMC.setOnClickListener {
            val peso = etPeso.text.toString().toFloatOrNull()
            val altura = etAltura.text.toString().toFloatOrNull()

            if (peso != null && altura != null && altura != 0f) {
                val imc = peso / (altura * altura)
                tvResultadoIMC.text = "Seu IMC é %.2f".format(imc)

                when {
                    imc < 18.5 -> tvClassificacaoIMC.text = "Sua classificação é: Abaixo do peso normal"
                    imc in 18.5..24.9 -> tvClassificacaoIMC.text = "Sua classificação é: Peso normal"
                    imc >= 25 -> tvClassificacaoIMC.text = "Sua classificação é: Acima do peso"
                }
            } else {
                tvResultadoIMC.text = "Por favor, insira peso e altura válidos!"
                tvClassificacaoIMC.text = ""
            }
        }

        vvMotivacional.setVideoURI(videoUri)

        val mediaController = MediaController(this)
        mediaController.setAnchorView(vvMotivacional)
        vvMotivacional.setMediaController(mediaController)

        vvMotivacional.requestFocus()
        vvMotivacional.start()

        btnMostrarExercicio.setOnClickListener {
            val exercicio = etExercicioFavorito.text.toString().trim()

            when (exercicio.lowercase()){
                "agachamento" -> {
                    ivImagemExercicio.setImageResource(R.drawable.agachamento)
                    tvNomeExercicio.text = "Agachamento: ativa quadriceps e glúteo"
                }
                "supino" -> {
                    ivImagemExercicio.setImageResource(R.drawable.supino)
                    tvNomeExercicio.text = "Supino: ativa peito e ombros"
                }
                "cardio" -> {
                    ivImagemExercicio.setImageResource(R.drawable.cardio)
                    tvNomeExercicio.text = "Cardio: aumento da resistência e queima de calorias"
                } else -> {
                ivImagemExercicio.setImageResource(0)
                tvNomeExercicio.text = "Exercício inválido, digite: agachamento, supino ou cardio."
            }
        }

    }

        btnSobre.setOnClickListener {
            startActivity(Intent(this, SobreActivity::class.java))
        }

        btnDicasTreino.setOnClickListener {
            startActivity(Intent(this, DicasActivity::class.java))
        }



        btnLimpar.setOnClickListener {
            etPeso.text.clear()
            etAltura.text.clear()
            etExercicioFavorito.text.clear()
            tvResultadoIMC.text = ""
            tvClassificacaoIMC.text = ""
            ivImagemExercicio.setImageDrawable(null)
            tvNomeExercicio.text = ""
        }
}
    }
